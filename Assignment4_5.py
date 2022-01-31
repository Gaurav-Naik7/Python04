from functools import reduce
from MarvellousNum import ChkPrime

def main():
    no=int(input("Enter number of elements in the List: "))
    ilist=[]
    for i in range(no):
        x=int(input("Enter a number: "))
        ilist.append(x)
    flist=list(filter(ChkPrime,ilist))
    mlist=list(map(lambda no:no*2,flist))
    ret=reduce(max,mlist)
    print("Output of reduce= ",ret)

if __name__=="__main__":
    main()
