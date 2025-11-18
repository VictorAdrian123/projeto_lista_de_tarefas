tarefas = [] 

def adicionar_tarefa(tarefas):
    nome = input("\nDigite o nome da tarefa: ")
    tarefa = {"nome": nome, "status": "pendente"}
    novo_id = len(tarefas) + 1
    tarefa = {"id": novo_id, "nome": nome, "status": "pendente"}
    tarefas.append(tarefa)
    print("\nTarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.")
    else:
        print("\nLista de tarefas:\n")
        for t in tarefas:
          print(f"{t['id']} - {t['nome']} - {t['status']}")
        print()

def marcar_concluida(tarefas):
    listar_tarefas(tarefas) 

    if len(tarefas) == 0:
        print("\nNao tem tarefas!")
        return
    
    numero = input("\nDigite o numero da tarefa para concluir: ")
    
    try:
        numero_int = int(numero)
    except:
        print("\nDigite um numero valido!")
        return
    
    if numero_int < 1 or numero_int > len(tarefas):
        print("\nNumero nao existe!")
        return
    
    indice = numero_int - 1
    tarefa = tarefas[indice]
    tarefa["status"] = "concluida"
    print("\nTarefa concluida!")

def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    
    if len(tarefas) == 0:
        print("\nNao tem tarefas!")
        return
    
    numero = input("\nDigite o numero da tarefa para editar: ")
    
    try:
        numero_int = int(numero)
    except:
        print("\nDigite um numero valido!")
        return
    
    if numero_int < 1 or numero_int > len(tarefas):
        print("\nNumero nao existe!")
        return
    
    indice = numero_int - 1
    tarefa = tarefas[indice]
    
    print("\nTarefa atual: " + tarefa["nome"])
    
    nova_descricao = input("\nNova descricao: ")
    
    if nova_descricao == "":
        print("\nDescricao nao pode ser vazia!")
        return
    
    tarefa["nome"] = nova_descricao 
    print("\nTarefa editada!")

def remover_tarefa(tarefas):

    entrada = False
    while not entrada:
        entrada = int(input("\nDigite o id da tarefa que deseja remover: "))

        for t in tarefas:
            if t['id'] == entrada:
                confirmar = input(f"\nTem certeza que deseja remover {t['nome']}? (s/n)").strip().lower()
                if confirmar == 's':
                    tarefas.remove(t)
                    print("\nTarefa removida!")
                else:
                    print("\nRemoção cancelada!")
                    return

                entrada = True
                break

        if not entrada:
            print("\nid inexistente. Digite novamente!\n")

def menu():
    print("\n<====== SISTEMA TO DO ======>\n")
    print()
    print("1. Adicionar tarefas")
    print("2. Listar tarefas")
    print("3. Marcar tarefas como concluida")
    print("4. Editar tarefas")
    print("5. Remover tarefas")
    print("6. Sair")

def main():
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            editar_tarefa(tarefas)
        elif opcao == "5":
            remover_tarefa(tarefas)
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção invalida. Tente novamente.")    

if __name__ == "__main__":
    main()

