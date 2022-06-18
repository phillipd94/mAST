
from abc import abstractmethod

class AST_Node(object):
    def __init__(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def Type(self):
        pass
    
    @property
    @abstractmethod
    def Args(self):
        pass
        
    def __str__(self):
        return '{} {}'.format(self.Type,self.Args)

class M_TerminalNode(AST_Node):

    @property
    @abstractmethod
    def Val(self):
        pass
        
    def __str__(self):
        return str(self.Val)
    

class M_String(M_TerminalNode):

    def __init__(self,string):
        assert isinstance(string, str)
        self.string_value = string
    
    @property
    def Type(self):
        return 'String'
    
    @property
    def Args(self):
        return []
        
    @property
    def Val(self):
        return self.string_value

class M_Numeric(M_TerminalNode):
    def __init__(self,val):
        assert any([isinstance(val, x) for x in (float,int)])
        self.numeric_value = val
    
    @property
    def Type(self):
        return 'Numeric'
    
    @property
    def Args(self):
        return []
        
    @property
    def Val(self):
        return self.numeric_value


class M_Identifier(M_TerminalNode):
    def __init__(self,name):
        assert isinstance(name, str)
        self.identifier_name = name
    
    @property
    def Type(self):
        return 'Identifier'
    
    @property
    def Args(self):
        return []
        
    @property
    def Val(self):
        return self.identifier_name

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
    
class M_IndexExpression(AST_Node):
    pass
    
class M_CompoundIndex(M_IndexExpression):
    def __init__(self,indices):
        self.indices = list(indices)
    
    @property
    def Type(self):
        return 'CompoundIndex'
        
    @property
    def Args(self):
        return self.indices
        
class M_SingleIndex(M_IndexExpression):
    def __init__(self,index):
        self.index = index
    
    @property
    def Type(self):
        return 'SingleIndex'
        
    @property
    def Args(self):
        return self.index
        
class M_PlaceholderNode(AST_Node):
    def __init__(self,ctx,children):
        self.ctx = ctx
        self.children = children
    
    @property
    def Type(self):
        return type(ctx)
        
    @property
    def Args(self):
        return [i.getText() for i in self.children]
        
if __name__ == '__main__':
    print('looksgood!')