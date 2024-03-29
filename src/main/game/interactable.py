class Interactable:

    def __init__(self, can_repeat = False):
        self.has_touched = False
        self.can_repeat = can_repeat

    def __repr__(self):
        str = "Interactable"
        for key in self.__dict__:
            str += f"\n\t{key} : {self.__dict__[key]}"
        return str
    
    def on_touch(self, func):
            self.touch_func = func()

    def touch(self):
        if not self.has_touched or self.can_repeat:
             self.touch_func()
        self.has_touched = True