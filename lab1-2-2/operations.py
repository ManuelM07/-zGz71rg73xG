from typing import List
import math


class Modeling:
    pass


class Operatons:

    def __init__(self) -> None:
        pass

    # a. Suma, resta y multiplicación de un vector por un escalar.
    def suma(self, *vectors) -> list:
        answer: List[float] = []
        answer = vectors[0]
        for i in range(1, len(vectors)):
            vector = vectors[i]
            for j in range(len(vector)):
                answer[j] += vector[j]
        return answer


    def resta(self, *vectors) -> list:
        answer: List[float] = []
        answer = vectors[0]
        for i in range(1, len(vectors)):
            vector = vectors[i]
            for j in range(len(vector)):
                answer[j] -= vector[j]
        return answer


    def mult_vec_sca(self, vector, scalar) -> list:
        for i in range(len(vector)):
            vector[i] *= scalar
        return vector


    # b. Multiplicación de vectores (cross product).
    def cross_product(self, vector1, vector2) -> list: 
        # TODO los vectores deben estar en R3 para que se pueda aplicar el cross product
        try:
            answer = [
                vector1[1]*vector2[2] - vector1[2]*vector2[1],
                -(vector1[0]*vector2[2] - vector1[2]*vector2[0]),
                vector1[0]*vector2[1] - vector1[1]*vector2[0],
            ]

            return answer
        except IndexError:
            print("Los vectores deben estar en R3")


    # c. Producto interno (producto punto)
    def producto_punto(self, vector1, vector2) -> float:
        answer = 0
        for i in range(len(vector1)):
            answer += vector1[i]*vector2[i]
        return answer


    # d. División de un vector por un escalar    
    def div_vec_sca(self, vector, scalar) -> list:
        for i in range(len(vector)):
            vector[i] /= scalar
        return vector


    # e. Calcular ángulo entre dos vectores
    def calc_angulo(self, vector1, vector2) -> float:
        return math.degrees(math.acos(self.producto_punto(vector1, vector2)/
                            (self._norm(vector1)*self._norm(vector2))))

    
    # f. Normalización de vectores
    def normalizacion(self, vector):
        norm = self._norm(vector)
        new_vector = []

        for com in vector:
            new_vector.append(com/norm)

        return new_vector


    # Aux funtions 
    def _norm(self, vector) -> float:
        """Retorna la norma de un vector"""
        norm = 0
        for x in vector:
            norm += x**2
        return math.sqrt(norm)





#op = Operatons()
#print(op.suma([2, -1, 4]))