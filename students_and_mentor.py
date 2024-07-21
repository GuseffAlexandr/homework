class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecture) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if self.grades:
            return round(sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values()), 1)
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if self.grades:
            return round(sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values()), 1)
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"

    def __lt__(self, other):
        if isinstance(other, Lecture):
            return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()


def average_student_grades(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return round(sum(total_grades) / len(total_grades), 1)
    return 0


def average_lecture_grades(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return round(sum(total_grades) / len(total_grades), 1)
    return 0


best_student = Student('Alexey', ' Ivanov', 'm')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

reviewer1 = Reviewer('Sergey', 'Sidorov')
reviewer1.courses_attached += ['Python']

lecturer1 = Lecture('Ekaterina', 'Smirnova')
lecturer1.courses_attached += ['Python']

reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 9)

best_student.rate_lecture(lecturer1, 'Python', 9)
best_student.rate_lecture(lecturer1, 'Python', 10)

best_student2 = Student('Maria', 'Petrova', 'w')
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['Основы программирования']

reviewer2 = Reviewer('Dmitry', 'Kuznetsov')
reviewer2.courses_attached += ['Python']

lecturer2 = Lecture('Anna', 'Vasilieva')
lecturer2.courses_attached += ['Python']

reviewer2.rate_hw(best_student2, 'Python', 8)
best_student2.rate_lecture(lecturer2, 'Python', 8)

print(best_student)
print(reviewer1)
print(lecturer1)
print()
print(best_student2)
print(reviewer2)
print(lecturer2)
print()

students_list = [best_student, best_student2]
lecturers_list = [lecturer1, lecturer2]

print(f"Средняя оценка за домашние задания по курсу Python: {average_student_grades(students_list, 'Python')}")
print(f"Средняя оценка за лекции по курсу Python: {average_lecture_grades(lecturers_list, 'Python')}")
