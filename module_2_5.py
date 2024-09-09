n = int(input('введите число n: '))
m = int(input('введите число m: '))
value = int(input('введите число value: '))
def get_matrix (n,m, value):
    matrix = []
    for i in range(n):
        matrix.append([value]*m)
    return matrix
print(get_matrix(n,m,value))