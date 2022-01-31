from functools import reduce

def nrange(value):
    if 70<=value<=90:
        return True
    else:
        return False

fn=lambda value:value+10

def main():
    Input_list=[4,34,36,76,68,24,89,23,86,90,45,70]
    nlist=list(filter(nrange,Input_list))
    mlist=list(map(fn,nlist))
    ret=reduce(lambda a,b:a*b,mlist)
    print(nlist)
    print(mlist)
    print(ret)

if __name__=="__main__":
    main()
