<h1 align="center">🤔 Motivação </h1>

Ao baixar o dataset diretamente da plataforma [Open Data SUS](https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao/resource/10aed154-04c8-4cf4-b78a-8f0fa1bc5af4), o mesmo pode vir com algumas células incoerentes.
Tal fato ocasiona um bug quando o pandas lê o arquivo csv e encontra
mais de um valor para a mesma célula. Para corrigir esse erro, basta realizar a seguinte sequência de passos no Mac OS e Linux:

### ⬇️ Download
Através do terminal, baixe o dataset através do seguinte comando:

    wget https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SIPNI/COVID/uf/uf%3DPB/part-00002-d09bb2f4-b1a1-427d-b409-3ba40f2c980f.c000.csv

### 📝 Altere o nome do arquivo
Renomeie o arquivo .csv que acabou de baixar para __dados_vacinacao.csv__

### ➗ Dividindo o arquivo .csv
O dataset possui quase 3 milhões de linhas sendo que o limite de leitura dos programas *Microsoft Office Excel* e *LibreOffice Calc* é de 1.048.576 linhas.
Dessa forma é inviável corrigir uma célula que esteja localizada além do limite de linhas desses programas

* Quebrando o csv em arquivos menores:

      split -l 1048576 dados_vacinacao.csv 

### 📝 Altere os nomes dos arquivos
O comando da linha anterior gerou 3 novos arquivos a partir do dataset original, respectivamente __xaa__, __xab__ e  __xac__, 
agora iremos chamá-los __pb1.csv__, __pb2.csv__ e __pb3.csv__

### Verificando qual(is) célula(s) apresenta(m) mais de um valor:
Abra sua IDE preferida ou o terminal na pasta onde os 3 arquivos descritos no passo anterior estão localizados e execute o seguinte código Python,
onde N se refere ao índice do fragmento do dataset original

```python
import pandas as pd
df = pd.read_csv('pbN.csv')
print(df)
```
### ✅ Corrigindo a célula que possui mais de um valor
Ao executar o código do passo anterior, você receberá o seguinte erro como saída:<br>

`ParserError: Error tokenizing data. C error: Expected 1 fields in line XXXXX, saw 2`

Na qual a linha da célula com erro é apontadada no lugar da sequência de 'X' e X é úm número.<br>

Então, utilizando seu programa de edição e visualização de planilhas, basta acessar célula *AXXXXX* e em seguida corrigir a célula que possui 2 valores.

### 💡 Concatenando os 3 datasets gerados
Após corrigir as linhas problemáticas em cada um dos datasets, é hora de juntá-los para formar um único arquivo.<br>
Basta executar o seguinte comando no terminal:

    cat pb1.csv pb2.csv pb3.csv > dados_vacinacao.csv
    
### 🔷 Considerações finais
Pronto, agora o dataset baixado da plataforma Open Data SUS pode ser lido sem nenhum problema pela biblioteca `pandas` do Python.

