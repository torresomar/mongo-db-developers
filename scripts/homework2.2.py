# Write a program in the language of your choice that will remove the grade of type "homework"
# with the lowest score for each student from the dataset in the handout. Since each document
# is one grade, it should remove one document per student. This will use the same data set as
# the last problem, but if you don't have it, you can download and re-import.

import pymongo
from bson.objectid import ObjectId

db_address = '127.0.0.1'
connection = pymongo.MongoClient(db_address,29017)
database = connection.students
collection = database.grades

student_grades = collection.group(['student_id'], None,{'list': []},'function(obj, prev) {prev.list.push(obj)}') 
print len(student_grades)
# Issuing a multiple document query
for student in student_grades:
    grade_to_remove = None
    print "Evaluating student"
    for grade in student["list"]:
        if grade["type"] == "homework":
            print "Grade => " + str(grade["score"])
            if grade_to_remove == None:
                grade_to_remove = grade
            else:
                if grade_to_remove["score"] > grade["score"]:
                    grade_to_remove = grade
    print "Lowest score for user is " + str(grade_to_remove["type"]) + " " + str(grade_to_remove["score"])
    collection.remove({'_id': ObjectId(grade_to_remove["_id"])})

print len(student_grades)
