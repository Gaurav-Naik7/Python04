fn=lambda value1,value2:value1*value2

def main():
    no1=int(input("Enter first number: "))
    no2=int(input("Enter second number: "))
    ret=fn(no1,no2)
    print(ret)

if __name__=="__main__":
    main()
