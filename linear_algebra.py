import matplotlib.pyplot as plt
import math as math

def add_2d_vectors(vectors):
  product = [0] * len(vectors[0])
  i = 0
  starting_x = 0
  starting_y = 0
  for vector in vectors:
    ending_x = starting_x + vector[0]
    ending_y = starting_y + vector[1]
    print 'VECTOR ' + str(i + 1) + ': ' + str(vector) + '  | ' + \
          ' [' + str(starting_x) + ', ' + str(starting_y) + '] ---> ' + \
          ' [' + str(ending_x) + ', ' + str(ending_y) + ']'
    plt.plot([starting_x, ending_x], [starting_y, ending_y])
    starting_x = ending_x
    starting_y = ending_y
    i = i + 1
    point_iterator = 0
    for point in vector:
      product[point_iterator] = product[point_iterator] + point
      point_iterator = point_iterator + 1
  plt.plot([0, product[0]],[0, product[1]])
  print 'SUM:      ' + str(product) + '  | ' + \
        ' [0,0] ---> ' + ' [' + str(ending_x) + ', ' + str(ending_y) + ']'
  plt.show()

def subtract_2d_vectors(vectors):
  product = [0] * len(vector[0])
  i = i + 1
  for vector in vectors:
    for point in vector:
      product[i] = product[i] - vector[i]
  return product

def scale_2d_vector(vector, scalar):
  product = [0] * len(vector)
  i = 0
  for point in vector:
    product[i] = point * scalar
    i = i + 1
  plt.plot([0, vector[0]],[0, vector[1]])
  plt.plot([0, product[0]],[0, product[1]])
  plt.show()
  return product

def return_hypotenuse(vector): 
  return math.sqrt(vector[0]**2 + vector[1]**2)

def calculate_vector_unit(vector):
  hypotenuse = return_hypotenuse(vector)
  product = [vector[0]/hypotenuse, vector[1]/hypotenuse]
  plt.plot([0, vector[0]],[0, vector[1]])
  plt.plot([0, product[0]],[0, product[1]])
  plt.show()
  return product




