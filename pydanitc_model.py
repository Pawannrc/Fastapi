from pydantic import BaseModel ,  Field , AnyUrl, EmailStr , field_validator # pip install email-validator for EmailStr

from typing import Optional , Annotated ,List , Dict

# In pydantic first capital word since start otherwise it shows error

class employee(BaseModel):

    name: Annotated[str, Field(..., description="Name of the employee")]   # three dot and comma use for make field require

    designation: List[str]  # list of string means jo bhi data list me jayenga woh string hoga nahi tau error 

    country_mobile_no : List # list me both data dal sakte hai str , int

    state_city: Dict

    email: EmailStr # emailstr use email kind of data you need fisrt install first email-validator than use emailstr

    work_hour:Annotated[Optional[str] ,Field(default=None,description='working hour')] # field use for meta data 

    per_hour: Optional[float]= None  # optionall use for make optional field and always set default value none

    salary: Annotated[int, Field(..., gt=0,le=50000, title='salary ', description='salary of employ')] # gt for greater than and le gor less than

    web : AnyUrl
    
    email_val : Annotated[EmailStr, Field( description="only use icci.com and hdfc.com")]

    @field_validator('email_val')     # use for vaidation only we use icci.com and hdfc.com 
    @classmethod
    def email_validation(cls,value):
        
        valid_domain=['icci.com','hdfc.com']

        # agar domain me @ ke baad yeh icci.com, hdfc.com hona chahiye nahi tau error raise ho jayenga

        domain_name=value.split('@')[-1]
        if domain_name not in valid_domain:
           raise ValueError('not valid domain : please select hdfc.com and icci.com')
        return value

def dict_view(employee:employee):
    print(employee.name)
    print(employee.designation)
    print(employee.state_city)
    print(employee.email)
    print(employee.work_hour)
    print(employee.per_hour)
    print(employee.salary)
    print(employee.web)
    print (employee.country_mobile_no)
    print(employee.email_val)


dict_data = {"name":"pawan",
             "designation":["jr.data scientist","Engineer"],
             "state_city":{"Mahrashtra":"Aurangabad"},
             "salary":20000,
             "email":"pawan@gmail.com",
             "per_hour": 600, 
             "web":"https://www.paw.com",
             "email_val":"paw@hdfc.com",
             "country_mobile_no":['india', 98903456257],
             "email_val":"paw@hdfc.com"}

newdata= employee(**dict_data)

dict_view(newdata)













