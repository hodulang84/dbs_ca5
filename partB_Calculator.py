# CA5 last updated on 30/11/2017
# 10359541 Seungmin Back

import math

class Calculator(object):
 
# map, lambda
    def add(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        elif isinstance(x, list) and isinstance(y, list):
            return map(lambda a,b: a+b, x,y)
        else:
            raise ValueError

    def subtract(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        elif isinstance(x, list) and isinstance(y, list):
            return map(lambda a,b: a-b, x,y)
        else:
            raise ValueError

    def multiply(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        elif isinstance(x, list) and isinstance(y, list):
            return map(lambda a,b:a*b, x,y)
        else:
            raise ValueError

    def divide(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x / y
        elif isinstance(x, list) and isinstance(y, list):
            return map(lambda a,b:a/b, x,y)
        else:
            raise ValueError
 
#filter, lambda          
    def list_exponent_is_even(self, x,y):
        if isinstance(x, list) and isinstance(y, list):
            return filter(lambda i:i%2==0, (map(lambda a,b:a**b, x,y)))
        else:
            raise ValueError

#reduce, lambda
    def list_sum(self, x):
        if isinstance(x, list):
            return reduce(lambda a,b:a+b, x)
        else:
            raise ValueError
    
    def list_max(self, x):
        if isinstance(x, list):
            return reduce(lambda a,b: a if (a>b) else b, x)
        else:
            raise ValueError
            
    def list_min(self, x):
        if isinstance(x, list):
            return reduce(lambda a,b: a if (a<b) else b, x) 
        else:
            raise ValueError

#list comprehension
    def square(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return x**2
        elif isinstance(x, list):
            return [a*a for a in x]
        else:
            raise ValueError

    def factorial(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return math.factorial(x)        
        elif isinstance(x, list):
            return [math.factorial(a) for a in x]
        else:
            raise ValueError