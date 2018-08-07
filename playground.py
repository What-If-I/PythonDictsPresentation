# class ClassNoInit(object):
#     a = 'a'
#     b = 'b'
#     c = 'c'

try:
    range = xrange
except NameError:
    pass


class Foo(object):

    def __init__(self, foo, bar, baz):
        self.foo = foo
        self.bar = bar
        self.baz = baz
#
#
# class ClassInitSlots(object):
#     __slots__ = ['a', 'b', 'c']
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c


# [ClassNoInit() for _ in xrange(10000000)]
[Foo('a', 'b', 'c') for _ in range(10000000)]
