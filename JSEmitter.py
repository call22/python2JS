from Python3Listener import Python3Listener
from Python3Parser import Python3Parser
from antlr4.tree.Tree import TerminalNodeImpl
# 一个
class JSEmitter(Python3Listener):
    def __init__(self):
        self.js = {}

    def getJS(self, ctx):
        return self.js[ctx]

    def setJS(self, ctx, value):
        self.js[ctx] = value

    def exitParse(self, ctx:Python3Parser.ParseContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    def exitSingle_input(self, ctx:Python3Parser.Single_inputContext):
        content = ''
        if ctx.simple_stmt() is not None:
            content += self.getJS(ctx.simple_stmt())
        elif ctx.compound_stmt() is not None:
            content += self.getJS(ctx.compound_stmt()) + ctx.NEWLINE().getText()
        else:
            content += ctx.NEWLINE().getText()
        self.setJS(ctx, content)

    def exitFile_input(self, ctx:Python3Parser.File_inputContext):
        content = ''
        for child in ctx.children:
            if isinstance(child, Python3Parser.StmtContext):
                content += self.getJS(child)
            elif isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == Python3Parser.NEWLINE:
                    content += child.getText()
        self.setJS(ctx, content)

    def exitEval_input(self, ctx:Python3Parser.Eval_inputContext):
        content = self.getJS(ctx.testlist())
        for line in ctx.NEWLINE():
            content += line.getText()
        self.setJS(ctx, content)

    def exitStmt(self, ctx:Python3Parser.StmtContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    def exitSimple_stmt(self, ctx:Python3Parser.Simple_stmtContext):
        content = ""
        for small_stmt in ctx.small_stmt():
            content = content + self.getJS(small_stmt)
        content += ctx.NEWLINE().getText()
        self.setJS(ctx, content)

    def exitSmall_stmt(self, ctx:Python3Parser.Small_stmtContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    def exitExpr_stmt(self, ctx:Python3Parser.Expr_stmtContext):
        content = self.getJS(ctx.getChild(0))
        if ctx.annassign() is not None:
            content += self.getJS(ctx.annassign())
        elif ctx.augassign() is not None:
            content += self.getJS(ctx.augassign())
            content += self.getJS(ctx.testlist(1))
        else:
            for item in ctx.testlist()[1:]:
                content += ' = ' + self.getJS(item)
        self.setJS(ctx, content)

    def exitAnnassign(self, ctx:Python3Parser.AnnassignContext):
        content = ' : ' + self.getJS(ctx.test(0))
        if ctx.test(1) is not None:
            content += ' = ' + self.getJS(ctx.test(1))
        self.setJS(ctx, content)

    def exitAugassign(self, ctx:Python3Parser.AugassignContext):
        self.setJS(ctx, ctx.getText())

    def exitPass_stmt(self, ctx:Python3Parser.Pass_stmtContext):
        self.setJS(ctx, ctx.getText())

    def exitFlow_stmt(self, ctx:Python3Parser.Flow_stmtContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    def exitBreak_stmt(self, ctx:Python3Parser.Break_stmtContext):
        self.setJS(ctx, ctx.getText())

    def exitContinue_stmt(self, ctx:Python3Parser.Continue_stmtContext):
        self.setJS(ctx, ctx.getText())

    def exitReturn_stmt(self, ctx:Python3Parser.Return_stmtContext):
        content = 'return '
        if ctx.testlist() is not None:
            content += self.getJS(ctx.testlist())
        self.setJS(ctx, content)

    def exitCompound_stmt(self, ctx:Python3Parser.Compound_stmtContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    def exitIf_stmt(self, ctx:Python3Parser.If_stmtContext):
        content = 'if' + self.getJS(ctx.test(0)) + '{\n' + self.getJS(ctx.suite(0)) + '}\n'
        test_len = len(ctx.test())
        for i in range(1,test_len):
            content += 'else if' + self.getJS(ctx.test(i)) + '{\n' + self.getJS(ctx.suite(i)) + '}\n'
        suite_len = len(ctx.suite())
        if suite_len - test_len == 1:   # else
            content += 'else{\n' + self.getJS(ctx.suite(suite_len-1)) + '}\n'
        self.setJS(ctx, content)

    def exitWhile_stmt(self, ctx:Python3Parser.While_stmtContext):
        content = 'while' + self.getJS(ctx.test()) + '{\n' + self.getJS(ctx.suite(0)) + '}\n'
        if ctx.suite(1) is not None:
            content += self.getJS(ctx.suite(1)) + '\n'  # else 相当于跳出后第一句
        self.setJS(ctx, content)

# for (x in range(1,3)):  --->   for ( x=1; x<3; x++){}
# 对所有range, 进行转变. 不能用js的for in --> 对象的使用方式
# 仅考虑数字吧
    def exitFor_stmt(self, ctx:Python3Parser.For_stmtContext):
        content = ''
        text = str(self.getJS(ctx.testlist()))
        if text.startswith('range('):    # 调用了range函数
            result = text.split(',')
            start = result[0].split('(')[1]
            end = result[1].split(')')[0]
            i = self.getJS(ctx.exprlist())
            content += 'for({} = {}; {} < {}; {}++)'.format(i,start, i, end, i) + '{\n' + self.getJS(ctx.suite(0)) + '}\n'
        else:
            raise KeyError('for error, does not suppose object\n')
        if ctx.suite(1) is not None:
            content += self.getJS(ctx.suite(1)) + '\n'
        self.setJS(ctx, content)

    def exitFuncdef(self, ctx:Python3Parser.FuncdefContext):    # 实力不足,忽略->test部分,一般也不用
        content = 'function {} {}{\n'.format(ctx.NAME().getText(), self.getJS(ctx.parameters()))
        content += self.getJS(ctx.suite()) + '}\n'
        self.setJS(ctx, content)

    def exitParameters(self, ctx:Python3Parser.ParametersContext):
        content = '({})'.format(self.getJS(ctx.argslist()))
        self.setJS(ctx, content)

# 对参数为*,**的暂时无法解决
    def exitArgslist(self, ctx:Python3Parser.ArgslistContext):
        content = ''
        if ctx.argslist_normal() is not None:
            content += self.getJS(ctx.argslist_normal())
        else:
            raise KeyError('parameters does not suppose *,** type')
        self.setJS(ctx, content)

    def exitArgslist_normal(self, ctx:Python3Parser.Argslist_normalContext):
        pdef_idx = 1
        test_idx = 0
        content = self.getJS(ctx.getChild(0))
        if ctx.getChild(1) == ctx.test(0):
            content += '=' + self.getJS(ctx.test(0))
            test_idx = 1
        for child in ctx.children[pdef_idx + test_idx :]:
            if child == ctx.pdef(pdef_idx):
                pdef_idx += 1
                content += ', ' + self.getJS(child)
            else:
                test_idx += 1
                content += '=' + self.getJS(child)
        self.setJS(ctx, content)

# js函数不会对参数值进行任何检查, 故不能指定类型
    def exitPdef(self, ctx:Python3Parser.PdefContext):
        content = ctx.NAME().getText()
        self.setJS(ctx, content)

    def exitSuite(self, ctx:Python3Parser.SuiteContext):
        content = ''
        if ctx.simple_stmt() is not None:
            content += self.getJS(ctx.simple_stmt())
        else:
            indent = ctx.INDENT().getText()
            dedent = ctx.DEDENT().getText()
            for stmt in ctx.stmt():
                content += indent + self.getJS(stmt)
            content += dedent
        self.setJS(ctx, content)

# 暂时没有弄懂 if else的作用
    def exitTest(self, ctx:Python3Parser.TestContext):
        content = self.getJS(ctx.or_test(0))
        if ctx.test() is not None:
            content += 'if ' + self.getJS(ctx.or_test(1)) + ' else ' + self.getJS(ctx.test())
        self.setJS(ctx, content)

    def exitOr_test(self, ctx:Python3Parser.Or_testContext):
        content = self.getJS(ctx.and_test(0))
        for item in ctx.and_test()[1:]:
            content += ' || ' + self.getJS(item)
        self.setJS(ctx, content)

    def exitAnd_test(self, ctx:Python3Parser.And_testContext):
        content = self.getJS(ctx.not_test(0))
        for item in ctx.not_test()[1:]:
            content += ' && ' + self.getJS(item)
        self.setJS(ctx, content)

    def exitNot_test(self, ctx:Python3Parser.Not_testContext):
       content = ''
       if ctx.not_test() is not None:
           content += '!' + self.getJS(ctx.not_test())
       else:
           content += self.getJS(ctx.comparison())
       self.setJS(ctx, content)

    def exitComparison(self, ctx:Python3Parser.ComparisonContext):
        content = ''
        for child in ctx.children:
            content += self.getJS(child)
        self.setJS(ctx, content)

# 未实现not in, is, is not的转换
    def exitComp_op(self, ctx:Python3Parser.Comp_opContext):
        text = ctx.getText()
        if text in ['not in', 'is', 'is not']:
            raise KeyError('comparision error, does not suppose "not in" "is" "is not"')
        else:
            self.setJS(ctx, ' {} '.format(text))

    def exitExpr(self, ctx:Python3Parser.ExprContext):
        content = self.getJS(ctx.xor_expr(0))
        for child in ctx.xor_expr()[1:]:
            content += ' | ' + self.getJS(child)
        self.setJS(ctx, content)

    def exitXor_expr(self, ctx:Python3Parser.Xor_exprContext):
        content = self.getJS(ctx.and_expr(0))
        for child in ctx.and_expr()[1:]:
            content += ' ^ ' + self.getJS(child)
        self.setJS(ctx, content)

    def exitAnd_expr(self, ctx:Python3Parser.And_exprContext):
        content = self.getJS(ctx.algorithm_expr(0))
        for child in ctx.algorithm_expr()[1:]:
            content += ' & ' + self.getJS(child)
        self.setJS(ctx, content)

# 在algorithm之后的尚未完成,整个程序暂时不要运行(因为自顶向下写的)
    def exitAlgorithm_expr(self, ctx:Python3Parser.Algorithm_exprContext):
        content = self.getJS(ctx.term(0))
        # op_idx = 0
        for term in ctx.term()[1:]:
            if ctx.op.type == Python3Parser.ADD:
                content += ' + ' + self.getJS(term)
            elif ctx.op.type == Python3Parser.SUB:
                content += ' - ' + self.getJS(term)
            # op_idx += 1
        self.setJS(ctx, content)

    def exitTerm(self, ctx:Python3Parser.TermContext):
        content = self.getJS(ctx.factor(0))
        # op_idx = 0
        for factor in ctx.factor()[1:]:
            if ctx.op.type == Python3Parser.STAR:
                content += ' * ' + self.getJS(factor)
            elif ctx.op.type == Python3Parser.DIV:
                content += ' / ' + self.getJS(factor)
            elif ctx.op.type == Python3Parser.MOD:
                content += ' % ' + self.getJS(factor)
            # op_idx += 1
        self.setJS(ctx, content)

    def exitFactor(self, ctx:Python3Parser.FactorContext):
        content = ''
        if ctx.op is None:
            content += self.getJS(ctx.power())
        elif ctx.op.type == Python3Parser.ADD:
            content += ' + ' + self.getJS(ctx.factor())
        elif ctx.op.type == Python3Parser.SUB:
            content += ' - ' + self.getJS(ctx.factor())
        elif ctx.op.type == Python3Parser.NOT_OP:
            content += '~' + self.getJS(ctx.factor())
        self.setJS(ctx, content)

    def exitPower(self, ctx:Python3Parser.PowerContext):
        content = self.getJS(ctx.atom_expr())
        if ctx.factor() is not None:
            content += '**' + self.getJS(ctx.factor())
        self.setJS(ctx, content)

    def exitAtom_expr(self, ctx:Python3Parser.Atom_exprContext):
        text = self.getJS(ctx.atom())
        content = self.getJS(ctx.atom())
        for trailer in ctx.trailer():
            content += self.getJS(trailer)
        self.setJS(ctx, content)

    def exitAtom(self, ctx:Python3Parser.AtomContext):
        content = ''
        if ctx.op is not None:
            if ctx.op.type == Python3Parser.OPEN_PAREN:
                content += '({})'.format(self.getJS(ctx.testlist_comp()) \
                                         if ctx.testlist_comp() is not None else '')
            elif ctx.op.type == Python3Parser.OPEN_BRACK:
                if ctx.testlist_comp() is not None:
                    content += '[{}]'.format(self.getJS(ctx.testlist_comp()))
                else:
                    content += 'new Array()'
        elif ctx.NAME() is not None:
            content += ctx.NAME().getText()
        elif ctx.NUMBER() is not None:
            content += ctx.NUMBER().getText()
        elif ctx.STRING(0) is not None:
            for s in ctx.STRING():
                content += s.getText()
        else:
            text = ctx.getText()
            if text == 'None':
                content += 'undefined'
            elif text == 'True':
                content += 'true'
            elif text == 'False':
                content += 'false'
        self.setJS(ctx, content)

    def exitTestlist_comp(self, ctx:Python3Parser.Testlist_compContext):
        self.setJS(ctx, self.getJS(ctx.testlist()))

    def exitTrailer(self, ctx:Python3Parser.TrailerContext):
        content = ''
        if ctx.op.type == Python3Parser.OPEN_PAREN:
            if ctx.arglist() is not None:
                content += '({})'.format(self.getJS(ctx.arglist()))
            else:
                content += '()'
        elif ctx.op.type == Python3Parser.OPEN_BRACK:
            content += '[{}]'.format(self.getJS(ctx.subscriptlist()))
        elif ctx.op.type == Python3Parser.DOT:
            content += '.' + ctx.NAME().getText()
        self.setJS(ctx, content)

    def exitSubscriptlist(self, ctx:Python3Parser.SubscriptlistContext):
        content = self.getJS(ctx.subscript(0))
        for sub in ctx.subscript()[1:]:
            content += ', ' + self.getJS(sub)
        self.setJS(ctx, content)

# 因为js不支持切片,故暂时不实现
    def exitSubscript(self, ctx:Python3Parser.SubscriptContext):
        if ctx.op is None:
            self.setJS(ctx, self.getJS(ctx.getChild(0)))
        else:
            raise KeyError('subsript error, does not suppose [:]')

    def exitExprlist(self, ctx:Python3Parser.ExprlistContext):
        content = self.getJS(ctx.expr(0))
        for expr in ctx.expr()[1:]:
            content += ',' + self.getJS(expr)
        self.setJS(ctx, content)

    def exitTestlist(self, ctx:Python3Parser.TestlistContext):
        content = self.getJS(ctx.getChild(0))
        for test in ctx.test()[1:]:
            content += ',' + self.getJS(test)
        self.setJS(ctx, content)

    def exitArglist(self, ctx:Python3Parser.ArglistContext):
        content = self.getJS(ctx.getChild(0))
        for argument in ctx.argument()[1:]:
            content += ',' + self.getJS(argument)
        self.setJS(ctx, content)

# 同样不考虑*, 和**情况
    def exitArgument(self, ctx:Python3Parser.ArgumentContext):
        content = ''
        length = len(ctx.test())
        if length == 2:
            content = self.getJS(ctx.test(0)) + '=' + self.getJS(ctx.test(1))
        elif length == 1:
            content = self.getJS(ctx.test(0))
        else:
            raise KeyError('argument error, does not suppose ** or *')
        self.setJS(ctx, content)
