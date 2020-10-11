from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QueryParser import QueryParser
else:
    from .QueryParser import QueryParser

# This class defines a complete listener for a parse tree produced by QueryParser.
class QueryListener(ParseTreeListener):

    # Enter a parse tree produced by RsqlParser#statement.
    def enterStatement(self, ctx:QueryParser.StatementContext):
        pass

    # Exit a parse tree produced by RsqlParser#statement.
    def exitStatement(self, ctx:QueryParser.StatementContext):
        pass


    # Enter a parse tree produced by RsqlParser#comparison.
    def enterComparison(self, ctx:QueryParser.ComparisonContext):
        pass

    # Exit a parse tree produced by RsqlParser#comparison.
    def exitComparison(self, ctx:QueryParser.ComparisonContext):
        pass


    # Enter a parse tree produced by RsqlParser#boolean_value.
    def enterBoolean_value(self, ctx:QueryParser.Boolean_valueContext):
        pass

    # Exit a parse tree produced by RsqlParser#boolean_value.
    def exitBoolean_value(self, ctx:QueryParser.Boolean_valueContext):
        pass


    # Enter a parse tree produced by RsqlParser#single_value.
    def enterSingle_value(self, ctx:QueryParser.Single_valueContext):
        pass

    # Exit a parse tree produced by RsqlParser#single_value.
    def exitSingle_value(self, ctx:QueryParser.Single_valueContext):
        pass


    # Enter a parse tree produced by RsqlParser#multi_value.
    def enterMulti_value(self, ctx:QueryParser.Multi_valueContext):
        pass

    # Exit a parse tree produced by RsqlParser#multi_value.
    def exitMulti_value(self, ctx:QueryParser.Multi_valueContext):
        pass


