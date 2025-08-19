import functions as func

if __name__ == '__main__':

    vector = func.SparseVector(2)

    vector.set_value(0, 3)
    vector.set_value(1, 2)

    vectorB = func.SparseVector(3)

    vectorB.set_value(0, 1)
    vectorB.set_value(1, 2)
    vectorB.set_value(2, 3)

    matrix = func.SparseMatrix(3, 3)

    matrix.set_element(1, 0, 1)
    matrix.set_element(1, 1, 2)
    matrix.set_element(0, 0, 1)
    matrix.set_element(0, 1, 2)

    matrix1 = func.SparseMatrix(3, 3)

    matrix1.set_element(0, 0, 3)
    matrix1.set_element(1, 0, 2)
    matrix1.set_element(2, 0, 4)
    matrix1.set_element(1, 1, 5)

    print("Matrix")
    matrix.print_as_computer()

    #print("Value")
    #print(matrix.get_value(1, 0))

    print("Matrix1")
    matrix1.print_as_computer()

    print("Matrix + Matrix1")
    E = matrix.sum_of_matrix(matrix1)
    E.print_as_computer()


    """
    
    print("Matrix1")
    print(matrix1.to_string_m())
    
    print("Matrix1 * Matrix")
    print(func.SparseMatrix.multiply_matrix_by_matrix(matrix1, matrix).to_string_m())
    print("num * Matrix")
    print(matrix.multiply_matrix_by_number(2).to_string_m())
    
    print("Matrix * Vector")
    print(matrix.multiply_matrix_by_vector(vector).to_string())
    print(vector.to_string())

    print(vectorB.to_string())

    print(vector.sum(vectorB).to_string())
    
    print("Vector")
    print(vectorB.to_string())
    print("Matrix1")
    print(matrix1.to_string_m())

    print("Matrix * Vector")
    print(matrix1.multiply_matrix_by_vector(vectorB).to_string())
    
"""

