# 💻 web-crawling-extra

Este é um projeto realizado para o processo seletivo da vaga de estágio em web crawling, oferecido pela empresa @Birdie. O projeto tinha como desafio a coleta de informações (*idSku, Nome do produto e Url*) de três categorias de produtos do site www.extra.com.br:

* 🖨️ Impressoras;
* 📺 Televisores;
* 🧊 Geladeiras.

Para fazer a coleta dessas informações foi usado o framework **Scrapy**, da linguagem **Python**. Utilizando esse framework, optei por criar três spiders, 1 para cada categoria. Com elas, foi possível colher informações de quase todos os produtos, localizados em uma API do extra - onde estavam as informações como *nome, marca, url* - e do ViaVarejo - onde estavam o *idSku do produto, preço, parcelamento e o id do lojista*.

## Criando novo projeto com o framework Scrapy

1. Abra o seu terminal e instale o Scrapy:

   ```$ pip install scrapy```

2. Com o Scrapy instalado, crie um novo projeto através do comando:

    ```$ scrapy startproject nomeDoProjeto```
 

## 👩‍💻 Processo de Desenvolvimento do Código

Durante a análise da página, que pode ser considerada bem dinâmica, por conta do uso de Javascript em diversos elementos da página, localizei 2 responses interessantes ao clicar no botão "ver mais produtos":

![tempsnip](https://user-images.githubusercontent.com/82274021/126075819-0fa7a689-c990-4df2-a2e8-8db9a6206d81.jpg)






