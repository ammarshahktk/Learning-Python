# Handle zero division error

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print('You cannot divide a number by zero')
        print(err)
    except TypeError as err:
        print(err)
    except:
        print("Unexpected Error !!! ")


print(divide(10,'0'))