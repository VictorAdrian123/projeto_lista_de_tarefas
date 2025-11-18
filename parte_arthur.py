def remover_tarefa(tarefas):

    entrada = False
    while not entrada:
        entrada = int(input("\nDigite o id da tarefa que deseja remover: "))

        for t in tarefas:
            if t['id'] == entrada:
                confirmar = input(f"\nTem certeza que deseja remover {t['titulo']}? (s/n)").strip().lower()
                if confirmar == 's':
                    tarefas.remove(t)
                    print("Tarefa removida com sucesso. ")
                else:
                    print("\nRemoção de Tarefa cancelada. ")
                    return

                entrada = True
                break

        if not entrada:
            print("\nid inexistente. Digite novamente!\n")