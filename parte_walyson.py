def marcar_concluida(tarefas):
    """Marca uma tarefa como concluída usando os conceitos solicitados"""
    print("\n--- LISTA DE TAREFAS ---")
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa[0]} - [{tarefa[1]}]")
    try:
        numero = int(input("\nDigite o número da tarefa a marcar como concluída: "))
        
        if 1 <= numero <= len(tarefas):
            indice = numero - 1
            descricao_atual, status_atual = tarefas[indice]
            
            novas_tarefas = []
            
            for i, tarefa in enumerate(tarefas):
                if i == indice:
                    novas_tarefas.append((tarefa[0], "concluída"))
                else:
                    novas_tarefas.append(tarefa)
                    rint(f" Tarefa '{descricao_atual}' marcada como concluída!")
            return novas_tarefas
            
        else:
            print(" Número inválido! Tarefa não encontrada.")
            return tarefas
            
    except ValueError:
        print(" Por favor, digite um número válido!")
        return tarefas
    
def editar_tarefa(tarefas):
    """Edita o nome de uma tarefa usando os conceitos solicitados"""

    print("\n--- LISTA DE TAREFAS ---")
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa[0]} - [{tarefa[1]}]")  
    try:
        numero = int(input("\nDigite o número da tarefa a editar: "))
        if 1 <= numero <= len(tarefas):
            indice = numero - 1

            novo_nome = input("Digite o novo nome da tarefa: ").strip()
            if novo_nome:
                descricao_antiga, status_atual = tarefas[indice]
                
                novas_tarefas = []
                for i, tarefa in enumerate(tarefas):
                    if i == indice:
                        novas_tarefas.append((novo_nome, tarefa[1]))

                else:
                        novas_tarefas.append(tarefa)
                
                print(f"Tarefa editada: '{descricao_antiga}' → '{novo_nome}'")
                return novas_tarefas
            else:
                print("O nome não pode estar vazio!")
                return tarefas
        else:
            print("Número inválido! Tarefa não encontrada.")
            return tarefas
            
    except ValueError:
        print("Por favor, digite um número válido!")
        return tarefas
            
                
               


