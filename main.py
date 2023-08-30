#Name: Rasha Ayman Abu Amro
#Date:30/8/2023
#Eng.Mohanad Alkrunz

print(""" Name: Rasha Ayman Abu Amro
          Date:30/8/2023
          Eng.Mohanad Alkrunz """)


import random


class Course:

    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 10000)
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    total_student_count = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(10000, 100000)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.course_list = []
        self.count = Student.total_student_count
        Student.total_student_count += 1

    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.course_list.append(course)


    def get_student_details(self):
        details={
            "Studant Id": self.student_id,
            "Name" : self.student_name,
            "Age":self.student_age,
            "Studant Number ":self.student_number,
            "Courses":[course.course_name for  course in self.course_list ]

        }
        return details

    def get_student_courses(self):
        for i in self.course_list:
            courses_dict = {course.course_id: {"Course Name": course.course_name, "Mark": course.course_mark}}
            return courses_dict

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.course_list)
        return total_marks / len(self.course_list)


student_list = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))

        if selection == 1:
            student_number = input("Enter Student Number")
            student_name = input("Enter Student Name")
            while True:
                try:
                    student_age = int(input("Enter Student Age"))
                    break
                except:
                    print("Invalid Value")

            student = Student(student_name, student_age, student_number)
            student_list.append(student)
            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number:")
            for i in student_list:
                if student_number == student.student_number:
                    student_list.remove(student)
                    print("deleted done")
                    break
                else:
                    print("Student Not Exist")


        elif selection == 3:
            student_number = input("Enter Student Number")
            for i in student_list:
                if student.student_number == student_number  :
                    print(student.get_student_details())

                else:
                    print("Student Not Exist")

        elif selection == 4:
            student_number = input("Enter Student Number")
            for i in student_list:
                if student_number == student.student_number:
                    print(student.get_student_average())

                else:
                    print("Student Not Exist")

        elif selection == 5:
            student_number = input("Enter Student Number")
            for i in student_list:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name: ")
                    course_mark = int(input("Enter Course Mark: "))
                    student.enroll_course(course_name, course_mark)
                    print("Course Added Successfully")
                    break
                else:
                    print("Student Not Exist")

        else:
            break

    except:
        print("Invalid Input")
