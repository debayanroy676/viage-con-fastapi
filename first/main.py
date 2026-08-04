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

from fastapi import FastAPI
#core fastapi application class
from fastapi import Path
#path function: used to provide metadata, validation rules and documentation hints for path parameter 
from fastapi import HTTPException
#custom builtin exception used to return custom error response
from fastapi import Query
#used to specify Queary parameters
import json
#to load json data

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get('/')
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message':'A fully functional API to manage patient records'}

@app.get('/view')
def view():
     data = load_data()
     return data
 
@app.get('/patients/{patient_id}')
def view_byid(patient_id: str = Path(..., description='Patient ID', example='P001')) :
    # ... -> required, example -> sets an example
    data = load_data()
    if patient_id in data :
         return data[patient_id]
    '''else :
        return {'error':'not found'}
        problem : error but what type ???? 
        it should be 404 because content doesnot exist
        thats why we use custom http exception
    '''
    raise HTTPException(status_code=404, detail='Patient Not Found') 

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='sort by height wright or BMI'), order: str = Query('asc', description='sort in ascending or descending order')):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields :
        raise HTTPException(status_code=400, detail=f'Invalid field selected from {valid_fields}')
    if order not in ['asc', 'desc'] :
        raise HTTPException(status_code=400, detail='Invalid order selection, expected values is asc or desc')
    data = load_data()
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by, 0), reverse=sort_order)
    return sorted_data

