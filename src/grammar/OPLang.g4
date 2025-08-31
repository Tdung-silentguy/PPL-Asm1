grammar OPLang;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// LEXICAL RULES ----------
// keywords
VAR      : 'var';
FUNC     : 'func';
IF       : 'if';
ELSE     : 'else';
WHILE    : 'while';
RETURN   : 'return';
// operators
PLUS     : '+';
MINUS    : '-';
MUL      : '*';
DIV      : '/';
MOD: 'mod';
ASSIGN   : '=';
EQ       : '==';
NEQ: '!=';
LT       : '<';
GT       : '>';
LEQ: '<=';
GEQ: '>=';
// brackets
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMICOLON: ';';
COMMA: ',';
// types
INT: 'int';
CHAR: 'char';
BOOL: 'bool';
VOID: 'void';
STRING: 'string';
// escape sequences
escseq  : NEWLINE
        | HTAB
        | BACKSLASH
        | SINGLEQUOTE
        | DOUBLEQUOTE;
NEWLINE: '\n';
HTAB: '\t';
BACKSLASH: '\\';
SINGLEQUOTE: '\'';
DOUBLEQUOTE: '\"';


// id & literals
ID       : [a-zA-Z_][a-zA-Z0-9_]*;
INTLIT   : [0-9]+;                      // integer literal
STRINGLIT: '"' (~["\\] | '\\' .)* '"';  // string literal
// whitespace
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs 
// exceptions
ERROR_CHAR: [^\x00-\x7F]; // non-ASCII character
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;


// SYNTAX (PARSER) RULES -------

// Entry point
program: (decl | stmt)* EOF; // write for program rule here using vardecl and funcdecl

// Declarations
decl: vardecl | funcdecl;

vardecl: vartype ID (ASSIGN expr)? SEMICOLON;

argdecl: vartype ID (COMMA vartype ID)?;
funcdecl: type ID LPAREN argdecl? RPAREN stmt?;


// Statements
stmt: vardecl
    | assignstmt
    | ifstmt
    | whilestmt
    | returnstmt
    | expr SEMICOLON
    | LBRACE stmt RBRACE;

condition: LPAREN expr RPAREN;

assignstmt: ID ASSIGN expr SEMICOLON;
ifstmt: IF condition stmt (ELSE stmt)?;
whilestmt: WHILE condition stmt;
returnstmt: RETURN expr SEMICOLON;


// Expression
expr: atom
    | expr (PLUS|MINUS|MUL|DIV|MOD) expr
    | expr (EQ|NEQ|LT|LEQ|GT|GEQ) expr
    | LPAREN expr RPAREN;
atom: INTLIT
    | STRINGLIT
    | ID
    | LPAREN atom RPAREN;

// Data type

vartype : INT
        | CHAR
        | BOOL;
type: vartype | VOID;