horarios = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


def menu():  #Menu de exibição
    menu = 0
    while(menu < 1):
        print("1 - Adicionar eventos\n2 - Ver horários\n3 - Mostrar todos eventos\n4 - Editar eventos\n5 - Sair")
        opc = int(input("Digite sua opção: "))
        if(opc == 1):
            registro()
            print("\n")
            continue
        elif(opc == 2):
            mostrarHorario()
            print("\n")
            continue
        elif(opc == 3):
            mostrarTudo()
            print("\n")
            continue
        elif(opc == 4):
            editarHorario()
            print("\n")
            continue
        elif(opc == 5):
            print("Desligando")
            break
        else:
            print("Opção inválida\n")


def registro():
    hora = int(input("Digite o horário desejado (Por exemplo, 23:00 = 23): "))
    desc = input("Digite o evento desejado: ")
    horarios.insert(hora, desc)


def mostrarHorario():
    hora = int(input("Digite o horário desejado (Por exemplo, 23:00 = 23): "))
    print(horarios[hora])
    if horarios[hora] in [""]:
        print("Nada registrado.")


def mostrarTudo():
    print(horarios)


def editarHorario():
    hora = int(input("Digite o horário desejado (Por exemplo, 23:00 = 23): "))
    desc = input("Digite o evento desejado: ")
    horarios.pop(hora)
    horarios.insert(hora, desc)

print("Agenda")
menu()
