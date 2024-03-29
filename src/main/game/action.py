def get(obj:object, field:str):
    if obj == None or field == None:
        raise ValueError("Invalid object reference")
    return obj.__dict__[field]

def set(obj:object, field:str, value):
    if obj == None or field == None:
        raise ValueError("Invalid object reference")
    obj.__dict__[field] = value

def show(obj):
    set(obj, "show", True)

def hide(obj):
    set(obj, "show", False)

def display(obj:object):
    if "show" in obj.__dict__ and obj.__dict__["show"] is True:
        return get(obj, "to_display")

actions = {
    "show": display,
    "display": display
}