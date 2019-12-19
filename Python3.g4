grammar Python3;

tokens { INDENT, DEDENT }

/*
 * Parser rules
 */
single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE;
// function
funcdef: 'def' NAME parameters ('->' test)? ':' suite;

// parameters
parameters: '(' (argslist)? ')';
argslist: argslist_normal(',' (argslist_start | argslist_starts)?)?
    | argslist_start
    | argslist_starts;
argslist_normal: pdef ('=' test)? (',' pdef ('=' test)?)*;
argslist_start: '*' (pdef)? (',' pdef ('=' test)?)* (',' (argslist_starts)?)?;
argslist_starts: '**' pdef (',')?;
pdef: NAME;

/* statement: 组成源代码
 * simple_stmt: pass, break, continue, return...不考虑regex
 * compound_stmt: if, else, elif, for, in, while...
 */
stmt: simple_stmt | compound_stmt;

simple_stmt: small_stmt (';' small_stmt)* (';')? NEWLINE;
small_stmt: pass_stmt | flow_stmt;
pass_stmt: 'pass';
flow_stmt: break_stmt | continue_stmt | return_stmt;
break_stmt: 'break';
continue_stmt: 'continue';
return_stmt: 'return' (testlist)?;

compound_stmt: if_stmt | while_stmt | for_stmt | funcdef;
if_stmt:
    'if' test ':' suite ('elif' test ':' suite)*(
        'else' ':' suite)?;
while_stmt:
    'while' test ':' suite ('else' ':' suite)?;
for_stmt:
    'for' exprlist 'in' testlist ':' suite ('else' ':' suite)?;

/*
 * suite: 子代码块, 组成statement
 */
suite: simple_stmt | NEWLINE INDENT stmt+ DEDENT;

/*
 * testlist: statement chunck? 集合运算逻辑的块儿
 * test: judge statement 单独语句
 */
testlist: test (',' test)* (',')?;

test: or_test ('if' or_test 'else' test)?;
or_test: and_test ('or' and_test)*;
and_test: not_test ('and' not_test)*;
not_test: 'not' not_test | comparison;
// comparison: compare expression, algorithm, logical judge
// 按照优先级划分
comparison: expr (comp_op expr)*;
comp_op:
    '<' | '>' | '==' | '>=' | '<=' | '!='
    | 'in' | 'not' 'in' | 'is' | 'is' 'not';

// expr: 语句中嵌套表达式
expr: xor_expr ('|' xor_expr)*;
xor_expr: and_expr ('^' and_expr)*;
and_expr: algorithm_expr ('&' algorithm_expr)*;
algorithm_expr: term (('+' | '-') term)*;
term: factor (('*' | '/') factor)*;
factor: ('+' | '-') atom;
atom:(
    '(' (testlist_comp)? ')'
    | '[' (testlist_comp)? ']'
    | NAME
    | NUMBER
    | STRING+
    | 'None'
    | 'True'
    | 'False'
);
// testlist_comp: 不考虑复杂运算, 相当于testlist, 递归块
testlist_comp: testlist;
exprlist: (expr) (',' (expr))*;

/*
 * Lexer rules
 * 优先匹配, 最长匹配
 */

STRING : STRING_LITERAL;

NUMBER : DECIMAL_INTEGER;

// keywords
DEF : 'def';
RETURN : 'return';
IF : 'if';
ELIF : 'elif';
ELSE : 'else';
WHILE : 'while';
FOR : 'for';
IN : 'in';
OR : 'or';
AND : 'and';
NOT : 'not';
IS : 'is';
NONE : 'None';
TRUE : 'True';
FALSE : 'False';
PASS : 'pass';
CONTINUE : 'continue';
BREAK : 'break';

NEWLINE
 : ( '\r'? '\n' | '\r' | '\f' ) SPACES?
 ;

// identifier
NAME
 : ID_START ID_CONTINUE*
 ;

// stringliteral    ::=     [stringprefix] shortstring
// stringprefix     ::=     'r' | 'R'
STRING_LITERAL
 : [rR]? ( SHORT_STRING )
 ;

DECIMAL_INTEGER
 : [1-9][0-9]*
 | [0]
 ;

// characters
DOT : '.';
STAR : '*';
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
COMMA : ',';
COLON : ':';
ASSIGN : '=';
OPEN_BRACK : '[';
CLOSE_BRACK : ']';
LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ : '!=';
ADD : '+';
MINUS : '-';
DIV : '/';

SKIP_
 : ( SPACES | COMMENT | LINE_JOINING ) -> skip
 ;

/*
 * fragments
 */
fragment ID_START
 : '_' | [a-z] | [A-Z]
 ;

fragment ID_CONTINUE
 : ID_START | [0-9]
 ;

fragment SHORT_STRING
 : '\'' ( STRING_NEXTLINE | ~[\\\r\n\f'] )* '\''
 | '"' ( STRING_NEXTLINE | ~[\\\r\n\f'] )* '"'
 ;

fragment STRING_NEXTLINE
 : '\\' .
 ;

fragment SPACES
 : [ \t]+;  // space or tab

fragment COMMENT
 : '#' ~[\r\n\f]*;  // comments

fragment LINE_JOINING
 : '\\' SPACES? ( '\r'? '\n' | '\r' | '\f' );
