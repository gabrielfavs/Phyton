"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitas:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em ou nome ou idade
    Exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua Idade: ")
if nome == '' or idade == '':
    print("Desculpe, você deixou campos vazios.")
else:
    print(f'Seu nome é {nome} e sua idade é {idade}')
    print(f'Seu nome invertido é {nome[-1:-10:-1]}')
    print(f'Seu nome contem (ou não) espaços? {nome in ' '} ')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[:1]}')
    print(f'A ultima letra do seu nome é: {nome[6:]}')





