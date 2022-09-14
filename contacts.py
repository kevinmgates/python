contacts = {
    "number": 4,
    "students": 
    [
        {"name":"Sarah", "email": "sarah@me.com"},
        {"name":"Tom", "email": "tom@me.com"},
        {"name":"Harry", "email": "harry@me.com"},
        {"name":"Sam", "email": "sam@me.com"}
    ]
}

for student in contacts["students"]:
    print(student['email'])