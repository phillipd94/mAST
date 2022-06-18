# Generated from .\MATLAB.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MATLABParser import MATLABParser
else:
    from MATLABParser import MATLABParser

# This class defines a complete generic visitor for a parse tree produced by MATLABParser.

class MATLABVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MATLABParser#atom_boolean.
    def visitAtom_boolean(self, ctx:MATLABParser.Atom_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_empty_array.
    def visitAtom_empty_array(self, ctx:MATLABParser.Atom_empty_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_empty_cell.
    def visitAtom_empty_cell(self, ctx:MATLABParser.Atom_empty_cellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_end.
    def visitAtom_end(self, ctx:MATLABParser.Atom_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_float.
    def visitAtom_float(self, ctx:MATLABParser.Atom_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_imaginary.
    def visitAtom_imaginary(self, ctx:MATLABParser.Atom_imaginaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_index_all.
    def visitAtom_index_all(self, ctx:MATLABParser.Atom_index_allContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_integer.
    def visitAtom_integer(self, ctx:MATLABParser.Atom_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_meta.
    def visitAtom_meta(self, ctx:MATLABParser.Atom_metaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_string.
    def visitAtom_string(self, ctx:MATLABParser.Atom_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_var.
    def visitAtom_var(self, ctx:MATLABParser.Atom_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#matlab_file.
    def visitMatlab_file(self, ctx:MATLABParser.Matlab_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#def_class.
    def visitDef_class(self, ctx:MATLABParser.Def_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#def_function.
    def visitDef_function(self, ctx:MATLABParser.Def_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#attrib_class_boolean.
    def visitAttrib_class_boolean(self, ctx:MATLABParser.Attrib_class_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#attrib_class_meta.
    def visitAttrib_class_meta(self, ctx:MATLABParser.Attrib_class_metaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#attrib_property_boolean.
    def visitAttrib_property_boolean(self, ctx:MATLABParser.Attrib_property_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#attrib_property_access.
    def visitAttrib_property_access(self, ctx:MATLABParser.Attrib_property_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#attrib_method_boolean.
    def visitAttrib_method_boolean(self, ctx:MATLABParser.Attrib_method_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#attrib_method_access.
    def visitAttrib_method_access(self, ctx:MATLABParser.Attrib_method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#atom_access.
    def visitAtom_access(self, ctx:MATLABParser.Atom_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#st_assign.
    def visitSt_assign(self, ctx:MATLABParser.St_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#st_command.
    def visitSt_command(self, ctx:MATLABParser.St_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#st_if.
    def visitSt_if(self, ctx:MATLABParser.St_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#st_for.
    def visitSt_for(self, ctx:MATLABParser.St_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#st_switch.
    def visitSt_switch(self, ctx:MATLABParser.St_switchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#st_try.
    def visitSt_try(self, ctx:MATLABParser.St_tryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#st_while.
    def visitSt_while(self, ctx:MATLABParser.St_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#function_params.
    def visitFunction_params(self, ctx:MATLABParser.Function_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#function_returns.
    def visitFunction_returns(self, ctx:MATLABParser.Function_returnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#statement.
    def visitStatement(self, ctx:MATLABParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_tree.
    def visitXpr_tree(self, ctx:MATLABParser.Xpr_treeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_tree_.
    def visitXpr_tree_(self, ctx:MATLABParser.Xpr_tree_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_array.
    def visitXpr_array(self, ctx:MATLABParser.Xpr_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_array_.
    def visitXpr_array_(self, ctx:MATLABParser.Xpr_array_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_cell.
    def visitXpr_cell(self, ctx:MATLABParser.Xpr_cellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_cell_.
    def visitXpr_cell_(self, ctx:MATLABParser.Xpr_cell_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_array_index.
    def visitXpr_array_index(self, ctx:MATLABParser.Xpr_array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_cell_index.
    def visitXpr_cell_index(self, ctx:MATLABParser.Xpr_cell_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_field.
    def visitXpr_field(self, ctx:MATLABParser.Xpr_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_function.
    def visitXpr_function(self, ctx:MATLABParser.Xpr_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#xpr_handle.
    def visitXpr_handle(self, ctx:MATLABParser.Xpr_handleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MATLABParser#command_argument.
    def visitCommand_argument(self, ctx:MATLABParser.Command_argumentContext):
        return self.visitChildren(ctx)



del MATLABParser