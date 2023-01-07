import os

import requests

SERVER_URL = 'http://127.0.0.1:8000/'
SERVER_DOCKER_URL = 'http://127.0.0.1/'
page_url = 'get_form/'
query_set = [
    {
        "cabinet_number": 345,
        "visit_date": "31.12.1995",
        "patient_email": "gfsgf@fhdh.ggh"
    },
    {
        "cabinet_number": "+7 999 999 99 99",
        "visit_date": "31.12.1995",
        "patient_email": "gfsgf@fhdh.ggh"
    },
    {
        "111cabinet_number": "987654",
        "111visit_date": "31.12.1995",
    },
    {
        "parent_name": "sdfjgkjljl",
        "parent_email": "rrrr3@tggg.ru",
        "parent_phone": "+7 912 034 87 65",
    },
    {
        "guest_email": "dgzsyk@lkjhgfd.com",
        "guest_phone": "+7 999 012 23 45",
    },
]
for query in query_set:
    response = requests.post(os.path.join(SERVER_DOCKER_URL, page_url), query)
    print(response.text)
