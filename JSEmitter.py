from Python3Listener import Python3Listener
from Python3Parser import Python3Parser

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
        for child in ctx.children:
            content += self.getJS(child)
        self.setJS(ctx, content)

    def exitFile_input(self, ctx:Python3Parser.File_inputContext):
        content = ''
        for child in ctx.children:
            content += self.getJS(child)
        self.setJS(ctx, content)

    def exitEval_input(self, ctx:Python3Parser.Eval_inputContext):
        content = ''
        for child in ctx.children:
            content += self.getJS(child)
        self.setJS(ctx, content)

    def exitStmt(self, ctx:Python3Parser.StmtContext):
        self.setJS(ctx, self.getJS(ctx.getChild(0)))

    def exitSimple_stmt(self, ctx:Python3Parser.Simple_stmtContext):
        content = ""
        for small_stmt in ctx.small_stmt():
            content = content + self.getJS(small_stmt) + '\n'
        content += self.getJS(ctx.getChild(ctx.getChildCount()-1))
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
            start = int(result[0].split('(')[1])
            end = int(result[1].split(')')[0])
            i = self.getJS(ctx.exprlist())
            content += 'for(%s = %d; %s < %d; %s++){\n'.format(i,start, i, end, i) + self.getJS(ctx.suite(0)) + '}\n'
        else:
            raise KeyError('for error, does not suppose object\n')
        if ctx.suite(1) is not None:
            content += self.getJS(ctx.suite(1)) + '\n'
        self.setJS(ctx, content)

    def exitFuncdef(self, ctx:Python3Parser.FuncdefContext):    # 实力不足,忽略->test部分,一般也不用
        content = 'function %s %s{\n'.format(self.getJS(ctx.NAME()), self.getJS(ctx.parameters()))
        content += self.getJS(ctx.suite()) + '}\n'
        self.setJS(ctx, content)

    def exitParameters(self, ctx:Python3Parser.ParametersContext):
        content = '(%s)'.format(self.getJS(ctx.argslist()))
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
        content = self.getJS(ctx.NAME())
        self.setJS(ctx, content)

    def exitSuite(self, ctx:Python3Parser.SuiteContext):
        content = ''
        if ctx.simple_stmt() is not None:
            content += self.getJS(ctx.simple_stmt())
        else:
            content += self.getJS(ctx.NEWLINE()) + self.getJS(ctx.INDENT())
            for stmt in ctx.stmt():
                content += self.getJS(stmt) + '\n'
            content += self.getJS(ctx.DEDENT())
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
        self.setJS(ctx, '('+content+')')

    def exitAnd_test(self, ctx:Python3Parser.And_testContext):
        content = self.getJS(ctx.not_test(0))
        for item in ctx.not_test()[1:]:
            content += ' && ' + self.getJS(item)
        self.setJS(ctx, '('+content+')')

    def exitNot_test(self, ctx:Python3Parser.Not_testContext):
       content = ''
       if ctx.not_test() is not None:
           content += self.getJS(ctx.not_test())
       else:
           content += self.getJS(ctx.comparison())
       self.setJS(ctx, '(!' + content + ')')

    def exitComparison(self, ctx:Python3Parser.ComparisonContext):
        content = ''
        for child in ctx.children:
            content += self.getJS(child)
        self.setJS(ctx, '('+content+')')

# 未实现not in, is, is not的转换
    def exitComp_op(self, ctx:Python3Parser.Comp_opContext):
        text = ctx.getText()
        if text in ['not in', 'is', 'is not']:
            raise KeyError('comparision error, does not suppose "not in" "is" "is not"')
        else:
            self.setJS(ctx, ' %s '.format(text))

    def exitExpr(self, ctx:Python3Parser.ExprContext):
        content = self.getJS(ctx.xor_expr(0))
        for child in ctx.xor_expr()[1:]:
            content += ' | ' + self.getJS(child)
        self.setJS(ctx, '('+content+')')

    def exitXor_expr(self, ctx:Python3Parser.Xor_exprContext):
        content = self.getJS(ctx.and_expr(0))
        for child in ctx.and_expr()[1:]:
            content += ' ^ ' + self.getJS(child)
        self.setJS(ctx, '('+content+')')

    def exitAnd_expr(self, ctx:Python3Parser.And_exprContext):
        content = self.getJS(ctx.algorithm_expr(0))
        for child in ctx.algorithm_expr()[1:]:
            content += ' & ' + self.getJS(child)
        self.setJS(ctx, '('+content+')')

# 在algorithm之后的尚未完成,整个程序暂时不要运行(因为自顶向下写的)
    # def exitAlgorithm_expr(self, ctx:Python3Parser.Algorithm_exprContext):
