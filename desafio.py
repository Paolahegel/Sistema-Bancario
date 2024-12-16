menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = float(input("Informe o valor desejado para o depósito: "))

        if valor_deposito > 0:
             saldo += valor_deposito
             extrato += f"Depósito de R$ {valor_deposito: .2f}\n"
             print("Depósito realizado com sucesso")

        else:
            print("Operação falhou! Informe um valor válido!")

    elif opcao == 2:
         valor_saque = float(input("Informe o valor do saque: "))

         excedeu_saldo = valor_saque > saldo

         excedeu_limite = valor_saque > limite

         excedeu_saques = numero_saques >= LIMITE_SAQUES

         if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

         elif excedeu_limite:
            print("Operação falhou! O valor do saque execede o limite.")

         elif excedeu_saques:
            print("Operação falhou!Número máximo de saques excedido!")
         
         elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque: .2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso")
            
    else:
        print("Operação falhou! O valor informado é inválido!")

    if opcao == 3:        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
