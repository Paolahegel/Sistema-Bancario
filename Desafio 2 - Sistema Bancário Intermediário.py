import textwrap 

def menu():
    menu_texto = """\n
    ===============MENU==============
    [1] \t Depositar
    [2] \t Sacar
    [3] \t Extrato
    [4] \t Cadastrar Usuário (Cliente)
    [5] \t Cadastrar Conta Bancária
    [6] \t Listar Contas
    [0] \t Sair

    =>"""
    return input(textwrap.dedent(menu_texto)) #retornando a opção que o usuário digitou

# argumentos nomeados
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque exced o limite.")

    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!") 
    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# argumentos por posição
def depósito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# argumentos por posição/nome
def mostrar_extrato(saldo, /, *, extrato ):
    print("\n ==============EXTRATO===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t \t R$ {saldo:.2f}")
    print("=======================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_de_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairo - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereço": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None


def criar_conta(AGENCIA, numero_conta, usuarios): 
    cpf = input("Informe o CPF do Usuário: ")
    usuario = filtrar_usuarios(cpf,usuarios)

    if usuario:
        print("\n Conta criado com sucesso!")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}

    else:
        print("\n usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

    return None
    
# na Main eu defino as constantes
def main():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        
        opcao = int(menu())
        
        if opcao == 1: 
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depósito(saldo, valor, extrato) #argumentos posicionais


        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
                
            saldo, extrato = saque( #argumentos nomeados
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITES_SAQUES,
                ) 
        
        elif opcao == 3:
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
