
def print_full_name(first_name, last_name):

    print(f"First name is {first_name} and Last Name is - {last_name}")


print_full_name("Sushain", "Dilishan") #Positional argument passing

print_full_name(first_name="test", last_name="dsadasd") #Keyword argument passing

def multiply(a, b):
    print(f"Multiplying - {a} and {b}")
    return a * b

result = multiply(11, 22)

print(result)

