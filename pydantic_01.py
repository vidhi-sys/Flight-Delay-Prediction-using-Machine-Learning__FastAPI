from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Annotated
class person(BaseModel):
    name:Annotated[str,Field(title='name of the person ',description='give string value as name ',examples=['vidhi','mahi','vaidik'])]
    age:int=Field(gt=3,lt=100)
    #type validation:step01-create class
    indian:Annotated[bool,Field(default=True,description='tell whether you are indian nationality or not')]
    allergies:list[str]=Field(max_length=10)
    contact_no:list[int]
    #data validation in pydantic
    email:EmailStr
    #custom validation by feild &used as meta data also
    weight:float=Field(gt=0)
    
#step02-some basic oops steps creatin fxn,object calling it   
def insert_data(person:person):
        print(person.name)
        print(person.email)
        print(person.weight)
        print('inserted into db')
     
info={'name':'vidhi','age':21,'weight':67.5,'indian':True,'allergies':['pollen','dust'],'contact_no':[91,9425221],'email':'vidhiudasi@email.com'}
#valid email address: An email address must have an @-sign. [type=value_error, input_value='vidhiudasimmm.com', input_type=str]
person01=person(**info) #** =unpacking dictionary
insert_data(person01)
"""def insert_data(name:str ,age :int):
    if(type(age)==int):
        
        print(name)
        print(age)
        print('inserted into db')
    else:
        raise TypeError('incorrect DT') ###   
simple fxn puts into db but if-else is too hectic to type
someone else uses this fxn but somevalues that arent expected may be put such as age datatype
insert_data('vidhi','twenty-one')
type validation problem 
insert_data('vidhi',21) 
Python's dynamic nature means
it still runs the code even if types mismatch (as shown in the add("2", "4") example in),
but type checkers will flag these as errors, offering a powerful way to build robust applications"""

