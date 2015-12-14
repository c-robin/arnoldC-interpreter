from antlr4 import *
from ArnoldCLexer import ArnoldCLexer
from ArnoldCParser import ArnoldCParser
from customVisitor import customVisitor
import logging
import sys

def main():
    input = FileStream("test.arnoldC")
    lexer = ArnoldCLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ArnoldCParser(stream)
    tree = parser.program()
    visitor = customVisitor()
    visitor.visit(tree)

 
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    main()