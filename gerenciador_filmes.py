## Inicio
entrada = input("Digite os títulos dos filmes separados por vírgula: ")
lista_filmes = entrada.split(",") # Divide a string em uma lista
print(f"Títulos dos filmes cadastrados: {lista_filmes}")
print()
print(f"Quantidade de filmes cadastrados: {len(lista_filmes)}") #Exibe todos os títulos de filme da lista de filmes
print(f"Nome do primeiro filme da lista: {lista_filmes[0]}") #Exibe o 1o título da lista de filmes
print(f"Nome do último filme da lista: {lista_filmes[-1]}") #Exibe o último título da lista de filmes

adiciona_filme_final_lista = input("Digite o título de um novo filme para adicionar no final da lista: ")
lista_filmes.append(adiciona_filme_final_lista.strip()) #Adiciona título no final da lista de filmes

adiciona_filme_inicio_lista = input("Digite o título de um novo filme para adicionar no início da lista: ")
lista_filmes.insert(0, adiciona_filme_inicio_lista.strip()) #Adiciona título no início da lista de filmes

remove_filme = input("Digite o nome do título do filme que deseja remover: ")
if remove_filme.strip() in lista_filmes:
    lista_filmes.remove(remove_filme.strip()) #Remove título do filme da lista de filmes
    print(f"** Sucesso! O título do filme '{remove_filme.strip()}' foi removido da lista de filmes. **")
else:
    print(f"O título do filme '{remove_filme.strip()}' não foi encontrado na lista de filmes.")

lista_filmes.sort() #Ordena a lista de filmes em ordem alfabética
print("\nExibindo a lista de títulos dos filmes em ordem alfabética:", lista_filmes)

lista_filmes.reverse() #Ordena a lista de filmes em ordem inversa
print("\nExibindo a lista de títulos dos filmes em ordem inversa:", lista_filmes)

copia_filmes = lista_filmes.copy() #Faz uma cópia da lista de filmes
lista_filmes.clear() #Executa uma limpeza na lista de filmes original

print("\nSegue a lista original limpa:", lista_filmes) #Exibe a lista original de filmes
print("Segue a cópia da lista original:", copia_filmes) #Exibe a lista de filmes copiada da lista original de filmes
## Fim ##