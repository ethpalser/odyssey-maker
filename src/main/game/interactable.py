from action import actions

class Interactable:

    def __init__(self, can_repeat = False):
        self.has_touched = False
        self.can_repeat = can_repeat
        self.on_touch = None

    def __repr__(self):
        str = "Interactable"
        for key in self.__dict__:
            str += f"\n\t{key} : {self.__dict__[key]}"
        return str
    
    def set_on_touch(self, action:str):
            if action in actions:
                self.on_touch = actions[action]
            else:
                self.on_touch = None

    def touch(self, *args):
        if not self.has_touched or self.can_repeat:
             self.on_touch(*args)
        self.has_touched = True