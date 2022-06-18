
from MatlabAST_ClassLib import *
from MatlabAST_XprTree import *
from MatlabAST_Operators import *

class M_FieldIndex(AST_Node):
    def __init__(self,identifiers):
        self.identifiers = identifiers
        
    @property
    def Type(self):
        return 'FieldIndex'
        
    @property
    def Args(self):
        return self.identifiers
        
class M_IndexedArray(AST_Node):
    def __init__(self,base,index):
        self.base = base
        self.index = index
        
    @property
    def Type(self):
        return 'IndexedArray'
        
    @property
    def Args(self):
        return [self.base,self.index]
    
class M_PlaceholderNode(AST_Node):
    def __init__(self,ctx,children):
        self.ctx = ctx
        self.children = children
    
    @property
    def Type(self):
        return type(self.ctx)
        
    @property
    def Args(self):
        if isinstance(self.children,str):
            return [self.children]
        return [i.getText() if hasattr(i,'getText') else str(i) for i in self.children]
        
    def __str__(self):
        return r'(PLACEHOLDER:{} {})'.format(str(self.Type).split('.')[-1].strip('\'>'),' '.join(self.Args))
        
class M_Statement(AST_Node):
    def __init__(self, children):
        if isinstance(children[-1], M_SEMI_COLON):
            self.statement = children[:-1]
        else:
            self.statement = children
    
    @property
    def Type(self):
        return 'Statement'
        
    @property
    def Args(self):
        return self.statement

class M_SingleAssignment(M_Statement):
    def __init__(self,lhs,eq,rhs):
        self.lhs = lhs
        self.rhs = rhs
        
    @property
    def Type(self):
        return 'SingleAssignment'
        
    @property
    def Args(self):
        return [self.lhs,self.rhs]
        
class M_IfStatement(AST_Node):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement
        
    @property
    def Type(self):
        return 'If'
        
    @property
    def Args(self):
        return [self.condition,self.statement]
        
class M_ElseIfStatement(AST_Node):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement
        
    @property
    def Type(self):
        return 'ElseIf'
        
    @property
    def Args(self):
        return [self.condition,self.statement]


class M_ElseStatement(AST_Node):
    def __init__(self, statement):
        self.statement = statement
        
    @property
    def Type(self):
        return 'Else'
        
    @property
    def Args(self):
        return [self.statement]

class M_Conditional(M_Statement):
    def __init__(self, if_condition, else_condition = None, *elif_conditions):
        self.if_condition = if_condition
        self.else_condition = else_condition
        self.elif_conditions = elif_conditions
    
    
    @property
    def Type(self):
        return 'Conditional'
        
    @property
    def Args(self):
        return [self.if_condition,*self.elif_conditions,self.else_condition]
        
        
class M_While(M_Statement):
    def __init__(self,condition,*code):
        self.condition = condition
        self.codeblock = code
        
    @property
    def Type(self):
        return 'While'
        
    @property
    def Args(self):
        return [self.condition,self.codeblock]
        
class M_For(M_Statement):
    def __init__(self, iter_val, iterator,code):
        self.iter_val = iter_val
        self.iterator = iterator
        self.codeblock = code
        
    @property
    def Type(self):
        return 'For'
        
    @property
    def Args(self):
        return [self.iterator,self.codeblock]
        
class M_CaseStatement(AST_Node):
    def __init__(self, value, statement):
        self.value = value
        self.statement = statement
        
    @property
    def Type(self):
        return 'Case'
        
    @property
    def Args(self):
        return [self.value,self.statement]
        
class M_OtherwiseStatement(AST_Node):
    def __init__(self, statement):
        self.statement = statement
        
    @property
    def Type(self):
        return 'Otherwise'
        
    @property
    def Args(self):
        return [self.statement]
        
class M_Switch(M_Statement):
    def __init__(self, switch_var, otherwise_statement, *case_statements):
        self.switch_var = switch_var
        self.case_statements = case_statements
        if len(otherwise_statement) == 0:
            otherwise_statement = None
        self.otherwise_statement = otherwise_statement
        
    @property
    def Type(self):
        return 'Switch'
        
    @property
    def Args(self):
        return [self.switch_var, self.case_statements, self.otherwise_statement]

class M_StatementList(AST_Node):
    def __init__(self, *stmts):
        self.stmts = stmts
        
    @property
    def Type(self):
        return 'StatementBlock'
        
    @property
    def Args(self):
        return self.stmts

def take_adjacent_statements(code_list):
    statements = []
    code_list = list(code_list)
    next_element = code_list.pop(0)
    if not isinstance(next_element, M_Statement):
        return ([],[next_element] + code_list)
        
    while isinstance(next_element, M_Statement):
        statements.append(next_element)
        if len(code_list) == 0:
            return (statements, [])
        next_element = code_list.pop(0)
    
    return (M_StatementList(statements), code_list)
    