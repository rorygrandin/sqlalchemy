"""Classes used in pickling tests, need to be at the module level for unpickling."""

from test.orm import _base

class User(_base.ComparableEntity):
    pass

class Order(_base.ComparableEntity):
    pass

class EmailUser(User):
    pass

class Address(_base.ComparableEntity):
    pass

# TODO: these are kind of arbitrary....
class Child1(_base.ComparableEntity):
    pass

class Child2(_base.ComparableEntity):
    pass

class Parent(_base.ComparableEntity):
    pass

class Screen(object):
   def __init__(self, obj, parent=None):
       self.obj = obj
       self.parent = parent

class Foo(object):
    def __init__(self, moredata):
        self.data = 'im data'
        self.stuff = 'im stuff'
        self.moredata = moredata
    __hash__ = object.__hash__
    def __eq__(self, other):
        return other.data == self.data and other.stuff == self.stuff and other.moredata==self.moredata


class Bar(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    __hash__ = object.__hash__
    def __eq__(self, other):
        return other.__class__ is self.__class__ and other.x==self.x and other.y==self.y
    def __str__(self):
        return "Bar(%d, %d)" % (self.x, self.y)

class OldSchool:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return other.__class__ is self.__class__ and other.x==self.x and other.y==self.y

class OldSchoolWithoutCompare:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class BarWithoutCompare(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Bar(%d, %d)" % (self.x, self.y)


class NotComparable(object):
    def __init__(self, data):
        self.data = data

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return NotImplemented

    def __ne__(self, other):
        return NotImplemented


class BrokenComparable(object):
    def __init__(self, data):
        self.data = data

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        raise NotImplementedError

    def __ne__(self, other):
        raise NotImplementedError

