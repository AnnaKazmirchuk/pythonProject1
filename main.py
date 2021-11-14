class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        def add_courses(self, course_name):
            self.finished_course.append(course_name)

    def lectures_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw_rate(self):
        sum_ = 0
        for grade in self.grades:
            sum_ += self.grades[grade]
        return round(sum_ / len(self.grades), 2)

    def __lt__(self, other):
        if self.average_hw_rate() < other.average_hw_rate():
            print(f'Средняя оценка за домашние задания выше у студента {another_student.name} {another_student.surname}')
            return self.average_hw_rate() < other.average_hw_rate()
        else:
            print(f'Средняя оценка за домашние задания выше у студента {self.name} {self.surname}')
            return self.average_hw_rate() < other.average_hw_rate()

    def __str__(self):
        res = f'Имя студента: {self.name}\nФамилия студента: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_hw_rate()}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress_str}\n' \
              f'Завершенные курсы: {self.finished_courses_str}'
        return res



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def average_lecture_rate(self):
        sum_ = 0
        for grade in self.grades:
            sum_ += self.grades[grade]
        return round(sum_ / len(self.grades), 2)

    def __lt__(self, other):
        if self.average_lecture_rate() < other.average_lecture_rate():
            print(f'Средняя оценка за лекции выше у лектора {another_lecturer.name} {another_lecturer.surname}')
            return self.average_lecture_rate() < other.average_lecture_rate()
        else:
            print(f'Средняя оценка за лекции выше у лектора {self.name} {self.surname}')
            return self.average_lecture_rate() < other.average_lecture_rate()


    def __str__(self):
        res = f'Имя лектора: {self.name}\nФамилия лектора: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_lecture_rate()}'
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя проверяющего: {self.name}\nФамилия проверяющего: {self.surname}'
        return res



some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.courses_in_progress_str = ", ".join(some_student.courses_in_progress)
some_student.finished_courses += ['Введение в программирование']
some_student.finished_courses_str = " ".join(some_student.finished_courses)
some_student.grades = {'Python':9, 'Git': 5}
another_student = Student('Anna', 'Kazmirchuk', 'Female')
another_student.grades = {'Python':9, 'Git':6}
another_student.courses_in_progress += ['Python', 'Git']
another_student.courses_in_progress_str = ", ".join(another_student.courses_in_progress)
another_student.finished_courses += ['Введение в программирование']
another_student.finished_courses_str = " ".join(another_student.finished_courses)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Oleg', 'Bulygin')
some_lecturer.courses_attached += ['Python', 'Git']
some_lecturer.grades = {'Python':10, 'Git':9}
another_lecturer = Lecturer('Elena', 'Nikitina')
another_lecturer.courses_attached += ['Python', 'Git']
another_lecturer.grades = {'Python':8, 'Git':7}


print(some_reviewer)
print(some_lecturer)
print(some_student)
some_lecturer.__lt__(another_lecturer)
some_student.__lt__(another_student)

students = [some_student, another_student]

def average_hw_rate_all_students(student, course_name):
    sum_ = 0
    for student in students:
        for course in student.grades:
            if course == course_name:
                sum_ += student.grades[course]
    return round(sum_ / len(students), 2)

print(f'Средння оценка по курсу {average_hw_rate_all_students(students, course_name = "Python")}')
print(f'Средння оценка по курсу {average_hw_rate_all_students(students, course_name = "Git")}')

lecturers = [some_lecturer, another_lecturer]

def average_lecture_rate_all_lectureres(lecturer, course_name):
    sum_ = 0
    for lecturer in lecturers:
        for course in lecturer.grades:
            if course == course_name:
                sum_ += lecturer.grades[course]
    return round(sum_ / len(lecturers), 2)

print(f'Средння оценка за лекции {average_lecture_rate_all_lectureres(lecturers, course_name = "Python")}')
print(f'Средння оценка за лекции {average_lecture_rate_all_lectureres(lecturers, course_name = "Git")}')