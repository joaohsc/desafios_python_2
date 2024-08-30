# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

txt = input()

count = 0
for char in txt:
    char = char.lower()
    
    # condição para validar letras a e com acento
    if char in (['a','â','ã','á', 'à']):
        count+=1

if count > 0:
    print(f"Existem {count} letras 'a' na string")
else:
    print("Não existem letras 'a' na string")
