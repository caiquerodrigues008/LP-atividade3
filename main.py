# Função para encontrar o menor de três números
def menor_numero(a, b, c):
    return min(a, b, c)

# Entradas do usuário
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# Encontrar o menor número
menor = menor_numero(a, b, c)

# Exibir o resultado
print(f"O menor número é: {menor}")
