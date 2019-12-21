__author__ = 'long'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from JSEmitter import JSEmitter


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1],encoding='utf-8')
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = Python3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Python3Parser(token_stream)
    tree = parser.parse()

    lisp_tree_str = tree.toStringTree(recog=parser)
    with open('result.txt', 'w') as fi:
        fi.write(lisp_tree_str)

    # listener
    print("Start Walking...")
    listener = JSEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    with open('result.js', 'w') as fi:
        fi.write(listener.getJS(tree))
