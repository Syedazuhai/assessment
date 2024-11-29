def temperature_converter():
    print("Temperature converter")
    print("1, convert Fahrenheit to Celsius")
    print("2, convert Celsius to Fahrenheit")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        celsius = float(input("Enter Temperature in Fahrenheit"))
        celsius = (fahrenheit - 32)* 5/9
        print(f"fahrenheit is equal to {Celsius}C")
    elif choice == "2":
        userinput = float(input("Enter temperature in celsius"))
        fahrenheit = (userinput * 9/5) + 32
        print(f"{userinput}C is equal to {fahrenheit}F")
    else:
        print("Invalid choice. Please enter 1 or 2. ")
temperature_converter()
