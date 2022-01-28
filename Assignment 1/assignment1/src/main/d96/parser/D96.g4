grammar D96;
// Võ Minh Toàn - 1915570
@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: code_declares+ EOF;

////////////////////////////////////////////////////////////////////////
// ////////////////////// declaration ///////////////////////////////////
// //////////////////////////////////////////////////////////////////////

code_declares:
	CLASS IDENTIFIERS (COLON class_type)? LP class_body* RP;

class_body:
	method_declare
	| class_attr_declare
	| special_init_method_declare;

class_attr_declare: (VAL | VAR) attr_decl SEMI;

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

method_id_list: IDENTIFIERS (COMMA IDENTIFIERS)*;

mid2:
	STATIC_MEM COMMA mid2 COMMA expr
	| IDENTIFIERS COMMA mid2 COMMA expr
	| STATIC_MEM mid1 expr
	| IDENTIFIERS mid1 expr;

mid1: COLON all_type ASSOP;

param_list: param (SEMI param)*;
param: method_id_list COLON all_type;
////////////////////////////////////////////////////////////////////////
// //////////////////////// statement ///////////////////////////////////
// //////////////////////////////////////////////////////////////////////
var_declare_stmt: (VAL | VAR) attr_decl2 SEMI;
attr_decl2: id_list2 COLON all_type | mid3;
mid3: IDENTIFIERS COMMA mid3 COMMA expr | IDENTIFIERS mid1 expr;
id_list2: IDENTIFIERS COMMA id_list2 | IDENTIFIERS;

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

assign_stmt: lhs ASSOP expr SEMI;

if_stmt:
	IF LB expr RB block_stmt (ELSEIF expr block_stmt)* (
		ELSE block_stmt
	)?;

for_stmt:
	FOREACH LB IDENTIFIERS IN (INTLIT | expr) '..' (
		INTLIT
		| expr
	) (BY (INTLIT | expr))? RB block_stmt;

break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI;
return_stmt: RETURN expr SEMI | RETURN SEMI;

invoca_stmt:
	class_type SCOOP STATIC_MEM LB list_expr RB SEMI
	| class_type SCOOP STATIC_MEM LB RB SEMI
	| expr8 DOTOP IDENTIFIERS LB list_expr RB SEMI
	| expr8 DOTOP IDENTIFIERS LB RB SEMI;

lhs: IDENTIFIERS (LSB expr8 RSB)* | expr8;

////////////////////////////////////////////////////////////////////////
// //////////////////////// expression //////////////////////////////////
// //////////////////////////////////////////////////////////////////////

expr_op: CONCAT | STRCMP;
expr1_op: GRTOP | GTEOP | LSTOP | LTEOP | EQLOP | IEQOP;
expr2_op: ANDOP | OROP;
expr3_op: ADDOP | SUBOP;
expr4_op: MULOP | DIVOP | MODOP;
expr5_op: NOTOP;
expr6_op: SUBOP;
expr7_op: LSB expr RSB;

expr: expr1 expr_op expr1 | expr1;
expr1: expr2 expr1_op expr2 | expr2;
expr2: expr2 expr2_op expr3 | expr3;
expr3: expr3 expr3_op expr4 | expr4; //binary
expr4: expr4 expr4_op expr5 | expr5;
expr5: expr5_op expr5 | expr6;
expr6: expr6_op expr6 | expr7; //unary
expr7: expr7 expr7_op | expr8;

expr8:
	expr8 DOTOP IDENTIFIERS LB list_expr RB
	| expr8 DOTOP IDENTIFIERS LB RB
	| expr8 DOTOP IDENTIFIERS
	| expr8 DOTOP IDENTIFIERS (LSB expr RSB)*
	| expr9;
expr9:
	| IDENTIFIERS SCOOP STATIC_MEM LB list_expr RB
	| IDENTIFIERS SCOOP STATIC_MEM LB RB
	| IDENTIFIERS SCOOP STATIC_MEM
	| IDENTIFIERS SCOOP STATIC_MEM (LSB expr RSB)*
	| expr10;

expr10:
	NEW IDENTIFIERS LB list_expr RB
	| NEW IDENTIFIERS LB RB
	| operand;

operand:
	literals
	| SELF
	| NULL
	| LB expr RB
	| IDENTIFIERS (LSB expr RSB)*;

list_expr: expr COMMA list_expr | expr;

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
fragment ILLEGAL_ESC_SEQ: '\\' ~[bfnrt'"\\] | '\\';
fragment CHARACTER: ~(["\r\n\f] | '\\') | ESCAPE_SEQUENCES;
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
array_member: (primitive_type | expr) (COMMA array_member)*;

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
DOTOP: '.';
SCOOP: '::';

IDENTIFIERS: [_a-zA-Z][0-9a-zA-Z_]*;
STATIC_MEM: '$' [_0-9a-zA-Z]+;

COMMENT: '##' .*? '##' -> skip; // non-greedy
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING:
	["] (CHARACTER | ILLEGAL_ESC_SEQ | [']["])* ([\r\n\f] | EOF) {
                    y = self.text
                    if y[-1] in ['\r','\n','\f']:
                        raise UncloseString(y[1:-1])
                    else:
                        raise UncloseString(y[1:])
                };
ILLEGAL_ESCAPE: (["] (CHARACTER | ['] ["])* ILLEGAL_ESC_SEQ) {
					raise IllegalEscape(self.text[1:]);
				};
ERROR_CHAR: .{raise ErrorToken(self.text)};