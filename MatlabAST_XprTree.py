

from MatlabAST_ClassLib import AST_Node, M_Numeric

class M_XprTree(AST_Node):
    pass
    
class M_UnaryExpression(M_XprTree):
    def __init__(self,base):
        self.base = base
    
    @property
    def Args(self):
        return [self.base]
    
class M_Expression(M_XprTree):
    pass
    
class M_ArithmeticExpression(M_Expression):
    pass



class M_Range(M_Expression):
    def __init__(self,start,stop):
        if isinstance(start,M_Range):
            self.start = start.start
            self.step = start.stop
        else:
            self.start = start
            self.step = M_Numeric(1)
        self.stop = stop
        
    @property
    def Type(self):
        return 'Range'
        
    @property
    def Args(self):
        return [self.start,self.step,self.stop]


    
class M_UnaryMinus(M_UnaryExpression):
    @property
    def Type(self):
        return 'UnaryMinus'
    
class M_UnaryNot(M_UnaryExpression):
    @property
    def Type(self):
        return 'UnaryNot'

class M_UnaryTranspose(M_UnaryExpression):
    @property
    def Type(self):
        return 'UnaryTranspose'
    
class M_UnaryConjugateTranspose(M_UnaryExpression):
    @property
    def Type(self):
        return 'UnaryConjugateTranspose'
    
class M_UnaryInverse(M_UnaryExpression):
    @property
    def Type(self):
        return 'UnaryInverse'
    


class M_Add(M_ArithmeticExpression):
    def __init__(self,*summands):
        self.summands = summands
    
    @property
    def Type(self):
        return 'Summation'
        
    @property
    def Args(self):
        return self.summands

class M_Pow(M_ArithmeticExpression):
    def __init__(self,base,*exp):
        self.base = base
        self.exp = exp
        
    @property
    def Type(self):
        return 'Exponential'
        
    @property
    def Args(self):
        return [self.base,self.exp]
    
class M_Product(M_ArithmeticExpression):
    def __init__(self,*factors):
        self.factors = factors
        
    @property
    def Type(self):
        return 'Exponential'
        
    @property
    def Args(self):
        return self.factors
    
class M_ElementwisePow(M_Pow):
    @property
    def Type(self):
        return 'ElementwiseExponential'
    
class M_ElementwiseProduct(M_Product):
    @property
    def Type(self):
        return 'ElementwiseProduct'
    


class M_BinaryRelationalExpression(M_Expression):
    def __init__(self,op,args):
        assert op in ('and','or')
        self.relation = op
        self.args = args
        
    @property
    def Type(self):
        return self.relation
        
    @property
    def Args(self):
        return self.args

class M_BooleanExpression(M_Expression):
        
    @property
    def Type(self):
        return self.relation
        
    @property
    def Args(self):
        return self.args
        
class M_OrExpression(M_BooleanExpression):
    def __init__(self,*args):
        self.relation = 'OR'
        self.args = args
        
class M_AndExpression(M_BooleanExpression):
    def __init__(self,*args):
        self.relation = 'AND'
        self.args = args

class M_RelationalExpression(M_Expression):
        
    @property
    def Type(self):
        return self.relation
        
    @property
    def Args(self):
        return self.args
    
class M_EqualityExpression(M_RelationalExpression):
    def __init__(self,*args):
        self.relation = 'Equality'
        self.args = args
        
class M_LessThanExpression(M_RelationalExpression):
    def __init__(self,*args):
        self.relation = 'LessThan'
        self.args = args

class M_GreaterThanExpression(M_RelationalExpression):
    def __init__(self,*args):
        self.relation = 'GreaterThan'
        self.args = args

    
def m_parenthesis_grouping(g0,g1,g2):
    return g1
    
def m_elementwise_xpose(g0,g1):
    return M_UnaryConjugateTranspose(g0)
    
def m_xpose(g0,g1):
    return M_UnaryTranspose(g0)
    
def m_elementwise_power(g0,g1,g2):
    return M_ElementwisePow(g0,g2)
    
def m_power(g0,g1,g2):
    return M_Pow(g0,g2)

def m_unary_plus(g0,g1):
    return M_UnaryPlus(g1)
    
def m_unary_minus(g0,g1):
    return M_UnaryMinus(g1)
    
def m_unary_not(g0,g1):
    return M_UnaryNot(g1)
    
def m_elementwise_product(g0,g1,g2):
    return M_ElementwiseProduct(g0,g2)
    
def m_elementwise_right_divide(g0,g1,g2):
    raise NotImplementedError
    
def m_elementwise_left_divide(g0,g1,g2):
    raise NotImplementedError
    
def m_product(g0,g1,g2):
    return M_Product(g0,g2)

def m_right_divide(g0,g1,g2):
    raise NotImplementedError
    
def m_left_divide(g0,g1,g2):
    raise NotImplementedError
    
def m_add(g0,g1,g2):
    return M_Add(g0,g2)
    
def m_subtract(g0,g1,g2):
    return M_Add(g0,M_UnaryMinus(g2))
    
def m_range(g0,g1,g2):
    return M_Range(g0,g2)
    
def m_lt(g0,g1,g2):
    return M_LessThanExpression(g0,g2)
    
