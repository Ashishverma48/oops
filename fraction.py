class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d

    # __str__magic method
    def __str__(self):
        return f"{self.num}\{self.den}"

    #  __add__ magic method

    def __add__(self, other):
        temp_num = self.num*other.den + self.den*other.num
        temp_den = self.den * other.den
        return f"{temp_num,temp_den}"

    # __sub__ magic method

    def __sub__(self, other):
        temp_num = self.num*other.den - other.num*self.den
        temp_den  = self.den *other.den

        return f"{temp_num,temp_den}"

#     __mul__ magic method
    def __mul__(self, other):
        temp_num = self.num *other.num
        temp_den = self.den *other.den

        return f"{temp_num},{temp_den}"

    # for dividion use __truediv__ magic method

    def __truediv__(self, other):
        temp_num = self.num*other.den
        temp_den = self.den *other.num

        return f"{temp_num},{temp_den}"



        
x = Fraction(4,3)
y = Fraction(3,2)

print(dir(int))
# print(type(x))
print(x)
print(y)
print(x+y)
print(x-y)

print(x*y)
print(x/y)