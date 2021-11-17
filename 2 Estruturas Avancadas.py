#listas e tuplas
nomesPaises =["Brasil", "Argentina", "China", "Canadá", "Japão"];
print(nomesPaises);

print("Tamanho da lista: ", len(nomesPaises));

print("País: ", nomesPaises[4]);
print("Páis: ", nomesPaises[-1]);

nomesPaises[4] = "Colômbia";
print("País: ", nomesPaises[4]);
print(nomesPaises);

print(nomesPaises[1:3]);
print(nomesPaises[1:-1]);
print(nomesPaises[2:]);
print(nomesPaises[:3]);
print(nomesPaises[:]);
print(nomesPaises[::2]);
print(nomesPaises[::-1]);

print("Brasil" in nomesPaises);
print("Canadá" not in nomesPaises);


listaCapitais = [];
listaCapitais.append("Brasília");
listaCapitais.append("Buenos Aires");
listaCapitais.append("Pequim");
listaCapitais.append("Bogotá");
print(listaCapitais);

listaCapitais.insert(2, "Paris");
print(listaCapitais);

listaCapitais.remove("Buenos Aires");
print(listaCapitais);

removido = listaCapitais.pop(2);
print(listaCapitais, removido);

nomesPaises = ("Brasil", "Argentina", "China", "Canadá", "Japão");
print(type(nomesPaises));

nomeEstado = "São Paulo";
print(type(nomeEstado));

print(len(nomesPaises));

b, c, a, ca, j = nomesPaises;
print(b, c, j);

print(*nomesPaises);


#Strings I
frase = "O prof disse: \"Aleluia irmãos\"";
print(frase);

empresa = "Google";
print(empresa[0]);
print(empresa[:3]);

nomeCidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasilia";
nomesCidades = nomeCidades.split((', '));
print(nomesCidades);

cabecalho = "     Menu Principal";
print(cabecalho.strip());

nomeCidade = "rIo DE JaneIRO";

print(nomeCidade.title()); #todas as iniciais
print(nomeCidade.capitalize()); #primeira letra
print(nomeCidade.lower()); #tudo minusculo
print(nomeCidade.upper()); #tudo maiusculo

#nomeCidade = input("Que cidade do Brasil é conhecida como cidade maravilhosa? ");
#nomeCidade = nomeCidade.strip();
#while nomeCidade.lower() != 'rio de janeiro':
    #print("Tenta de novo");
    #nomeCidade = input("Que cidade do Brasil é conhecida como cidade maravilhosa? ");

#print("Conseguiu champs");

mensagem = "Você viu o que o Pietro disse na sala ontem?";
fuiCitado = "Pietro" in mensagem;
print(fuiCitado);


## Strings II
cumprimento = "olá, ";
nome = "Felipe";
print(cumprimento + nome);
print(nome*5);

nome = 'Felipe';
idade = 35;
nFilhos = 2;
print(nome + " tem " + str(idade) + " anos e " + str(nFilhos) + " filhos.");
print('{} tem {} anos e {} filhos.'.format(nome, idade, nFilhos));
print(f'{nome} tem {idade} anos e {nFilhos} filhos');

preçoGasolina = 3.476;
print("O preço da gasolina hoje subiu e está em R$ {:.2f}", preçoGasolina);



#Dicionários
dadosCidade = {
    'nome': "São Paulo",
    "estado": "São Paulo",
    "area": 1521,
    "populacaoMilhoes": 12.15,
};
print(type(dadosCidade));
print(dadosCidade);

dadosCidade["país"] = "Brasil";
print(dadosCidade);

print(dadosCidade['nome']);

dadosCidade["area"] = 1500;
print(dadosCidade);

dadosCidade2 = dadosCidade;
dadosCidade2["nome"] = "Santos"
print(dadosCidade);
print(dadosCidade2);

dadosCidade3 = dadosCidade.copy();
dadosCidade3["estado"] = "Rio de Janeiro";
print(dadosCidade3);
print(dadosCidade);

novosDados = {
    "nome": "São Paulo",
    "populacaoMilhoes": 15,
    "fundacao": "25/01/1554",
};

dadosCidade.update(novosDados);
print(dadosCidade);

print(dadosCidade.get("prefeito"));

print(dadosCidade.keys()); #retorna uma lista de chaves de um dicionario
print("-----");
print(dadosCidade.values()); #retorna uma lista de valores de um dicionario
print("-----");
print(dadosCidade.items()); #retorna uma lista de tuplas (chave, valor) de um dicionario
print("-----");


#Estruturas de Repetição - FOR
nomesCidades = ["São Paulo", "londres", "Tóquio", "Paris"];
for nome in nomesCidades:
    print(nome);

contador = 0;
nomesCidades = ["São Paulo", "londres", "Tóquio", "Paris"];
while contador < len(nomesCidades):
    print(nomesCidades[contador])
    contador = contador + 1;

nomesCidades = ["São Paulo", "londres", "Tóquio", "Paris"];
for nome in nomesCidades:
    print(nome);

cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacaoMilhoes': 12.2
};
for chave in cidade:
    print(f'{chave}: {cidade[chave]}')

nomesCidades = ["São Paulo", "londres", "Tóquio", "Paris"];
for nome in nomesCidades:
    nome = "Rio de Janeiro";
print(nomesCidades);

for posicao in range(len(nomesCidades)):
    nomesCidades[posicao] = "Rio de Janeiro";
print(nomesCidades);

print(list(range(10)));
print(list(range(2,10)));
print(list(range(2,10,2)));


#Funcoes I
def hello():
    print("Olá mundo");

hello();

def calculaMedia(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3;
    media = soma/3;
    return media;

print(calculaMedia(10, 5, 3));

resultado2 = calculaMedia(valor1 =9, valor2=10, valor3=7);
print(resultado2);

def calculaMedia(valor1 = 3, valor2 = 5, valor3 = 7):
    soma = valor1 + valor2 + valor3;
    media = soma/3;
    return media;

print(calculaMedia());


#Funçoes II
def calculaMedia(*args, margem):
    soma = sum(args);
    media = soma/len(args);
    return media;

print(calculaMedia (10,9,8,7, margem=0.3));

def printInfo(**kwargs):
    print(kwargs, type(kwargs))

printInfo(nome="Pietro", sobrenome="Pinheiro")


