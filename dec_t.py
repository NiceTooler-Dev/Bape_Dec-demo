#瞎写的
from collections import namedtuple
from typing import Any
Module_List = []
def Create_Module():
    ModuleInfo = namedtuple("mi",["name","des","cat","runner"])
    return ModuleInfo
ModuleInfo = Create_Module()
class Module_Message:
    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def wrapper(*args, **kwds):
            im = Create_Module()
            im.name = self.name
            im.runner = cls().run
            Module_List.append(im)
            clss = cls
            return clss
        return wrapper



@Module_Message(name="KillArua")
class No:
    def __init__(self):
        print("Running")
    
    def run(*args, **kwargs):
        print(Module_List[0].name +"start!")

o = No()
Module_List[0].runner()
