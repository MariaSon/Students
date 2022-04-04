from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.student_hw_mark = []

    def mean_hw_mark(self):
        if self.grades:
            for grades in self.grades.values():
                for grade in grades:
                    self.student_hw_mark.append(grade)
            return mean(self.student_hw_mark)
        else:
            return f'У студента нет оценок за домашнее задание!'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                f'{self.mean_hw_mark()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def marks_lector(self, lecturer, course, mark):
        if mark in range(11):
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                          and course in self.courses_in_progress:
                if course in lecturer.marks:
                    lecturer.marks[course] += [mark]
                else:
                    lecturer.marks[course] = [mark]
            else:
                return print('Ошибка! Проверьте корректность ввода данных о лекторе и курсе.')
        else:
            print(f'Ошибка! Ваша оценка - "{mark}" меньше 0 или больше 10.')

    def __lt__(self, other):
        return self.mean_hw_mark() > other.mean_hw_mark()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                      and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.marks = {}
        self.mark_list = []

    def mean_lector_mark(self):
        if self.marks:
            for marks in self.marks.values():
                for mark in marks:
                    self.mark_list.append(mark)
            return round(mean(self.mark_list), 2)
        else:
            return f'У лектора нет оценок от студентов!'

    def rate_hw(self, student, course, grade):
        print(f'Ошибка {self.name} - лектор и не может выставлять оценки студентам')

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: '
                f'{self.mean_lector_mark()}')

    def __lt__(self, other):
        return self.mean_lector_mark() > other.mean_lector_mark()


class Reviewer(Mentor):
    ...


def mean_hw_grades(students, course):
    persons = []
    course_grades = []
    grades_for_mean = []
    for person in students:
        if isinstance(person, Student):
            persons.append(person)
    for student in persons:
        if course in student.courses_in_progress:
            for grades in student.grades.keys():
                if course in grades:
                    course_grades.append(student.grades[course])
        else:
            print(f'У студента {student.name} нет курса {course}!')
    for grades_list in course_grades:
        for grade in grades_list:
            grades_for_mean.append(grade)
    return f'Средняя оценка за домашнее задание по курсу {course} - {round(mean(grades_for_mean), 2)}'


def mean_lecturer_grades(lectors, course):
    lectors_list = []
    lectors_grades = []
    lectors_grades_for_mean = []
    for person in lectors:
        if isinstance(person, Lecturer):
            lectors_list.append(person)
    for lector in lectors_list:
        if course in lector.courses_attached:
            for grades in lector.marks.keys():
                if course in grades:
                    lectors_grades.append(lector.marks[course])
        else:
            print(f'Лектор {lector.name} не читает лекции по курсу {course}!')
    for grades_list in lectors_grades:
        for grade in grades_list:
            lectors_grades_for_mean.append(grade)
    return f'Средняя оценка за лекции по курсу {course} - {round(mean(lectors_grades_for_mean), 2)}'


Olga_student = Student('Olga', 'Gromova', 'female')
Olga_student.courses_in_progress += ['Python', 'HTML', 'C#']

Lev_student = Student('Lev', 'Somov', 'male')
Lev_student.courses_in_progress += ['Python', 'HTML']

Ivan_mentor = Mentor('Ivan', 'Barinov')
Ivan_mentor.courses_attached += ['Python']

Alexey_mentor = Mentor('Alexey', 'Stepanov')
Alexey_mentor.courses_attached += ['C#']

Dmitriy_lector = Lecturer('Dmitriy', 'Ivanov')
Dmitriy_lector.courses_attached += ['Python', 'HTML']

Roman_lector = Lecturer('Roman', 'Liskov')
Roman_lector.courses_attached += ['C#', 'HTML']

Oleg_reviewer = Reviewer('Oleg', 'Fedorov')
Oleg_reviewer.courses_attached += ['Python', 'HTML']

Boris_reviewer = Reviewer('Boris', 'Koreev')
Boris_reviewer.courses_attached += ['C#']


Olga_student.marks_lector(Dmitriy_lector, 'Python', 10)
Olga_student.marks_lector(Dmitriy_lector, 'Python', 7)
Olga_student.marks_lector(Dmitriy_lector, 'HTML', 9)
Olga_student.marks_lector(Roman_lector, 'C#', 9)

Lev_student.marks_lector(Dmitriy_lector, 'Python', 9)
Lev_student.marks_lector(Dmitriy_lector, 'HTML', 8)

Oleg_reviewer.rate_hw(Olga_student, 'Python', 9)
Oleg_reviewer.rate_hw(Olga_student, 'HTML', 8)
Oleg_reviewer.rate_hw(Lev_student, 'Python', 10)
Oleg_reviewer.rate_hw(Lev_student, 'HTML', 7)

Boris_reviewer.rate_hw(Olga_student, 'C#', 7)


print('-------------')
print(Olga_student)
print('-------------')
print(Lev_student)
print('-------------')
print(Ivan_mentor)
print('-------------')
print(Alexey_mentor)
print('-------------')
print(Dmitriy_lector)
print('-------------')
print(Roman_lector)
print('-------------')
print(Oleg_reviewer)
print('-------------')
print(Boris_reviewer)
print('-------------')
print(Dmitriy_lector.__lt__(Roman_lector))
print('-------------')
print(Olga_student.__lt__(Lev_student))
print('-------------')
print(mean_hw_grades([Olga_student, Lev_student], 'Python'))
print('-------------')
print(mean_hw_grades([Olga_student, Lev_student], 'C#'))
print('-------------')
print(mean_lecturer_grades([Dmitriy_lector, Roman_lector], 'HTML'))
print('-------------')
print(mean_lecturer_grades([Dmitriy_lector, Roman_lector], 'Python'))
