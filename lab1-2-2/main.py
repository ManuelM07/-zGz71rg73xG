from operations import Operatons

op = Operatons()

####### TESTS #######

# a. suma
print("------------------------------------")
print("\t\tSUMA")
print(op.suma([1, 2, 3], [4, 5, 6]))
print(op.suma([2, -7, 23], [-4, 52, 11], [12, 14, 7]))
print("------------------------------------")

# a. Resta
print("------------------------------------")
print("\t\tRESTA")
print(op.resta([1, 2, 3], [4, 5, 6]))
print(op.resta([2, -7, 23], [-4, 52, 11], [12, 14, 7]))
print("------------------------------------")

# a. multiplicación vector por escalar
print("------------------------------------")
print("\tMULTIPLICACIÓN POR ESCALAR")
print(op.mult_vec_sca([1, 2, 3], 4))
print(op.mult_vec_sca([2, -7, 23], -6))
print("------------------------------------")

# b. cross product
print("------------------------------------")
print("\tCROSS PRODUCT")
print(op.cross_product([1, 2, 3], [4, 5, 6]))
print(op.cross_product([2, -7, 23], [-4, 52, 11]))
print("------------------------------------")

# c. producto punto
print("------------------------------------")
print("\tPRODUCTO PUNTO")
print(op.producto_punto([1, 2, 3], [4, 5, 6]))
print(op.producto_punto([2, -7, 23], [-4, 52, 11]))
print("------------------------------------")

# d. División de un vector por un escalar
print("------------------------------------")
print("\tDIVISIÓN POR ESCALAR")
print(op.div_vec_sca([1, 2, 3], 4))
print(op.div_vec_sca([20, 40, 60], 2))
print("------------------------------------")

# e. Calcular ángulo entre dos vectores
print("------------------------------------")
print("\tANGULO ENTRE 2 VECTORES")
print(op.calc_angulo([1, 2, 3], [4, 5, 6]))
print(op.calc_angulo([20, 40, 60], [-4, 52, 11]))
print("------------------------------------")

# e. Normalización de vectore
print("------------------------------------")
print("\tNORMALIZACIÓN DE VECTOR")
print(op.normalizacion([1, 2, 3]))
print(op.normalizacion([12, 33, 55]))
print("------------------------------------")