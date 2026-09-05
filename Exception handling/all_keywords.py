a = int(input("Enter first number- "))
b = int(input("Enter your second number- "))

try:
    if b < 0:
        raise ValueError("second number cannot be negative")   # raise: manually throw an exception

    result = a / b                                              # risky code

except ZeroDivisionError:
    print("Can't divide by zero!")                              # except: handle the exception

except ValueError as err:
    print(f"Invalid input: {err}")                               # except: handle a different exception

else:
    print("Success:", result)                                    # else: runs only if no exception occurred

finally:
    print("This always runs.")                                   # finally: always runs, good for cleanup
