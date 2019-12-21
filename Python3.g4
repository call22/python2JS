grammar Python3;

tokens { INDENT, DEDENT}

@lexer::header{
from Python3Parser import Python3Parser
from antlr4.Token import *
}

@lexer::members{
    self.lastToken = None
    self.tokens = []
    self.indentStack = []

def emit(self,t=None):
    if t == None :
        s = self._factory.create(self._tokenFactorySourcePair, self._type, self._text, self._channel, self._tokenStartCharIndex,
                                 self.getCharIndex()-1, self._tokenStartLine, self._tokenStartColumn)
        self.emitToken(s)
        self.tokens.append(s)
        return s
    else:
        self.emitToken(t)
        self.tokens.append(t)
        return t

def commonToken(self,type,text):
    stop = self.getCharIndex()-1
    if len(text)==0 :
        start = stop
    else:
        start = stop - len(text)+1
    return CommonToken(self._tokenFactorySourcePair,type,self.DEFAULT_TOKEN_CHANNEL,start,stop)

def createDedent(self):
    dedent = self.commonToken(Python3Parser.DEDENT,'')
    dedent.line = self.lastToken.line
    return dedent

@staticmethod
def getIndentationCount(spaces):
    count = 0
    for ch in spaces:
        if ch == '\t':
            count +=( 4 - (count%4))
        elif ch == ' ':
            count += 1
        else :
            pass
    return count

def nextToken(self):
    # Check if the end-of-file is ahead and there are still some DEDENTS expected
    if(self._input.LA(1)==Token.EOF and len(self.indentStack)!=0):
        # Remove ant trailing EOF tokens from our buffer
        i = len(self.tokens)-1
        while i>= 0 :
            if(self.tokens[i].type==Token.EOF):
                self.tokens.pop(i)
            i-=1
        # First emit an extra line break that serves as the end of the stmt
        self.emit(self.commonToken(Python3Parser.NEWLINE,'\n'))
        # Now emit as much DEDENT tokens as needed
        while len(self.indentStack)!=0 :
            self.emit(self.createDedent())
            self.indentStack.pop()
        # put the EOF back on the token stream .
        self.emit(self.commonToken(Python3Parser.EOF,'<EOF>'))
    next = super().nextToken()
    if (next.channel == Token.DEFAULT_CHANNEL):
        # Keep track of the last token on the default channel
        self.lastToken = next
    if len(self.tokens) == 0 :
        return next
    else :
        temp = self.tokens[0]
        self.tokens.pop(0)
        return temp

def atStartOfInput(self):
    if super().getCharIndex()==0 and super().line==1 :
        return True
    else:
        return False
}
/*
 * Parser rules
 */
//parse:(single_input)* EOF;

parse: single_input | file_input | eval_input;

single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE;
file_input: (NEWLINE | stmt)* EOF;
eval_input: testlist NEWLINE* EOF;

/* statement: 组成源代码
 * simple_stmt: pass, break, continue, return...不考虑regex
 * compound_stmt: if, else, elif, for, in, while...
 */
stmt: simple_stmt | compound_stmt;

simple_stmt: small_stmt (';' small_stmt)* (';')? NEWLINE;
small_stmt: (expr_stmt | pass_stmt | flow_stmt);

expr_stmt: testlist (annassign | augassign testlist | ('=' testlist)*);
annassign: ':' test ('=' test)?;
augassign: ('+=' | '-=' | '*=' | '@=' | '/=' | '%=' | '&=' | '|=' | '^=' |
            '<<=' | '>>=' | '**=' | '//=');
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
pdef: NAME (':' test)?;


/*
 * suite: 子代码块, 组成statement
 */
suite: simple_stmt | NEWLINE INDENT stmt+ DEDENT;

/*
 * testlist: statement chunck? 集合运算逻辑的块儿
 * test: judge statement 单独语句
 */

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
term: factor (('*' | '/' | '%' | '//' ) factor)*;
factor: ('+' | '-' | '~') factor | power;
power: atom_expr ('**' factor)?;
atom_expr: atom trailer*;
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
trailer: '(' (arglist)? ')' | '[' subscriptlist ']' | '.' NAME;
subscriptlist: subscript (',' subscript)* (',')?;
subscript: test | (test)? ':' (test)? (sliceop)?;
sliceop: ':' (test)?;
exprlist: (expr) (',' (expr))*;
testlist: test (',' test)* (',')?;

// 调用函数
arglist: argument (',' argument)*  (',')?;
argument: ( test | test '=' test | '**' test | '*' test);
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
 :  ( {self.atStartOfInput()}? SPACES
    | ( '\r'? '\n' | '\r' | '\f' ) SPACES?)
    {
        newLine = self.text
        for i in newLine :
            if i == '\r' or i == '\n' or i == '\f':
                pass
            else:
                newLine.replace(str(i),'')

        spaces = self.text.replace('\r','')
        spaces = self.text.replace('\n','')
        spaces = self.text.replace('\f','')

        next = self._input.LA(1)

        if(next=='\r' or next == '\n' or next == '\f' or next == '<EOF>'):
            self.skip()
        else:
            self.emit(self.commonToken(self.NEWLINE,newLine))
            indent = self.getIndentationCount(spaces)
            previous = 0
            if len(self.indentStack) != 0 :
                previous = self.indentStack.pop()
                self.indentStack.append(previous)
                # it is equal to indentStack.peek()
            if indent==previous :
                # skip indents of the same size as the present indent-size
                self.skip()
            elif indent > previous :
                self.indentStack.append(indent)
                self.emit(self.commonToken(Python3Parser.INDENT,spaces))
            else:
                # Possibly emit more than 1 DEDENT token
                while len(self.indentStack)!=0 and self.indentStack[len(self.indentStack)-1]>indent:
                    self.emit(self.createDedent())
                    self.indentStack.pop()
    }
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
 : ( SPACES | COMMENT | LINE_JOINING )+ -> skip
 ;

UNKNOWN_CHAR: .;
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
 : '\\' SPACES? ( '\r'?'\n' | '\r' | '\f' );
