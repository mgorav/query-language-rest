# Generated from /Users/paul.rutledge/PyCharmProjects/rsql-python/rest-query-grammar.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QueryParser import QueryParser
else:
    from RsqlParser import RsqlParser

# This class defines a complete generic visitor for a parse tree produced by QueryParser.

class QueryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RsqlParser#statement.
    def visitStatement(self, ctx:QueryParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RsqlParser#comparison.
    def visitComparison(self, ctx:QueryParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RsqlParser#boolean_value.
    def visitBoolean_value(self, ctx:QueryParser.Boolean_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RsqlParser#single_value.
    def visitSingle_value(self, ctx:QueryParser.Single_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RsqlParser#multi_value.
    def visitMulti_value(self, ctx:QueryParser.Multi_valueContext):
        return self.visitChildren(ctx)



del QueryParser