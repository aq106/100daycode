"""Remote Base Test Failure After Simple Amaris...1.5 years after 4 to 5 unbelievable blunders...
"""
from functools import wraps

def log(f):
    @wraps(f)
    def d_f(*args,**k):
        #a=",".join(k.values())
        sa=[str(a) for a in args]
        a=",".join(sa)
        n=f.__name__
        print("LOG:",f"{n}({a})")
        f(*args,**k)
    return d_f

def reverse_args(f):
    @wraps(f)
    def d_f(*args,**k):
        f(*args[::-1])
    return d_f

@log
def my_func(a):
    print("Aoa", a)

my_func("Salam")

@log
@reverse_args
def first(*a):
    #print(a,type(a))
    myargs = a
    for ma in myargs:
        print(ma)
        break
    #print(str(a[0]))
    #return str(a[1])

first(1,2,3)

# import inspect

# def log(f):
#     def d_f():
#         print("LOG:", f.__name__,str(inspect.signature(f)))
#         #dir(f)
#         f()
#     return d_f

# @log
# def my_func(a="abc"):
#     print("Aoa",a)

# my_func()
# my_func("a")
