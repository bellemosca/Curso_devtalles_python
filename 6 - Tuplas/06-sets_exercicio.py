python_course = {"Maria", "Luis", "Felipe", "Monica"}
java_course = {"Felipe", "Luis", "Eduardo", "Rebeca"}

two_courses = python_course.intersection(java_course)
# print(two_courses)

only_python = python_course.difference(java_course)
# print(only_python)

all_students = python_course.union(java_course)
print(all_students)
