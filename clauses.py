# General clause string
clause = ""
number = 0

# Row i, column j contains exactly one value from 1 to 9.
# 81 clauses
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            clause += `i` + `j` + `k` + ' '
        clause += '0 \n'

# Only one value for every row i column j
# 2916 clauses
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(k+1, 10):
                clause +=  '-' + `i` + `j` + `k` + ' ' + '-' + `i` + `j` + `l`
                clause += ' 0 \n'

print(clause)
