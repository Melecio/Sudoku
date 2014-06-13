import sys, os
from constants import *

# Creates the CNF formated file for minisat
def encode(sudoku_in, clauses, encoding):
    if encoding == 1:
        restriction_number = 8829
    if encoding == 2:
        restriction_number = 11988

    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku_in[i][j] != '.':
                clauses += str(i + 1) + str(j + 1) + str(sudoku_in[i][j]) + ' 0\n'
                restriction_number += 1

    clauses = 'p cnf 729 ' + str(restriction_number) + '\n' + clauses

    output = open('sudoku.cnf', 'w')
    output.write(clauses)
    output.close()


def check(sol):
    for x in range(0, 81):
        for i in NEIGHBORS[x]:
            if sol[i//9][i%9] == sol[x//9][x%9]:
                return False
    return True


solution = NINExNINE
# Decodes the minisat output
def decode(solution_filename,file):
    variables = read_sol_file(solution_filename)
    out = ''

    for var in variables:
        if int(var) > 0:
            solution[int(var[0])-1][int(var[1])-1] = int(var[2])

    for i in range(0, 9):
        for j in range(0, 9):
            out += str(solution[i][j])
        out += '\n'

    if not check(solution):
        print('the solution given is wrong')

    file.write(out + '\n')


def read_sol_file(filename):
    file = open(filename,'r')
    file.readline()

    variables = file.readline()
    variables = variables.split(' ')[:-1]

    file.close()
    return variables
