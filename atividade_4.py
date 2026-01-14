import pandas as pd

# ler o arquivo csv
df = pd.read_csv("dados_estudantes.csv")

# tirar os espacos e deixar tudo minusculo
df["turno"] = df["turno"].str.lower().str.strip()

# todos os valores que estão em nota vam ser numeros inteiros
df["nota"] = pd.to_numeric(df["nota"], errors="coerce")

print("-------------------------------------------------------------")

#criar uma nova coluna com o desempenho
def classificar_desempenho(nota):
   
    if nota >= 7:
        return "bom"
    elif nota >= 5:
        return "regular"
    else:
        return "baixo"
df["desempenho"] = df["nota"].apply(classificar_desempenho)
# print(df)

df = df.dropna (subset = ["nota"])

destaques = {} 

for _, linha in df.iterrows():
    if linha["nota"] >= 9:
        destaques[linha["id"]] = linha["nota"]

print(destaques)

print("-------------------------------------------------------------")

media_por_turno = {}
for turno in df["turno"].unique():
    media = df[df["turno"] == turno]["nota"].mean()
    media_por_turno[turno] = media

print("Media por turno:", media_por_turno)


orcamento = 20

while orcamento > 0:
    orcamenro -=5
    print ("gastei 5 reais")
