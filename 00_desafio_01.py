def menu():
    menu = """"
    ============ M E N U ============
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q]  Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("=== Depósito realizado com sucesso ===")
    else:
        print("@@@ Operação Falhou! O valor informado é inválido! @@@")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print(" @@@ Operação Falhou! Você não tem saldo suficiente! @@@")

    elif excedeu_limite:
        print(" @@@ Operação Falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print(" @@@ Operação Falhou! Numero máximo de saques excedidos. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
        numero_saques += 1

    else:
        print(" @@@ Operação Falhou! O valor informado é inválido! @@@")

    return  saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n=============EXTRATO=============")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("Não foram realizada movimentações" if not extrato else extrato)
    print("\n=================================")

def criar_usuario():
    cpf = input("Informe o CPF (Somente números): ")
    usuario = 0

    if usuario:
        print("@@@ Já existe um usuário com esse CPF @@@")

    nome = input("Informe o nome completo: ")
    data_de_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    print(" === Usuário criado com sucesso! ===")

def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = 0
    
    if usuario:
        print(" === Conta criada com sucesso === ")
        return {"Nome": nome, "Data-de-Nascimento": data_de_nascimento, "Endereço": endereco}

    else:
        print("@@@ Usuário não encontrado. Favor cadastrar usuário! @@@")

def filtrar_usuario():
    usuarios_filtrados = [usuario for usuario in usuarios if usuarios["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas():
    pass

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":

            exibir_extrato(saldo, extrato=extrato)    

        elif opcao == "nc":
            criar_conta()               

        elif opcao == "lc":
            listar_contas()

        elif opcao == "nu":
            criar_usuario()

        elif opcao == "q":
            print("Obrigado pela preferência !!!")
            break

        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")