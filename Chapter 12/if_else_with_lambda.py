# if else with lambda

# def func(s):
#     if len(s) > 5:
#         return True 
#     return False

func = lambda s : True if len(s) > 5 else False 
print(func('abc'))