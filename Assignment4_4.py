from functools import reduce
def main():
    no=int(input("Enter number of elements in the List: "))
    ilist=[]
    for i in range(no):
        x=int(input("Enter a number: "))
        ilist.append(x)
    flist=list(filter(lambda no:no%2==0,ilist))
    mlist=list(map(lambda no:no*no,flist))
    ret=reduce(lambda a,b:a+b,mlist)
    print("Output of reduce= ",ret)

if __name__=="__main__":
    main()
