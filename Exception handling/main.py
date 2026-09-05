a=int(input("Enter first number- "))
b=int(input("Enter your second number- "))

try:
    print(a/b)
except Exception as err:
    print(f"sorry there is some error {err}")


finally:
    print("not matters if there is error or not i will run")
    
print("this line get exceutate")

