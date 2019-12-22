from antlr4.error.ErrorListener import *

class Python3ErrorListener(ErrorListener):
    def __init__(self, output):
        self.output = output
        self._symbol = ''

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offendingSymbol.text
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("rule stack: {}".format(str(stack)))
        print("line {} : {} at {} : {}".format(str(line),
                                               str(column),
                                               str(offendingSymbol).replace(" ", u'\u23B5'),
                                               msg.replace(" ", u'\u23B5')))

    @property
    def symbol(self):
        return self._symbol

    def output(self):
        return self.output