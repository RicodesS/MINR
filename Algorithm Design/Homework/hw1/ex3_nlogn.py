import sys

class Project:
    def __init__(self,name,requirement,value):
        self.name = name
        self.req = requirement
        self.val = value

def print_proj(lst):
    print("Printing projects...")
    for i in lst:
        print(i.name,i.req,i.val)


def satisfy(C):
        
    p1 = Project("p1",10,2)
    p2 = Project("p2",6,-2)
    p3 = Project("p3",0,6)
    p4 = Project("p4",20,7)
    p5 = Project("p5",4,1)
    p6 = Project("p6",7,-3)

    lst = [p1,p2,p3,p4,p5,p6]

    vsum = C

    for i in range(len(lst)):
        vsum = vsum + lst[i].val

    if vsum < 0:
        sys.exit("No possible combination")

    pos = []
    neg = []

    for i in range(len(lst)):
        if lst[i].val >= 0:
            pos.append(lst[i])
        else:
            neg.append(lst[i])

    pos.sort(key = lambda x: x.req)

    neg.sort(key = lambda x:x.req, reverse = True)

    res = pos + neg

    rsum = C
    for i in range(len(res)):
        if(C >= res[i].req):
            rsum = rsum + res[i].val
        else:
            print("NO.")
            exit()
    print("Computed: ",rsum)


def main():

    for i in range(12):
        print(i)
        satisfy(i)

main()