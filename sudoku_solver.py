import subprocess
import sys, os, time
from encoder import *
from decoder import *
from clauses import *

def main():
    if (len(sys.argv) == 1 or len(sys.argv) >2):
        print("use: sudoku_solver <sudoku_instances_file>")
        exit(1)

    # Create constant_clauses file
    clauses()
    sudoku = [9*[0] for x in range(9)]
    instances = open(sys.argv[1],'r')
    solution_fd = open('solution','w')

    for s in instances:
        for i in range(81):
            sudoku[i//9][i%9] = s[i]

        encode(sudoku)

        start = time.time()
        subprocess.call(["./build/release/bin/minisat","sudoku.cnf","sudoku_solution"],stdout=open('minisat.out','w'),stderr=open('minisat.err','w'))
        lapse = time.time()
        delta = lapse - start

        try:
            o = open("sudoku_solution","r")
            o.close()
        except:
            print("No hay solucion para [" + s +"]\n")
            continue

        variables = read_sol_file("sudoku_solution")

        solution_fd.write(s + str(delta) + '\n\n')
        decode(variables,solution_fd)

    os.remove('sudoku.cnf')
    os.remove('sudoku_solution')
    os.remove('constant_clauses')
    instances.close()


main()
