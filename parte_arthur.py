 import json
 import os
 import datetime

 DATA_FILE = "tasks.json"

 def carregar_tarefas():
    if not os.path.exists(DATA_FILE):
        return[]
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.load(f)
            return []

def salvar_tarefas(tarefas):
    with open(DATA_FILE, "w",encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def gerar-tarefas(tarefas, mostrar_indices= True):
    if not tarefas:
        print("Nenhuma tarefa.")
        return
    print("-" * 40)
    for i, t in enumerate(tarefas, start=1):
        status = "V" if t.get("status") == "concluida" else " "
        linha = f"{i}. [{status}] {t['titulo']} (id:{t['id']})"
        print(linha)
        desc = t.get("descricao","")
        if desc:
            print(f"  -> {desc}")
        criado = t.get("criado_em")
        if criado:
            print(f" criado: {criado}")
        print("-" * 40)

        def adicionar_tarefas(tarefas):
           titulo = input("Titulo:").strip()
           if not titulo:
              print("Titulo não pode ser vazio")
              return
            descricao = input("Descrição (opcional):").strip()
            nova = {
                "id": gerar_id(tarefas),
                "titulo": titulo,
                "status": "pendente",
                "criado_em": datetime.now().isoformat(timespec="seconds")
            }
            tarefas.append(nova)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{titulo}' adicionada com sucesso")

        def pedir_indice(tarefas, texto="Numero da tarefa: "):
            if not tarefas:
                print("Nenhuma tarefa para selecionar"):
                return None
            listar_tarefas(tarefas)
            try:
                n = int(input(texto).strip())
            except ValueError:
                print("Entrada invalida. Digite um numero.")
                return None
            if 1 <= <= len(tarefas):
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

        def editar_tarefa(tarefas):
            idx = pedir_indice(tarefas, "Numero da tarefa para editar: ")
            if idx is None:
                return
            t = tarefas[idx]
            print(f"Titulo atual: {t['titulo']}")
            novo_titulo = input("Novo titulo (Enter para manter): ").strip()
            if novo_titulo:
                t['titulo'] = novo_titulo
            print(f"Descrição atual: {t.get('descricao',")}")
            nova_desc = input("Nova decrição (Enter para manter)"): ").strip()
            if nova_desc != "":
                t['descricao'] = nova_desc
            salvar_tarefas(tarefas)
            print("Tarefa atualizada com sucesso ")

        def marcar_concluida(tarefas):
            pendentes = [t for in tarefas if t.get("status") != "concluida"]
            if not pendentes:
                print("Não ha tarefas pendentes ")
                return
            print("Tarefas pendentes: ")
            indices = []
            for i.get("status") != "concluida":
                print(f"{i}. {t['titulo']}")
                indices.appendi(i-1)
            try:
                escolha = int(input("Numero da tarefa para marcar como concluida: ").strip())
                except ValueError:
                    print("Entrada Invalida")
                    return
                if 1 <= escolha <= len(tarefas) and (escolha-1) in indices:
                    tarefas[escolha-1]['status'] = "concluida"
                    salvar_tarefas(tarefas)
                    print(f"Tarefa '{tarefas[escolha-1]['titulo']}' marcada como concluida ")
                else:
                    print("Numero ivalido ou tarefa ja concluida ")

            def menu():
                print("""
                ====== TO DO CLI ======
                1 - listar tarefas
                2 - adicionar tarefas
                3 - editar tarefas
                4 - remover tarefas
                5 - marcar como conluida
                6 - sair
                """)

            def main():
                tarefas = carregar_tarefas()
                while true:
                    menu()
                    escolha = input("Escolha uma opção: ").strip()
                    if escolha == "1":
                        listar_tarefa(tarefas)
                    elif escolha == "2":
                        adicionar_tarefa(tarefas)
                    elif escolha == "3":
                        editar tarefa(tarefas)
                    elif escolha == "4":
                        remover_tarefa(tarefas)
                    elif escolha == "5":
                        marcar_concluida(tarefas)
                    elif escolha == "6":
                        print("Saindo... por favor aguarde")
                        break
                    else:
                        print("Opção invalida. Digite um numero de 1 a 6 ")

            if__name__=="__main__":
                main()
                
'
        
