tarefas = []

def adicionar_tarefa(tarefas):
    nome = input("Digite o nome da tarefa: ")
    tarefa = {"nome": nome, "status": "pendente"}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nLista de tarefas:")
        for i, t in enumerate(tarefas):
            print(i + 1, "-", t["nome"], "-", t["status"])
        print()

def marcar_concluida(tarefas):
    listar_tarefas(tarefas) 

    if len(tarefas) == 0:
        print("Nao tem tarefas!")
        return
    
    numero = input("Digite o numero da tarefa para concluir: ")
    
    try:
        numero_int = int(numero)
    except:
        print("Digite um numero valido!")
        return
    
    if numero_int < 1 or numero_int > len(tarefas):
        print("Numero nao existe!")
        return
    
    indice = numero_int - 1
    tarefa = tarefas[indice]
    tarefa["status"] = "concluida"
    print("Tarefa concluida!")

def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    
    if len(tarefas) == 0:
        print("Nao tem tarefas!")
        return
    
    numero = input("Digite o numero da tarefa para editar: ")
    
    try:
        numero_int = int(numero)
    except:
        print("Digite um numero valido!")
        return
    
    if numero_int < 1 or numero_int > len(tarefas):
        print("Numero nao existe!")
        return
    
    indice = numero_int - 1
    tarefa = tarefas[indice]
    
    print("Tarefa atual: " + tarefa["nome"])
    
    nova_descricao = input("Nova descricao: ")
    
    if nova_descricao == "":
        print("Descricao nao pode ser vazia!")
        return
    
    tarefa["nome"] = nova_descricao 
    print("Tarefa editada!")

def remover_tarefa(tarefas):
    print("Função remover_tarefa ainda não implementada")

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

