
class Enum:
    """ Represents an Enum Value """
    
    def __init__(self, name, value):
        """ Initialize the enum """
        self.name = name
        self.value = value
        
    def __repr__(self):
        """ Return the string representation of this code """
        return self.name