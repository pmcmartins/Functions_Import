var = 5

def function1():
    print("Value in 1st function :",var)

def function2():
    # Modify global variable
    # function will treat it as a local variable
    global_var = 555
    print("Value in 2nd function :", var)

def function3():
    print("Value in 3rd function :",var)

function1()
function2()
function3()