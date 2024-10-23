
menu = """

======Bem Vindo(a)!======
Escolha a opção desejada:
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo Usuário
[c] Criar Conta
[q] Sair

=> """

LIMITE_SAQUES = 3
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = []
numero_saques = 0
pessoas = []
contas = 1

def depositar(saldo, extrato):
    valor = float(input("Informe o valor que deseja depositar: "))

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")

    else:
        print("Operação falhou. O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques):
    valor = float(input("Informe o valor que deseja sacar: "))
        
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("Operação falhou! O Valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso.")

    else:
        print("Operação falhou. Valor informado não é válido.")

    return saldo, extrato, numero_saques

def criar_usuario(pessoas):

    cpf = input("CPF: ")   
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            print("Usuário já cadastrado")
            return

    nome = input("Nome Completo: ")
    data_nascimento = input("Data de Nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/estado): ")
    
    nova_pessoa = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }

    pessoas.append(nova_pessoa)
    print("Cadastrado com Sucesso!!")

def criar_conta(agencia, pessoas):   
    global contas
    cpf = input("Digite o CPF: ")
    
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            numero_conta = f"{AGENCIA}-{contas}"
            print("Conta criada com sucesso!")
            print(f"Número da conta: {numero_conta}")
            contas += 1 
            return numero_conta, contas

    print("Usuário não encontrado. Conta não criada.")
    return None, contas

def gerar_extrato(saldo, *, extrato):
    print("\n===============Extrato===============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for ext in extrato:
            print(ext)

    print(f"\nSaldo: R$ {saldo:.2f}")
    print("======================================")

while True:

    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)

    elif opcao == "u":
        criar_usuario(pessoas)

    elif opcao == "c":
        criar_conta(AGENCIA, pessoas)

    elif opcao == "e":
        gerar_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("Obrigado por utilizar os nossos serviços!")
        break

    else:
        print("Operação inválida. Insira novamente a opçao desejada.")