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

# Personalize as opções aqui
num_combinations = 10000000
test_data = generate_test_data(num_combinations)
save_to_file(test_data)
print(f"Base de dados de teste gerada com {num_combinations * 2} combinações.")
