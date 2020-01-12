from Python3Listener import Python3Listener
from Python3Parser import Python3Parser
from antlr4.tree.Tree import TerminalNodeImpl
from table import FuncTable

Func = FuncTable()
Func.initTree()

# 声明变量的方式:
# 1. 表达式 a = 1,
# 2. for i in range(1)形式


class JSEmitter(Python3Listener):
    def __init__(self):
        self.js = {}
        self.procHead = []
        self.errorLog = []
        self.assign = False # expr flag
        self.for_var = False   # for flag, signal

    def clearAll(self):
        self.js = {}
        self.errorLog = []
        self.procHead = []

    def getJS(self, ctx):
        return self.js[ctx]

    def setJS(self, ctx, value):
        self.js[ctx] = value

    def exitParse(self, ctx: Python3Parser.ParseContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))


    def exitSingle_input(self, ctx: Python3Parser.Single_inputContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitFile_input(self, ctx: Python3Parser.File_inputContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, Python3Parser.StmtContext):
                content += self.getJS(child)
            elif isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.NEWLINE:
                    content += child.getText()
        self.setJS(ctx, content)

    def exitEval_input(self, ctx: Python3Parser.Eval_inputContext):
        content = self.getJS(ctx.testlist())
        for line in ctx.NEWLINE():
            content += line.getText()
        self.setJS(ctx, content)

    def exitStmt(self, ctx: Python3Parser.StmtContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    def exitSimple_stmt(self, ctx: Python3Parser.Simple_stmtContext):
        content = ""
        for child in ctx.children:
            if isinstance(child, Python3Parser.Small_stmtContext):
                content += self.getJS(child)
            elif isinstance(child, TerminalNodeImpl):
                content += child.getText()
        self.setJS(ctx, content)

    def exitSmall_stmt(self, ctx: Python3Parser.Small_stmtContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    # 变量声明
    def enterExpr_stmt(self, ctx:Python3Parser.Expr_stmtContext):
        if ctx.getChildCount() > 1 and isinstance(ctx.getChild(1), TerminalNodeImpl):
            if ctx.getChild(1).getSymbol().type == Python3Parser.ASSIGN:
                # 赋值语句, 有可能为变量定义.
                self.assign = True

    def exitExpr_stmt(self, ctx: Python3Parser.Expr_stmtContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitAnnassign(self, ctx: Python3Parser.AnnassignContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitAugassign(self, ctx: Python3Parser.AugassignContext):
        self.setJS(ctx, ctx.getText())

    def exitPass_stmt(self, ctx: Python3Parser.Pass_stmtContext):
        self.setJS(ctx, ctx.getText())

    def exitFlow_stmt(self, ctx: Python3Parser.Flow_stmtContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    def exitBreak_stmt(self, ctx: Python3Parser.Break_stmtContext):
        self.setJS(ctx, ctx.getText())

    def exitContinue_stmt(self, ctx: Python3Parser.Continue_stmtContext):
        self.setJS(ctx, ctx.getText())

    def exitReturn_stmt(self, ctx: Python3Parser.Return_stmtContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                content += child.getText() + ' '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitCompound_stmt(self, ctx: Python3Parser.Compound_stmtContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    def exitIf_stmt(self, ctx: Python3Parser.If_stmtContext):
        indent = ''
        if isinstance(ctx.parentCtx.parentCtx.parentCtx, Python3Parser.SuiteContext):
            indent = ctx.parentCtx.parentCtx.parentCtx.INDENT().getText()

        content = ''
        for child in ctx.children:
            if isinstance(child, Python3Parser.TestContext):
                content += self.getJS(child)
            elif isinstance(child, Python3Parser.SuiteContext):
                content += self.getJS(child) + indent + '}\n'
            elif isinstance(child, TerminalNodeImpl):
                if (child.getSymbol().type == Python3Parser.COLON):
                    content += '{'
                elif (child.getSymbol().type == Python3Parser.ELIF):
                    content += indent + 'else if'
                else:
                    content += indent + child.getText()
        self.setJS(ctx, content)

    def exitWhile_stmt(self, ctx: Python3Parser.While_stmtContext):
        indent = ''
        if isinstance(ctx.parentCtx.parentCtx.parentCtx, Python3Parser.SuiteContext):
            indent = ctx.parentCtx.parentCtx.parentCtx.INDENT().getText()

        content = ctx.getChild(0).getText() + self.getJS(ctx.test()) + '{\n' + self.getJS(ctx.suite(0)) + indent + '}\n'
        if ctx.suite(1) is not None:
            content += indent + self.getJS(ctx.suite(1)) + '\n'  # else 相当于跳出后第一句
        self.setJS(ctx, content)

    # 变量声明
    def enterFor_stmt(self, ctx:Python3Parser.For_stmtContext):
        self.for_var = True

    # for (x in range(1,3)):  --->   for ( x=1; x<3; x++){}
    # 对所有range, 进行转变. 不能用js的for in --> 对象的使用方式
    # 仅考虑数字吧
    def exitFor_stmt(self, ctx: Python3Parser.For_stmtContext):
        # 计算{}需要的缩进
        indent = ''
        if isinstance(ctx.parentCtx.parentCtx.parentCtx, Python3Parser.SuiteContext):
            indent = ctx.parentCtx.parentCtx.parentCtx.INDENT().getText()

        content = ''
        text = str(self.getJS(ctx.testlist()))
        if text.startswith('range('):  # 调用了range函数
            result = text.split(',')
            start = result[0].split('(')[1]
            end = result[1].split(')')[0]
            i = self.getJS(ctx.exprlist())
            content += 'for({} = {}; {} < {}; {}++)'.format(i, start, i, end, i)
            content += '{\n' + self.getJS(ctx.suite(0)) + indent + '}\n'
        else:
            e = 'For error, does not suppose object'
            self.errorLog.append(e)
            #raise KeyError('for error, does not suppose object\n')
        if ctx.suite(1) is not None:
            content += indent + self.getJS(ctx.suite(1)) + '\n'
        self.setJS(ctx, content)

    def enterFuncdef(self, ctx:Python3Parser.FuncdefContext):
        # calculate parameters number
        min_param = 0
        max_param = 0
        param = ctx.parameters()
        if param.argslist() is not None:
            normal = param.argslist().argslist_normal()
            max_param = len(normal.pdef())
            min_param = max_param - len(normal.test())
        # add fucntion
        Func.add(ctx.NAME().getText(), "default", (min_param, max_param), self.procHead)
        self.procHead.append(ctx.NAME().getText())

    def exitFuncdef(self, ctx: Python3Parser.FuncdefContext):  # 实力不足,忽略->test部分,一般也不用
        # 计算{}需要的缩进
        indent = ''
        if isinstance(ctx.parentCtx.parentCtx.parentCtx, Python3Parser.SuiteContext):
            indent = ctx.parentCtx.parentCtx.parentCtx.INDENT().getText()

        content = 'function {} {}'.format(ctx.NAME().getText(), self.getJS(ctx.parameters()))
        content += '{\n' + self.getJS(ctx.suite()) + indent + '}\n'
        self.setJS(ctx, content)
        self.procHead.pop()

    def exitParameters(self, ctx: Python3Parser.ParametersContext):
        content = '({})'.format(self.getJS(ctx.argslist()))
        self.setJS(ctx, content)

    # 对参数为*,**的暂时无法解决
    def exitArgslist(self, ctx: Python3Parser.ArgslistContext):
        content = ''
        if ctx.getChildCount() == 1 and ctx.argslist_normal() is not None:
            content += self.getJS(ctx.argslist_normal())
        else:
            e = 'Parameters does not suppose *,** type'
            self.errorLog.append(e)
            # raise KeyError('parameters does not suppose *,** type')
        self.setJS(ctx, content)

    def exitArgslist_normal(self, ctx: Python3Parser.Argslist_normalContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    # js函数不会对参数值进行任何检查, 故不能指定类型
    def exitPdef(self, ctx: Python3Parser.PdefContext):
        content = ctx.NAME().getText()
        self.setJS(ctx, content)

    def exitSuite(self, ctx: Python3Parser.SuiteContext):
        content = ''
        if ctx.simple_stmt() is not None:
            content += self.getJS(ctx.simple_stmt())
        else:
            indent = ctx.INDENT().getText()
            dedent = ctx.DEDENT().getText()
            for child in ctx.children:
                if isinstance(child, TerminalNodeImpl):
                    if child.getSymbol().type == Python3Parser.NEWLINE:
                        content += child.getText()
                else:
                    content += indent + self.getJS(child)
            content += dedent
        self.setJS(ctx, content)

    # 暂时没有弄懂 if else的作用
    def exitTest(self, ctx: Python3Parser.TestContext):
        if ctx.getChildCount() == 1:
            self.setJS(ctx, self.getJS(ctx.getChild(0)))
        else:
            content = self.getJS(ctx.getChild(2)) + ' ? ({}) : {}'.format(self.getJS(ctx.getChild(0)), self.getJS(ctx.test()))
            self.setJS(ctx, content)

    def exitOr_test(self, ctx: Python3Parser.Or_testContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.OR:
                    content += ' || '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitAnd_test(self, ctx: Python3Parser.And_testContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.AND:
                    content += ' && '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitNot_test(self, ctx: Python3Parser.Not_testContext):
        content = ''
        if isinstance(ctx.getChild(0), TerminalNodeImpl):
            content += '!' + self.getJS(ctx.not_test())
        else:
            content += self.getJS(ctx.comparison())
        self.setJS(ctx, content)

    def exitComparison(self, ctx: Python3Parser.ComparisonContext):
        content = ''
        for child in ctx.children:
            content += self.getJS(child)
        self.setJS(ctx, content)

    # 未实现not in, is, is not的转换
    def exitComp_op(self, ctx: Python3Parser.Comp_opContext):
        text = ctx.getText()
        if text in ['not in', 'is', 'is not']:
            e = 'comparision error, does not suppose "not in" "is" "is not"'
            self.errorLog.append(e)
            #raise KeyError('comparision error, does not suppose "not in" "is" "is not"')
        elif text == '==':
            self.setJS(ctx, '===')
        elif text == '!=':
            self.setJS(ctx, '!==')
        else:
            self.setJS(ctx, ' {} '.format(text))

    def exitExpr(self, ctx: Python3Parser.ExprContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.OR_OP:
                    content += ' | '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitXor_expr(self, ctx: Python3Parser.Xor_exprContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.XOR:
                    content += ' ^ '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitAnd_expr(self, ctx: Python3Parser.And_exprContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.AND_OP:
                    content += ' & '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    # 在algorithm之后的尚未完成,整个程序暂时不要运行(因为自顶向下写的)
    def exitAlgorithm_expr(self, ctx: Python3Parser.Algorithm_exprContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.ADD:
                    content += ' + '
                elif child.getSymbol().type == Python3Parser.SUB:
                    content += ' - '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitTerm(self, ctx: Python3Parser.TermContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.STAR:
                    content += ' * '
                elif child.getSymbol().type == Python3Parser.DIV:
                    content += ' / '
                elif child.getSymbol().type == Python3Parser.MOD:
                    content += ' % '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitFactor(self, ctx: Python3Parser.FactorContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.ADD:
                    content += ' + '
                elif child.getSymbol().type == Python3Parser.SUB:
                    content += ' - '
                elif child.getSymbol().type == Python3Parser.NOT_OP:
                    content += ' ~ '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitPower(self, ctx: Python3Parser.PowerContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.POWER:
                    content += ' ** '
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitAtom_expr(self, ctx: Python3Parser.Atom_exprContext):
        # 补丁, rang()类似函数调用
        if (len(ctx.trailer()) > 0) and ctx.trailer(0).expr_param() is not None and ctx.trailer(0).op is None:
            content = ''
        else:
            content = self.getJS(ctx.atom())
        for trailer in ctx.trailer():
            content += self.getJS(trailer)
        self.setJS(ctx, content)

    def enterAtom(self, ctx:Python3Parser.AtomContext):
        # judge name var, add local var and check var's legal
        name_child = ctx.getChild(0)
        if isinstance(name_child, TerminalNodeImpl) and\
                name_child.getSymbol().type == Python3Parser.NAME and\
                ctx.parentCtx.getChildCount() == 1: # 确认为变量名而非函数名
            # 变量声明
            if self.assign or self.for_var:
                Func.add_var(name_child.getText(), '', self.procHead)
                self.assign = False
                self.for_var = False
            elif not Func.find_var(name_child.getText(), '', self.procHead):
                e = "variable %s is not defined in code" % name_child.getText()
                self.errorLog.append(e)

    def exitAtom(self, ctx: Python3Parser.AtomContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.NONE:
                    content += 'undefined'
                elif child.getSymbol().type == Python3Parser.TRUE:
                    content += 'true'
                elif child.getSymbol().type == Python3Parser.FALSE:
                    content += 'false'
                else:
                    content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitTestlist_comp(self, ctx: Python3Parser.Testlist_compContext):
        self.setJS(ctx, self.getJS(ctx.testlist()))

    def exitTrailer(self, ctx: Python3Parser.TrailerContext):
        content = ''
        if ctx.op is not None and ctx.op.type == Python3Parser.OPEN_BRACK:
            content += '[{}]'.format(self.getJS(ctx.subscriptlist()))
        # 对调用函数的参数进行处理, 不支持类属性获取, example: a.type
        else:
            if ctx.op is None:
                func_name = self.getJS(ctx.parentCtx.atom())
            else:
                content += '.'
                func_name = ctx.NAME().getText()

            param_num = 0
            if ctx.expr_param().arglist() is not None:
                param_num = len(ctx.expr_param().arglist().argument())
            func_info = Func.find(func_name, self.procHead)
            if func_info:
                func_param = func_info.param
                if param_num < func_param[0] or param_num > func_param[1]:
                    e = 'Parameters Error: too many or few parameters in ' % func_name
                    self.errorLog.append(e)
                else:
                    if func_info.type == "default":
                         content += func_name + self.getJS(ctx.expr_param())
                    elif func_info.type == "alien":
                        # 暂时只考虑类似len()函数
                        content += self.getJS(ctx.expr_param())[1:-1] + '.' + 'length'
                    else:
                        content += func_info.type + self.getJS(ctx.expr_param())
            else:
                e = 'Function Error: cannot find %s in code' % func_name
                self.errorLog.append(e)
        self.setJS(ctx, content)

    def exitExpr_param(self, ctx:Python3Parser.Expr_paramContext):
        content = '({})'.format(self.getJS(ctx.arglist()) if ctx.arglist() is not None else '')
        self.setJS(ctx, content)

    def exitSubscriptlist(self, ctx: Python3Parser.SubscriptlistContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    # 因为js不支持切片,故暂时不实现
    def exitSubscript(self, ctx: Python3Parser.SubscriptContext):
        if ctx.op is None:
            self.setJS(ctx, self.getJS(ctx.getChild(0)))
        else:
            e = 'Subsript error, does not suppose [:]'
            self.errorLog.append(e)
            #raise KeyError('subsript error, does not suppose [:]')

    def exitExprlist(self, ctx: Python3Parser.ExprlistContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitTestlist(self, ctx: Python3Parser.TestlistContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    def exitArglist(self, ctx: Python3Parser.ArglistContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)

    # 同样不考虑*, 和**情况
    def exitArgument(self, ctx: Python3Parser.ArgumentContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.STAR or child.getSymbol().type == Python3Parser.POWER:
                    e = 'Argument error, does not suppose ** or *'
                    self.errorLog.append(e)
                    # raise KeyError('argument error, does not suppose ** or *')
                else:
                    content += child.getText()
            else:
                content += self.getJS(child)
        self.setJS(ctx, content)
