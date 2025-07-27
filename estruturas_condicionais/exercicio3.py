letra = input("Digite uma letra: ")
vogais = ['a', 'e', 'i', 'o', 'u']

if letra.lower() in vogais:
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")