# 3) Observe o trecho de código abaixo: 
# int INDICE = 12, SOMA = 0, K = 1; 
# enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } 
# imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?


# Para responder essa pergunta vou implementar um código exemplo

# declaração das variáveis
id = 12
sum = 0
k=1

# Repetição while com condição de parada quando k < id
while k < id:
  # incremento de k a cada iteração
  k += 1

  # soma da variável sum com o valor de k
  sum = sum+k

print(sum)

# Resposta: 77