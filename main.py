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
              f'Завеершенные курсы: {self.finished_courses_str}'
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
some_student.grades = {'Python':8, 'Git':9}
another_student = Student('Anna', 'Kazmirchuk', 'Female')
another_student.grades = {'Python':9, 'Git':10}

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Oleg', 'Bulygin')
some_lecturer.courses_attached += ['Python', 'Git']
some_lecturer.grades = {'Python':10, 'Git':9}
another_lecturer = Lecturer('Elena', 'Nikitina')
another_lecturer.courses_attached += ['Python', 'Git']
another_lecturer.grades = {'Python':8, 'Git':7}


# some_reviewer.rate_hw(some_student, 'Python', 10)
# some_reviewer.rate_hw(some_student, 'Python', 9)
# some_reviewer.rate_hw(some_student, 'Python', 9)

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print()
some_lecturer.__lt__(another_lecturer)
print()
some_student.__lt__(another_student)