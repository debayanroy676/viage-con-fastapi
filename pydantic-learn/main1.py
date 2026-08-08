#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2026 Debayan Roy <debayanroy676@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from pydantic import BaseModel

class Patient(BaseModel): #Type Validation Schema using Pydantic
	name: str
	age: int
	
def insert_to_DB(patient: Patient) :
	ret = "failure"
	print(f"Inserted Data\nName : {patient.name}\nAge = {patient.age}")
	ret = "success"
	print(ret)

patient_info1 = {
	"name" : "Debayan",
	"age" : 20
}

patient_info2 = {
	"name" : "Debayan",
	"age" : '20'
}

patient1 = Patient(**patient_info1)
insert_to_DB(patient1)


patient2 = Patient(**patient_info2) # '20' converted to 20 by Pydantic (string to integer)
insert_to_DB(patient2)
