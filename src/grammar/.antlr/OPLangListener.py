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



del OPLangParser