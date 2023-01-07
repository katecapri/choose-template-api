from pymongo import MongoClient

client = MongoClient('mongodb://user:pass@mongodb:27017/?retryWrites=true&w=majority')
database = client["templates_db"]
templates = database['templates']
templates_ = [
    {
        "name": "Primary school student",
        "student_firstname": "text",
        "student_lastname": "text",
        "student_birthday": "date",
        "class_number": "text",
        "parent_name": "text",
        "parent_email": "email",
        "parent_phone": "phone",
    },
    {
        "name": "Visit to the doctor",
        "patient_name": "text",
        "patient_birthday": "date",
        "patient_email": "email",
        "patient_phone": "phone",
        "doctor_name": "text",
        "cabinet_number": "text",
        "visit_date": "date",
        "visit_time": "text",
    },
    {
        "name": "Hotel rental",
        "hotel_address": "text",
        "guest_name": "text",
        "guest_email": "email",
        "guest_phone": "phone",
        "room_number": "text",
        "rental_start_date": "date",
        "rental_end_date": "date",
    },
]
templates.insert_many(templates_)
