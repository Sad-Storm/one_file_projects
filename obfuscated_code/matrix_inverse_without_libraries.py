"""
Hello! The me of 2 years ago created this and am amazed at how obfuscated the code is
I did it because I wanted to challenge myself to see how to take inverse matrices of shapes larger then (2,2)
"""

def exy(matrix,x,y):
    return [element[:x]+element[x+1:] for element in matrix[:y]+matrix[y+1:]]
#-25 is goal for determinant


def determinant(matrix):
    s=0
    for x in range(len(matrix[0])):
        em=exy(matrix,x,0)
        if len(matrix[0])>2:
            val=determinant(em)
        else:
            val=em[0][0]
        s+=matrix[0][x]*val*(2*(x%2==0)-1)
    return s
#print(determinant(mat))
#print(np.linalg.determinant(mat))

def adjoint(matrix):
    return [[determinant(exy(matrix,y,x))*(2*((x+y)%2==0)-1) for x in range(len(matrix[0]))] for y in range(len(matrix))]
    
def inverse(matrix):
    return [[x/determinant(matrix) for x in y] for y in adjoint(matrix)]

def dot(matrix_1,matrix_2):
    bl=[]
    for x1 in range(len(matrix_1)):
        sl=[]
        for y1 in range(len(matrix_2[0])):
            s=0
            for x,y in list(zip(matrix_1[x1],[y[y1] for y in matrix_2])):
                s+=x*y
            sl.append(round(s,5))
        bl.append(sl)
    return bl

def main():
    import numpy as np
    npmat=np.random.randint(-5,5,(4,4))
    matrix=[[float(x) for x in y] for y in npmat]
    inverse_matrix=inverse(matrix)
    print(np.linalg.inv(npmat))
    for x in inverse_matrix:
        print(x)
    for x in dot(matrix,inverse_matrix):
        print(x)

if __name__=="__main__":
    main()

