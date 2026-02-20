import os

lista_compras = []

while True:
    print("Selecione uma das opcões abaixo.")
    opcoes = input("[i]nserir [a]pagar [l]istar [s]sair: ")
    
    
    letras_permitidas = 'i' or 'I', 'a' or 'A', 'l' or 'L', 's' or 'S'
    
    if opcoes not in letras_permitidas:
        print("Você não selecionou uma das opcões")
        os.system('cls')
        continue
    elif opcoes == 'i' or opcoes == 'I':
        if opcoes == '':
            print("Você não inseriu nenhum item")
        else: 
          inserir = input("Digite o item que você deseja inserir: ")
          lista_compras.append(inserir)
          os.system('cls')
        continue
    elif opcoes == 'l' or opcoes == 'L':
        for indice, nome in enumerate(lista_compras):
           print(indice, nome)
           continue
    elif opcoes == 'a' or opcoes == 'A':
        excluir = input('Digite o número do que você deseja apagar na lista: ')
        apagar = int(excluir)
        lista_compras.pop(apagar)
        os.system('cls')
        print('Item removido com sucesso!!')
        continue 
    elif opcoes == 's' or opcoes == 'S':
        print('Você selecionou a opcão de sair')
        print('Aqui esta sua lista de compras: ')
        for indice, nome in enumerate(lista_compras):
           print(indice, nome)
           continue
       
    break
os.system('cls')
print('Muito obrigado por escolhe o melhor surpermercado!!!')        