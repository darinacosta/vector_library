
//vectors can be any number of dimensions (R2 - 2-tuples; R3 - 3-tuples, etc)
add_vectors = function(vectors){
  var product = [];
  product.length = vectors[0].length;
  for (var v=0;v<product.length;v++){
    product[v] = 0;
  }
  for (var i=0;i<vectors.length;i++){
    for (var v=0;v<vectors[i].length;v++){
      product[v] = product[v] + vectors[i][v];
    }
  }
  return product
}

subtract_vectors = function(vectors){
  var product = [];
  for (var v=0;v<vectors[0].length;v++){
    product[v] = vectors[0][v];
  }
  for (var i=1;i<vectors.length;i++){
    for (var v=0;v<vectors[i].length;v++){
      product[v] = product[v] - vectors[i][v];
    }
  }
  return product;
}

//Scalars scale the size of the vector
multiply_vector_by_scalar = function(vector, scalar){
  var product = [];
  for (var i=0;i<vector.length;i++){
    product[i] = vector[i] * scalar
  };
  return product;
}