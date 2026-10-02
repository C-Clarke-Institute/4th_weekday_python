# create function for cal total
#create funtion to cal_average
#create function to grade average
#check marks

scores = [76, 89, 90, 55, 90]

def calculate_total (marks_list):

    total = 0
    for mark in marks_list:
        total += mark

    return  total

def calculate_average(marks):
    total = calculate_total(marks)
    return total /len(marks)

def grade_average(average):
    if average >= 75:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

def check_result(marks):

    for mark in marks:
        if mark < 40 :
            return "Fail"

    return "pass"


total = calculate_total(scores)
average = calculate_average(scores)
grade = grade_average(average)
result= check_result(scores)

print(f"""
Total : {total}
Average : {average}
Grade : {grade}
Result : {result} """)




