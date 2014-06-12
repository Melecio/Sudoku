import os

# Creates the cnf formated file for minisat
def encode(input):
    restriction_number = 11988
    clauses = open('constant_clauses','r')
    aux_fd = open('tmpfile','w')
    for i in clauses:
        aux_fd.write(i);
    aux_fd.close()
    aux_fd = open('tmpfile','a')
    for i in range(9):
        for j in range(9):
            if input[i][j] != '.':
                aux_fd.write(str(i+1) + str(j+1) + str(input[i][j]) + " 0\n")
                restriction_number += 1
    aux_fd.close()

    aux_fd = open('tmpfile','r')
    output = open('sudoku.cnf','w')

    output.write("p cnf 729 "+str(restriction_number) + "\n")
    for l in aux_fd.readlines():
        output.write(l)
    aux_fd.close()
    os.remove('tmpfile')
    output.close()