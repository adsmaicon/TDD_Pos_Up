def soma(a, b):
    """
        Funcao faz a soma de dois numeros.

        Ex:
            >>> soma(1, 2)= 3
            >>> soma(3, 4)= 7
    """

    return a + b

if __name__ == '__main__':

    resultado = soma(1, 2)
    if resultado == 3:
        print 'Soma 1 + 2 = 3 esta certo'
    else:
        print 'Soma nao funcionou'
