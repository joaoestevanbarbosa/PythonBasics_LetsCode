import request as r
url = 'https://api.covid19api.com/dayone/country/brazil';
resp = r.get(url);
resp.status_code;

rawData = resp.json();
rawData[0];

finalData = []
for obs in rawData:
    finalData.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']]);

finalData.insert(0,['confirmados', 'obitos','recuperados','ativos','data']);
finalData;

for i in range(1, len(finalData)):
    finalData[i][DATA] = finalData[i][DATA][:10];

import datetime as dt
print(dt.time(12,6,21,7), 'h:min:s:ms');
print('-----');
print(dt.datetime(2020,4,25), 'Ano-mês-dia');
print('-----');
print(dt.datetime(2020, 4, 25, 12, 6, 21, 7), 'Ano-mês-dia h:min:s:ms')

natal = dt.date(2021,12,25);
reveillon = dt.date(2021,1,1);

print((reveillon - natal));
print((reveillon - natal).days);
print((reveillon - natal).seconds);
print((reveillon - natal).microseconds);

import csv
with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file);
    writer.writerow((finalData));

for i in range(1, len(finalData)):
    finalData[i][DATA] = dt.datetime.strptime((finalData[i][DATA], '%Y-%m-%d'));

def getDatasets(y,labels):
    if type(y[0]) == list:
        datasets = [];
        for i in range (len(y)):
            datasets.append({
                'label':labels[i],
                'data': y[i]
            });
        return datasets;
    else:
        return [
            {
                'label':labels[0],
                'data': y
            }
        ];

def setTitle (title=''):
    if title != '':
        display ='true';
    else:
        display = 'false';
    return {
        'title': title,
        'display': display
    };

def creatChart(x,y,labels,kind='bar',title=''):
    datasets = getDatasets(y,labels);
    options = setTitle(title);

    chart ={
        'type': kind,
        'data' : {
            'labels': x,
            'datasets': datasets
        },
        'options': 'options'
    }
    return chart;

def getAPIChart(chart):
    urlBase = 'https://quickchart.io/chart';
    resp = r.get(f'{urlBase}?c={str(chart)}');
    return resp.content;

def saveImage(path, content):
    with open(path,'wb') as image:
        image.write(content);

from PIL import Image;
from IPython.display import display;

def displayImage(path):
    imgPil = Image.open(path);
    display(imgPil);

yData1 = [];
for obs in finalData[1::10]:
    yData1.append(obs[CONFIRMADORS]);

yData2 = [];
for obs in finalData[1::10]:
    yData2.append(obs[RECUPERADOS]);

labels = ['Confirmados', 'Recuperados'];

x=[];
for obs in finalData[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'));

chart = creatChart(x, [yData1,yData2], labels, title="Gráfico confirmados vs recuperados")
chatContent = getAPIChart((chart));
saveImage('meu-primeiro-grafico.png', chatContent);
displayImage('meu-primeiro-grafico.png');

from urllib.parse import quote
def getAPIQRCode(link):
    text = quote(link) #parsing do link para url
    urlBase = 'https://quiclchart.io/qr';
    resp = r.get(f'{urlBase}?text={text}');
    return resp.content;

urlBase = 'https://quickchart.io/chart';
link = f'{urlBase}?c={str(chart)}';
getAPIQRCode(link);
saveImage('qr-cod-png', getAPIQRCode(link));
displayImage('qr-cod-png');