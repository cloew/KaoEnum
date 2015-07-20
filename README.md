# KaoEnum

*KaoEnum* is a Python package to provide simple Enum objects.
Typically, Python doesn't need regular enums, but sometimes they can be handy.

## Usage

*KaoEnum* provides two ways to build enums (*enum* and *enum_as*).

### enum
Here's an example using the *enum* decorator.

```python
from kao_enum import enum

@enum
class States:
    Running = 0
    Jumping = 1
        
States.fromName("Running") # States.Running
States.fromValue(1) # States.Jumping
```

A class using an enum decorator will have all values not starting with '_' changed to be wrapped in an enum object.
The decorated class provides two class methods:
* *fromName* - returns the enum object with the given name
* *fromValue* - returns the enum object with the given value

### enum_as
The *enum_as* decorator allows you to specify the class to be used for each enum name-value pair.
Here's an example using the *enum_as* decorator.

```python
from kao_enum import enum_as

class SpecialEnum:
    def __init__(self, name, value):
        self.name = name
        self.value = value

@enum_as(SpecialEnum)
class States:
    Running = 0
    Jumping = 1
```

The *enum_as* decorator provides the same methods as *enum*, but allows you to provide custom functionality on the enum objects for your convenience.
The Enum object class is only required to have a constructor that accepts the name and value (as seen above).

Note the variable names on the class do not need to be 'name' and 'value'.
The following is also valid:
```python
class SpecialEnum:
    def __init__(self, notName, notValue):
        self.notName = notName
        self.notValue = notValue
```