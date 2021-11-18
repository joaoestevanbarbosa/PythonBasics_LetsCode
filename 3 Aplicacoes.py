#Manipulação de Arquivos
arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8'); #abrindo em modo de leitura
texto = arquivo.read();
print(texto);
arquivo.close();

arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8');
linha = arquivo.readline();
while linha != '':
    print(linha, end='');
    linha = arquivo.readline();
arquivo.close();

arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8');
for linha in arquivo:
    print(linha, end='');
arquivo.close();

with open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read();
    print (texto);

with open('arquivo_teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Teste\n");
    arquivo.write("Teste2\n");
with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:
    print (arquivo.read(), end='');

with open('arquivo_teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Teste3\n");
with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:
    print (arquivo.read(), end='');


#Arquivo CSV
import csv;
with open('brasil_covid.csv', 'r', encoding='utf-8') as arquivoCSV:
    leitor = csv.reader(arquivoCSV);
    next(leitor);
    for linha in leitor:
        if float(linha[2])>1:
            print(linha);

with open('brasil_covid.csv', 'r') as csvFile:
    linhas = csvFile.read();
    linhas = linhas.split('\n');
    for linha in linhas:
        linha = linha.split(',');
        print(linha);

with open('users.csv','w', encoding='utf-8', newline='')  as arquivoUsers:
    escritor = csv.writer(arquivoUsers);
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero']);
    escritor.writerow(['Pietro', 'Riveito', 'pietro@email.com', 'M']);

header =['nome', 'sobrenome'];
dados = [];
opt = input("O que deseja fazer?\n1 - Cadastras \n0 - Sair\n")
while opt != '0':
    nome = input("Qual seu nome?");
    sobrenome = input("Qual seu sobrenome?");
    dados.append([nome, sobrenome]);
    opt = input("O que deseja fazer?\n1 - Cadastras \n0 - Sair\n")

print(dados);

with open('users.csv','w', encoding='utf-8', newline='')  as arquivoCSV:
    writer = csv.writer(arquivoCSV);
    writer.writerow(header);
    writer.writerow(dados);

with open('users.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',');
    for row in csvReader:
        print(row);



#APIs
!pip install requests
import requests
url = 'https://api.exchangerate-api.com/v6/latest';
req = requests.get(url);
print(req.status_code);

dados = req.json();
print(dados);

valorReais = float(input("Informe o valor em reais para conversao \n"));
cotacao = dados['rates']['BRL'];
print(f'R${valorReais} em dolar valem US${(valorReais/cotacao):.2f}');
