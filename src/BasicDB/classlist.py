from basicdb import *
import sys

db_filename = "registrar.json"

tbl_rooms = "rooms"
tbl_students = "students"
tbl_courses = "courses"
tbl_enrollments = "enrollments"

def init_db():
    if db == None:
        load_db(db_filename)

def get_course_info(course_id):
    try:
        course = where(db_from(tbl_courses), "courseid", course_id)

        if len(course) == 0:
            raise Exception("Unable to find course with id: " + course_id)

        course_detail = join(db_from(tbl_courses), where(db_from(tbl_courses), "courseid", course_id), "courseid").pop()
        rooms = join(db_from(tbl_rooms), course, "roomid").pop()
        enrollments = join(db_from(tbl_students), where(db_from(tbl_enrollments), "courseid", course_id), "studentid")
        
        print(course_detail["coursename"] + " meets " + rooms["times"] + " in " + rooms["roomname"])
        
        students = []
        for s in enrollments:
            students.append(s["firstname"] + " " + s["lastname"])

        for s in sorted(students):
            print(s)

        enrolled = len(students)
        print("Current enrollment: " + str(enrolled))
        print("Remaining capacity: " + str(int(rooms["capacity"]) - enrolled))

    except Exception as err:
        print(err)

if __name__ == "__main__":

    init_db()

    try:
        course_id = sys.argv[1]

        get_course_info(course_id)

    except Exception as err:
        print("Error getting course info for: " + course_id)