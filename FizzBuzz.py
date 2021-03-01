def FizzBuzz(x):
    if (x % 3 == 0) and (x % 5 == 0):
        return FizzBuzz
    else:
        if (x % 3 == 0):
            return Fizz
        else:
            if (x % 5 == 0):
                return Buzz
    if (x % 3 != 0) and (x % 5 != 0):
        return x
    
