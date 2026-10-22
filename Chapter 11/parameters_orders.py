# function with all parameters 
# very important to understand 

#PADK : (parameters, *args, default parameters, **kwargs)
# this is the order of parameters
# parameters 
# args 
# default parameters
# **kwargs


def func(name,*args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('Ammar', 1,2,3, a = 1, b = 2)

