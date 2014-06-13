#! /usr/bin/env python

import subprocess
import sys, os, time, os.path
from encoder   import encode, decode
from clauses   import clauses
from constants import *

def main():
    if len(sys.argv) != 3:
        print('use: sudoku_solver <sudoku_instances_file> <encoding>')
        exit(1)

    if sys.argv[2] != '1' and sys.argv[2] != '2':
        print('use 1 for minimal or 2 for extendend in encoding')
        exit(1)

	if not os.path.isfile('./build/release/bin/minisat'):
        print('run `make r` first')
        exit(1)

    # Get constant clauses
    encoding        = int(sys.argv[2])
    clauses_string  = clauses(encoding)
    sudoku          = NINExNINE
    instances       = open(sys.argv[1],'r')
    solution_file   = open('solution','w')
    minisat_solname = 'sudoku_solution'
    sudoku_cnf      = 'sudoku.cnf'

    for inst in instances:
        for i in range(0, 81):
            sudoku[i//9][i%9] = inst[i]

        encode(sudoku, clauses_string, encoding)

        # Get a solution and measure it's time
        start = time.time()
        subprocess.call(['./build/release/bin/minisat', sudoku_cnf, minisat_solname], stdout = open(os.devnull, 'w'), stderr = open(os.devnull, 'w'))
        delta = time.time() - start

        # If the file was created
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

# If this is the module running
if __name__ == '__main__':
    main()
