class SparseVector:
    def __init__(self, size):
        self.elements = []
        self.size = size
    class Element:
        def __init__(self, position, value):
            self.position = position
            self.value = value

    def set_value(self, position, value):
        if position < 0 or position >= self.size:
            raise ValueError("The vector doesn't have this position")
        for i in range(0, len(self.elements)):
            if self.elements[i].position == position:
                if value != 0:
                    self.elements[i].value = value
                else:
                    self.elements.pop(i)
                return
        if value != 0:
            self.elements.append(SparseVector.Element(position, value))

    def get_value(self, position):
        if position < 0 or position >= self.size:
            raise ValueError("The vector doesn't have this position")
        for i in range(0, len(self.elements)):
            if self.elements[i].position == position:
                return self.elements[i].value
        return 0

    def to_string(self):
        result = ""
        for i in range(0, self.size):
            result += str(self.get_value(i)) + ", "
        return result

    def sum(self, other):
        if self.size != other.size:
            raise ValueError("The vectors aren't the same size")
        res_vec = SparseVector(self.size)
        for element in self.elements:
            res_vec.set_value(element.position, element.value)
        for element in other.elements:
            old_value = res_vec.get_value(element.position)
            res_vec.set_value(element.position, element.value + old_value)
        return res_vec




class SparseMatrix:
    def __init__(self, width, height):
        self.elements = []
        self.width = width
        self.height = height
    class Element:
        def __init__(self, row, column, value):
            self.row = row
            self.column = column
            self.value = value

    def set_element(self, row, column, value):
        if row < 0 or column < 0 or row >= self.height or column >= self.width:
            raise ValueError ("The matrix doesn't have those positions")
        for idx in range(0, len(self.elements)):
            if self.elements[idx].row == row and self.elements[idx].column == column:
                if value != 0:
                    self.elements[idx].value = value
                else:
                    self.elements.pop(idx)
                return
        if value != 0:
            self.elements.append(self.Element(row, column, value))


    def get_value(self, row, column):
        if column < 0 or row < 0 or column >= self.width or row >= self.height:
            raise ValueError ("The matrix doesn't have this position")
        for element in self.elements:
            if element.column == column and element.row == row:
                return element.value
        return 0

    def to_string_m(self):
        result = ""
        for i in range(self.height):
            for k in range(self.width):
                result += str(self.get_value(i, k)) + ", "
            result = result.rstrip(', ') + "\n"
        return result

    def multiply_matrix_by_number(self, number):
        res_mat = SparseMatrix(self.width, self.height)
        if number == 0:
            return res_mat
        for element in self.elements:
            res_mat.elements.append(SparseMatrix.Element(element.row, element.column, element.value * number))

        return res_mat

    def multiply_matrix_by_vector(self, vector):
        if self.width != vector.size:
            raise ValueError ("The matrix and the vector are not the same size")
        res_vec = SparseVector(self.height)
        for element in self.elements:
            current_value = res_vec.get_value(element.row)
            res_vec.set_value(element.row, current_value + element.value * vector.get_value(element.column))

        return res_vec

    def copy(self):
        res_mat = SparseMatrix(self.width, self.height)

        for element in self.elements:
            res_mat.set_element(element.row, element.column, element.value)
        return res_mat

    def sum_of_matrix(self, matrix):
        if self.width != matrix.width or self.height != self.height:
            return ValueError("The matrixes are nor the same size")

        res_mat = self.copy()

        for element in matrix.elements:
            current_value = res_mat.get_value(element.row, element.column)
            res_mat.set_element(element.row, element.column, element.value + current_value)
        return res_mat

    def multiply_matrix_by_matrix(matrixL, matrixR):
        if matrixR.width != matrixL.height:
            raise ValueError
        res_mat = SparseMatrix(matrixR.width, matrixL.height)
        for elementL in matrixL.elements:
            for elementR in matrixR.elements:
                if elementL.column == elementR.row:
                    row, column = elementL.row, elementR.column
                    cur_val = res_mat.get_value(row, column)
                    new_value = cur_val + elementL.value * elementR.value
                    res_mat.set_element(row, column, new_value)
        return res_mat


    def print_as_computer(self):
        result = ""
        for element in self.elements:
            result += f"({element.row}, {element.column}, {element.value}), " + "\n"
        result = result.rstrip(', ') + "\n"
        print(result)







