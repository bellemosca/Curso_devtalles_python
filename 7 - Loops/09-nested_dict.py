nested_dict = {
    "Pessoa1": {"Nome": "Isabelle", "idade": 33, "cidade": "Fortaleza"},
    "Pessoa2": {"Nome": "Eduardo", "idade": 26, "cidade": "Campinas"},
    "Pessoa3": {"Nome": "Felipe", "idade": 37, "cidade": "Natal"},
}

for key, value in nested_dict.items():
    print(f"{key}:")
    for sub_key, sub_value in value.items():
        print(f" {sub_key}: {sub_value}")
