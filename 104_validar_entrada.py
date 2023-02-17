def leiaInt(txt):
    ok = False
    valor = 0
    while True:
        n = input(txt)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[31m ERRO! Digite um número inteiro válido! \033[0m')
        if ok:
            break
    return n

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')

Não sei se te vejo como você gostaria de se ver, mas eu te vejo maravilhosa <3