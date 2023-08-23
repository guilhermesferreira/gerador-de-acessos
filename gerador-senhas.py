import random
from unidecode import unidecode

def load_data_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = [line.strip() for line in f]
    return data

def save_data_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write("%s\n" % item)

def remove_accents(text):
    return unidecode(text)

def generate_test_data(num_combinations=100):
    passwords = load_data_from_file("senhas.txt")
    names = load_data_from_file("nomes.txt")
    test_data = []
    for _ in range(num_combinations):
        full_name = random.choice(names)
        full_name = remove_accents(full_name)  # Remove acentos
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
            
    return test_data

def remove_duplicates(filename):
    data = load_data_from_file(filename)
    initial_lines = len(data)
    unique_data = list(set(data))
    num_duplicates = initial_lines - len(unique_data)
    save_data_to_file(unique_data, filename) 
    
    print("Informações sobre a remoção de duplicados:")
    print(f"Arquivo: {filename}")
    print(f"Quantidade inicial de linhas: {initial_lines}")
    print(f"Quantidade de linhas duplicadas: {num_duplicates}")
    print(f"Quantidade de linhas removidas: {num_duplicates}")
    print(f"Nova quantidade de linhas: {len(unique_data)}")


def main_menu():
    print("1. Gerar lista de dados de teste")
    print("2. Verificar e remover duplicados da lista de usuários")
    print("3. Verificar e remover duplicados da lista de senhas")
    print("4. Verificar e remover duplicados do arquivo base")
    
    choice = input("Escolha uma opção: ")
    
    if choice == "1":
        num_combinations = int(input("Digite o número de combinações desejado: "))
        test_data = generate_test_data(num_combinations)
        save_data_to_file(test_data, "base_teste.txt")
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
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main_menu()