import numpy as np, math # Para operações básicas com vetores e matrizes

def norma_vetor(vetor):
    soma_quadrados = 0.0
  
    # Calcula a soma dos quadrados dos elementos do vetor
    for elemento in vetor:
        soma_quadrados += elemento ** 2
    
    # Retorna a raiz quadrada da soma dos quadrados
    norma = math.sqrt(soma_quadrados)
    
    return norma

def gram_schmidt(matriz):
    """
    Realiza a decomposição QR de uma matriz matriz usando o processo de Gram-Schmidt.

    Args:
    - matriz: Matriz quadrada (numpy array)

    Returns:
    - Q: Matriz ortogonal (numpy array)
    - R: Matriz triangular superior (numpy array)
    """

    tam_matriz = matriz.shape[0]
    Q = np.zeros_like(matriz, dtype=float)
    R = np.zeros_like(matriz, dtype=float)

    for j in range(tam_matriz):
        vetor = matriz[:, j]

        print(f"vetor: {j+1}", vetor)

        for i in range(j):
            R[i, j] = np.dot(Q[:, i], matriz[:, j])
            vetor -= R[i, j] * Q[:, i]
        R[j, j] = norma_vetor(vetor)
        Q[:, j] = vetor / R[j, j]
    
    return Q, R

def metodo_qr(matriz_inicial, max_iteracoes=100):
    """
    Aplica o método QR iterativo para encontrar autovalores de uma matriz matriz_inicial.

    Args:
    - matriz_inicial: Matriz quadrada (numpy array)
    - max_iteracoes: Número máximo de iterações (opcional)

    Returns:
    - autovalores: Lista de autovalores aproximados
    """

    A_k = matriz_inicial.copy()
    tam_matriz = matriz_inicial.shape[0]
    autovalores = []

    for k in range(max_iteracoes):
        print("vetor")
        Q, R = gram_schmidt(A_k)

        print(f"Matriz Q_{k+1}:")
        print(Q)
        print(f"Matriz R_{k+1}:")
        print(R)

        A_k = np.dot(R, Q) # Multiplicação RxQ
        print(f"Matriz A_{k+1}:")
        print(A_k)

        # Extração dos autovalores da diagonal de A_k
        autovalores_k = [A_k[i, i] for i in range(tam_matriz)]
        autovalores.append(autovalores_k)

        # Critério de parada (quando a matriz se torna triangular)
        if np.allclose(np.triu(A_k, k=1), np.zeros_like(A_k, dtype=float), atol=1e-8):
            break

    return autovalores

# Exemplo de uso:
if __name__ == "__main__":
    # Definindo uma matriz de exemplo
    matriz_inicial = np.array([
        [2, 3, 0],
        [0, 4, 0],
        [2, -3, 1]
    ], dtype=float)

    # Aplicando o método QR para encontrar os autovalores
    autovalores = metodo_qr(matriz_inicial,3)

    print("Autovalores aproximados:")
    for i, autovalor in enumerate(autovalores[-1]):
        print(f"lambda_{i+1} =", autovalor)
