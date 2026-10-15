x = 10  # Global variable

def show():
    y = 5  # Local variable
    print("Local =", y)
    print("Global =", x)

show()
print("Outside =", x)