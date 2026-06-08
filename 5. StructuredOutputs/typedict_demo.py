from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int 
    
new_person = Person = {'name': 'nishita', 'age': '22'}
print(new_person)