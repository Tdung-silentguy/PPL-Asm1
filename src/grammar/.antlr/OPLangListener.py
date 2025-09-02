# Generated from /home/tdung/assignment/PPL/oplang-compiler/src/grammar/OPLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OPLangParser import OPLangParser
else:
    from OPLangParser import OPLangParser

# This class defines a complete listener for a parse tree produced by OPLangParser.
class OPLangListener(ParseTreeListener):

    # Enter a parse tree produced by OPLangParser#program.
    def enterProgram(self, ctx:OPLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by OPLangParser#program.
    def exitProgram(self, ctx:OPLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by OPLangParser#decl.
    def enterDecl(self, ctx:OPLangParser.DeclContext):
        pass

    # Exit a parse tree produced by OPLangParser#decl.
    def exitDecl(self, ctx:OPLangParser.DeclContext):
        pass


    # Enter a parse tree produced by OPLangParser#vardecl.
    def enterVardecl(self, ctx:OPLangParser.VardeclContext):
        pass

    # Exit a parse tree produced by OPLangParser#vardecl.
    def exitVardecl(self, ctx:OPLangParser.VardeclContext):
        pass


    # Enter a parse tree produced by OPLangParser#argdecl.
    def enterArgdecl(self, ctx:OPLangParser.ArgdeclContext):
        pass

    # Exit a parse tree produced by OPLangParser#argdecl.
    def exitArgdecl(self, ctx:OPLangParser.ArgdeclContext):
        pass


    # Enter a parse tree produced by OPLangParser#funcdecl.
    def enterFuncdecl(self, ctx:OPLangParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by OPLangParser#funcdecl.
    def exitFuncdecl(self, ctx:OPLangParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by OPLangParser#stmt.
    def enterStmt(self, ctx:OPLangParser.StmtContext):
        pass

    # Exit a parse tree produced by OPLangParser#stmt.
    def exitStmt(self, ctx:OPLangParser.StmtContext):
        pass


    # Enter a parse tree produced by OPLangParser#condition.
    def enterCondition(self, ctx:OPLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by OPLangParser#condition.
    def exitCondition(self, ctx:OPLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by OPLangParser#assignstmt.
    def enterAssignstmt(self, ctx:OPLangParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by OPLangParser#assignstmt.
    def exitAssignstmt(self, ctx:OPLangParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by OPLangParser#ifstmt.
    def enterIfstmt(self, ctx:OPLangParser.IfstmtContext):
        pass

    # Exit a parse tree produced by OPLangParser#ifstmt.
    def exitIfstmt(self, ctx:OPLangParser.IfstmtContext):
        pass


    # Enter a parse tree produced by OPLangParser#whilestmt.
    def enterWhilestmt(self, ctx:OPLangParser.WhilestmtContext):
        pass

    # Exit a parse tree produced by OPLangParser#whilestmt.
    def exitWhilestmt(self, ctx:OPLangParser.WhilestmtContext):
        pass


    # Enter a parse tree produced by OPLangParser#returnstmt.
    def enterReturnstmt(self, ctx:OPLangParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by OPLangParser#returnstmt.
    def exitReturnstmt(self, ctx:OPLangParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by OPLangParser#expr.
    def enterExpr(self, ctx:OPLangParser.ExprContext):
        pass

    # Exit a parse tree produced by OPLangParser#expr.
    def exitExpr(self, ctx:OPLangParser.ExprContext):
        pass


    # Enter a parse tree produced by OPLangParser#atom.
    def enterAtom(self, ctx:OPLangParser.AtomContext):
        pass

    # Exit a parse tree produced by OPLangParser#atom.
    def exitAtom(self, ctx:OPLangParser.AtomContext):
        pass


    # Enter a parse tree produced by OPLangParser#vartype.
    def enterVartype(self, ctx:OPLangParser.VartypeContext):
        pass

    # Exit a parse tree produced by OPLangParser#vartype.
    def exitVartype(self, ctx:OPLangParser.VartypeContext):
        pass


    # Enter a parse tree produced by OPLangParser#type.
    def enterType(self, ctx:OPLangParser.TypeContext):
        pass

    # Exit a parse tree produced by OPLangParser#type.
    def exitType(self, ctx:OPLangParser.TypeContext):
        pass



del OPLangParser