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
