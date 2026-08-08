from pydantic import BaseModel, Field, field_validator, AnyUrl, EmailStr
from typing import Optional, Annotated

class Employee(BaseModel) :
	name : Annotated[str, Field(max_length=50, title="Name of Employee", description="Enter the name of the employee in less than 50 characters", examples=['Debayan', 'nelson', 'Roy Keane'], strict=True)]
	
	age : Annotated[int, Field(title="Age of the employee", description="Enter the age of the employee", strict=True)]
	
	email : Annotated[EmailStr, Field(title="Contact Email", description="Enter valid contact email of the employee")]
	
	linkedin : Annotated[AnyUrl, Field(title="Linkedin Profile Link", description="Enter the Linkedin Profile URL of the employee")]
	
	married : Annotated[Optional[bool], Field(title="Enter the Employee Married Details", description="True for married, False for not, optional field", strict=False)] = None
	
	### field validator and decorator validation methods ###
	
	# Validator method for employee age
	@field_validator('age', mode='after')
	@classmethod
	def validate_age(cls, value) :
		if not 18 <= value <= 60: 
			raise ValueError("Age should be in between 18 and 60 years")
		else :
			return value
			
	# Validator method for employee name
	@field_validator('name', mode='after')
	@classmethod
	def validate_name(cls, value) :
		return value.upper()

def add_to_DB(employee : Employee) :
	print(employee.name)
	print(employee.age)
	print(employee.email)
	print(employee.linkedin)
	print(employee.married)
	
employee_info = {
	'name' : 'Debayan Roy',
	'age' : 20,
	'email' : "debayanroy676@gmail.com",
	'linkedin' : "https://www.linkedin.com/debayanroy",
	'married' : None
}

employee1 = Employee(**employee_info)
add_to_DB(employee1)
