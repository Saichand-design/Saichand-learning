#student Details
student_id = 101
student_name = "ravi"
student_age = 20

#score details
quize_score = 80
assigment_score = 95
exam_score = 90

#attendance Details
student_attendance = 95

#use arithmetic operators to calculate
total_score = quize_score + assigment_score + exam_score
average_score = total_score / 3

#use Relational operators to determine
#if the student is passing based on average score 75
is_passed = average_score >= 75 #False

#use increment operators to update
#attendance (simulate an additional attend session)
student_attendance = student_attendance + 1 #correct -> long syntax
student_attendance += 1 # correct -> concise Syntax (compound assigment operators)

#use logical operators to determine eligibility 
#if the student qualifies for an award
#(required high attendance i.e 90 and above and a passing grade)
qualified_award = student_attendance>= 90 and is_passed

#student information section: ID, name,age
#academic performace section : Individual scores,total and average
#status sections: passing status and award eligibility 

print("=========================")
print(f"student ID: {student_id}")
print(f"student Name: {student_name}")
print(f"student Age: {student_age}")
print(f"Total Score: {total_score}")
print(f"Average score: {average_score}")

print("=====STUDENT ATTENDANCE REPORT")
print(f"current attendance:{student_attendance}")

print("==========================")
print("=======STUDENT SCORE REPORT")
print(f"student Passed:{is_passed}")
print(f"student Qualified for Award: {qualified_award}")
