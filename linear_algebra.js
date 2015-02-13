add_vectors = function(args){
  var product = [];
  product.length = args[0].length;
  for (var v=0;v<product.length;v++){
    product[v] = 0;
  }
  for (var i=0;i<args.length;i++){
    for (var v=0;v<args[i].length;v++){
      product[v] = product[v] + args[i][v];
    }
  }
  return product
}

multiply_vector_by_scalar = function(vector, scalar){
  var product = [];
  for (var i=0;i<vector.length;i++){
    product[i] = vector[i] * scalar
  };
  return product;
}