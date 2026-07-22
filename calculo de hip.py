cat1= float(input('inserir um cateto:'))

while cat1 <= 0:
    print('valor ínválido');
    cat1= float(input('inserir um cateto novamente:'))
    
if cat1 > 0:
        cat2= float(input('inserir um segundo cateto:'))
    
while cat2 <= 0:
    print('valor ínválido');
    cat2= float(input('inserir um segundo cateto novamente:'))

if cat2 > 0:
        
        hip = (cat1**1 + cat2**2)**(1/2)
            
        print('o valor da hipotenusa é', hip)
        