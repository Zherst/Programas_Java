nomes = ['mouse','teclado','monitor','gabinete']
precos = [14.90,29.90,399.90,250.00]
estoque = [100,150,20,35]

nome = input('Dígite o produto desejado: ')
for x in nomes:
    if x == nome:
        n = nomes.index(nome)
if  n == 999:
    print('produto não habilitado')
else:
    print('produto:',nomes[n],'\npreços - $',precos[n],'\nestoque:',estoque[n])