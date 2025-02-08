# Documentação do Projeto: Predição de Seguro de Saúde

## Sobre o Projeto
Este projeto é uma aplicação web desenvolvida com **Streamlit** que realiza a previsão do custo de seguros de saúde com base em quatro parâmetros fornecidos pelo usuário: idade, índice de massa corporal (BMI), número de filhos e status de fumante. O objetivo é demonstrar como modelos de machine learning podem ser integrados em uma interface web interativa e intuitiva.

O projeto utiliza um modelo de machine learning treinado com **scikit-learn** e foi projetado para ser fácil de usar tanto para previsões individuais quanto para previsões em lote (via upload de arquivos CSV).

---

## Estrutura do Projeto
A organização do projeto segue boas práticas para separar componentes e funcionalidades:

### Diretórios e Arquivos Principais:

```bash
project_root/
│── app/
│   ├── app.py  # Arquivo principal da aplicação
│
│── app_multipages/pages/
│   ├── Project_Description.py  # Apresentação do projeto
│   ├── 1_What_if_Prediction.py  # Previsões simuladas
│   ├── 2_File_Prediction.py  # Upload de CSV para previsões em lote
│
│── data/
│   ├── insurance.csv  # Arquivo de dados de exemplo
│
│── img/
│   ├── health_insurance_img.jpg
│   ├── stethoscope.png
│
│── models/
│   ├── model.pkl  # Modelo treinado
│
│── README.md  # Documentação do projeto
│── requirements.txt  # Lista de dependências
```

---

## Funcionalidades do Projeto

### 1. **Previsão Individual**
O usuário insere os seguintes parâmetros:
- Idade
- Índice de Massa Corporal (BMI)
- Número de filhos
- Status de fumante (Sim ou Não)

A aplicação utiliza o modelo carregado de `model.pkl` para prever o custo do seguro baseado nesses parâmetros.

### 2. **Previsão "What If"**
Permite ao usuário testar diferentes cenários modificando os valores manualmente e verificando como eles afetam o custo previsto do seguro.

### 3. **Previsão em Arquivo**
Os usuários podem enviar um arquivo CSV contendo múltiplas entradas. O sistema realiza previsões em lote e retorna um arquivo CSV com as previsões anexadas.

---

## Requisitos do Sistema
### Linguagem e Versões:
- **Python**: 3.8 ou superior

### Dependências:
Instale todas as dependências listadas no arquivo `requirements.txt` usando o comando:
```bash
pip install -r requirements.txt
```

Bibliotecas principais:
- **Streamlit**: Interface do usuário
- **Pandas**: Manipulação de dados
- **scikit-learn**: Modelo de machine learning

---

## Como Executar o Projeto

1. **Clone o Repositório**
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

2. **Configure o Ambiente Virtual**
Utilize `conda` para criar e ativar o ambiente virtual:
```bash
conda create -n stenv python=3.8
conda activate stenv
```

3. **Instale as Dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o Projeto**
```bash
streamlit run app/app.py
```

---

## Arquitetura dos Códigos

### **`app.py`**
Arquivo principal para previsão individual. Solicita os parâmetros do usuário e exibe o custo do seguro previsto:
```python
age = st.number_input(label='Age', value=18, min_value=18, max_value=120)
bmi = st.number_input(label='BMI', value=30.)
children = st.slider(label='Children', min_value=0, max_value=5)
smoker = st.selectbox(label='Smoker', options=['no','yes'])

with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def prediction():
    df_input = pd.DataFrame([{ 'age': age, 'bmi': bmi, 'children': children, 'smoker': smoker }])
    prediction = model.predict(df_input)[0]
    return prediction
```

### **`1_What_if_Prediction.py`**
Fornece uma interface para testar diferentes cenários modificando os valores de entrada e exibindo os resultados previstos.

### **`2_File_Prediction.py`**
Aceita um arquivo CSV para realizar previsões em lote. Retorna os resultados em um novo arquivo CSV que pode ser baixado:
```python
if data:
    df_input = pd.read_csv(data)
    insurance_prediction = model.predict(df_input)
    df_output = df_input.assign(prediction=insurance_prediction)

    st.download_button(
        label='Download CSV',
        data=df_output.to_csv(index=False).encode('utf-8'),
        mime='text/csv',
        file_name='predicted_insurance.csv'
    )
```

