# Generated from /home/tdung/assignment/PPL/oplang-compiler/src/grammar/OPLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,142,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,1,3,
        1,42,8,1,1,2,1,2,1,2,1,2,3,2,48,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,58,8,3,1,4,1,4,1,4,1,4,3,4,64,8,4,1,4,1,4,3,4,68,8,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,82,8,5,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,98,8,8,1,9,1,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,114,
        8,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,122,8,11,10,11,12,11,125,
        9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,134,8,12,1,13,1,13,
        1,14,1,14,3,14,140,8,14,1,14,0,1,22,15,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,0,3,1,0,7,11,1,0,13,18,1,0,25,27,147,0,34,1,0,0,0,
        2,41,1,0,0,0,4,43,1,0,0,0,6,51,1,0,0,0,8,59,1,0,0,0,10,81,1,0,0,
        0,12,83,1,0,0,0,14,87,1,0,0,0,16,92,1,0,0,0,18,99,1,0,0,0,20,103,
        1,0,0,0,22,113,1,0,0,0,24,133,1,0,0,0,26,135,1,0,0,0,28,139,1,0,
        0,0,30,33,3,2,1,0,31,33,3,10,5,0,32,30,1,0,0,0,32,31,1,0,0,0,33,
        36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,
        0,37,38,5,0,0,1,38,1,1,0,0,0,39,42,3,4,2,0,40,42,3,8,4,0,41,39,1,
        0,0,0,41,40,1,0,0,0,42,3,1,0,0,0,43,44,3,26,13,0,44,47,5,30,0,0,
        45,46,5,12,0,0,46,48,3,22,11,0,47,45,1,0,0,0,47,48,1,0,0,0,48,49,
        1,0,0,0,49,50,5,23,0,0,50,5,1,0,0,0,51,52,3,26,13,0,52,57,5,30,0,
        0,53,54,5,24,0,0,54,55,3,26,13,0,55,56,5,30,0,0,56,58,1,0,0,0,57,
        53,1,0,0,0,57,58,1,0,0,0,58,7,1,0,0,0,59,60,3,28,14,0,60,61,5,30,
        0,0,61,63,5,19,0,0,62,64,3,6,3,0,63,62,1,0,0,0,63,64,1,0,0,0,64,
        65,1,0,0,0,65,67,5,20,0,0,66,68,3,10,5,0,67,66,1,0,0,0,67,68,1,0,
        0,0,68,9,1,0,0,0,69,82,3,4,2,0,70,82,3,14,7,0,71,82,3,16,8,0,72,
        82,3,18,9,0,73,82,3,20,10,0,74,75,3,22,11,0,75,76,5,23,0,0,76,82,
        1,0,0,0,77,78,5,21,0,0,78,79,3,10,5,0,79,80,5,22,0,0,80,82,1,0,0,
        0,81,69,1,0,0,0,81,70,1,0,0,0,81,71,1,0,0,0,81,72,1,0,0,0,81,73,
        1,0,0,0,81,74,1,0,0,0,81,77,1,0,0,0,82,11,1,0,0,0,83,84,5,19,0,0,
        84,85,3,22,11,0,85,86,5,20,0,0,86,13,1,0,0,0,87,88,5,30,0,0,88,89,
        5,12,0,0,89,90,3,22,11,0,90,91,5,23,0,0,91,15,1,0,0,0,92,93,5,3,
        0,0,93,94,3,12,6,0,94,97,3,10,5,0,95,96,5,4,0,0,96,98,3,10,5,0,97,
        95,1,0,0,0,97,98,1,0,0,0,98,17,1,0,0,0,99,100,5,5,0,0,100,101,3,
        12,6,0,101,102,3,10,5,0,102,19,1,0,0,0,103,104,5,6,0,0,104,105,3,
        22,11,0,105,106,5,23,0,0,106,21,1,0,0,0,107,108,6,11,-1,0,108,114,
        3,24,12,0,109,110,5,19,0,0,110,111,3,22,11,0,111,112,5,20,0,0,112,
        114,1,0,0,0,113,107,1,0,0,0,113,109,1,0,0,0,114,123,1,0,0,0,115,
        116,10,3,0,0,116,117,7,0,0,0,117,122,3,22,11,4,118,119,10,2,0,0,
        119,120,7,1,0,0,120,122,3,22,11,3,121,115,1,0,0,0,121,118,1,0,0,
        0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,23,1,0,0,0,
        125,123,1,0,0,0,126,134,5,31,0,0,127,134,5,32,0,0,128,134,5,30,0,
        0,129,130,5,19,0,0,130,131,3,24,12,0,131,132,5,20,0,0,132,134,1,
        0,0,0,133,126,1,0,0,0,133,127,1,0,0,0,133,128,1,0,0,0,133,129,1,
        0,0,0,134,25,1,0,0,0,135,136,7,2,0,0,136,27,1,0,0,0,137,140,3,26,
        13,0,138,140,5,28,0,0,139,137,1,0,0,0,139,138,1,0,0,0,140,29,1,0,
        0,0,14,32,34,41,47,57,63,67,81,97,113,121,123,133,139
    ]

