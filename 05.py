total_marks = 0
total_students = 0
best_mark = 0
average_mark = list()
best_student = ""
students = list()
while True:
    name = input("What is the students name?").lower()
    if name == "x":
        print(f"The average mark is {sum(average_mark)/len(average_mark)}, The best mark is {best_mark} "
              f"and the best student is {best_student}")
        print(students)
        break
    else:
        mark = int(input("What is the students mark [1-100] "))
        if mark == range(90, 100):
            mark = "A+"
        elif mark == range(85, 89):
            mark = "A"
        elif mark == range(80, 84):
            mark = "A-"
        elif mark == range(75, 79):
            mark = "B+"
        elif mark == range(70, 74):
            mark = "B"
        elif mark == range(65, 69):
            mark = "B-"
        elif mark == range(60, 64):
            mark = "C+"

    students.append(name, mark)
    average_mark.append(mark)
    if mark >= best_mark:
        best_mark = mark
        best_student = name
