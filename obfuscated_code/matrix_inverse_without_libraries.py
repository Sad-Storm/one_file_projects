def exy(m,x,y):
    return [l[:x]+l[x+1:] for l in m[:y]+m[y+1:]]
#-25 is goal for det


def det(m):
    s=0
    for x in range(len(m[0])):
        em=exy(m,x,0)
        if len(m[0])>2:
            val=det(em)
        else:
            val=em[0][0]
        s+=m[0][x]*val*(2*(x%2==0)-1)
    return s
#print(det(mat))
#print(np.linalg.det(mat))

def adj(m):
    return [[det(exy(m,y,x))*(2*((x+y)%2==0)-1) for x in range(len(m[0]))] for y in range(len(m))]
    
def inv(m):
    return [[x/det(m) for x in y] for y in adj(m)]

def dot(m1,m2):
    bl=[]
    for x1 in range(len(m1)):
        sl=[]
        for y1 in range(len(m2[0])):
            s=0
            for x,y in list(zip(m1[x1],[y[y1] for y in m2])):
                s+=x*y
            sl.append(round(s,5))
        bl.append(sl)
    return bl

def main():
    import numpy as np
    npmat=np.random.randint(-5,5,(4,4))
    mat=[[float(x) for x in y] for y in npmat]
    for x in inv(mat):
        print(x)
    print(np.linalg.inv(npmat))

if __name__=="__main__":
    main()

