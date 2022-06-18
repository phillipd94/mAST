
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
        return r'({} {})'.format(self.Type,' '.join(map(str,self.Args)))
        
    def __repr__(self):
        return str(self)

class M_ValueNode(AST_Node):

    @property
    @abstractmethod
    def Val(self):
        pass
        
    def __str__(self):
        return r'(ValueNode:{} {})'.format(self.Type,self.Val)
    

class M_String(M_ValueNode):

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

class M_Numeric(M_ValueNode):
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
        
class M_Boolean(M_ValueNode):
    def __init__(self,val):
        assert val in ['true','false']
        self.boolean_value = val
    
    @property
    def Type(self):
        return 'Boolean'
    
    @property
    def Args(self):
        return None
        
    @property
    def Val(self):
        return self.boolean_value


class M_Identifier(M_ValueNode):
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


if __name__ == '__main__':
    pass