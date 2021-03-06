grammar D96;
// Võ Minh Toàn - 1915570
@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: code_declares+ EOF;
//////////////////////////////// declaration //////////////////////////////////
code_declares:
	CLASS IDENTIFIERS (COLON class_type)? LP class_body* RP;

class_body:
	method_declare
	| class_attribute_declare
	| special_init_method_declare;

class_attribute_declare: (VAL | VAR) attr_decl SEMI;

// Constructor & Destructor
special_init_method_declare:
	(CONSTRUCTOR LB param_list? | DESTRUCTOR LB) RB block_stmt;

method_declare:
	STATIC_MEM LB param_list? RB block_stmt
	| IDENTIFIERS LB param_list? RB block_stmt;

attr_decl: (id_list COLON all_type) | mid2;

id_list: (IDENTIFIERS | STATIC_MEM) (
		COMMA (IDENTIFIERS | STATIC_MEM)
	)*;

mid2:
	STATIC_MEM COMMA mid2 COMMA expression
	| IDENTIFIERS COMMA mid2 COMMA expression
	| STATIC_MEM mid1 expression
	| IDENTIFIERS mid1 expression;

mid1: COLON all_type ASSOP;

param_list: param (SEMI param)*;
param: IDENTIFIERS (COMMA IDENTIFIERS)* COLON all_type;
/////////////////////////// EXPRESSION //////////////////////////
expression:
	expression1 (CONCAT | STRCMP) expression1
	| expression1; // String expression
expression1:
	expression2 (GRTOP | GTEOP | LSTOP | LTEOP | EQLOP | IEQOP) expression2
	| expression2; // > >= < <= == != expression
expression2:
	expression2 (ANDOP | OROP) expression3
	| expression3; // && || expression
expression3:
	expression3 (ADDOP | SUBOP) expression4
	| expression4; // +- expression
expression4:
	expression4 (MULOP | DIVOP | MODOP) expression5
	| expression5; // */% expression
expression5: NOTOP expression5 | expression6; // ! expression
expression6: SUBOP expression6 | expression7; // - expression
expression7:
	expression7 LSB expression RSB
	| expression8; // [] expression

expression8:
	expression8 DOTOP IDENTIFIERS (LSB expression RSB)*
	| expression8 DOTOP IDENTIFIERS LB (expression_list)? RB
	| expression9;

expression9:
	IDENTIFIERS SCOOP STATIC_MEM (LSB expression RSB)*
	| IDENTIFIERS SCOOP STATIC_MEM LB (expression_list)? RB
	| expression10;

expression10: NEW IDENTIFIERS LB expression_list? RB | operand;

operand:
	IDENTIFIERS
	| literals
	| SELF
	| NULL
	| LB expression RB
	| IDENTIFIERS (LSB expression RSB)*;

expression_list: expression (COMMA expression)*;
////////////////////////END EXPRESSION //////////////////////////

////////////////////////////////////////////////////////////////////////
// //////////////////////// statement ///////////////////////////////////
// //////////////////////////////////////////////////////////////////////
var_declare_stmt: var_attr_stmt | val_attr_stmt;
var_attr_stmt: VAR attr_stmt SEMI;
val_attr_stmt: VAL attr_stmt SEMI;

attr_stmt: attr_stmt_no_init | attr_stmt_full;

attr_stmt_no_init: id_list_without_static COLON all_type;

id_list_without_static:
	IDENTIFIERS COMMA id_list_without_static
	| IDENTIFIERS;

attr_stmt_full:
	IDENTIFIERS COMMA attr_stmt_full COMMA expression
	| IDENTIFIERS mid1 expression;

block_stmt: LP stmt3* RP;

stmt3:
	var_declare_stmt
	| assign_stmt
	| if_stmt
	| for_stmt
	| block_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| invoca_stmt;

assign_stmt: lhs ASSOP expression SEMI;

lhs: IDENTIFIERS (LSB expression8 RSB)* | expression8;

if_stmt:
	IF LB expression RB block_stmt (
		ELSEIF LB expression RB block_stmt
	)* (ELSE block_stmt)?;

for_stmt:
	FOREACH LB IDENTIFIERS IN (INTLIT | expression) DOTDOT (
		INTLIT
		| expression
	) (BY (INTLIT | expression))? RB block_stmt;

break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI;
return_stmt: RETURN expression SEMI | RETURN SEMI;

