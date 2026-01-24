# Dados, Python e Estatística: Caminhos para STEM

Resumo
--------
- Durante o projeto adquiri conhecimento introdutório em dados, Python e estatística com um projeto final para demonstrar o que aprendi.

Objetivo
--------
- Fornecer uma introdução prática e aplicada a análise de dados com Python.
- Mostrar conceitos básicos de estatística descritiva e visualização.
- Estimular o interesse por carreiras em Ciência de Dados, Estatística e áreas correlatas (STEM).

Autores e Agradecimentos
------------------------
- Idealização e realização: Ana Júlia Amaro Pereira Rocha — graduanda em Ciência de Dados e IA, FGV-EMAp.
- Contribuição/apoio pedagógico: Ivone Alves de Azevedo — professora de matemática, Escola Estadual Hauy Petruceli Mayrink.
- Escola parceira: Escola Estadual Hauy Petruceli Mayrink, Santa Maria do Suaçuí, MG.

Conteúdo do repositório
-----------------------
- Notebooks Jupyter com exercícios e projetos (análises, visualizações e etapas de tratamento de dados).
- Um diretório `meuDataset/` com notebooks e análises sobre um dataset pessoal usado nos exercícios.
- Referências a arquivos CSV usados pelos notebooks; ver seção Dados e Observações.

Notebooks principais (descrição rápida)
--------------------------------------
- `atividade_6.ipynb` — Introdução ao Jupyter Notebook; leitura e exploração de um CSV (`dados_estudantes.csv`), limpeza básica, gráficos com Matplotlib/Seaborn.
- `projeto1.ipynb` — Projeto de análise: "Análise de uso de IA nas escolas". Leitura de CSV (`data/students_ai_usage.csv`), exploração, visualização e observações.
- `meuDataset/kleber_date.ipynb` — Notebook com análise exploratória detalhada de um dataset com colunas como `horas_celular`, `horas_sono`, `tempo_redes`, `tempo_estudo`, `nivel_concentracao`, `passos_dia`, entre outras.

Dados e observações sobre caminhos
---------------------------------
- Alguns notebooks leem arquivos CSV em caminhos relativos. Exemplos detectados:
  - `atividade_6.ipynb` lê `dados_estudantes.csv` (procure este arquivo na raiz do repositório ou ajuste o caminho conforme sua organização).
  - `projeto1.ipynb` lê `data/students_ai_usage.csv` (coloque o CSV dentro de um diretório `data/` ou ajuste o caminho no notebook).
- Confirme os caminhos dos arquivos nos notebooks antes de executar. Se os arquivos CSV não existirem no repositório, providencie-os localmente e adapte os caminhos.
- Recomendo criar uma pasta `data/` contendo os CSVs originais e uma pasta `outputs/` (opcional) para salvar figuras e versões processadas.

Como reproduzir (passo a passo)
-------------------------------
1. Pré-requisitos
   - Python 3.9+ (ou 3.8)
   - Jupyter Notebook ou JupyterLab
   - Pip

2. Instalar dependências (exemplo)
   - Crie e ative um ambiente virtual (recomendado):
     - python -m venv .venv
     - source .venv/bin/activate  (Linux/macOS) ou .venv\Scripts\activate (Windows)
   - Instale pacotes:
     - pip install pandas matplotlib seaborn numpy jupyter

   Sugestão de pacote (exemplo para um requirements.txt):
   ```
   pandas>=1.3
   numpy>=1.21
   matplotlib>=3.4
   seaborn>=0.11
   jupyter
   ```

3. Abrir os notebooks
   - jupyter notebook
   - ou jupyter lab
   - Navegue até os notebooks listados e execute as células sequencialmente.

4. Recomendações
   - Verifique e ajuste os caminhos para arquivos CSV nos notebooks (`pd.read_csv("caminho/arquivo.csv")`).
   - Execute as células de limpeza e visualização em ordem para evitar erros por variáveis não definidas.
   - Salve versões dos dados processados em `data/processed/` para rastreabilidade.

Estrutura proposta / desenho gráfico do repositório
---------------------------------------------------
Abaixo um diagrama em texto que representa a estrutura atual detectada no repositório e sugestões de organização para facilitar reprodução e manutenção.

```text
Caminhos-Para-STEM/
├── README.md                          # (arquivo que você está lendo)
├── atividade_6.ipynb                  # Notebook: introdução ao Jupyter + análise de "dados_estudantes.csv"
├── projeto1.ipynb                     # Notebook: "Analise de uso de IA nas escolas" (usa data/students_ai_usage.csv)
├── dados_estudantes.csv?              # (sugerido) CSV referenciado por atividade_6.ipynb — confirmar presença
├── data/                              # (sugerido) pasta para datasets
│   └── students_ai_usage.csv?         # CSV referenciado por projeto1.ipynb — confirmar presença
└── meuDataset/
    └── kleber_date.ipynb              # Notebook: análise exploratória e visualizações detalhadas
```

Observações:
- Itens marcados com `?` indicam arquivos referenciados nos notebooks que devem existir localmente. Caso não estejam no repositório, inclua-os em `data/` ou ajuste os caminhos dos notebooks.
- Recomendo padronizar a pasta `data/` para todos os datasets brutos e `notebooks/` caso deseje separar os notebooks em subpastas no futuro.

Boas práticas e próximas melhorias sugeridas
------------------------------------------
- Adicionar um `requirements.txt` com as versões mínimas dos pacotes usados.
- Incluir um pequeno script `setup.sh` ou `Makefile` para criar ambiente e instalar dependências.
- Normalizar os caminhos dos datasets para `data/` e atualizar os notebooks para usarem caminhos relativos padronizados.
- Adicionar um notebook de "00-setup.ipynb" com instruções de instalação e verificação de ambiente (checagem de pacotes e caminhos).
- Incluir um arquivo LICENSE se desejar definir termos de uso.

Contribuição
-----------
- Pull requests são bem-vindos. Para contribuições:
  1. Fork do repositório.
  2. Crie um branch com um nome descritivo: feature/nome-da-feature.
  3. Adicione testes ou notas explicando alterações nos notebooks.
  4. Abra um PR descrevendo a mudança e por que ela é útil.

Agradecimentos
--------------
Obrigado à Ana Júlia Amaro e à equipe da Escola Estadual Hauy Petruceli Mayrink pelo trabalho voluntário e apoio pedagógico.
