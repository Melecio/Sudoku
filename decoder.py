import sys
from constants import NEIGHBORS

sol = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def check(sol):
    for x in range(0,81):
        for i in NEIGHBORS[x]:
            if sol[i//9][i%9] == sol[x//9][x%9]:
                return False
    return True

# Decodes the minisat output
def decode(variables,file):
    out = ''
    for i in variables:
        if int(i) > 0:
            sol[int(i[0])-1][int(i[1])-1] = int(i[2])
    for i in range(9):
        for j in range(9):
            out += str(sol[i][j])
        out += '\n'
    if not check(sol):
        print("Error en la solucion")
    file.write(out + '\n')

def read_sol_file(filename):
    file = open(filename,"r")
    variables = ""
    file.readline()
    variables = file.readline()
    variables = variables.split(" ")[:-1]
    file.close()
    return variables
