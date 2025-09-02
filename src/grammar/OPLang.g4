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
// preserved keywords (not including keywords used as operators, types, etc.)
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FALSE: 'false';
FINAL: 'final';
FOR: 'for';
IF: 'if';
NIL: 'nil';
RETURN: 'return';
STATIC: 'static';
THEN: 'then';
THIS: 'this';
TO: 'to';
TRUE: 'true';
DOWNTO: 'downto';
// keywords that can be used as ID
WHILE: 'while';
OTHER: 'other'; // used in constrdecl
// operators
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LEQ: '<=';
GEQ: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCAT: '^';
NEW: 'new';

ASSIGN: ':=';
// separators
LBRAC: '(';
RBRAC: ')';
LSQBRAC: '[';
RSQBRAC: ']';
LPAREN: '{';
RPAREN: '}';
SEMICOLON: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
// other marks
TILDE: '~';
BLOCKCMTOPEN: '/*';
BLOCKCMTCLOSE: '*/';
LINECMTMARK: '//';
NUMBERSIGN: '#';
// types
INT: 'int';
CHAR: 'char';
BOOL: 'bool';
VOID: 'void';
STRING: 'string';
FLOAT: 'float';
// Escape sequence
fragment ESCSEQPART: [bfrnt"\\];
fragment NOTESCSEQPART: ~[bfrnt"\\];
fragment ESCSEQ: '\\' ESCSEQPART;
// fragment là một bộ phận cấu thành của một token, ko thể làm một token đứng độc lập

// id & literals
ID: [a-zA-Z_][a-zA-Z0-9_]*;
// literals
literal : INTLIT
        | FLOATLIT
        | BOOLLIT
        | STRINGLIT
        | ELELIT
        | ARRAYLIT
        | LINECMTLIT
        | BLOCKCMTLIT;
INTLIT: [0-9]+;                      // integer literal
FLOATLIT: [0-9]+ ('.' [0-9]*)? (('E'|'e') ('+'|'-')? [0-9]+)?;
BOOLLIT: TRUE | FALSE;
STRINGLIT: '"' ( ~["\\] | ESCSEQ )* '"';  // each character is either an escape sequence or not
ELELIT: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT; // element literal
ARRAYLIT: LPAREN ELELIT (COMMA ELELIT)* RPAREN; // array literal

LINECMTLIT: '#' . (EOF | '\n');
BLOCKCMTLIT: BLOCKCMTOPEN . (EOF | BLOCKCMTCLOSE);
// whitespace



WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs 
// exceptions
ERROR_CHAR:  ~[\u0000-\u007F]; // a non-ASCII character
// Character set is ASCII
ILLEGAL_ESCAPE: '\\' NOTESCSEQPART; // a \\ followed by a char not in ESCSEQPART
UNCLOSE_STRING: '"' (~["\\\n\r] | '\\' .)*;
// This is similar to STRINGLIT, but without ending doublequote.
// It ends at \n or EOF (not accepting it by ~["\\\n\r])
// This is only considered after STRINGLIT
// --- I still can't figure out a way to not include the opening '"', despite requirements.


// SYNTAX (PARSER) RULES -------

// Entry point
program: (decl | stmt)* EOF; // write for program rule here using vardecl and funcdecl

// Data type
vartype : INT
        | FLOAT
        | BOOL
        | STRING;
reftype: vartype '&';
returntype: vartype | VOID; // return types
refreturntype: returntype '&';
type: vartype | CLASS;


// Declarations
decl: classdecl | memdecl;

classdecl: CLASS ID (EXTENDS ID)? LPAREN (memdecl)* RPAREN;

memdecl: ((STATIC? FINAL?) | (FINAL? STATIC?)) (vardecl | funcdecl | constrdecl | destrdecl);
// with vardecl it's an attribute, with funcdecl it's a method
vardecl: vartype ID (ASSIGN expr)? SEMICOLON;
arraydecl: vartype LSQBRAC INTLIT RSQBRAC ID SEMICOLON;

argdecl: vartype ID (SEMICOLON vartype ID)*;
funcdecl: (returntype | refreturntype) ID LBRAC argdecl? RBRAC stmt;
// constructor & destructor
constrdecl: ID LBRAC ((ID OTHER) | argdecl)? LBRAC;
destrdecl: TILDE ID LBRAC LBRAC stmt;


// Expression
expr: atomicexpr
    | arithmeticexpr
    | booleanexpr
    | relationalexpr
    | stringexpr
    | indexexpr
    | LBRAC expr RBRAC;

atomicexpr  : ID
            | literal;
//    | LBRAC atom RBRAC;
arithmeticexpr: signidentity
    | signnegation
    | add
    | sub
    | mul
    | floatdiv
    | intdiv
    | remainder;
signidentity: PLUS (ID|INTLIT|FLOATLIT);
signnegation: MINUS (ID|INTLIT|FLOATLIT);
add: (ID|INTLIT|FLOATLIT) PLUS (ID|INTLIT|FLOATLIT);
sub: (ID|INTLIT|FLOATLIT) MINUS (ID|INTLIT|FLOATLIT);
mul: (ID|INTLIT|FLOATLIT) MUL (ID|INTLIT|FLOATLIT);
floatdiv: (ID|INTLIT|FLOATLIT) DIV (ID|INTLIT|FLOATLIT);
intdiv: (ID|INTLIT|FLOATLIT) '\\' (ID|INTLIT|FLOATLIT);
remainder: (ID|INTLIT|FLOATLIT) MOD (ID|INTLIT|FLOATLIT);
booleanexpr : and
            | or
            | not;
and: (ID|BOOLLIT) AND (ID|BOOLLIT);
or: (ID|BOOLLIT) OR (ID|BOOLLIT);
not: NOT (ID|BOOLLIT);
relationalexpr  : eq
                | neq
                | gt 
                | lt
                | geq
                | leq;
eq: (ID|literal) EQ (ID|literal);
neq: (ID|literal) NEQ (ID|literal);
gt: (ID|literal) LT (ID|literal);
lt: (ID|literal) LT (ID|literal);
geq: (ID|literal) GEQ (ID|literal);
leq: (ID|literal) LEQ (ID|literal);

stringexpr: (ID | STRINGLIT) CONCAT (ID | STRINGLIT);
indexexpr: expr LSQBRAC expr RSQBRAC;
accessexpr  : instanceatrb
            | instancemeth
            | staticatrb
            | staticmeth;
instanceatrb: expr DOT ID;
staticatrb: ID DOT ID;
instancemeth: expr DOT ID LBRAC (expr (COMMA expr)*)? RBRAC;
staticmeth: ID DOT ID LBRAC (expr (COMMA expr)*)? RBRAC;

objcreation: NEW ID LBRAC (expr (COMMA expr)*)? RBRAC;

// Statements
stmt: vardecl
    | arraydecl
    | refdecl
    | assignstmt
    | ifstmt
    | forstmt
    | breakstmt
    | continuestmt
    | whilestmt
    | returnstmt
    | expr SEMICOLON
    | LPAREN stmt RPAREN;


assignstmt: ID ASSIGN expr SEMICOLON;
refdecl: reftype '&' ID ASSIGN expr;
ifstmt: IF expr THEN stmt (ELSE stmt)?;
forstmt: FOR ID ASSIGN expr (TO|DOWNTO) expr DO stmt;
whilestmt: WHILE expr stmt;

breakstmt: BREAK SEMICOLON;
continuestmt: CONTINUE SEMICOLON;
returnstmt: RETURN expr SEMICOLON;
methodcall: (staticmeth | instancemeth) SEMICOLON;