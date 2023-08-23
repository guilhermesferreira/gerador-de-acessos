import random  # Importa o módulo random para gerar números aleatórios
from unidecode import unidecode  # Importa a função unidecode do módulo unidecode para remover acentos
import gc  # Importar o módulo gc para realizar a coleta de lixo

# Função para carregar dados de um arquivo e retornar uma lista de strings
def load_data_from_file(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:  
            if ':' not in line:  # Verifica se a linha não contém dois pontos
                data.append(line.strip())
    return data 

# Função para salvar dados em um arquivo
def save_data_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write("%s\n" % item)  # Escreve cada item da lista no arquivo, seguido de uma nova linha

# Função para remover acentos de um texto usando a função unidecode
def remove_accents(text):
    return unidecode(text)

def generate_test_data_batch(names, passwords, batch_size):
    test_data = []
    for _ in range(batch_size):
        full_name = random.choice(names)
        full_name = remove_accents(full_name)
        
        if "@" in full_name:
            # Se o nome já contém um "@" (possivelmente um email), adicionamos apenas a senha
            password = random.choice(passwords)
            test_data.append(f"{full_name}:{password}")
        else:
            if " " in full_name:
                first_name, last_name = full_name.split(" ", 1)
                email_base = [
                    full_name.replace(" ", "").lower(),
                    f"{first_name.lower()}.{last_name.lower()}",
                    f"{first_name.lower()}_{last_name.lower()}",
                ]
            else:
                first_name = full_name
                email_base = [full_name.lower()]

            password = random.choice(passwords)

            for email in email_base:
                email_hotmail = f"{email}@hotmail.com"
                email_gmail = f"{email}@gmail.com"
                test_data.append(f"{email_hotmail}:{password}")
                test_data.append(f"{email_gmail}:{password}")
                test_data.append(f"{email.split('@')[0]}:{password}")
            
    return test_data

def generate_test_data(num_combinations=100, batch_size=1000000):
    passwords = load_data_from_file("senhas.txt")
    names = load_data_from_file("nomes.txt")
    
    with open("base_teste.txt", "w", encoding="utf-8") as f:
        for batch_num in range(num_combinations // batch_size):
            print(f"Gerando e salvando dados {batch_num + 1}/{num_combinations // batch_size}")
            batch_data = generate_test_data_batch(names, passwords, batch_size)
            for item in batch_data:
                f.write("%s\n" % item)
            import gc
            gc.collect()
        
        remaining_data = generate_test_data_batch(names, passwords, num_combinations % batch_size)
        for item in remaining_data:
            f.write("%s\n" % item)
    
    print(f"Base de dados de teste gerada com {num_combinations * 2} combinações.")

    
# Função para remover duplicados de um arquivo
def remove_duplicates(filename):
    data = load_data_from_file(filename)  # Carrega dados do arquivo
    initial_lines = len(data)  # Número de linhas inicial
    # Filtra as linhas que contêm dois pontos e as linhas sem dois pontos
    data_with_colon = []
    data_without_colon = []
    for line in data:
        if ':' in line:
            data_with_colon.append(line)
        else:
            data_without_colon.append(line)
    unique_data = list(set(data_with_colon))  # Remove duplicados usando um conjunto
    num_duplicates = initial_lines - len(unique_data)  # Calcula o número de duplicados
    num_lines_removed = len(data_without_colon) + (initial_lines - len(data_with_colon))  # Calcula o número de linhas removidas sem :
    save_data_to_file(unique_data, filename)  # Salva os dados únicos no arquivo
    
    print("Informações sobre a remoção de duplicados:")
    print(f"Arquivo: {filename}")
    print(f"Quantidade inicial de linhas: {initial_lines}")
    print(f"Quantidade de linhas duplicadas: {num_duplicates}")
    print(f"Quantidade de linhas sem dois pontos: {len(data_without_colon)}")
    print(f"Quantidade de linhas removidas: {num_lines_removed}")
    print(f"Nova quantidade de linhas: {len(unique_data)}")

# Função para mostrar um menu e executar ações com base nas opções escolhidas
def main_menu():
    print("1. Gerar lista de dados de teste")
    print("2. Verificar e remover duplicados da lista de usuários")
    print("3. Verificar e remover duplicados da lista de senhas")
    print("4. Verificar e remover duplicados do arquivo base")
    
    choice = input("Escolha uma opção: ")
    
    if choice == "1":
        num_combinations = int(input("Digite o número de combinações desejado: "))
        test_data = generate_test_data(num_combinations)
        print(f"Base de dados de teste gerada com {num_combinations * 2} combinações.")
    elif choice == "2":
        users_data = load_data_from_file("nomes.txt")
        remove_duplicates("nomes.txt")
        print("Duplicados removidos da lista de usuários com sucesso.")
    elif choice == "3":
        passwords_data = load_data_from_file("senhas.txt")
        remove_duplicates("senhas.txt")
        print("Duplicados removidos da lista de senhas com sucesso.")
    elif choice == "4":
        remove_duplicates("base_teste.txt")
        print("Duplicados removidos do arquivo base com sucesso.")
    else:
        print("Opção inválida.")

# Executa o menu principal quando o script é executado
if __name__ == "__main__":
    main_menu()
