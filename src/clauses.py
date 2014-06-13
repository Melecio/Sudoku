# Generates constant clauses
def clauses(encoding):
    # General clause string
    clause = ''

    # Individual cell clauses
    for x in range(1, 10):
        for y in range(1, 10):
            # There is at least one number in each entry
            # 81 clauses
            for z in range(1, 10):
                clause += str(x) + str(y) + str(z) + ' '
            clause += '0 \n'

            # At most one number in each entry
            # 2916 clauses
            # Extended
            if encoding == 2:
                for z in range(1, 9):
                    for i in range(z+1, 10):
                        clause += '-' + str(x) + str(y) + str(z) + ' '
                        clause += '-' + str(x) + str(y) + str(i) + ' '
                        clause += '0 \n'

    # Row clauses
    for y in range(1, 10):
        for z in range(1, 10):
            # Each number appears at least once in each row
            # 81 clauses
            # Extended
            if encoding == 2:
                for x in range(1, 10):
                    clause += str(x) + str(y) + str(z) + ' '
                clause += '0 \n'

            # Each number appears at most once in each row
            # 2916 clauses
            for x in range(1, 9):
                for i in range(x+1, 10):
                    clause += '-' + str(x) + str(y) + str(z) + ' '
                    clause += '-' + str(i) + str(y) + str(z) + ' '
                    clause += '0 \n'

    # Column clauses
    for x in range(1, 10):
        for z in range(1, 10):
            # Each number appears at least once in each column
            # 81 clauses
            # Extended
            if encoding == 2:
                for y in range(1, 10):
                    clause += str(x) + str(y) + str(z) + ' '
                clause += '0 \n'

            # Each number appears at most once in each column
            # 2916 clauses
            for y in range(1, 9):
                for i in range(y+1, 10):
                    clause += '-' + str(x) + str(y) + str(z) + ' '
                    clause += '-' + str(x) + str(i) + str(z) + ' '
                    clause += '0 \n'

    ## Block clauses
    for z in range(1,10):
        for i in range(0,3):
            for j in range(0,3):
                # Each number appears at least once in each block
                # 81 clauses
                # Extended
                if encoding == 2:
                    for x in range(1,4):
                        for y in range(1,4):
                            clause += str(3*i + x) + str(3*j + y) + str(z) + ' '
                    clause += '0 \n'

                # Each number appears at most once in each block
                # 2916 clauses
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


if __name__ == '__main__':
    print clauses(1)
