from statistics import mean
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            raise('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def medium_grade(self, course):
        list_grades = self.grades[course]
        list_avg = mean(list_grades)
        return list_avg

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {print(medium_grade())}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise('Ошибка')

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


student1 = Student('Ruoy', 'Eman', 'male')
student2 = Student('Emma', 'Leen', 'female')
student3 = Student('Inna', 'Cos', 'female')
student1.courses_in_progress += ['Python', 'Java']
student2.courses_in_progress += ['C++']
student3.courses_in_progress += ['Java']
print(f'Student1 courses in progress {student1.courses_in_progress}')
print(f'Student2 courses in progress {student2.courses_in_progress}')
print(f'Student3 courses in progress {student3.courses_in_progress}\n')

reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Any', 'Body')
reviewer3 = Reviewer('Ino', 'Agent')
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['C++']
reviewer3.courses_attached += ['Java']

print(f'Reviewer1 attached course: {reviewer1.courses_attached}')
print(f'Reviewer2 attached course: {reviewer2.courses_attached}')
print(f'Reviewer3 attached course: {reviewer3.courses_attached}\n')

lecturer1 = Lecturer('Ivan', 'Ivanov')
lecturer2 = Lecturer('Petr', 'Petrov')
lecturer3 = Lecturer('Sidr', 'Sidorov')
lecturer1.courses_attached += ['Python']

student1.rate_hw(lecturer1, 'Python', 5)
student1.rate_hw(lecturer1, 'Python', 7)
student1.rate_hw(lecturer1, 'Python', 9)
print(lecturer1.grades)
print(lecturer1.medium_grade('Python'))
print(lecturer1)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student2, 'C++', 8)
reviewer2.rate_hw(student2, 'C++', 9)
reviewer2.rate_hw(student2, 'C++', 6)
reviewer3.rate_hw(student3, 'Java', 7)
reviewer3.rate_hw(student3, 'Java', 10)
reviewer3.rate_hw(student3, 'Java', 4)

print(f'Student1 grades: {student1.grades}')
print(f'Student2 grades: {student2.grades}')
print(f'Student3 grades: {student3.grades}')











