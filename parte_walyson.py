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

if __name__ == "__main__":
    main()

            
   
