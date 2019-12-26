__author__ = 'long'

import sys
import os
from antlr4 import *
from antlr4.InputStream import InputStream

from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from JSEmitter import JSEmitter
from filter import spaceFilter


if __name__ == '__main__':
    file_name = 'result'
    lexer_name = 'lexer.py'
    # 由于词法分析对空行处理有bug, 故先预处理, 将空行消除
    if len(sys.argv) > 1:
        file_name = sys.argv[1].split('.')[0]
        spaceFilter(sys.argv[1], lexer_name)
    else:
        with open('lexer_tmp.py', 'w') as fi:
            fi.write(sys.stdin.read())
        spaceFilter('lexer_tmp.py', lexer_name)
        os.remove('lexer_tmp.py')

    input_stream = FileStream(lexer_name, encoding='utf-8')
    os.remove(lexer_name)

    lexer = Python3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Python3Parser(token_stream)
    tree = parser.parse()

    lisp_tree_str = tree.toStringTree(recog=parser)

    # listener
    print("Start Walking...")
    listener = JSEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.clearAll()
    walker.walk(listener, tree)
    if len(listener.errorLog) > 0:
        for e in listener.errorLog:
            print(e)
    else:
        with open('tmp.js', 'w') as fi:
            fi.write(listener.getJS(tree))
        spaceFilter('tmp.js', file_name+'.js')
        os.remove('tmp.js')