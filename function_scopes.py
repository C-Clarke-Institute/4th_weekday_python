def test_scope(): #naming convention - snake case
    y = 2 #function scoped variable
    global x #Modifiying global scope variable
    x = 2
    print(f"Value of z - {z}")
    print(f"Value of X - {x}")

z = 3
x = 1 #global scope
test_scope()
print(x)