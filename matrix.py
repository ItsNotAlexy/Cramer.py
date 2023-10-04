def CountDeterminant(matrix):
    return (
        matrix[0][0] * matrix[1][1] * matrix[2][2]
        + matrix[0][1] * matrix[1][2] * matrix[2][0]
        + matrix[0][2] * matrix[1][0] * matrix[2][1]
        - matrix[0][2] * matrix[1][1] * matrix[2][0]
        - matrix[0][1] * matrix[1][0] * matrix[2][2]
        - matrix[0][0] * matrix[1][2] * matrix[2][1]
    )

def CramerRule(matrix, vector):
    det = CountDeterminant(matrix)
    if det == 0:
        print("Determinant of the coefficient matrix is equal to 0. No unique solution.")
        return
    else:
        det_dx = CountDeterminant(
            [
                [vector[0], matrix[0][1], matrix[0][2]],
                [vector[1], matrix[1][1], matrix[1][2]],
                [vector[2], matrix[2][1], matrix[2][2]],
            ]
        )

        det_dy = CountDeterminant(
            [
                [matrix[0][0], vector[0], matrix[0][2]],
                [matrix[1][0], vector[1], matrix[1][2]],
                [matrix[2][0], vector[2], matrix[2][2]],
            ]
        )
        det_dz = CountDeterminant(
            [
                [matrix[0][0], matrix[0][1], vector[0]],
                [matrix[1][0], matrix[1][1], vector[1]],
                [matrix[2][0], matrix[2][1], vector[2]],
            ]
        )

        print("Determinant of detA is: ", int(det))
        print("Determinant of detAx is: ", int(det_dx))
        print("Determinant of detAy is: ", int(det_dy))
        print("Determinant of detAz is: ", int(det_dz))

        
        x = det_dx / det
        y = det_dy / det
        z = det_dz / det

        print("Value of x is: ", int(x))
        print("Value of y is: ", int(y))
        print("Value of z is: ", int(z))

def main():
    matrix = []
    vector = []

    print("Welcome to Cramer's rule calculator")
    print("Enter 3x3 coefficient matrix values: ")
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(float(input()))

    print("Enter 3x1 vector values: ")
    for i in range(3):
        vector.append(float(input()))

    CramerRule(matrix, vector)

if __name__ == "__main__":
    main()