def m_leq(g0,g1,g2):
    return M_OrExpression( M_LessThanExpression(g0,g2), M_EqualityExpression(g0,g2) )
    
def m_geq(g0,g1,g2):
    return M_OrExpression( M_GreaterThanExpression(g0,g2), M_EqualityExpression(g0,g2) )
    
def m_gt(g0,g1,g2):
    return M_GreaterThanExpression(g0,g2)
    
def m_eq(g0,g1,g2):
    return M_EqualityExpression(g0,g2)
    
def m_neq(g0,g1,g2):
    return M_UnaryNot(M_EqualityExpression(g0,g2))
    
def m_bin_and(g0,g1,g2):
    raise NotImplementedError
    
def m_bin_or(g0,g1,g2):
    raise NotImplementedError
    
def m_logical_and(g0,g1,g2):
    raise NotImplementedError
    
def m_logical_or(g0,g1,g2):
    raise NotImplementedError
    
from MatlabAST_Operators import *

'''
    |	LEFT_PARENTHESIS xpr_tree RIGHT_PARENTHESIS
    |	xpr_tree (ELMENT_WISE_TRANSPOSE | TRANSPOSE)
    |	xpr_tree (ELMENT_WISE_POWER | POWER) xpr_tree
    |	(PLUS | MINUS | NOT) xpr_tree
    |	xpr_tree (ELMENT_WISE_TIMES | ELMENT_WISE_RIGHT_DIVIDE | ELMENT_WISE_LEFT_DIVIDE) xpr_tree
    |	xpr_tree (TIMES | RIGHT_DIVIDE | LEFT_DIVIDE) xpr_tree
    |	xpr_tree (PLUS | MINUS) xpr_tree
    |	xpr_tree COLON xpr_tree
    |	xpr_tree LESS_THAN xpr_tree
    |	xpr_tree LESS_THAN_OR_EQUAL xpr_tree
    |	xpr_tree GREATER_THAN xpr_tree
    |	xpr_tree GREATER_THAN_OR_EQUAL xpr_tree
    |	xpr_tree EQUALS xpr_tree
    |	xpr_tree NOT_EQUAL xpr_tree
    |	xpr_tree BINARY_AND xpr_tree
    |	xpr_tree BINARY_OR xpr_tree
    |	xpr_tree LOGICAL_AND xpr_tree
    |	xpr_tree LOGICAL_OR xpr_tree
'''

xpr_tree_map = {
    (M_LEFT_PARENTHESIS,AST_Node,M_RIGHT_PARENTHESIS) : m_parenthesis_grouping,
    (AST_Node,M_ELMENT_WISE_TRANSPOSE) : m_elementwise_xpose,
    (AST_Node,M_TRANSPOSE) : m_xpose,
    (AST_Node, M_ELMENT_WISE_POWER, AST_Node) : m_elementwise_power,
    (AST_Node, M_POWER, AST_Node) : m_power,
    (M_PLUS, AST_Node) : m_unary_plus,
    (M_MINUS, AST_Node) : m_unary_minus,
    (M_NOT, AST_Node) : m_unary_not,
    (AST_Node, M_ELMENT_WISE_TIMES, AST_Node) : m_elementwise_product,
    (AST_Node, M_ELMENT_WISE_RIGHT_DIVIDE, AST_Node) : m_elementwise_right_divide,
    (AST_Node, M_ELMENT_WISE_LEFT_DIVIDE, AST_Node) : m_elementwise_left_divide,
    (AST_Node, M_TIMES, AST_Node) : m_product,
    (AST_Node, M_RIGHT_DIVIDE, AST_Node) : m_right_divide,
    (AST_Node, M_LEFT_DIVIDE, AST_Node) : m_left_divide,
    (AST_Node, M_PLUS, AST_Node) : m_add,
    (AST_Node, M_MINUS, AST_Node) : m_subtract,
    (AST_Node, M_COLON, AST_Node) : m_range,
    (AST_Node, M_LESS_THAN, AST_Node) : m_lt,
    (AST_Node, M_LESS_THAN_OR_EQUAL, AST_Node) : m_leq,
    (AST_Node, M_GREATER_THAN, AST_Node) : m_gt,
    (AST_Node, M_GREATER_THAN_OR_EQUAL, AST_Node) : m_geq,
    (AST_Node, M_EQUALS, AST_Node) : m_eq,
    (AST_Node, M_NOT_EQUAL, AST_Node) : m_neq,
    (AST_Node, M_BINARY_AND, AST_Node) : m_bin_and,
    (AST_Node, M_BINARY_OR, AST_Node) : m_bin_or,
    (AST_Node, M_LOGICAL_AND, AST_Node) : m_logical_and,
    (AST_Node, M_LOGICAL_OR, AST_Node) : m_logical_or,
}

#def get_pattern_type(node_sequence):
#    for k,n in xpr_tree_map.items():
#        if all([isinstance(i,j) for i,j in zip(node_sequence,k)]):
#            return n

def identify_xpr_tree(children):
    for k,n in xpr_tree_map.items():
        if all([isinstance(i,j) for i,j in zip(children,k)]):
            return n(*children)
    raise RuntimeError('NO EXPRESSION MATCH!!! -> {}'.format(' '.join([str(i) for i in children])))
    
    
    
    