invoca_stmt:
	class_type SCOOP STATIC_MEM LB expression_list? RB SEMI
	| expression8 DOTOP IDENTIFIERS LB expression_list? RB SEMI;

// type
all_type: prim_type | arr_type | class_type;
prim_type: int_type | float_type | boolean_type | string_type;

arr_type: ARRAY LSB (prim_type | arr_type) COMMA NZINTLIT RSB;

class_type: IDENTIFIERS;
int_type: INT;
float_type: FLOAT;
string_type: STRING;
boolean_type: BOOLEAN;

// literals integer
fragment NZDECIMAL: [1-9]('_'? [0-9])*;
fragment NZBINARY: '0' [bB] '1' ('_'? [01])*;
fragment NZOCTAL: '0' [1-7]('_'? [0-7])*;
fragment NZHEXA: '0' [xX] [1-9A-F]('_'? [0-9A-F])*;
NZINTLIT: (NZDECIMAL | NZBINARY | NZOCTAL | NZHEXA) {
	self.text = self.text.replace("_", "")
};
INTLIT: (
		NZDECIMAL
		| NZBINARY
		| NZOCTAL
		| NZHEXA
		| '0'
		| '0' [Xx] '0'
		| '0' [bB] '0'
		| '00'
	) {
	self.text = self.text.replace("_", "")
};
// float
fragment EXP: [Ee][+-]? [0-9]+;
fragment DEC_FLOAT: '.' [0-9]*;
FLOATLIT: (
		(NZDECIMAL | '0') DEC_FLOAT EXP
		| (NZDECIMAL | '0') DEC_FLOAT
		| (NZDECIMAL | '0') EXP
		| DEC_FLOAT EXP
	) {
	self.text = self.text.replace("_", "")
};

BOOLIT: TRUE | FALSE;

fragment ESCAPE_SEQUENCES:
	'\\b'
	| '\\f'
	| '\\n'
	| '\\r'
	| '\\t'
	| '\\\\'
	| '\\' ['];
fragment ILLEGAL_ESC_SEQ: '\\' ~[bfnrt'"\\] | '\\' | [']["];
fragment CHARACTER: ~(["\r\n\f\t\b] | '\\') | ESCAPE_SEQUENCES;
STRINGLIT: (["] (CHARACTER | [']["])* ["]) {
	self.text = self.text[1:-1]
};

primitive_type:
	INTLIT
	| NZINTLIT
	| FLOATLIT
	| STRINGLIT
	| BOOLIT;

indexed_array: ARRAY LB (array_member |) RB;
array_member: (primitive_type | expression) (COMMA array_member)*;

multi_array: multi_in_multi | index_in_multi | empty_multi;

multi_in_multi: ARRAY LB multi_arrays RB;
index_in_multi: ARRAY LB multi_array_mem RB;
empty_multi: ARRAY LB RB;

multi_arrays: multi_array COMMA multi_arrays | multi_array;
multi_array_mem: indexed_array (COMMA multi_array_mem)*;

literals: primitive_type | indexed_array | multi_array;

// Scope
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
COLON: ':';
SEMI: ';';
COMMA: ',';

// keywords
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
SELF: 'Self';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';

// operators
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
NOTOP: '!';
ANDOP: '&&';
OROP: '||';
EQLOP: '==';
ASSOP: '=';
IEQOP: '!=';
GRTOP: '>';
LSTOP: '<';
GTEOP: '>=';
LTEOP: '<=';
STRCMP: '==.';
CONCAT: '+.';
DOTDOT: '..';
DOTOP: '.';
SCOOP: '::';

IDENTIFIERS: [_a-zA-Z][0-9a-zA-Z_]*;
STATIC_MEM: '$' [_0-9a-zA-Z]+;

COMMENT: '##' .*? '##' -> skip; // non-greedy
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING:
	["] (CHARACTER | ILLEGAL_ESC_SEQ)* (EOF | '\r' | '\f' | '\n') {
		y = self.text
		if y[-1] in ['\r','\n','\f']:
				raise UncloseString(y[1:-1])
		else:
				raise UncloseString(y[1:])
	};
ILLEGAL_ESCAPE: (
		["] (CHARACTER | ['] ["])* (
			ILLEGAL_ESC_SEQ
			| '\t'
			| '\b'
		)
	) {
			raise IllegalEscape(self.text[1:]);
		};
ERROR_CHAR: .{raise ErrorToken(self.text)};