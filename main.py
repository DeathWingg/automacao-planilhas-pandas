import pandas as pd


def limpar_e_analisar_dados():
    print("Iniciando o processo de limpeza...")

    # 1. Ler os dados sujos
    df = pd.read_csv("alunos_sujos.csv")
    print(f"Total de linhas originais: {len(df)}")

    # 2. Remover duplicatas (mantendo a primeira ocorrência do ID)
    df = df.drop_duplicates(subset=["ID"], keep="first")
    print(f"Linhas após remover duplicatas: {len(df)}")

    # 3. Tratar dados nulos (removendo linhas que tenham qualquer campo vazio)
    df = df.dropna()
    print(f"Linhas após remover nulos: {len(df)}")

    # 4. Padronizar as datas
    # O parâmetro dayfirst=True resolve o problema de datas como 15/02/2023
    df["Data_Inscricao"] = pd.to_datetime(
        df["Data_Inscricao"], format="mixed", dayfirst=True
    )
    df["Data_Inscricao"] = df["Data_Inscricao"].dt.strftime("%Y-%m-%d")

    # 5. Análise: Calcular a média de notas por curso
    print("\nCalculando a média de notas por curso...")
    resumo_cursos = df.groupby("Curso")["Nota"].mean().reset_index()
    resumo_cursos.columns = ["Curso", "Media_Notas"]
    resumo_cursos = resumo_cursos.sort_values(by="Media_Notas", ascending=False)

    # 6. Salvar o resultado em um Excel bonito com duas abas
    arquivo_saida = "relatorio_final.xlsx"
    with pd.ExcelWriter(arquivo_saida, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Dados_Limpos", index=False)
        resumo_cursos.to_excel(writer, sheet_name="Resumo_Cursos", index=False)

    print(
        f"\nSucesso! O arquivo '{arquivo_saida}' foi gerado com as abas 'Dados_Limpos' e 'Resumo_Cursos'."
    )


if __name__ == "__main__":
    limpar_e_analisar_dados()
