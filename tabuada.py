while True:
    print('\n'*50)
    print('********** MENU DE OPÇÕES **********')
    print('* <1> Adição                       *')
    print('* <2> Subtração                    *')
    print('* <3> Multiplicação                *')
    print('* <4> Divisão                      *')
    print('* <0> Sair                         *')
    print('************************************')
    op = int(input('Digite a opção: '));
    
    
    while op < 0 or op > 4:
        print('opção inválida');
        op = int(input('Digite a opção: '))
    if op == 0:
        break
    
    
    else:
        n = int(input('digite o número para tabuada: '))
        while n < 1 or n > 10:
            print(' Digite um valor de 1 a 10 ');
            n = int(input('digite o número para tabuada: '))
            
            
        if op == 1:
            cont = 1
            while cont <= 10:
                print(f'{n} + {cont} = {n+cont}')
                cont = cont + 1
                
        elif op == 2:
            cont = 1
            while cont <= 10:
                print(f'{n} - {cont} = {n-cont}')
                cont = cont + 1
                
        elif op == 3:
            cont = 1
            while cont <= 10:
                print(f'{n} x {cont} = {n*cont}')
                cont = cont + 1
                
        else:
            cont = 1
            while cont <= 10:
                print(f'{n} / {cont} = {round(n/cont)}')
                cont = cont + 1
                
    input('Enter pra continuar...')
print('programa sendo encerrado......')
                
        
                
                