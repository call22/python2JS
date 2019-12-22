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
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1],encoding='utf-8')
    else:
        input_stream = InputStream(sys.stdin.read())

    # with open('input.txt', 'w') as fi:
    #     fi.write(str(input_stream))
    lexer = Python3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Python3Parser(token_stream)
    tree = parser.parse()

    lisp_tree_str = tree.toStringTree(recog=parser)
    with open('lexer.txt', 'w') as fi:
        fi.write(lisp_tree_str)

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
        spaceFilter('tmp.js', 'result.js')
        os.remove('tmp.js')