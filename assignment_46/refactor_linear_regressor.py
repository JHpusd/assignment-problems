def calculate_coefficients(self):
    final_dict = {}
    mat = [[1 for x in list(self.df.data_dict.values())[0][0]]]
    mat_dict = {}
    for key in self.df.data_dict:
      if key != self.dependent_variable:
        mat_dict[key] = self.df.data_dict[key]
    for row in range(len(mat_dict)):
      mat.append(list(self.df.data_dict.values())[row][0])
    mat = Matrix(mat)
    mat = mat.transpose()
    mat_pseudoinv = mat.transpose().matrix_multiply(mat).inverse().matrix_multiply(mat_t)
    multiplier = [[num] for num in list(self.df.data_dict.values())[1][0]]
    multiplier_mat = mat_pseudoinv.matrix_multiply(Matrix(multiplier))
    for num in range(len(multiplier_mat.elements)):
      if num == 0:
        key = 'constant'
      else:
        key = list(self.df.data_dict.keys())[num-1]
      final_dict[key] = [row[0] for row in multiplier_mat.elements][num]
    return final_dict
