fn=lambda no:no**2

def main():
    no=int(input("Enter a number: "))    
    ret=fn(no)
    print(ret)

if __name__=="__main__":
    main()
