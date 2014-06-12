#! /usr/bin/env python

# General clause string
clause = ''
# This variable is for documenting purposes only. (MP)
number = 0


## Individual cell clauses

# Every cell contains one value from 1 to 9.
# 81 clauses
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            clause += `x` + `y` + `z` + ' '
        clause += '0 \n'

# Exactly one value for every cell
# 2916 clauses
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 9):
            for i in range(z+1, 10):
                clause +=  '-' + `x` + `y` + `z` + ' ' + '-' + `x` + `y` + `i`
                clause += ' 0 \n'

## Row clauses

# Row  contains a value in range 1 to 9.
# 81 clauses
for y in range(1, 10):
    for z in range(1, 10):
        for i in range(1, 10):
            clause += `x` + `y` + `z` + ' '
        clause += '0 \n'

# Exactly one value for every row
# 2916 clauses
for y in range(1, 10):
    for z in range(1, 10):
        for x in range(1, 9):
            for i in range(x+1, 10):
                clause +=  '-' + `x` + `y` + `z` + ' ' + '-' + `i` + `y` + `z`
                clause += ' 0 \n'

## Column clauses

# Every column contains a value in range 1 to 9.
# 81 clauses
for x in range(1, 10):
    for z in range(1, 10):
        for y in range(1, 10):
            clause += `x` + `y` + `z` + ' '
        clause += '0 \n'

# Exactly one value for every column
# 2916 clauses
for x in range(1, 10):
    for z in range(1, 10):
        for y in range(1, 9):
            for i in range(y+1, 10):
                clause +=  '-' + `x` + `y` + `z` + ' ' + '-' + `x` + `i` + `z`
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

output = open('constant_clauses', 'w')
output.write(clause)
output.close()

