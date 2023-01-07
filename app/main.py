import re
from urllib.parse import unquote

from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pymongo import MongoClient

app = FastAPI()
client = MongoClient('mongodb://user:pass@mongodb:27017/?retryWrites=true&w=majority')
database = client["templates_db"]
templates = database['templates']


def check_date(field):
    try:
        if len(field.split('.')) == 3:
            if len(field.split('.')[0]) == 2 and 0 < int(field.split('.')[0]) < 32:
                if len(field.split('.')[1]) == 2 and 0 < int(field.split('.')[1]) < 13:
                    if len(field.split('.')[2]) == 4 and 0 < int(field.split('.')[2]) < 3001:
                        return True
        if len(field.split('-')) == 3:
            if len(field.split('-')[2]) == 2 and 0 < int(field.split('-')[2]) < 32:
                if len(field.split('-')[1]) == 2 and 0 < int(field.split('-')[1]) < 13:
                    if len(field.split('-')[0]) == 4 and 0 < int(field.split('-')[0]) < 3001:
                        return True
    except:
        return False


def check_phone(field):
    try:
        if re.match(r'\+7\+*\d{3}\+*\d{3}\+*\d{2}\+*\d{2}', field):
            if re.match(r'\+7\+*\d{3}\+*\d{3}\+*\d{2}\+*\d{2}', field).start() == 0:
                if re.match(r'\+7\+*\d{3}\+*\d{3}\+*\d{2}\+*\d{2}', field).end() == 16:
                    return True
        elif re.match(r'\+7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}', field):
            if re.match(r'\+7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}', field).start() == 0:
                if re.match(r'\+7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}', field).end() == 16:
                    return True
    except:
        return False


def check_email(field):
    try:
        if '@' in field:
            if len(field.split('@')) == 2 and len(field.split('@')[0]) > 0 and '.' in field.split('@')[1]:
                if len(field.split('@')[1].split('.')[0]) > 0 and len(field.split('@')[1].split('.')[1]) > 0:
                    return True
    except:
        return False


def type_of_field(field):
    print(field)
    if check_date(field):
        return 'date'
    if check_phone(field):
        return 'phone'
    if check_email(field):
        return 'email'
    return 'text'


@app.get("/")
async def root():
    return "Check"


@app.get("/get_form/")
async def get_form():
    html_text = ''
    for template in templates.find():
        html_text += f'<h2>{template["name"]}</h2>'
        for key, value in template.items():
            html_text += f'<p>{key}: {value}</p>'
    return HTMLResponse(html_text)


@app.post("/get_form/")
def get_template(data=Body()):
    conditions = unquote(data).split('&')
    print(conditions)
    condition_dict = {}
    for condition in conditions:
        print(str(condition.split('=')[1]))
        condition_dict[condition.split('=')[0]] = type_of_field(str(condition.split('=')[1]))
    if templates.find_one(condition_dict):
        return templates.find_one(condition_dict)['name']
    else:
        return condition_dict
