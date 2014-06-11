#! /usr/bin/env python

# General clause string
clause = ''
# This variable is for documenting purposes only. (MP)
number = 0


## Individual cell clauses

# Every cell contains one value from 1 to 9.
# 81 clauses
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            clause += `i` + `j` + `k` + ' '
        clause += '0 \n'

# Exactly one value for every cell
# 2916 clauses
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(k+1, 10):
                clause +=  '-' + `i` + `j` + `k` + ' ' + '-' + `i` + `j` + `l`
                clause += ' 0 \n'

## Row clauses

# Row  contains a value in range 1 to 9.
# 81 clauses
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            clause += `i` + `k` + `j` + ' '
        clause += '0 \n'

# Exactly one value for every row
# 2916 clauses
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(k+1, 10):
                clause +=  '-' + `i` + `k` + `j` + ' ' + '-' + `i` + `l` + `j`
                clause += ' 0 \n'

## Column clauses

# Every column contains a value in range 1 to 9.
# 81 clauses
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            clause += `k` + `i` + `j` + ' '
        clause += '0 \n'

# Exactly one value for every column
# 2916 clauses
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(k+1, 10):
                clause += '-' + `k` + `i` + `j` + ' ' + '-' + `l` + `i` + `j` + ' '
                clause += '0 \n'

## Block clauses

# Each number appears at least once in each block
# 81 clauses
for z in range(1,10):
    for i in range(0,3):
        for j in range(0,3):
            for x in range(1,4):
                for y in range(1,4):
                    clause += `(3*i + x)` + `(3*j + y)` + `z` + ' '
            clause += '0 \n'

# Each number appears at most once in each block
# 2916 clauses
for z in range(1,10):
    for i in range(0,3):
        for j in range(0,3):
            for x in range(1,4):
                for y in range(1,4):
                    for k in range(y+1,4):
                        clause += '-' + `(3*i + x)` + `(3*j + y)` + `z` + ' '
                        clause += '-' + `(3*i + x)` + `(3*j + k)` + `z` + ' '
                        clause += '0 \n'
                    for k in range(x+1,4):
                        for l in range(1,4):
                            clause += '-' + `(3*i + x)` + `(3*j + y)` + `z` + ' '
                            clause += '-' + `(3*i + k)` + `(3*j + l)` + `z` + ' '
                            clause += '0 \n'

print(clause)
