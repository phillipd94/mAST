
from MatlabAST_ClassLib import *

class M_TerminalNode(AST_Node):
    operator = ''
    
    def __init__(self):
        pass

    @property
    def Type(self):
        return self.operator
        
    @property
    def Args(self):
        return []

class M_ELMENT_WISE_LEFT_DIVIDE(M_TerminalNode):
	operator = 'M_ELMENT_WISE_LEFT_DIVIDE'

class M_ELMENT_WISE_POWER(M_TerminalNode):
	operator = 'M_ELMENT_WISE_POWER'

class M_ELMENT_WISE_RIGHT_DIVIDE(M_TerminalNode):
	operator = 'M_ELMENT_WISE_RIGHT_DIVIDE'

class M_ELMENT_WISE_TIMES(M_TerminalNode):
	operator = 'M_ELMENT_WISE_TIMES'

class M_ELMENT_WISE_TRANSPOSE(M_TerminalNode):
	operator = 'M_ELMENT_WISE_TRANSPOSE'

class M_EQUALS(M_TerminalNode):
	operator = 'M_EQUALS'

class M_GREATER_THAN_OR_EQUAL(M_TerminalNode):
	operator = 'M_GREATER_THAN_OR_EQUAL'

class M_LESS_THAN_OR_EQUAL(M_TerminalNode):
	operator = 'M_LESS_THAN_OR_EQUAL'

class M_LOGICAL_AND(M_TerminalNode):
	operator = 'M_LOGICAL_AND'

class M_LOGICAL_OR(M_TerminalNode):
	operator = 'M_LOGICAL_OR'

class M_NOT_EQUAL(M_TerminalNode):
	operator = 'M_NOT_EQUAL'

class M_ASSIGN(M_TerminalNode):
	operator = 'M_ASSIGN'

class M_BINARY_AND(M_TerminalNode):
	operator = 'M_BINARY_AND'

class M_BINARY_OR(M_TerminalNode):
	operator = 'M_BINARY_OR'

class M_COLON(M_TerminalNode):
	operator = 'M_COLON'

class M_GREATER_THAN(M_TerminalNode):
	operator = 'M_GREATER_THAN'

class M_LEFT_DIVIDE(M_TerminalNode):
	operator = 'M_LEFT_DIVIDE'

class M_LESS_THAN(M_TerminalNode):
	operator = 'M_LESS_THAN'

class M_MINUS(M_TerminalNode):
	operator = 'M_MINUS'

class M_NOT(M_TerminalNode):
	operator = 'M_NOT'

class M_PLUS(M_TerminalNode):
	operator = 'M_PLUS'

class M_POWER(M_TerminalNode):
	operator = 'M_POWER'

class M_RIGHT_DIVIDE(M_TerminalNode):
	operator = 'M_RIGHT_DIVIDE'

class M_TIMES(M_TerminalNode):
	operator = 'M_TIMES'

class M_TRANSPOSE(M_TerminalNode):
	operator = 'M_TRANSPOSE'

class M_AT(M_TerminalNode):
	operator = 'M_AT'

class M_COMMA(M_TerminalNode):
	operator = 'M_COMMA'

class M_DOT(M_TerminalNode):
	operator = 'M_DOT'

class M_END(M_TerminalNode):
	operator = 'M_END'

class M_SEMI_COLON(M_TerminalNode):
	operator = 'M_SEMI_COLON'

class M_LEFT_BRACE(M_TerminalNode):
	operator = 'M_LEFT_BRACE'

class M_LEFT_PARENTHESIS(M_TerminalNode):
	operator = 'M_LEFT_PARENTHESIS'

class M_LEFT_SQUARE_BRACKET(M_TerminalNode):
	operator = 'M_LEFT_SQUARE_BRACKET'

class M_QUESTION(M_TerminalNode):
	operator = 'M_QUESTION'

class M_RIGHT_BRACE(M_TerminalNode):
	operator = 'M_RIGHT_BRACE'

