# Typing

from typing import List, Dict, Union
def func() -> None: # -> None means return type is None
    print("xyz")

def func1(name: str) -> List[Dict(str, Union(str, int))]: # for type hinting we have to import 
    