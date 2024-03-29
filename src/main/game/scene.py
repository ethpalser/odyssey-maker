class Scene:

    def __init__(self):
        pass

    def __repr__(self) -> str:
        str = "Encounter"
        for key in self.__dict__:
            str += f"\n\t{key} : {self.__dict__[key]}"
        return str