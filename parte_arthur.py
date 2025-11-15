def pedir_indice(tarefas, texto="Numero da tarefa: "):
            if not tarefas:
                print("Nenhuma tarefa para selecionar")
                return None
            listar_tarefas(tarefas)
            try:
                n = int(input(texto).strip())
            except ValueError:
                print("Entrada invalida. Digite um numero.")
                return None
            if 1 <= len(tarefas):
                return n - 1
            print("Numero invalido.")
            return None

def remover_tarefa(tarefas):
            idx = pedir_indice(tarefas,"Numero da tarefa para remover: ")
            if idx is None:
                return
            confirm = input(f"Tem certeza que quer remover '{tarefas[idx]['titulo']}'? (s/N: ").strip().lower()
            if confirm == "s":
                removida = tarefas.pop(idx)
                salvar_tarefas(tarefas)
                print(f"Tarefa '{removida['titulo']}' removida com sucesso. " )
            else:
                print("Remoção cancelada. ")
                
            if escolha == "4":
                remover_tarefa(tarefas)
            elif escolha == "6":
                print("Saindo... por favor aguarde")
                break

            else:
                print("Opção invalida. Digite um numero de 1 a 6 ")