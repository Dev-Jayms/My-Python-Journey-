# Erro handling 2
'''This function define addition function that takes two(2) arguments and returns the sum of them'''


def addition(sum1, sum2):
    try:
        return sum1 + sum2
    # except (TypeError, ZeroDivisionError) as err:
    #     print(err)

    # This a general exception block
    # except:
    #     return "Only numbers are accepted and you can'africa divide by zero."
    except TypeError:
        return ("You can'africa divide a number and a letter.")
    except ZeroDivisionError:
        return ("You can'africa divide by Zero.")
    except NameError as e:
        return ("Only numbers are accepted.", str(e))


print(addition(8, 2))
print(addition(8, "g"))
print(addition(8, 0))
# print(addition(8, j))
