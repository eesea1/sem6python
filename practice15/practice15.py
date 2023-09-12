class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course_name):
        if course_name in self.courses_in_progress and self.grades[course_name] != []:
            self.finished_courses.append(course_name)
        else:
            self.courses_in_progress.append(course_name)

    def rateLect(self, lect, course, grade):
        if course in lect.coursesAttached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lect.grades:
                lect.grades[course].append(grade)
            else:
                lect.grades[course] = [grade]

    def average(self):
        sum = 0
        count = 0
        for grade in self.grades.values():
            count += len(grade)
            for element in grade:
                sum += element
        if count == 0:
            return "Нет оценок"
        return round(sum / count, 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.coursesAttached = []

    def rateStudent(self, student, course, grade):
        if course in self.coursesAttached and (
                course in student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

    def addCourse(self, course):
        self.coursesAttached.append(course)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.coursesAttached = []

    def rateStudent(self, student, course, grade):
        if course in self.coursesAttached and (
                course in student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

    def add_course(self, course):
        self.coursesAttached.append(course)

    @staticmethod
    def __name__():
        return "Mentor"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.coursesAttached = []

    def averageRating(self):
        sum = 0
        count = 0
        for grade in self.grades.values():
            count += len(grade)
            for element in grade:
                sum += element
        if count == 0:
            return "Не оценен"
        return round(sum / count, 2)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.coursesAttached = []

    def rateStudent(self, student, course, grade):
        if course in self.coursesAttached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

def avgGradeStudentsOfCourse(studentsList, courseName):
    grades = []
    for student in studentsList:
        if courseName in student.grades:
            grades.extend(student.grades[courseName])
    if grades:
        return sum(grades) / len(grades)
    else:
        return

def avgGradeLecturersOfCourse(lecturersList, courseName):
    grades = []
    for lecturer in lecturersList:
        if courseName in lecturer.grades:
            grades.extend(lecturer.grades[courseName])
    if grades:
        return sum(grades) / len(grades)
    else:
        return


student = Student("zhenya ", "aasdf", "Man")
student.add_course("Python")

student2 = Student("vasya ", "aasdf", "Man")
student2.add_course("Python")

lecturer = Lecturer("Ivan", "asgsdg")
lecturer.add_course("Python")


rev1 = Reviewer("Alexandre", "Strel")
rev1.add_course("Python")

rev1.rateStudent(student, "Python", 5)
rev1.rateStudent(student2, "Python", 3)

print(avgGradeStudentsOfCourse([student, student2], "Python"))