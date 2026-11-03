import pandas as pd

# Criando dados falsos e "sujos" de alunos
dados = {
    "ID": [1, 2, 3, 4, 5, 6, 6, 7, 8, 9],  # O ID 6 está duplicado
    "Nome": [
        "Ana",
        "Bruno",
        "Carlos",
        "Diana",
        "Eduardo",
        "Fernanda",
        "Fernanda",
        "Gabriel",
        "Helena",
        None,
    ],  # Tem um nulo
    "Curso": [
        "Ciências Sociais",
        "Informática",
        "Ciências Sociais",
        "Informática",
        None,
        "Administração",
        "Administração",
        "Ciências Sociais",
        "Informática",
        "Administração",
    ],  # Tem um nulo
    "Nota": [8.5, 7.0, 9.0, 5.5, 6.0, 8.0, 8.0, 7.5, 10.0, 4.0],
    "Data_Inscricao": [
        "2023-01-15",
        "15/02/2023",
        "2023-03-10",
        "10/04/2023",
        "2023-05-20",
        "2023-06-15",
        "2023-06-15",
        "2023-07-01",
        "2023-08-22",
        "2023-09-30",
    ],  # Datas em formatos diferentes
}

# Convertendo para um DataFrame do Pandas e salvando como CSV
df = pd.DataFrame(dados)
df.to_csv("alunos_sujos.csv", index=False, encoding="utf-8")
print("Planilha 'alunos_sujos.csv' criada com sucesso!")
