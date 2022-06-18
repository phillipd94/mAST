# Generated from .\MATLAB.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MATLABParser import MATLABParser
else:
    from MATLABParser import MATLABParser

# This class defines a complete listener for a parse tree produced by MATLABParser.
class MATLABListener(ParseTreeListener):

    # Enter a parse tree produced by MATLABParser#atom_boolean.
    def enterAtom_boolean(self, ctx:MATLABParser.Atom_booleanContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_boolean.
    def exitAtom_boolean(self, ctx:MATLABParser.Atom_booleanContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_empty_array.
    def enterAtom_empty_array(self, ctx:MATLABParser.Atom_empty_arrayContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_empty_array.
    def exitAtom_empty_array(self, ctx:MATLABParser.Atom_empty_arrayContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_empty_cell.
    def enterAtom_empty_cell(self, ctx:MATLABParser.Atom_empty_cellContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_empty_cell.
    def exitAtom_empty_cell(self, ctx:MATLABParser.Atom_empty_cellContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_end.
    def enterAtom_end(self, ctx:MATLABParser.Atom_endContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_end.
    def exitAtom_end(self, ctx:MATLABParser.Atom_endContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_float.
    def enterAtom_float(self, ctx:MATLABParser.Atom_floatContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_float.
    def exitAtom_float(self, ctx:MATLABParser.Atom_floatContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_imaginary.
    def enterAtom_imaginary(self, ctx:MATLABParser.Atom_imaginaryContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_imaginary.
    def exitAtom_imaginary(self, ctx:MATLABParser.Atom_imaginaryContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_index_all.
    def enterAtom_index_all(self, ctx:MATLABParser.Atom_index_allContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_index_all.
    def exitAtom_index_all(self, ctx:MATLABParser.Atom_index_allContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_integer.
    def enterAtom_integer(self, ctx:MATLABParser.Atom_integerContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_integer.
    def exitAtom_integer(self, ctx:MATLABParser.Atom_integerContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_meta.
    def enterAtom_meta(self, ctx:MATLABParser.Atom_metaContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_meta.
    def exitAtom_meta(self, ctx:MATLABParser.Atom_metaContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_string.
    def enterAtom_string(self, ctx:MATLABParser.Atom_stringContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_string.
    def exitAtom_string(self, ctx:MATLABParser.Atom_stringContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_var.
    def enterAtom_var(self, ctx:MATLABParser.Atom_varContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_var.
    def exitAtom_var(self, ctx:MATLABParser.Atom_varContext):
        pass


    # Enter a parse tree produced by MATLABParser#matlab_file.
    def enterMatlab_file(self, ctx:MATLABParser.Matlab_fileContext):
        pass

    # Exit a parse tree produced by MATLABParser#matlab_file.
    def exitMatlab_file(self, ctx:MATLABParser.Matlab_fileContext):
        pass


    # Enter a parse tree produced by MATLABParser#def_class.
    def enterDef_class(self, ctx:MATLABParser.Def_classContext):
        pass

    # Exit a parse tree produced by MATLABParser#def_class.
    def exitDef_class(self, ctx:MATLABParser.Def_classContext):
        pass


    # Enter a parse tree produced by MATLABParser#def_function.
    def enterDef_function(self, ctx:MATLABParser.Def_functionContext):
        pass

    # Exit a parse tree produced by MATLABParser#def_function.
    def exitDef_function(self, ctx:MATLABParser.Def_functionContext):
        pass


    # Enter a parse tree produced by MATLABParser#attrib_class_boolean.
    def enterAttrib_class_boolean(self, ctx:MATLABParser.Attrib_class_booleanContext):
        pass

    # Exit a parse tree produced by MATLABParser#attrib_class_boolean.
    def exitAttrib_class_boolean(self, ctx:MATLABParser.Attrib_class_booleanContext):
        pass


    # Enter a parse tree produced by MATLABParser#attrib_class_meta.
    def enterAttrib_class_meta(self, ctx:MATLABParser.Attrib_class_metaContext):
        pass

    # Exit a parse tree produced by MATLABParser#attrib_class_meta.
    def exitAttrib_class_meta(self, ctx:MATLABParser.Attrib_class_metaContext):
        pass


    # Enter a parse tree produced by MATLABParser#attrib_property_boolean.
    def enterAttrib_property_boolean(self, ctx:MATLABParser.Attrib_property_booleanContext):
        pass

    # Exit a parse tree produced by MATLABParser#attrib_property_boolean.
    def exitAttrib_property_boolean(self, ctx:MATLABParser.Attrib_property_booleanContext):
        pass


    # Enter a parse tree produced by MATLABParser#attrib_property_access.
    def enterAttrib_property_access(self, ctx:MATLABParser.Attrib_property_accessContext):
        pass

    # Exit a parse tree produced by MATLABParser#attrib_property_access.
    def exitAttrib_property_access(self, ctx:MATLABParser.Attrib_property_accessContext):
        pass


    # Enter a parse tree produced by MATLABParser#attrib_method_boolean.
    def enterAttrib_method_boolean(self, ctx:MATLABParser.Attrib_method_booleanContext):
        pass

    # Exit a parse tree produced by MATLABParser#attrib_method_boolean.
    def exitAttrib_method_boolean(self, ctx:MATLABParser.Attrib_method_booleanContext):
        pass


    # Enter a parse tree produced by MATLABParser#attrib_method_access.
    def enterAttrib_method_access(self, ctx:MATLABParser.Attrib_method_accessContext):
        pass

    # Exit a parse tree produced by MATLABParser#attrib_method_access.
    def exitAttrib_method_access(self, ctx:MATLABParser.Attrib_method_accessContext):
        pass


    # Enter a parse tree produced by MATLABParser#atom_access.
    def enterAtom_access(self, ctx:MATLABParser.Atom_accessContext):
        pass

    # Exit a parse tree produced by MATLABParser#atom_access.
    def exitAtom_access(self, ctx:MATLABParser.Atom_accessContext):
        pass


    # Enter a parse tree produced by MATLABParser#st_assign.
    def enterSt_assign(self, ctx:MATLABParser.St_assignContext):
        pass

    # Exit a parse tree produced by MATLABParser#st_assign.
    def exitSt_assign(self, ctx:MATLABParser.St_assignContext):
        pass


    # Enter a parse tree produced by MATLABParser#st_command.
    def enterSt_command(self, ctx:MATLABParser.St_commandContext):
        pass

    # Exit a parse tree produced by MATLABParser#st_command.
    def exitSt_command(self, ctx:MATLABParser.St_commandContext):
        pass


    # Enter a parse tree produced by MATLABParser#st_if.
    def enterSt_if(self, ctx:MATLABParser.St_ifContext):
        pass

    # Exit a parse tree produced by MATLABParser#st_if.
    def exitSt_if(self, ctx:MATLABParser.St_ifContext):
        pass


    # Enter a parse tree produced by MATLABParser#st_for.
    def enterSt_for(self, ctx:MATLABParser.St_forContext):
        pass

    # Exit a parse tree produced by MATLABParser#st_for.
    def exitSt_for(self, ctx:MATLABParser.St_forContext):
        pass


    # Enter a parse tree produced by MATLABParser#st_switch.
    def enterSt_switch(self, ctx:MATLABParser.St_switchContext):
        pass

    # Exit a parse tree produced by MATLABParser#st_switch.
    def exitSt_switch(self, ctx:MATLABParser.St_switchContext):
        pass


    # Enter a parse tree produced by MATLABParser#st_try.
    def enterSt_try(self, ctx:MATLABParser.St_tryContext):
        pass

    # Exit a parse tree produced by MATLABParser#st_try.
    def exitSt_try(self, ctx:MATLABParser.St_tryContext):
        pass


    # Enter a parse tree produced by MATLABParser#st_while.
    def enterSt_while(self, ctx:MATLABParser.St_whileContext):
        pass

    # Exit a parse tree produced by MATLABParser#st_while.
    def exitSt_while(self, ctx:MATLABParser.St_whileContext):
        pass


    # Enter a parse tree produced by MATLABParser#function_params.
    def enterFunction_params(self, ctx:MATLABParser.Function_paramsContext):
        pass

    # Exit a parse tree produced by MATLABParser#function_params.
    def exitFunction_params(self, ctx:MATLABParser.Function_paramsContext):
        pass


    # Enter a parse tree produced by MATLABParser#function_returns.
    def enterFunction_returns(self, ctx:MATLABParser.Function_returnsContext):
        pass

    # Exit a parse tree produced by MATLABParser#function_returns.
    def exitFunction_returns(self, ctx:MATLABParser.Function_returnsContext):
        pass


    # Enter a parse tree produced by MATLABParser#statement.
    def enterStatement(self, ctx:MATLABParser.StatementContext):
        pass

    # Exit a parse tree produced by MATLABParser#statement.
    def exitStatement(self, ctx:MATLABParser.StatementContext):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_tree.
    def enterXpr_tree(self, ctx:MATLABParser.Xpr_treeContext):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_tree.
    def exitXpr_tree(self, ctx:MATLABParser.Xpr_treeContext):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_tree_.
    def enterXpr_tree_(self, ctx:MATLABParser.Xpr_tree_Context):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_tree_.
    def exitXpr_tree_(self, ctx:MATLABParser.Xpr_tree_Context):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_array.
    def enterXpr_array(self, ctx:MATLABParser.Xpr_arrayContext):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_array.
    def exitXpr_array(self, ctx:MATLABParser.Xpr_arrayContext):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_array_.
    def enterXpr_array_(self, ctx:MATLABParser.Xpr_array_Context):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_array_.
    def exitXpr_array_(self, ctx:MATLABParser.Xpr_array_Context):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_cell.
    def enterXpr_cell(self, ctx:MATLABParser.Xpr_cellContext):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_cell.
    def exitXpr_cell(self, ctx:MATLABParser.Xpr_cellContext):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_cell_.
    def enterXpr_cell_(self, ctx:MATLABParser.Xpr_cell_Context):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_cell_.
    def exitXpr_cell_(self, ctx:MATLABParser.Xpr_cell_Context):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_array_index.
    def enterXpr_array_index(self, ctx:MATLABParser.Xpr_array_indexContext):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_array_index.
    def exitXpr_array_index(self, ctx:MATLABParser.Xpr_array_indexContext):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_cell_index.
    def enterXpr_cell_index(self, ctx:MATLABParser.Xpr_cell_indexContext):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_cell_index.
    def exitXpr_cell_index(self, ctx:MATLABParser.Xpr_cell_indexContext):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_field.
    def enterXpr_field(self, ctx:MATLABParser.Xpr_fieldContext):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_field.
    def exitXpr_field(self, ctx:MATLABParser.Xpr_fieldContext):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_function.
    def enterXpr_function(self, ctx:MATLABParser.Xpr_functionContext):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_function.
    def exitXpr_function(self, ctx:MATLABParser.Xpr_functionContext):
        pass


    # Enter a parse tree produced by MATLABParser#xpr_handle.
    def enterXpr_handle(self, ctx:MATLABParser.Xpr_handleContext):
        pass

    # Exit a parse tree produced by MATLABParser#xpr_handle.
    def exitXpr_handle(self, ctx:MATLABParser.Xpr_handleContext):
        pass


    # Enter a parse tree produced by MATLABParser#command_argument.
    def enterCommand_argument(self, ctx:MATLABParser.Command_argumentContext):
        pass

    # Exit a parse tree produced by MATLABParser#command_argument.
    def exitCommand_argument(self, ctx:MATLABParser.Command_argumentContext):
        pass



del MATLABParser