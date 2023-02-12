total_marks = 0
total_students = 0
best_mark = 0
average_mark = list("name", "mark", "grade")
best_student = ""
while True:
    name = input("What is the students name?").lower()
    if name == "x":
        print(f"The average mark is {sum(average_mark)/len(average_mark)}, The best mark is {best_mark} "
              f"and the best student is {best_student}")
        break
    else:
        mark = int(input("What is the students mark [1-100] "))
        average_mark.append(mark)
        if mark >= best_mark:
            best_mark = mark
            best_student = name
