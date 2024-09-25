def calculate_grade(lab: int,quiz: int,as_1: float,as_2: float,as_3: float,as_4: float,mid_1: float,mid_2: float,final: float,prep: float)->int:
   print("Your grade is: " +str(round((lab/6*20) + (quiz/6*15) +(as_1+as_2+as_3+as_4)*0.04 +(mid_1+mid_2)*0.125 +(final*0.18)+(prep*0.06))))
lab=int(input("Enter the number of labs completed: "))
if lab>6:
   lab=6
quiz=int(input("Enter the number of quizzes completed: "))
if quiz>6:
   quiz=6
as_1=float(input("Enter grade for Assignment 1: "))
as_2=float(input("Enter grade for Assignment 2: "))
as_3=float(input("Enter grade for Assignment 3: "))
as_4=float(input("Enter grade for Assignment 4: "))
mid_1=float(input("Enter grade for Midterm 1: "))
mid_2=float(input("Enter grade for Midterm 2: "))
final=float(input("Enter grade for Final Exam: "))
prep=float(input("Enter grade for Midterms and Final Preparation: "))

calculate_grade(lab,quiz,as_1,as_2,as_3,as_4,mid_1,mid_2,final,prep)

