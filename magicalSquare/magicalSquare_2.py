#!/usr/bin/env python3

def verify_matrix(matrix: list[int]) -> bool:
    """
    Verify if sum of columns, rows and diagonals are equal
    """
    result: list[int] = []

    # Sum of lines
    for i in range(0, len(matrix)):
        result.append(sum(matrix[i]))

    # Sum of columns
    sum_col = [
            sum(line[col] for line in matrix)
            for col in range(len(matrix[0]))
            ]
    result.append(sum_col)

    # Sum of diagonal
    sum_diag = sum([
            matrix[i][i]
            for i in range(len(matrix))
            ])
    result.append(sum_diag)

    # sum of anti-diagonal
    sum_anti = sum([
            matrix[i][len(matrix)-1-i]
            for i in range(len(matrix))
            ])
    result.append(sum_anti)

    result_flat = [
                n
                for elmnt in result
                for n in (elmnt if isinstance(elmnt, list) else [elmnt])
            ]

    return len(set(result_flat)) == 1


def print_matrix(matrix: list[int]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(f" | {matrix[i][j]}", end="")
        print(" |")


if __name__ == "__main__":
    matrix: list[int] = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    print("matrix is correct") if verify_matrix(matrix) \
        else print("matrix is not correct")
