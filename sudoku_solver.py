#! /usr/bin/env python

import subprocess
import sys, os, time, os.path
from encoder   import encode, decode
from clauses   import clauses
from constants import *

def main():
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print('use: sudoku_solver <sudoku_instances_file>')
        exit(1)

    clauses_string  = clauses()
    sudoku          = NINExNINE
    instances       = open(sys.argv[1],'r')
    solution_file   = open('solution','w')
    minisat_solname = 'sudoku_solution'
    sudoku_cnf      = 'sudoku.cnf'

    for inst in instances:
        for i in range(81):
            sudoku[i//9][i%9] = inst[i]

        encode(sudoku, clauses_string)

        # get a solution and measure it's time
        start = time.time()
        subprocess.call(['./build/release/bin/minisat', sudoku_cnf, minisat_solname], stdout = open(os.devnull, 'w'), stderr = open(os.devnull, 'w'))
        lapse = time.time()
        delta = lapse - start

        # if the file was created
        if os.path.isfile(minisat_solname):
            solution_file.write("-----------------------\ninstance: '" + inst + "'\ntime: " + str(delta) + '\n\n')
            decode(minisat_solname, solution_file)
        else:
            print("there is no solution for the instance '" + inst[:-1] +"'\n")

    if os.path.isfile(minisat_solname):
        os.remove(minisat_solname)
    os.remove(sudoku_cnf)

    instances.close()
    solution_file.close()

# if this is the module running
if __name__ == '__main__':
    main()
