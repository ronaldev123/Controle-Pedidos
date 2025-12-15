#Variáveis
continuar='s'
cont = "s"
perfil = 0
option = 0
prod=[]
valor_uni=0
cod=0
temp = []
temp_cod =[]
lista_prod=[]
nova_desc=[]
dados=[]
op_alt=[]
conteudo=[]
teste = []
pedido = []
#Funções
def menuprincipal():
    print('BEM-VINDO AO SISTEMA!')
    print('1- Administrador')
    print('2- Operador')
    print('0- Sair')
    op_main=input('Digite a opção desejada: ')
    while(op_main == "" or (op_main !='1' and op_main !='2' and op_main !='0')):
        print('Digite uma opção válida!')
        op_main=input('Digite a opção desejada: ')
    return op_main
 
def menu_adm():
    print('1- Cadastrar')
    print('2- Listar')
    print('3- Editar')
    print('4- Apagar')
    print('0- Sair')
    op_adm=input('Digite a opção desejada: ')
    while(op_adm == "" or (op_adm !='1' and op_adm !='2' and op_adm !='3' and op_adm !='4' and op_adm !='0')):
        print('Digite uma opção válida!')
        op_adm=input('Digite a opção desejada: ')
    return op_adm
 
def busca_cod():
    codigo = 0
    arquivo = open('pedido.txt', 'r')
    dados = arquivo.readlines()
    if dados == []:
        codigo = 100
    else:
        for i in range(len(dados)):
            dados[i] = dados[i].strip('\n')
            dados[i] = dados[i].split('-')
            temp.append(dados[i][0])
        arquivo.close()
 
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        numeros = set(temp)
        esperado = set(range(min(numeros), max(numeros) + 1))
        faltantes = sorted(esperado - set(numeros))
        if faltantes == []:
            codigo = str(max(temp) + 1)
        else:
            for numero in faltantes:
                temp_cod.append(numero)
            codigo = str(temp_cod[0])
    return codigo
 
def cadastro():
    arq=open('pedido.txt', 'a+', encoding='utf-8')
    cod = busca_cod()
    prod= input("Digite o nome do produto: ")
    valor_uni=input("Digite o valor do produto: ")
    arq.writelines('{} - {} - {}\n'.format(cod,prod,valor_uni))
    arq.close()
    print('produto cadastrado\n')
 
def listar():
    print('Lista dos produtos!')
    arq=open('pedido.txt','r', encoding='utf-8')
    for linha in arq:
        print(linha)
    arq.close()
 
def alterar():
    listar()
    arq = open('pedido.txt', 'r', encoding='utf-8')
    conteudo = arq.readlines()
    arq.close()
    op_alt = input('Deseja editar algum produto? (s/n): ')
    while op_alt == 's':
        item = input('Digite o nome do item que deseja editar: ')
        pos = -1
        i = 0
        while i < len(conteudo):
            if item in conteudo[i]:
                pos = i
            else:
                ''
            i += 1
 
        if pos != -1:
            print('Item encontrado: ' + conteudo[pos].strip())
            for i in range(len(conteudo)):
                teste.append(conteudo[i].strip("\n").split(" - "))
            nova_desc = input("Digite a nova descrição: ")
            while nova_desc == "":
                nova_desc = input("Insira uma descrição válida!!!\nDigite a nova descrição: ")
            novo_valor = input("Digite o novo valor: ")
            while (novo_valor == "" or novo_valor.isalpha()):
                novo_valor = input("Insira um valor válido!!!\nDigite o novo valor: ")
            novo_item = str(teste[pos][0]) +  " - " + nova_desc + " - " + novo_valor + "\n"
            conteudo[pos] = novo_item
        else:
            print('Item não encontrado.')
 
        op_alt = input('Deseja editar outro produto? (s/n): ')
 
    arq = open('pedido.txt', 'w', encoding='utf-8')
    arq.writelines(conteudo)
    arq.close()
   
def remover():
    listar()
    rem=input('\nDigite o codigo que deseja remover: ')
    arq=open('pedido.txt','r', encoding='utf-8')
    linhas=arq.readlines()
    arq=open('pedido.txt','w', encoding='utf-8')
    for linha in linhas:
        if not linha.startswith(rem):
            arq.write(linha)
    arq.close()
    print('produto removido')
 
def operador ():
    pedido = []
    itens_pedidos=[]
    continuar = "s"
    total=0
    arquivo=open('pedido.txt','r')
    dados=arquivo.readlines()
    arquivo.close()
    if dados == []:
        print(cadastro)
    else:
        conf = input("Gostaria de iniciar o pedido? (s/n)\n")
        if conf != "s":
            print('Pedido cancelado!')
        nome = input("Digite o nome do cliente:\n")
    while continuar == "s":
        item_encontrado=''
        print("Aqui está nosso cardápio")
        listar()
        codigo=input('Digite o codigo do item solicitado:\n')
        i=0
        while i < len(dados):
            linhas = dados[i].strip()
            partes=linhas.split(' - ')
            if partes[0] == codigo:
                item_encontrado=linhas
                pedido.append(partes)
                nome_prod=partes[1]
                valor_uni=float(partes[2])
                qtd = int(input("Digite a quantidade:\n"))
                subtotal = qtd * valor_uni
                total += subtotal
                itens_pedidos.append((nome_prod, qtd, valor_uni, subtotal))
            i=i+1
        if item_encontrado=='':
            print('Item não encontrado!!!')
        else:
            print('Item adicionado!')        
        continuar = input("Deseja adicionar outro item? (s/n)\n")
 
    print(f"\nResumo do pedido de {nome}:")
    for item in itens_pedidos:
        print(f"{item[0]} - {item[1]}x R$ {item[2]:.2f} = R$ {item[3]:.2f}")
    print(f"\nTotal a pagar: R$ {total:.2f}")
    print('\nPedido feito com sucesso!\n')
 
 
#Main
while continuar == "s":
    perfil = menuprincipal()
    if perfil == "0":
        continuar = "n"
    elif  perfil == "1":
        while cont == "s":
            option = menu_adm()
            if option == "0":
                cont = "n"
            elif option == "1":
                cadastro()
            elif option == "2":
                listar()
            elif option == "3":
                alterar()
            else:
                remover()
    else:
        operador ()
 