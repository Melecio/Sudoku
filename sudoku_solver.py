import subprocess
import sys, os, time
from encoder import *
from decoder import *
from constants import *

def main():
    if (len(sys.argv) == 1 or len(sys.argv) >2):
        print("use: sudoku_solver <sudoku_instances_file>")
        exit(1)

    clauses_string = clauses()

    sudoku = NINExNINE
    instances     = open(sys.argv[1],'r')
    solution_file = open('solution','w')

    for inst in instances:
        for i in range(81):
            sudoku[i//9][i%9] = inst[i]

        encode(sudoku)

        start = time.time()
        subprocess.call(["./build/release/bin/minisat","sudoku.cnf","sudoku_solution"],stdout=open('minisat.out','w'),stderr=open('minisat.err','w'))
        lapse = time.time()
        delta = lapse - start

        try:
            o = open("sudoku_solution","r")
            o.close()
        except:
            print("No hay solucion para [" + inst +"]\n")
            continue

        variables = read_sol_file("sudoku_solution")

        solution_file.write(inst + str(delta) + '\n\n')
        decode(variables,solution_file)

    os.remove('sudoku.cnf')
    os.remove('sudoku_solution')
    os.remove('constant_clauses')
    instances.close()

# if this is the module running
if __name__ == "__main__":
    main()


################################## clauses #####################################

# Generate constant clauses
def clauses():

    # General clause string
    clause = ''

    ## Individual cell clauses

    # There is at least one number in each entry
    # 81 clauses
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                clause += str(x) + str(y) + str(z) + ' '
            clause += '0 \n'

    # At most one number in each entry
    # 2916 clauses
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 9):
                for i in range(z+1, 10):
                    clause += '-' + str(x) + str(y) + str(z) + ' '
                    clause += '-' + str(x) + str(y) + str(i) + ' '
                    clause += '0 \n'

    ## Row clauses

    # Each number appears at least once in each row
    # 81 clauses
    for y in range(1, 10):
        for z in range(1, 10):
            for x in range(1, 10):
                clause += str(x) + str(y) + str(z) + ' '
            clause += '0 \n'

    # Each number appears at most once in each row
    # 2916 clauses
    for y in range(1, 10):
        for z in range(1, 10):
            for x in range(1, 9):
                for i in range(x+1, 10):
                    clause += '-' + str(x) + str(y) + str(z) + ' '
                    clause += '-' + str(i) + str(y) + str(z) + ' '
                    clause += '0 \n'

    ## Column clauses

    # Each number appears at least once in each column
    # 81 clauses
    for x in range(1, 10):
        for z in range(1, 10):
            for y in range(1, 10):
                clause += str(x) + str(y) + str(z) + ' '
            clause += '0 \n'

    # Each number appears at most once in each column
    # 2916 clauses
    for x in range(1, 10):
        for z in range(1, 10):
            for y in range(1, 9):
                for i in range(y+1, 10):
                    clause += '-' + str(x) + str(y) + str(z) + ' '
                    clause += '-' + str(x) + str(i) + str(z) + ' '
                    clause += '0 \n'

    ## Block clauses

    # Each number appears at least once in each block
    # 81 clauses
    for z in range(1,10):
        for i in range(0,3):
            for j in range(0,3):
                for x in range(1,4):
                    for y in range(1,4):
                        clause += str(3*i + x) + str(3*j + y) + str(z) + ' '
                clause += '0 \n'

    # Each number appears at most once in each block
    # 2916 clauses
    for z in range(1,10):
        for i in range(0,3):
            for j in range(0,3):
                for x in range(1,4):
                    for y in range(1,4):
                        for k in range(y+1,4):
                            clause += '-' + str(3*i + x) + str(3*j + y) + str(z) + ' '
                            clause += '-' + str(3*i + x) + str(3*j + k) + str(z) + ' '
                            clause += '0 \n'
                        for k in range(x+1,4):
                            for l in range(1,4):
                                clause += '-' + str(3*i + x) + str(3*j + y) + str(z) + ' '
                                clause += '-' + str(3*i + k) + str(3*j + l) + str(z) + ' '
                                clause += '0 \n'

    return clause

################################## encoder #####################################
