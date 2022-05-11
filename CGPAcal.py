import pandas as pd

global session_count
global semester_count
print('please press 1 if you are calculating just a semester\n press 2 if you are calculating for a session ')
while True:
    try:
        sem_ses_pick = int(input('Are you calculating a semester or session: '))
        if sem_ses_pick == 1:
            semester_count = int(input('How many semesters are you calculating: '))
        elif sem_ses_pick == 2:
            session_count = int(input('How many sessions are you calculating: '))
        else:
            raise ValueError('read the instructions again')
    except (TypeError, ValueError):
        print('please read the instructions again\n'
              'here are the instructions:\n'
              'press 1 if you are calculating just a semester\n'
              'press 2 if you are calculating for a session')
    else:
        break

global session
global semester

sum_grade = []
unit_add = []
total_courses = []
grade_store = []
score_store = []
semester_store = []
session_store = []


class GpaCalculator:

    def point_cal():

        session = input('session: ')
        semester = input('semester: ')
        session_store.append(session)
        semester_store.append(semester)
        i = 1
        while True:
            try:
                no_of_courses = int(input('No of courses:'))
            except (TypeError, ValueError):
                print('please input a number')
            else:
                break
        while i <= no_of_courses:
            course = (input('Course Title:'))
            while True:
                try:
                    unit = int(input('Unit:'))
                except (TypeError, ValueError):
                    print('input a valid number')
                else:
                    break

            while True:
                try:
                    score = int(input('Score:'))
                except (TypeError, ValueError):
                    print('input a valid number')
                else:
                    break

            if score > 69 < 101:
                cal = 5 * unit
                sum_grade.append(cal)
                unit_add.append(unit)
                total_courses.append(course)
                score_store.append(score)
                grade_store.append('A')

            elif score > 59 < 70:
                cal = 4 * unit
                sum_grade.append(cal)
                unit_add.append(unit)
                total_courses.append(course)
                score_store.append(score)
                grade_store.append('B')

            elif score > 49 < 60:
                cal = 3 * unit
                sum_grade.append(cal)
                unit_add.append(unit)
                total_courses.append(course)
                score_store.append(score)
                grade_store.append('C')

            elif score > 44 < 50:
                cal = 2 * unit
                sum_grade.append(cal)
                unit_add.append(unit)
                total_courses.append(course)
                score_store.append(score)
                grade_store.append('D')

            elif score > 39 < 45:
                cal = 1 * unit
                sum_grade.append(cal)
                unit_add.append(unit)
                total_courses.append(course)
                score_store.append(score)
                grade_store.append('E')

            elif score > 0 < 39:
                cal = 0 * unit
                sum_grade.append(cal)
                unit_add.append(unit)
                total_courses.append(course)
                score_store.append(score)
                grade_store.append('F')

            else:
                print("error")

            i = i + 1
        total_grade = sum(sum_grade)
        total_units = sum(unit_add)
        cgpa = round((total_grade / total_units), 2)
        print(f"your cgpa at the end of {semester} semester({session} session) is {cgpa}")

    def gpa_cal(point_cal):
        if sem_ses_pick == 1:
            count = 1
            while count <= semester_count:
                point_cal()
                count = count + 1
        if sem_ses_pick == 2:
            count = 1
            s_count = session_count * 2
            while count <= s_count:
                point_cal()
                count = count + 1

    gpa_cal(point_cal)

    def comments():
        total_grade = sum(sum_grade)
        total_units = sum(unit_add)
        cgpa = round((total_grade / total_units), 2)
        if cgpa > 4.49 < 5.00:
            print(f' A Cgpa of {cgpa} whew!!! First Class Honours! You are a genius')
        elif cgpa > 3.49 < 4.50:
            print(f' A Cgpa of {cgpa} whew!!!Second Class Honours Upper Division! You are brilliant')
        elif cgpa > 2.39 < 3.50:
            print(f' A Cgpa of {cgpa} whew!!! Second Class Honours Lower Division! You tried your best\n Try develop '
                  f'yourself in some skills')
        elif cgpa > 1.49 < 2.40:
            print(f' A Cgpa of {cgpa} whew!!! Second Class Honours Lower Division! You tried your best')
        elif cgpa > 0.99 < 1.50:
            print(f' A Cgpa of {cgpa} whew!!! Second Class Honours Lower Division! You tried your best')
        else:
            print(f' A Cgpa of {cgpa} whew!!! withdrawal\n Consider something else apart from education')

    comments()


print('here is a summary of your details')
compiled = pd.DataFrame(list(zip(session_store, semester_store, total_courses, unit_add, score_store, grade_store, sum_grade)),
                        columns=['Session' 'Semester' 'Courses', 'Units', 'Scores', 'Grades', 'Points'])
print(compiled)


