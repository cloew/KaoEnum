from .enum import Enum

def enum_as(enumCls):
    """ Return a decorator that uses the given class as the Enum Value Class """
    def asEnum(cls):
        valueToEnum = {}
        for name in dir(cls):
            if not name.startswith('_'):
                value = getattr(cls, name)
                
                enumObj = enumCls(name, value)
                setattr(cls, name, enumObj)
                valueToEnum[value] = enumObj
                
        cls.__valueToEnum = valueToEnum
        
        @classmethod
        def fromName(cls, name):
            try:
                return getattr(cls, name)
            except KeyError:
                return None
        cls.fromName = fromName
        
        @classmethod
        def fromValue(cls, value):
            try:
                return cls.__valueToEnum[value]
            except KeyError:
                return None
        cls.fromValue = fromValue
        return cls
    return asEnum

enum = enum_as(Enum)
    