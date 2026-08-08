from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict


class Patient(BaseModel) :
	name : str
	age : int
	bmi : int 
	allergies : Optional[List[str]] = None
	contact : Dict[str, str]

def add_to_DB(patient : Patient) :
	print(patient.name)
	print(patient.age)
	print(patient.bmi)
	print(patient.allergies)
	print("Phone = "+patient.contact['phone']+"\nAddress = "+patient.contact['address'])

patient1_info = {
	'name' : "Debayan",
	'age' : 20,
	'bmi' : 18,
	'allergies' : ['Dust', 'Pollen'],
	'contact' : {
		'phone' : "9088550933",
		'address' : "Sonarpur"
	}
}

patient1 = Patient(**patient1_info)
add_to_DB(patient1)
