def classify_age(age=0): #Setting a default value
    if age < 13:
        return "child"
    elif age < 19:
        return "Teen"
    elif age < 50:
        return "Adult"
    else:
        return "Senior citizen"

print(classify_age())