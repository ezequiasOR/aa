n, q = map(int, input().split())
s = input()
count = s.count('ABC')
s = list(s)
t = len(s)

def pode_checar_depois(x):
    if x+1 <= (t-2) and x+2 <= (t-1):
        return True
    return False


def pode_checar_meio(x):
    if x-1 >= 0 and x+1 <= (t-1):
        return True
    return False


def pode_checar_antes(x):
    if x-2 >= 0 and x-1 >= 1:
        return True
    return False


for _ in range(q):
    x, c = input().split()
    x = int(x) - 1

    antes1 = '---'
    meio1 = '---'
    depois1 = '---'

    if pode_checar_antes(x):
        antes1 = s[x-2] + s[x-1] + s[x]
    
    if pode_checar_meio(x):
        meio1 = s[x-1] + s[x] + s[x+1]


    if pode_checar_depois(x):
        depois1 = s[x] + s[x+1] + s[x+2]


    s[int(x)] = c


    antes2 = '---'
    meio2 = '---'
    depois2 = '---'

    if pode_checar_antes(x):
        antes2 = s[x-2] + s[x-1] + s[x]

    
    if pode_checar_meio(x):
        meio2 = s[x-1] + s[x] + s[x+1]


    if pode_checar_depois(x):
        depois2 = s[x] + s[x+1] + s[x+2]

    
    if antes1 == 'ABC' or meio1 == 'ABC' or depois1 == 'ABC':
        count -= 1
    if antes2 == 'ABC' or meio2 == 'ABC' or depois2 == 'ABC':
        count += 1
    
    print(count)
