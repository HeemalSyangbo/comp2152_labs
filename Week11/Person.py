class Person:
    def __init__(self, p_name, p_age, p_height):
        print("Constructing the person object")
        self._name = p_name
        self._age = p_age
        self._height = p_height
        self.public_prop = "I'm Public"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def _del_(self):
        print("The garbage collector is automatically destroying the person object!")