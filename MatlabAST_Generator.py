from MATLABVisitor import MATLABVisitor
from MATLABParser import MATLABParser
from MATLABLexer import MATLABLexer

from MatlabAST_Statement import *

from antlr4 import *

def is_conditional_token(element):
    return any(map(lambda x:isinstance(element,x),(M_IF,M_ELSEIF,M_ELSE,M_CASE,M_SWITCH,M_OTHERWISE)))

class MatlabAST_Constructor(MATLABVisitor):

    def aggregateResult(self, running, new):
        if running is None:
            running = []
        if new is None or isinstance(new, M_END):
            return running
        if isinstance(new, list):
            return running + new
        return running + [new]

    def visitTerminal(self,ctx):
        if value := operator_classes.get(ctx.getText(),None):
            return value()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MATLABParser#atom_boolean.
    def visitAtom_boolean(self, ctx:MATLABParser.Atom_booleanContext):
        return M_Boolean(ctx.getText())

    # Visit a parse tree produced by MATLABParser#atom_empty_array.
    def visitAtom_empty_array(self, ctx:MATLABParser.Atom_empty_arrayContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#atom_empty_cell.
    def visitAtom_empty_cell(self, ctx:MATLABParser.Atom_empty_cellContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#atom_end.
    def visitAtom_end(self, ctx:MATLABParser.Atom_endContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#atom_float.
    def visitAtom_float(self, ctx:MATLABParser.Atom_floatContext):
        return M_Numeric(float(ctx.getText()))


    # Visit a parse tree produced by MATLABParser#atom_imaginary.
    def visitAtom_imaginary(self, ctx:MATLABParser.Atom_imaginaryContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#atom_index_all.
    def visitAtom_index_all(self, ctx:MATLABParser.Atom_index_allContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#atom_integer.
    def visitAtom_integer(self, ctx:MATLABParser.Atom_integerContext):
        return M_Numeric(int(ctx.getText()))


    # Visit a parse tree produced by MATLABParser#atom_meta.
    def visitAtom_meta(self, ctx:MATLABParser.Atom_metaContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#atom_string.
    def visitAtom_string(self, ctx:MATLABParser.Atom_stringContext):
        #return self.visitChildren(ctx)
        return M_String(ctx.getText())


    # Visit a parse tree produced by MATLABParser#atom_var.
    def visitAtom_var(self, ctx:MATLABParser.Atom_varContext):
        #print([i.getText() if i is not None else i for i in self.visitChildren(ctx)])
        return M_Identifier(ctx.getText())


    # Visit a parse tree produced by MATLABParser#matlab_file.
    def visitMatlab_file(self, ctx:MATLABParser.Matlab_fileContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#def_class.
    def visitDef_class(self, ctx:MATLABParser.Def_classContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#def_function.
    def visitDef_function(self, ctx:MATLABParser.Def_functionContext):
        print(list(self.visitChildren(ctx)))
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#attrib_class_boolean.
    def visitAttrib_class_boolean(self, ctx:MATLABParser.Attrib_class_booleanContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#attrib_class_meta.
    def visitAttrib_class_meta(self, ctx:MATLABParser.Attrib_class_metaContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#attrib_property_boolean.
    def visitAttrib_property_boolean(self, ctx:MATLABParser.Attrib_property_booleanContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#attrib_property_access.
    def visitAttrib_property_access(self, ctx:MATLABParser.Attrib_property_accessContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#attrib_method_boolean.
    def visitAttrib_method_boolean(self, ctx:MATLABParser.Attrib_method_booleanContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#attrib_method_access.
    def visitAttrib_method_access(self, ctx:MATLABParser.Attrib_method_accessContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#atom_access.
    def visitAtom_access(self, ctx:MATLABParser.Atom_accessContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#st_assign.
    def visitSt_assign(self, ctx:MATLABParser.St_assignContext):
        return M_SingleAssignment(*self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#st_command.
    def visitSt_command(self, ctx:MATLABParser.St_commandContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#st_if.
    def visitSt_if(self, ctx:MATLABParser.St_ifContext):
        children = list(self.visitChildren(ctx))
        if_element = []
        elif_elements = []
        else_element = []
        while len(children) > 0:
            next_element = children.pop(0)
            if isinstance(next_element, M_IF):
                condition = children.pop(0)
                statements = []
                while True:
                    if not children:
                        break
                    if is_conditional_token(children[0]):
                        break
                    statements.append(children.pop(0))
                if_element.append(M_IfStatement(condition,statements))
            elif isinstance(next_element, M_ELSEIF):
                condition = children.pop(0)
                statements = []
                while True:
                    if not children:
                        break
                    if is_conditional_token(children[0]):
                        break
                    statements.append(children.pop(0))
                elif_elements.append(M_ElseIfStatement(condition,statements))
            elif isinstance(next_element, M_ELSE):
                else_element.append(M_ElseStatement(children))
            elif isinstance(next_element, M_END):
                pass
        if not len(if_element) == 1:
            raise RuntimeError('invalid number of if statements: {}'.format(str(if_element)))
        if not len(else_element) == 1:
            raise RuntimeError('invalid number of else statements: {}'.format(str(else_element)))
        return M_Conditional(if_element,else_element,*elif_elements)

    # Visit a parse tree produced by MATLABParser#st_for.
    def visitSt_for(self, ctx:MATLABParser.St_forContext):
        children = self.visitChildren(ctx)
        iterval = children[1]
        iter_range = children[3]
        iter_stmt = children[4]
        return M_For(iterval,iter_range,iter_stmt)


    # Visit a parse tree produced by MATLABParser#st_switch.
    def visitSt_switch(self, ctx:MATLABParser.St_switchContext):
        children = self.visitChildren(ctx)
        cases = []
        otherwise = []
        assert isinstance(children.pop(0), M_SWITCH)
        switch_expr = children.pop(0)
        while len(children) > 0:
            next_element = children.pop(0)
            if isinstance(next_element, M_CASE):
                match_element = children.pop(0)
                statements = []
                while True:
                    if not children:
                        break
                    if is_conditional_token(children[0]):
                        break
                    statements.append(children.pop(0))
                cases.append(M_CaseStatement(match_element,statements))
            elif isinstance(next_element, M_OTHERWISE):
                statements = []
                while True:
                    if not children:
                        break
                    if is_conditional_token(children[0]):
                        break
                    statements.append(children.pop(0))
                otherwise.append(M_OtherwiseStatement(statements))
            elif isinstance(next_element, M_END):
                pass
            else:
                raise RuntimeError('first element of switch case object is not a terminal statement!')
        if len(otherwise) > 1:
            raise RuntimeError('multiple otherwise cases in switch case!')
        return M_Switch(switch_expr,otherwise,cases)


    # Visit a parse tree produced by MATLABParser#st_try.
    def visitSt_try(self, ctx:MATLABParser.St_tryContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#st_while.
    def visitSt_while(self, ctx:MATLABParser.St_whileContext):
        children = self.visitChildren(ctx)
        assert isinstance(children[0], M_WHILE)
        return M_While(children[1], *children[2:])


    # Visit a parse tree produced by MATLABParser#function_params.
    def visitFunction_params(self, ctx:MATLABParser.Function_paramsContext):
        
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#function_returns.
    def visitFunction_returns(self, ctx:MATLABParser.Function_returnsContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#statement.
    def visitStatement(self, ctx:MATLABParser.StatementContext):
        return M_Statement(self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#xpr_tree.
    def visitXpr_tree(self, ctx:MATLABParser.Xpr_treeContext):
        children = self.visitChildren(ctx)
        if len(children) == 1:
            return children[0]
        return identify_xpr_tree(children)


    # Visit a parse tree produced by MATLABParser#xpr_tree_.
    def visitXpr_tree_(self, ctx:MATLABParser.Xpr_tree_Context):
        children = self.visitChildren(ctx)
        if len(children) == 1:
            return children[0]
        return identify_xpr_tree(children)


    # Visit a parse tree produced by MATLABParser#xpr_array.
    def visitXpr_array(self, ctx:MATLABParser.Xpr_arrayContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#xpr_array_.
    def visitXpr_array_(self, ctx:MATLABParser.Xpr_array_Context):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#xpr_cell.
    def visitXpr_cell(self, ctx:MATLABParser.Xpr_cellContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#xpr_cell_.
    def visitXpr_cell_(self, ctx:MATLABParser.Xpr_cell_Context):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#xpr_array_index.
    def visitXpr_array_index(self, ctx:MATLABParser.Xpr_array_indexContext):
        children = self.visitChildren(ctx)
        return M_IndexedArray(children[0],children[2])


    # Visit a parse tree produced by MATLABParser#xpr_cell_index.
    def visitXpr_cell_index(self, ctx:MATLABParser.Xpr_cell_indexContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#xpr_field.
    def visitXpr_field(self, ctx:MATLABParser.Xpr_fieldContext):
        children = self.visitChildren(ctx)
        return M_FieldIndex([children[0],children[2]])


    # Visit a parse tree produced by MATLABParser#xpr_function.
    def visitXpr_function(self, ctx:MATLABParser.Xpr_functionContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#xpr_handle.
    def visitXpr_handle(self, ctx:MATLABParser.Xpr_handleContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))


    # Visit a parse tree produced by MATLABParser#command_argument.
    def visitCommand_argument(self, ctx:MATLABParser.Command_argumentContext):
        return M_PlaceholderNode(ctx,self.visitChildren(ctx))
        
# taken from pygrun
def beautify_lisp_string(in_string):
    indent_size = 3
    add_indent = ' ' * indent_size
    out_string = in_string[0]  # no indent for 1st (
    indent = ''
    for i in range(1, len(in_string)):
        if in_string[i] == '(' and in_string[i + 1] != ' ':
            indent += add_indent
            out_string += "\n" + indent + '('
        elif in_string[i] == ')':
            out_string += ')'
            if len(indent) > 0:
                indent = indent.replace(add_indent, '', 1)
        else:
            out_string += in_string[i]
    return out_string

if __name__ == '__main__':
    file_name = 'example1.m'
    input_stream = FileStream(file_name)
    lexer = MATLABLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    parser = MATLABParser(token_stream)
    
    func_start_rule = getattr(parser, 'matlab_file')
    parser_ret = func_start_rule()
    testvisitor = MatlabAST_Constructor().visit(parser_ret)
    
    with open('testoutput.txt','w') as f:
        f.write(beautify_lisp_string(str(testvisitor)))
    

    
    print(beautify_lisp_string(str(testvisitor)))