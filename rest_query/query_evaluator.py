from generated.QueryParser import *
from generated.QueryLexer import *
from generated.QueryVisitor import *
import ast

class QueryVisitor(object):

	def and_node(self, children):
		raise NotImplementedError

	def or_node(self, children):
		raise NotImplementedError

	def wrap(self, child):
		raise NotImplementedError

	def operator(self, key, operator, values):
		raise NotImplementedError


class Visitor(QueryVisitor):
	def __init__(self, delegate: QueryVisitor):
		self.delegate = delegate

	def visitStatement(self, ctx: QueryParser.StatementContext):
		if ctx.left and ctx.op and ctx.right:
			if ctx.op.type == QueryParser.AND_OPERATOR:
				return self.delegate.and_node((self.visit(ctx.left), self.visit(ctx.right)))
			elif ctx.op.type == QueryParser.OR_OPERATOR:
				return self.delegate.or_node((self.visit(ctx.left), self.visit(ctx.right)))
		elif ctx.wrapped:
			return self.delegate.wrap(self.visit(ctx.wrapped))
		elif ctx.node:
			return self.visit(ctx.node)

	def visitComparison(self, ctx: QueryParser.ComparisonContext):
		return self.delegate.operator(ctx.key.text, ctx.op.text, self.visit(ctx.value))

	def visitBoolean_value(self, ctx: QueryParser.Boolean_valueContext):
		return bool(ctx.getText())

	def visitSingle_value(self, ctx: QueryParser.Single_valueContext):
		if ctx.TRUE() or ctx.FALSE():
			return bool(ctx.getText())
		elif ctx.NUMERIC_LITERAL():
			textual = ctx.getText()
			if '.' in textual:
				return float(ctx.getText())
			else:
				return int(ctx.getText())
		elif ctx.STRING_LITERAL():
			return ast.literal_eval(ctx.getText())
		else:
			raise NotImplementedError


def parse(rsql: str, visitor: QueryVisitor):
	lexer = QueryLexer(InputStream(rsql))
	parser = QueryParser(CommonTokenStream(lexer))
	tree = parser.statement()
	return tree.accept(Visitor(visitor))
