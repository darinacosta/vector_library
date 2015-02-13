import matplotlib.pyplot as plt

def add_2d_vectors(vectors):
  product = [0] * len(vectors[0])
  i = 0
  starting_x = 0
  starting_y = 0
  for vector in vectors:
    print 'vector ' + str(i) + ': ' + str(vector)
    ending_x = starting_x + vector[0]
    ending_y = starting_y + vector[1]
    plt.plot([starting_x, ending_x], [starting_y, ending_y])
    starting_x = ending_x
    starting_y = ending_y
    i = i + 1
    point_iterator = 0
    for point in vector:
      product[point_iterator] = product[point_iterator] + point
      point_iterator = point_iterator + 1
  plt.plot([0, product[0]],[0, product[1]])
  print 'sum:      ' + str(product)
  plt.show()

def plot_vector(vector):
  x = [0, vector[0]]
  y = [0, vector[1]]
  plt.plot(x,y)
  plt.show()