import pandas as pd
from pathlib import Path


# =========================
# CONFIGURAÇÕES
# =========================
DATA_DIR = Path("data")
INPUT_FILE = DATA_DIR / "raw_dados.csv"
OUTPUT_FILE = DATA_DIR / "dados_tratados.csv"


# =========================
# EXTRACT
# =========================
def extract_data(filepath: Path) -> pd.DataFrame:
    """
    Lê o arquivo CSV bruto e retorna um DataFrame.
    """
    df = pd.read_csv(filepath)
    print(f"[EXTRACT] Registros lidos: {len(df)}")
    return df


# =========================
# TRANSFORM
# =========================
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica regras de limpeza, padronização e qualidade de dados.
    """

    registros_iniciais = len(df)

    # 1️⃣ Remover registros sem nome
    df = df.dropna(subset=["nome"])

    # 2️⃣ Converter colunas numéricas (erros viram NaN)
    df["idade"] = pd.to_numeric(df["idade"], errors="coerce")
    df["salario"] = pd.to_numeric(df["salario"], errors="coerce")

    # 3️⃣ Preencher idade ausente com a mediana
    mediana_idade = df["idade"].median()
    df["idade"] = df["idade"].fillna(mediana_idade)

    # 4️⃣ Remover registros com salário ausente
    df = df.dropna(subset=["salario"])

    # 5️⃣ Remover menores de idade
    df = df[df["idade"] >= 18]

    # 6️⃣ Padronizar textos
    colunas_texto = ["nome", "cidade", "departamento"]
    for coluna in colunas_texto:
        df[coluna] = (
            df[coluna]
            .astype(str)
            .str.strip()
            .str.title()
        )

    # 7️⃣ Preencher cidade vazia com valor padrão
    df["cidade"] = df["cidade"].replace("Nan", "São Paulo")

    # 8️⃣ Remover duplicados (baseado em nome e cidade)
    df = df.drop_duplicates(subset=["nome", "cidade"])

    registros_finais = len(df)
    print(f"[TRANSFORM] Registros iniciais: {registros_iniciais}")
    print(f"[TRANSFORM] Registros finais: {registros_finais}")

    return df


# =========================
# LOAD
# =========================
def load_data(df: pd.DataFrame, output_path: Path) -> None:
    """
    Salva o DataFrame tratado em CSV.
    """
    df.to_csv(output_path, index=False)
    print(f"[LOAD] Arquivo gerado em: {output_path}")


# =========================
# PIPELINE
# =========================
def main():
    df_raw = extract_data(INPUT_FILE)
    df_clean = transform_data(df_raw)
    load_data(df_clean, OUTPUT_FILE)


if __name__ == "__main__":
    main()
