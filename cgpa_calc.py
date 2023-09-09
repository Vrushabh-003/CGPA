def calculate_cgpa(grades, credit_hours):
    total_credit_points = 0
    total_credit_hours = 0
    
    for grade, credit_hour in zip(grades, credit_hours):
        if grade == 'A':
            grade_point = 4.0
        elif grade == 'A-':
            grade_point = 3.7
        elif grade == 'B+':
            grade_point = 3.3
        elif grade == 'B':
            grade_point = 3.0
        elif grade == 'B-':
            grade_point = 2.7
        elif grade == 'C+':
            grade_point = 2.3
        elif grade == 'C':
            grade_point = 2.0
        elif grade == 'C-':
            grade_point = 1.7
        elif grade == 'D+':
            grade_point = 1.3
        elif grade == 'D':
            grade_point = 1.0
        else:
            grade_point = 0.0
        
        total_credit_points += grade_point * credit_hour
        total_credit_hours += credit_hour
    
    cgpa = total_credit_points / total_credit_hours
    return cgpa

num_courses = int(input("Enter the number of courses: "))
grades = []
credit_hours = []

for i in range(num_courses):
    grade = input(f"Enter the grade for course {i+1}: ")
    credit_hour = int(input(f"Enter the credit hours for course {i+1}: "))
    grades.append(grade)
    credit_hours.append(credit_hour)

final_cgpa = calculate_cgpa(grades, credit_hours)
print(f"Your CGPA is: {final_cgpa:.2f}")
