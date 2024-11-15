def factorial(x):
    if x < 0:
        print("Please enter a non negative integer")
for i in range(6):
    print(i+1)

#factorial of say, 6 is 6*5*4*3*2
factorial = 1
for i in range(6, 1, -1):
    if factorial == 0:
       factorial = i
    else:
        factorial *=i
print(factorial)