class OPLangParser ( Parser ):

    grammarFileName = "OPLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'func'", "'if'", "'else'", "'while'", 
                     "'return'", "'+'", "'-'", "'*'", "'/'", "'mod'", "'='", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'('", 
                     "')'", "'{'", "'}'", "';'", "','", "'int'", "'char'", 
                     "'bool'", "'void'", "'string'" ]

    symbolicNames = [ "<INVALID>", "VAR", "FUNC", "IF", "ELSE", "WHILE", 
                      "RETURN", "PLUS", "MINUS", "MUL", "DIV", "MOD", "ASSIGN", 
                      "EQ", "NEQ", "LT", "GT", "LEQ", "GEQ", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "SEMICOLON", "COMMA", "INT", "CHAR", 
                      "BOOL", "VOID", "STRING", "ID", "INTLIT", "STRINGLIT", 
                      "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_argdecl = 3
    RULE_funcdecl = 4
    RULE_stmt = 5
    RULE_condition = 6
    RULE_assignstmt = 7
    RULE_ifstmt = 8
    RULE_whilestmt = 9
    RULE_returnstmt = 10
    RULE_expr = 11
    RULE_atom = 12
    RULE_vartype = 13
    RULE_type = 14

    ruleNames =  [ "program", "decl", "vardecl", "argdecl", "funcdecl", 
                   "stmt", "condition", "assignstmt", "ifstmt", "whilestmt", 
                   "returnstmt", "expr", "atom", "vartype", "type" ]

    EOF = Token.EOF
    VAR=1
    FUNC=2
    IF=3
    ELSE=4
    WHILE=5
    RETURN=6
    PLUS=7
    MINUS=8
    MUL=9
    DIV=10
    MOD=11
    ASSIGN=12
    EQ=13
    NEQ=14
    LT=15
    GT=16
    LEQ=17
    GEQ=18
    LPAREN=19
    RPAREN=20
    LBRACE=21
    RBRACE=22
    SEMICOLON=23
    COMMA=24
    INT=25
    CHAR=26
    BOOL=27
    VOID=28
    STRING=29
    ID=30
    INTLIT=31
    STRINGLIT=32
    WS=33
    ERROR_CHAR=34
    ILLEGAL_ESCAPE=35
    UNCLOSE_STRING=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OPLangParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.DeclContext)
            else:
                return self.getTypedRuleContext(OPLangParser.DeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(OPLangParser.StmtContext,i)


        def getRuleIndex(self):
            return OPLangParser.RULE_program




    def program(self):

        localctx = OPLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8022130792) != 0):
                self.state = 32
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.decl()
                    pass

                elif la_ == 2:
                    self.state = 31
                    self.stmt()
                    pass


                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(OPLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(OPLangParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(OPLangParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_decl




    def decl(self):

        localctx = OPLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(OPLangParser.VartypeContext,0)


        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(OPLangParser.SEMICOLON, 0)

        def ASSIGN(self):
            return self.getToken(OPLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_vardecl




    def vardecl(self):

        localctx = OPLangParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.vartype()
            self.state = 44
            self.match(OPLangParser.ID)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 45
                self.match(OPLangParser.ASSIGN)
                self.state = 46
                self.expr(0)


            self.state = 49
            self.match(OPLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.VartypeContext)
            else:
                return self.getTypedRuleContext(OPLangParser.VartypeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.ID)
            else:
                return self.getToken(OPLangParser.ID, i)

        def COMMA(self):
            return self.getToken(OPLangParser.COMMA, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_argdecl




    def argdecl(self):

        localctx = OPLangParser.ArgdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_argdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.vartype()
            self.state = 52
            self.match(OPLangParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 53
                self.match(OPLangParser.COMMA)
                self.state = 54
                self.vartype()
                self.state = 55
                self.match(OPLangParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(OPLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def argdecl(self):
            return self.getTypedRuleContext(OPLangParser.ArgdeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(OPLangParser.StmtContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_funcdecl




    def funcdecl(self):

        localctx = OPLangParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.type_()
            self.state = 60
            self.match(OPLangParser.ID)
            self.state = 61
            self.match(OPLangParser.LPAREN)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0):
                self.state = 62
                self.argdecl()


            self.state = 65
            self.match(OPLangParser.RPAREN)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 66
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(OPLangParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(OPLangParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(OPLangParser.IfstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(OPLangParser.WhilestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(OPLangParser.ReturnstmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(OPLangParser.SEMICOLON, 0)

        def LBRACE(self):
            return self.getToken(OPLangParser.LBRACE, 0)

        def stmt(self):
            return self.getTypedRuleContext(OPLangParser.StmtContext,0)


        def RBRACE(self):
            return self.getToken(OPLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_stmt




    def stmt(self):

        localctx = OPLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.returnstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.expr(0)
                self.state = 75
                self.match(OPLangParser.SEMICOLON)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.match(OPLangParser.LBRACE)
                self.state = 78
                self.stmt()
                self.state = 79
                self.match(OPLangParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_condition




    def condition(self):

        localctx = OPLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(OPLangParser.LPAREN)
            self.state = 84
            self.expr(0)
            self.state = 85
            self.match(OPLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(OPLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(OPLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_assignstmt




    def assignstmt(self):

        localctx = OPLangParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(OPLangParser.ID)
            self.state = 88
            self.match(OPLangParser.ASSIGN)
            self.state = 89
            self.expr(0)
            self.state = 90
            self.match(OPLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(OPLangParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(OPLangParser.ConditionContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(OPLangParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(OPLangParser.ELSE, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_ifstmt




    def ifstmt(self):

        localctx = OPLangParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(OPLangParser.IF)
            self.state = 93
            self.condition()
            self.state = 94
            self.stmt()
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 95
                self.match(OPLangParser.ELSE)
                self.state = 96
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(OPLangParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(OPLangParser.ConditionContext,0)


        def stmt(self):
            return self.getTypedRuleContext(OPLangParser.StmtContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_whilestmt




    def whilestmt(self):

        localctx = OPLangParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(OPLangParser.WHILE)
            self.state = 100
            self.condition()
            self.state = 101
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(OPLangParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(OPLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_returnstmt




    def returnstmt(self):

        localctx = OPLangParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(OPLangParser.RETURN)
            self.state = 104
            self.expr(0)
            self.state = 105
            self.match(OPLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(OPLangParser.AtomContext,0)


        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def PLUS(self):
            return self.getToken(OPLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(OPLangParser.MINUS, 0)

        def MUL(self):
            return self.getToken(OPLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(OPLangParser.DIV, 0)

        def MOD(self):
            return self.getToken(OPLangParser.MOD, 0)

        def EQ(self):
            return self.getToken(OPLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(OPLangParser.NEQ, 0)

        def LT(self):
            return self.getToken(OPLangParser.LT, 0)

        def LEQ(self):
            return self.getToken(OPLangParser.LEQ, 0)

        def GT(self):
            return self.getToken(OPLangParser.GT, 0)

        def GEQ(self):
            return self.getToken(OPLangParser.GEQ, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OPLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 108
                self.atom()
                pass

            elif la_ == 2:
                self.state = 109
                self.match(OPLangParser.LPAREN)
                self.state = 110
                self.expr(0)
                self.state = 111
                self.match(OPLangParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 121
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 115
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 116
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3968) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 117
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 118
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 119
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 120
                        self.expr(3)
                        pass

             
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(OPLangParser.INTLIT, 0)

        def STRINGLIT(self):
            return self.getToken(OPLangParser.STRINGLIT, 0)

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(OPLangParser.AtomContext,0)


        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_atom




    def atom(self):

        localctx = OPLangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_atom)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(OPLangParser.INTLIT)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(OPLangParser.STRINGLIT)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.match(OPLangParser.ID)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.match(OPLangParser.LPAREN)
                self.state = 130
                self.atom()
                self.state = 131
                self.match(OPLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(OPLangParser.INT, 0)

        def CHAR(self):
            return self.getToken(OPLangParser.CHAR, 0)

        def BOOL(self):
            return self.getToken(OPLangParser.BOOL, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_vartype




    def vartype(self):

        localctx = OPLangParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(OPLangParser.VartypeContext,0)


        def VOID(self):
            return self.getToken(OPLangParser.VOID, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_type




    def type_(self):

        localctx = OPLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.vartype()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(OPLangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




