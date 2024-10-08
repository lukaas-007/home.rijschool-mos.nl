import json
import mysql.connector

def parse_lessons(response_data):
    """Parses and formats the lesson data from the response."""
    if response_data:
        # Remove the first and last characters from the response body
        response_data = response_data[1:-1]
        lesson_data = '[' + response_data + ']'
        all_lessons = json.loads(lesson_data)
        
        formated_lessons = []
        for lesson in all_lessons:
            formated_lessons.append({
                "start": lesson['start'],
                "end": lesson['end'],
                "id": lesson['id'],
                "primary_color": lesson['primary_color'],
                "students_with_absence": lesson['students_with_absence'],
                "typeName": lesson['typeName'],
                "note": lesson['note']
            })
        return formated_lessons
    return []

def save_lessons_to_database(lessons):
    """Saves the lesson data to the clarien table."""
    mydb = mysql.connector.connect(
    host="phpmyadmin.lucasvanbriemen.nl",
    user="LucasDatabase",
    password="LucasDatabase",
    database="rijles"
    )

    mycursor = mydb.cursor()
    
    for lesson in lessons:
        sql = "INSERT INTO clarien (start, end, id, primary_color, students_with_absence, typeName, note) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (lesson['start'], lesson['end'], lesson['id'], lesson['primary_color'], lesson['students_with_absence'], lesson['typeName'], lesson['note'])
        mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
        