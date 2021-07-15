# web-scraping-extra
Web Scraping realizado no site www.extra.com.br. O desafio, oferecido pela empresa Birdie durante o processo seletivo de estágio em Web Crawling, consistia em raspar os dados dos produtos das categorias: impressoras, televisores e refrigeradores. Durante a análise do funcionamento do website, foram encontradas "responses" que seriam úteis para a detecção de arquivos com os dados dos produtos. Em uma dessas "responses", encontrei o link da API do ViaVarejo, grupo de onde o Extra faz parte.

Com o link da API, utilizei o framework Scrapy do Python para realizar a raspagem dos links de forma mais eficaz e para, futuramente, automatizar o processo de coleta dos dados. Utilizei, também, o módulo JSON do python e a biblioteca Pandas, que auxilia na parte da criação de dataframes, ótimos para fazer uma boa manipulação de tabelas e informações.

Com as ferramentas utilizadas, consegui fazer o scrap de 100 produtos de cada categoria. Porém, irei implementar novos códigos para trabalhar a paginação.

*Todos os resultados foram importados em forma de uma planilha excel(xlsx).

