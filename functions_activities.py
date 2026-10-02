
def cal_are():
    width = int(input("Width : "))
    length = int(input("Length : "))
    return width * length

print(cal_are())


def cal_area_with_args(width, length) :
    return width * length

a = int(input("width : "))
b = int(input("length : "))

cal_area_with_args(a,b)


def grade_cal(marks) :

    if marks >= 75 :
        print("A")
    elif marks >= 65 :
        print("B")
    elif marks >=50:
        print("C")
    else :
        return "F"

grade_cal(67)





