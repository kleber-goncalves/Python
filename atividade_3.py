import pandas as pd

df = pd.read_csv("dados_estudantes.csv")
print(df.head())
print("-----------------------------------------------------------")
# Verificação de erros de digitação
df.info()

print("-----------------------------------------------------------")


# Deixar os dados padronizados
df["turno"] = df["turno"].str.lower().str.strip()
df["escola"] = df["escola"].str.lower().str.strip()
df["idade"] = pd.to_numeric(df["idade"],errors="coerce")
df["nota"] = pd.to_numeric(df["nota"],errors="coerce")
df.info()

print("-----------------------------------------------------------")

# Tirar valores nulos
df_limpo = df.dropna(subset = ["idade","nota"])
df_limpo.info()

print("-----------------------------------------------------------")

# agrupar os dados e mostrar a média
media_por_turno = df_limpo.groupby("turno")["nota"].mean()
media_por_idade = df_limpo.groupby("turno")["idade"].mean()
melhor_turno = media_por_turno.idxmax()

print(f"Turno com maior media: {melhor_turno} ")

print("-----------------------------------------------------------")


print("Media por idade: ",media_por_idade)

print("-----------------------------------------------------------")
