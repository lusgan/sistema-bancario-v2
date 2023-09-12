
menu = """
1 -Depositar
2- Sacar
3- Extrato
4- Criar usuario
5- Criar conta
6- Sair
"""
          
saldo = 0
n_saques = 0
extrato = []
usuarios = []
contas = []

def depositar(saldo,extrato,/):
    valor = float(input("Insira o valor do deposito:"))
    if valor<0:
        print("valor invalido")
    else:
        print("deposito executado.")
        NovoSaldo = saldo + valor
        extrato.append(("deposito",f"R${valor:.2f}"))
        return NovoSaldo

def sacar(*,saldo, extrato, n_saques, limite = 500, LIMITE_SAQUES = 3):
        valor = float(input("Insira o valor desejado:"))
        
        if(valor>saldo):
            print("nao ha saldo suficiente na conta")
        
        elif n_saques==LIMITE_SAQUES:
            print("Limite de saques diarios atingido")
        
        elif valor>limite:
            print("o valor maximo permitido para saque eh R$500")
            
        else:
            saldo-=valor
            n_saques+=1
            print(f"saque efetuado, saldo atual = R${saldo:.2f}")
            extrato.append(("saque",f"R${valor:.2f}"))
            return saldo

def exibir_extrato(saldo,/,*,extrato):
    if len(extrato)==0:
        print("Nao foram realizadas movimentacoes")
    
    else:
    
        print("\nExtrato:")
        for item in extrato:
            print(f"{item[0]} ----- {item[1]}")
        
        print("\n---------------------------")
        print(f"saldo total = R${saldo:.2f}")
        print("---------------------------")

def criar_usuario():
    cpf = input("Insira seu CPF:")
    usuario_ja_existe = False
    for e in usuarios:
        if cpf in e["cpf"]:
            usuario_ja_existe = True
            print("Ja existe usuario com esse CPF!")
    
    if not usuario_ja_existe:
        dic = {}
        dic["cpf"] = cpf
        dic["nome"] = input("Insira seu nome:")
        dic["data_nascimento"] = input("data de nascimento (dd-mm-aaaa):")
        dic["endereco"] = input("Informe o endereco (rua,n°- bairro - cidade/sigla estado):")
        
        usuarios.append(dic)
        print("------------------------------")
        print("Usuario criado com sucesso!")
        print("------------------------------")


def criar_conta():
    
    conta = {}
    
    cpf = input("Insira seu CPF:")
    usuario_ja_existe = False
    for e in usuarios:
        if cpf in e["cpf"]:
            usuario_ja_existe = True
            conta["usuario"] = e
            conta["numero"] = len(contas)+1
            conta["agencia"] = "0001"
            contas.append(conta)
                        
    if not usuario_ja_existe:
        print("Usuario nao encontrado!")
        return
    

while True:
    opcao = int(input(menu))
    
    if opcao==1:
        saldo = depositar(saldo,extrato)
            
              
    elif opcao==2:
       
        saldo = sacar(saldo=saldo,extrato=extrato,n_saques=n_saques)
            
            
    elif opcao==3:
        
        exibir_extrato(saldo, extrato = extrato)
            
    elif opcao==4:
        criar_usuario()
        
    elif opcao==5:
        criar_conta()
        
    elif opcao==6:
        break
    
    else:
        print("opcao invalida, por favor selecione novamente a opcao desejada")
    
