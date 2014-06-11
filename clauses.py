# General clause string
clause = ""
number = 0

# Row i, column j contains exactly one value  from 1 to 10
# 729 clauses

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            clause += `i` + `j` + `k` + ' '
        clause += '0 \n'




print(clause)

