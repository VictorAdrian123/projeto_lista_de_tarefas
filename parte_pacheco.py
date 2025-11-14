def adicionar_tarefa(tarefas):
    nome = input("Digite o nome da tarefa: ")
    tarefa = {"nome": nome, "status": "pendente"}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas):
        numero = indice + 1
        print(f"{numero}. {tarefa['nome']} — {tarefa['status']}")
    print()