import csv
import random
import pandas as pd

all_students_for_exam = []

def same_teacher_Time_date(schedule):
    print("SAME TEACHER AT SAME TIME & DATE")

    same_teacher_time = 0
    extra_schedule2 = schedule
    ii = 0
    kk = 0
    total_len = len(extra_schedule2) - 1
    for x in schedule:
        ii = kk
        for pp in range(total_len):
            if x[2] == extra_schedule2[ii + 1][2] and x[3] == extra_schedule2[ii + 1][3] and x[4] == \
                    extra_schedule2[ii + 1][4]:
                print(str(extra_schedule2[ii + 1][2]) + " " + str(extra_schedule2[ii + 1][3]) + " " +
                      extra_schedule2[ii + 1][4] + "  SAME TEACHER AT SAME TIME, DATE!!")
                same_teacher_time += 1
            ii += 1
        total_len -= 1
        kk += 1
    print("Number of same teacher assigned at exact same time: " + str(same_teacher_time))
    return same_teacher_time

def consective_Duty(schedule):
    print("CONSECTIVE DUTY OF TEACHERS")

    same_teacher = 0
    extra_schedule2 = schedule
    ii = 0
    kk = 0
    total_len = len(extra_schedule2) - 1
    for x in schedule:
        ii = kk
        for pp in range(total_len):
            if x[2] == extra_schedule2[ii + 1][2] and x[4] == extra_schedule2[ii + 1][4] and x[3][2] == extra_schedule2[ii + 1][3][0]:
                print(str(extra_schedule2[ii + 1][2]) + "  consective duty!!")
                same_teacher += 1
            ii += 1
        total_len -= 1
        kk += 1
    print("Teachers assigned consective duty : "+ str(same_teacher))
    return same_teacher

def same_room_time_date(schedule):
    print("CLASHE IF SAME ROOM AT SAME TIME & DATE")

    same_time_room = 0
    extra_schedule = schedule
    i = 0
    k = 0
    total_len = len(extra_schedule)-1
    for x in schedule:
        i = k
        for pp in range(total_len):
            if x[0] == extra_schedule[i+1][0] and x[3] == extra_schedule[i+1][3] and x[4] == extra_schedule[i+1][4]:
                print(str(extra_schedule[i+1][0])+" "+str(extra_schedule[i+1][3])+" "+extra_schedule[i+1][4]+"  SAME TIMEE AND ROOM!!")
                same_time_room+=1
            i += 1
        total_len -= 1
        k += 1
    print("Number of same Time,date and room clashes :"+ str(same_time_room))
    return same_time_room

def student_clashes(schedule,all_students):
    print("STUDENT CLASHES")
    clash_exams = []
    tuples = []
    paralel_exams = 0
    i = 0
    k = 0
    outside = 0
    total_len = len(schedule) - 1
    for x in schedule:
        inside = 0
        i = k
        for pp in range(total_len):
            if x[3] == schedule[i + 1][3] and x[4] == schedule[i + 1][4]:
                clash_exams.append(schedule[i + 1])
                tuples.append((outside,(inside+1)+outside))
                paralel_exams += 1
            i += 1
            inside += 1
        total_len -= 1
        k += 1
        outside += 1
    print(tuples)
    print("Number of paralel exams happening: "+str(paralel_exams))

    total_stu_clashes = 0
    for iterator in range(len(tuples)):
        tt = 0
        for x in all_students[tuples[iterator][0]]:
            har = 0

            for y in all_students[tuples[iterator][1]]:

                if x == y:

                    total_stu_clashes += 1
                har += 1
            tt += 1
    print("Total number of students clashes are : "+ str(total_stu_clashes))
    return total_stu_clashes

def Student_consective_exam(schedule):

    print("CONSECTIVE EXAM STUDENTS")
    ConsectiveExamtuples = []
    consectiveExms = 0
    i = 0
    k = 0
    outside = 0
    total_len = len(schedule) - 1
    for x in schedule:
        inside = 0
        i = k
        for pp in range(total_len):
            if x[4] == schedule[i + 1][4] and x[3][2] == schedule[i + 1][3][0]:

                ConsectiveExamtuples.append((outside, (inside + 1) + outside))
                consectiveExms += 1
            i += 1
            inside += 1
        total_len -= 1
        k += 1
        outside += 1

    print(ConsectiveExamtuples)

    Viatims_of_consective_exams = []

    for iterator in range(len(ConsectiveExamtuples)):
        tt = 0
        for x in all_students_for_exam[ConsectiveExamtuples[iterator][0]]:
            har = 0
            for y in all_students_for_exam[ConsectiveExamtuples[iterator][1]]:

                if x == y:

                    Viatims_of_consective_exams.append(x)
                har += 1
            tt += 1
    print("Total victim of consective exams : " + str(len(Viatims_of_consective_exams)))
    return len(Viatims_of_consective_exams)

def Random_solution(all_rooms,all_courses,all_teachers,time_slots,Days):

    schedule = []
    while len(all_courses) !=0:   # EVERY COURSE GET ASSIGNED
        exam_list = []
        students = []

        room_rand = random.choice(all_rooms)
        course_rand = random.choice(all_courses)

        col_list = ["ID", "Student Name", "Course Code"]  #GETTING STUDENT NAMES
        df = pd.read_csv("studentCourses.csv", usecols=col_list)
        indexes = []
        i = 0
        for x in df["Course Code"]:
            if x == course_rand:
                indexes.append(i)
            i += 1
        for p in indexes:
            students.append(df["Student Name"][p])
        all_students_for_exam.append(students)
        teacher_rand = random.choice(all_teachers)
        time_rand = random.choice(time_slots)
        day_rand = random.choice(Days)
        all_courses.remove(course_rand)
        exam_list.append(room_rand)
        exam_list.append(course_rand)
        exam_list.append(teacher_rand)
        exam_list.append(time_rand)
        exam_list.append(day_rand)

        schedule.append(exam_list)

    l=0
    for x in schedule:
        print(x)
    return schedule

def Finding_Solution(all_rooms,all_courses,all_teachers,time_slots,Days):

    i=0
    best_sol=1

    for x in range(100):
        random_schedule = Random_solution(all_rooms, all_courses, all_teachers, time_slots, Days)
        same_time_room_clash = same_room_time_date(random_schedule)
        consective_duty_clash = consective_Duty(random_schedule)
        same_teacher_time_clash = same_teacher_Time_date(random_schedule)
        total_student = student_clashes(random_schedule, all_students_for_exam)
        student_with_consective = Student_consective_exam(random_schedule)
        current_sol=(same_time_room_clash * 10.0) + (same_teacher_time_clash * 3.0) +(consective_duty_clash*3)+ (total_student * 3) + (student_with_consective*3)
        print("Current Solution Cost: ",current_sol)
        if current_sol > best_sol:
            best_sol=current_sol
        i=i+1
        print("i count:",i)
    print("BEST SOLUTION COST:",best_sol, )


#GETTING ROOMS FILE
file = open("rooms.csv")
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
i=0
all_rooms = []
for k in rows:
    all_rooms.append(rows[i][0])
    i+=1
file.close()

#GETTING COURSES FILE
file = open("courses.csv")
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
i=0
all_courses = []
for k in rows:
    all_courses.append(rows[i][0])
    i+=1
file.close()

#GETTING TEACHERS FILE
file = open("teachers.csv")
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
i=0
all_teachers = []
for k in rows:
    all_teachers.append(rows[i][0])
    i+=1
file.close()


time_slots = ["9-11","11 - 1","2 - 4"]
Days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

Finding_Solution(all_rooms,all_courses,all_teachers,time_slots,Days)