class M_RIGHT_PARENTHESIS(M_TerminalNode):
	operator = 'M_RIGHT_PARENTHESIS'

class M_RIGHT_SQUARE_BRACKET(M_TerminalNode):
	operator = 'M_RIGHT_SQUARE_BRACKET'
    
m_ops = [M_ELMENT_WISE_LEFT_DIVIDE,M_ELMENT_WISE_POWER,M_ELMENT_WISE_RIGHT_DIVIDE,M_ELMENT_WISE_TIMES,M_ELMENT_WISE_TRANSPOSE,M_EQUALS,M_GREATER_THAN_OR_EQUAL,M_LESS_THAN_OR_EQUAL,M_LOGICAL_AND,M_LOGICAL_OR,M_NOT_EQUAL,M_ASSIGN,M_BINARY_AND,M_BINARY_OR,M_COLON,M_GREATER_THAN,M_LEFT_DIVIDE,M_LESS_THAN,M_MINUS,M_NOT,M_PLUS,M_POWER,M_RIGHT_DIVIDE,M_TIMES,M_TRANSPOSE,M_AT,M_COMMA,M_DOT,M_END,M_SEMI_COLON,M_LEFT_BRACE,M_LEFT_PARENTHESIS,M_LEFT_SQUARE_BRACKET,M_QUESTION,M_RIGHT_BRACE,M_RIGHT_PARENTHESIS,M_RIGHT_SQUARE_BRACKET]

m_ops_syms = ['./', '.^', '.\\', '.*', ".'", '==', '>=', '<=', '&&', '||', '~=', '=', '&', '|', ':', '>', '/', '<', '-', '~', '+', '^', '\\', '*', "'", '@', ',', '.', 'end', ';', '{', '(', '[', '?', '}', ')', ']']
    
class M_BREAK(M_TerminalNode):
    operator = 'break'
    
class M_CASE(M_TerminalNode):
    operator = 'case'
    
class M_CATCH(M_TerminalNode):
    operator = 'catch'
    
class M_CLASSDEF(M_TerminalNode):
    operator = 'classdef'
    
class M_CONTINUE(M_TerminalNode):
    operator = 'continue'
    
class M_ELSE(M_TerminalNode):
    operator = 'else'
    
class M_ELSEIF(M_TerminalNode):
    operator = 'elseif'
    
class M_END(M_TerminalNode):
    operator = 'end'
    
class M_FOR(M_TerminalNode):
    operator = 'for'
    
class M_FUNCTION(M_TerminalNode):
    operator = 'function'
        
class M_GET(M_TerminalNode):
    operator = 'get'
        
class M_GLOBAL(M_TerminalNode):
    operator = 'global'
        
class M_IF(M_TerminalNode):
    operator = 'if'
    
class M_OTHERWISE(M_TerminalNode):
    operator = 'otherwise'
    
class M_PERSISTENT(M_TerminalNode):
    operator = 'persistent'
    
class M_PROPERTIES(M_TerminalNode):
    operator = 'properties'
    
class M_RETURN(M_TerminalNode):
    operator = 'return'
    
class M_SET(M_TerminalNode):
    operator = 'set'
    
class M_SWITCH(M_TerminalNode):
    operator = 'switch'
    
class M_TRY(M_TerminalNode):
    operator = 'try'
    
class M_WHILE(M_TerminalNode):
    operator = 'while'
    

    
    
m_keys = [M_BREAK,M_CASE,M_CATCH,M_CLASSDEF,M_CONTINUE,M_CONTINUE,M_ELSE,M_ELSEIF,M_END,M_FOR,M_FUNCTION,M_GET,M_GLOBAL,M_IF,M_OTHERWISE,M_PERSISTENT,M_PROPERTIES,M_RETURN,M_SET,M_SWITCH,M_TRY,M_WHILE]

m_keys_syms = [i.operator for i in m_keys]

operator_classes = {i:j for i,j in zip(tuple(m_ops_syms + m_keys_syms),
                                       tuple(m_ops + m_keys))}


