#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#tipos de variáveis


# In[11]:


print("hello world");


# In[5]:


int x = -10;


# In[10]:


print (x);


# In[13]:


print(type(x));


# In[18]:


preco = 19.99;
print(preco);
print(type(preco));
#não dá pra escrever o tipo da variável antes de declarar;


# In[20]:


cidade = "São Paulo";
print(cidade, type(cidade));


# In[21]:


disponivel = True;
print(disponivel, type(disponivel));


# In[ ]:


#operadores


# In[22]:


x = 50;
y = 2;


# In[23]:


print(x+y);
print(x*y);
print(x-y);
print(x/y);


# In[25]:


print(x**y); #exponencial
print(x//y); #divisao inteira sem arrendondamento
print(x%y); #pega o resto


# In[26]:


temCafe = True;
temPao = False;


# In[28]:


print(not temCafe);
print(temCafe or temPao);
print(temCafe and temPao);


# In[1]:


dolar = 5.4;
real = 1;
print(dolar > real);
print(dolar < real);
print(dolar == real);
print(dolar >= real);
print(dolar <= real);
print(dolar != real); #diferente


# In[ ]:


#estruturas sequenciais


# In[2]:


idade = input ("Informe sua idade: ");
print(idade, type(idade));


# In[3]:


idade = int(idade);
print(idade, type(idade));


# In[ ]:


int('123abc'); #vai dar erro por causa do abc


# In[6]:


print(float('123.25'));
print(str(123.25));
print(bool(''));
print(bool('abc'));
print(bool(0));
print(bool(-2));


# In[7]:


salarioMensal = input("Digite o valor do seu salário mensal: ");
salarioMensal = float(salarioMensal);

gastoMensal = input("Digite o valor do seu gasto mensal em média: ");
gastoMensal = float(gastoMensal);

salarioTotal = salarioMensal * 12;
gastoTotal = gastoMensal * 12;

montanteEconomizado = salarioTotal - gastoTotal;
print("O montante que você pode economizar ao fim do ano é de", montanteEconomizado);


# In[ ]:


#estruturas condicionais


# In[10]:


valorPassagem = 4.3;

valorCorrida = input ("Qual é o valor da corrida? ");

if float(valorCorrida) <= valorPassagem * 5:
    print("Pague a corrida");
if float(valorCorrida) > valorPassagem * 5:
    print("Pegue um busão");


# In[11]:


valorPassagem = 4.3;

valorCorrida = input("Qual é o valor da corrida? ");

if float(valorCorrida) <= valorPassagem * 5:
    print("Pague a corrida");
if float(valorCorrida) > valorPassagem * 5:
    print("Pegue um busão");


# In[17]:


valorPassagem = 4.3;

valorCorrida = input("Qual é o valor da corrida? ");

if float(valorCorrida) <= valorPassagem * 5:
    print("Pague a corrida");
else:
    if float(valorCorrida) <= valorPassagem * 6:
        print("Aguarde um momento, o valor pode abaixar");
    else: 
        print("Pegue um busão");


# In[18]:


valorPassagem = 4.3;

valorCorrida = input("Qual é o valor da corrida? ");

if float(valorCorrida) <= valorPassagem * 5:
    print("Pague a corrida");
elif float(valorCorrida) <= valorPassagem * 6:
    print("Aguarde um momento, o valor pode abaixar");
else: 
    print("Pegue um busão");


# In[ ]:


#estruturas de repetição - while


# In[21]:


contador = 0;

while contador < 10:
    contador = contador + 1;
    if contador ==1:
        print(contador, "item limpo");
    else:
            print(contador, "itens limpos");
            
print("Fim da repetição do bloco while");


# In[23]:


contador = 0;

while True:
    if contador <=10:
        contador = contador + 1;
        if contador == 1:
            print(contador,"item limpo");
        else:
            print(contador,"itens limpos");
    else: 
        break; 
        
print("Fim da repetição do bloco while");


# In[1]:


texto = input ("Digite a sua senha: ");

while texto != "LetsCode":
    texto = input("senha inválida, tente novamente ");
    
print("Acesso permitido ");


# In[2]:


contador = 0;

while contador < 10:
    contador = contador + 1;
    if contador ==1:
        continue
    else:
        print(contador, "itens limpos");
            
print("Fim da repetição do bloco while");


# In[ ]:




