# Generated from ArnoldC.g4 by ANTLR 4.5.1
from antlr4 import *
from ArnoldCVisitor import ArnoldCVisitor
import logging

# This class defines a complete generic visitor for a parse tree produced by ArnoldCParser.

# store variables (only one scope)
memory = {}

class customVisitor(ArnoldCVisitor):

    # Visit a parse tree produced by ArnoldCParser#program.
    def visitProgram(self, ctx):
        logging.debug("program")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#main_function.
    def visitMain_function(self, ctx):
        logging.debug("main_function")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#statements.
    def visitStatements(self, ctx):
        logging.debug("statements")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#statement.
    def visitStatement(self, ctx):
        logging.debug("statement")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#print_stmt.
    def visitPrint_stmt(self, ctx):
        logging.debug("print_stmt")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#print_sconst_stmt.
    def visitPrint_sconst_stmt(self, ctx):
        logging.debug("print_sconst_stmt")
        print(ctx.children[1].symbol.text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#print_var_stmt.
    def visitPrint_var_stmt(self, ctx):
        logging.debug("print_var_stmt")
        print(memory[ctx.children[1].symbol.text])
        return self.visitChildren(ctx)
    
    
    # Visit a parse tree produced by ArnoldCParser#var_decl_stmt.
    def visitVar_decl_stmt(self, ctx):
        var = self.visit(ctx.children[3])
        memory[ctx.children[1].symbol.text] = var
        return self.visitChildren(ctx)
        

    # Visit a parse tree produced by ArnoldCParser#var_assign_stmt.
    def visitVar_assign_stmt(self, ctx):
        key = ctx.children[1].symbol.text
        value = self.visit(ctx.children[3])
        func = self.visit(ctx.children[4])
        memory[key] = func(value)
        return self.visitChildren(ctx)



    ##################################
    # Expressions
    ##################################


    # Visit a parse tree produced by ArnoldCParser#varexpr.
    def visitVarexpr(self, ctx):
        return memory[ctx.children[0].symbol.text]


    # Visit a parse tree produced by ArnoldCParser#numberexpr.
    def visitNumberexpr(self, ctx):
        return int(ctx.children[0].symbol.text)


    # Visit a parse tree produced by ArnoldCParser#trueexpr.
    def visitTrueexpr(self, ctx):
        return 1


    # Visit a parse tree produced by ArnoldCParser#falseexpr.
    def visitFalseexpr(self, ctx):
        return 0
    
    ##################################
    # Operations
    ##################################
        
    # Visit a parse tree produced by ArnoldCParser#operations.
    def visitOperations(self, ctx):
        if len(ctx.children) > 1:
            func = self.visit(ctx.children[0])
            op = self.visit(ctx.children[1])
            return lambda x:op(func(x))
        else:
            op = self.visit(ctx.children[0])
            return op


    # Visit a parse tree produced by ArnoldCParser#plusop.
    def visitPlusop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:x+var


    # Visit a parse tree produced by ArnoldCParser#minusop.
    def visitMinusop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:x-var


    # Visit a parse tree produced by ArnoldCParser#multiplicationop.
    def visitMultiplicationop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:x*var


    # Visit a parse tree produced by ArnoldCParser#divisionop.
    def visitDivisionop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:x/var

    # Visit a parse tree produced by ArnoldCParser#equalop.
    def visitEqualop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:1 if x==var else 0

    # Visit a parse tree produced by ArnoldCParser#greaterop.
    def visitGreaterop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:1 if x>var else 0


    # Visit a parse tree produced by ArnoldCParser#orop.
    def visitOrop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:0 if x==var and x == 0 else 1


    # Visit a parse tree produced by ArnoldCParser#andop.
    def visitAndop(self, ctx):
        var = self.visit(ctx.children[1])
        return lambda x:1 if x != 0 and var!= 0 else 0
