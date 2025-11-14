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
    
tarefas = []

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