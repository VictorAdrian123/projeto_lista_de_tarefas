from parte_walyson import editar_tarefa, marcar_concluida
from parte_pacheco import adicionar_tarefa, listar_tarefas


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



