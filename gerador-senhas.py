import random
from unidecode import unidecode

def load_passwords_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f]
    return passwords

def load_names_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f]
    return names

def remove_accents(text):
    return unidecode(text)

def generate_test_data(num_combinations=100):
    passwords = load_passwords_from_file("senhas.txt")
    names = load_names_from_file("nomes.txt")
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

def save_to_file(test_data, filename="base_teste.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        for item in test_data:
            f.write("%s\n" % item)

def check_duplicates(filename="base_teste.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    unique_lines = set(lines)
    if len(unique_lines) != len(lines):
        print("O arquivo contém itens duplicados.")
    else:
        print("O arquivo não contém itens duplicados.")

def main_menu():
    print("1. Gerar lista de dados de teste")
    print("2. Verificar se o arquivo base contém itens duplicados")
    
    choice = input("Escolha uma opção: ")
    
    if choice == "1":
        num_combinations = int(input("Digite o número de combinações desejado: "))
        test_data = generate_test_data(num_combinations)
        save_to_file(test_data)
        print(f"Base de dados de teste gerada com {num_combinations * 2} combinações.")
    elif choice == "2":
        check_duplicates()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main_menu()
