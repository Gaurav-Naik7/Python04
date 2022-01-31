def ChkPrime(value):
    for i in range(2,value):
        if value%i==0:
            return False
            break
    else:
        return True
