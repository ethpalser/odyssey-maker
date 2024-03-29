from interactable import Interactable

class Entity(Interactable):
    
    def __init__(self):
        super(Interactable, self).__init__()

    def __repr__(self) -> str:
        str = "Entity"
        for key in self.__dict__:
            str += f"\n\t{key} : {self.__dict__[key]}"
        return str