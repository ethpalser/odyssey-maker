class Instance:

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        str = "Instance"
        for key in self.__dict__:
            str += f"\n\t{key} : {self.__dict__[key]}"
        return str