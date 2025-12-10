## Exception Handling Example:
# Demonstrates try, multiple except blocks, else, and finally.
try:
    n=int(input("enter the number: "))
    a=10/n

except ZeroDivisionError:
    print("enter non-zero value")

except ValueError:
    print("enter valid value")

else:
    print("your answer is",a)

finally:
    print("end of the program")



