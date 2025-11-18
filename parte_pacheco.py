def adicionar_tarefa(tarefas):
    nome = input("Digite o nome da tarefa: ")
    tarefa = {"nome": nome, "status": "pendente"}
    novo_id = len(tarefas) + 1
    tarefa = {"id": novo_id, "titulo": nome, "status": "pendente"}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nLista de tarefas:")
        for t in tarefas:
          print(f"{t['id']} - {t['titulo']} - {t['status']}")
        print()
 
 