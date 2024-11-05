# Error handling
# 1. Try
# 2. Except
# 3. Else
# 4. Finally
while True:
    try:
        age = int(input("What's your age?: "))
        print(10/age)
        print(age)
# You can use as many except block as need in your program.
    # print(10/0)
    except ZeroDivisionError:
        print("Age can'africa be zero.")
    except:
        print("Please enter a number.")
    else:
        print("Thank you.")
        break
    finally:
        print("End of program.")
