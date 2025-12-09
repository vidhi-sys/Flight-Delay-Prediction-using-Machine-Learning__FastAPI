from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import List,Dict,Annotated
class person(BaseModel):
    name:Annotated[str,Field(title='name of the person ',description='give string value as name ',examples=['vidhi','mahi','vaidik'])]
    age:int=Field(gt=3,lt=100)
    indian:Annotated[bool,Field(default=True,description='tell whether you are indian nationality or not')]
    allergies:list[str]=Field(max_length=10)
    contact_no:list[int]
    #checking whther the person belongs to vitbhopal or not
    email:EmailStr
    weight:float=Field(gt=0)  
    @field_validator('email')
    #decorator
    @classmethod
    def email_validator(cls,value):
        valid=['vit.com','vitb.com','vitbhopal.ac.in'] 
        domain_name = value.split('@')[-1]

        if domain_name not in valid:
            raise ValueError('Not a valid domain')
        return value

def insert_data(person:person):
        print(person.name)
        print(person.email)
        print(person.weight)
        print('inserted into db')     
info={'name':'vidhi','age':21,'weight':67.5,'indian':True,'allergies':['pollen','dust'],'contact_no':[91,9425221],'email':'vidhiudasi@vitb.com'}
person01=person(**info) 
insert_data(person01)
