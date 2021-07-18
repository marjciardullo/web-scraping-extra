# 💻 web-crawling-extra

Este é um projeto realizado para o processo seletivo da vaga de estágio em web crawling, oferecido pela empresa @Birdie. O projeto tinha como desafio a coleta de informações (*idSku, Nome do produto e Url*) de três categorias de produtos do site www.extra.com.br:

* 🖨️ Impressoras;
* 📺 Televisores;
* 🧊 Geladeiras.

Para fazer a coleta dessas informações foi usado o framework **Scrapy**, da linguagem **Python**. Utilizando esse framework, optei por criar três spiders, 1 para cada categoria. Com elas, foi possível colher informações de quase todos os produtos, localizados em uma API do extra - onde estavam as informações como *nome, marca, url* - e do ViaVarejo - onde estavam o *idSku do produto, preço, parcelamento e o id do lojista*.

## 📁 Criando novo projeto com o framework Scrapy

1. Abra o seu terminal e instale o Scrapy:

   ```$ pip install scrapy```

2. Com o Scrapy instalado, crie um novo projeto através do comando:

    ```$ scrapy startproject nomeDoProjeto```
    
 
### 🧮 Importando módulos necessários para o projeto

Dentro da página do seu projeto, importe os seguintes módulos:

1. Módulo Json:

   ```import json```

2. Módulo Math:
   
   ```import math```

## 👩‍💻 Processo de Desenvolvimento do Código

Durante a análise da página, que pode ser considerada bem dinâmica, por conta do uso de Javascript em diversos elementos da página, localizei 2 responses interessantes ao clicar no botão "ver mais produtos":

![tempsnip](https://user-images.githubusercontent.com/82274021/126075819-0fa7a689-c990-4df2-a2e8-8db9a6206d81.jpg)

Na segunda url, pude perceber que havia a alteração de uma pequena informação conforme eu fui analisando a paginação desse link oferecido:

![tempsnipasssas](https://user-images.githubusercontent.com/82274021/126076573-ee1efca9-a18b-455f-b3b1-c24b74349100.jpg)

Diante dessa informação, constatei que, em cada página, haviam dados de apenas 20 produtos e o número total de produtos daquela categoria específica. Portanto, com essas informações valiosas, coletei o número total e dividi pelo número de produtos por página, o que resultou em um número total de páginas que eu deveria realizar um crawl.

   * *Para fazer um arredondamento do resultado dessa divisão, é recomendável utilizar a biblioteca math.*

Dentro dessa url, e após a coleta da maior parte de informações sugeridas, percebi que, para coletar as informações restantes (localizadas na 1ª response na primeira imagem acima), eu precisava apenas coletar o Id dos produtos da página e juntá-los à nova Url:

![asjduasd](https://user-images.githubusercontent.com/82274021/126077162-bc56ee8e-0efd-4995-9ef7-5d27d08adcb4.jpg)

Após a solução elaborada em relação à paginação, coletei a maior parte de informações possíveis e salvei em csv através do comando:

   ```scrapy crawl nomeDaSpider -o nome-Do-Arquivo.csv```










