from rest_query import *
from tinydb import *
import operator, functools


class TinyDBQuerying(QueryGeneratingVisitor):

    def and_node(self, children):
        return functools.reduce(operator.and_, children)

    def or_node(self, children):
        return functools.reduce(operator.or_, children)

    def wrap(self, child):
        return (child)

    def operator(self, key, operator, values):
        if operator == '==':
            return where(key) == values
        elif operator == '!=':
            return where(key) != values
        elif operator == '=gt=':
            return where(key) > values
        elif operator == '=ge=':
            return where(key) >= values
        elif operator == '=lt=':
            return where(key) < values
        elif operator == '=le=':
            return where(key) <= values
        elif operator == '=ex=':
            return where(key).exists() if values == True else ~where(key).exists()
        elif operator == '=in=':
            return where(key).any(values)
        elif operator == '=out=':
            return ~where(key).any(values)
        else:
            raise NotImplementedError


tiny_db_querying = parse("(blah=ex=true;foo=='bar'),someNumber!=3.0", TinyDBQuerying())

print(tiny_db_querying)
