menu = """"
============
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
============
=> 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("Depósito realizado com sucesso")

        else:
            print("Operação Falhou! O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if  excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação Falhou! Numero máximo de saques excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
            numero_saques += 1

        else:
            print("Operação Falhou! O valor informado é inválido!")

    elif opcao == "e":
        print("\n=============EXTRATO=============")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("Não foram realizada movimentações" if not extrato else extrato)
        print("\n=================================")

    elif opcao == "q":
        print("Obrigado pela preferência !!!")
        break

    else:
        print("Opção Inválida, por favor selecione novamente a operação desejada.")