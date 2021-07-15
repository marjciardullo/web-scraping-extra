import scrapy
import json
import pandas as pd


class ScrapingItem(scrapy.Spider):
    name = "scrapData"
    allowed_domains = ['prd-api-partner.viavarejo.com.br']

    def start_requests(self):
        urls = []

        data_list = ['https://prd-api-partner.viavarejo.com.br/api/search?resultsPerPage=100&' +
                     'terms=tv&page=2&salesChannel=desktop&apiKey=extra',
                     'https://prd-api-partner.viavarejo.com.br/api/search?resultsPerPage=100&terms=impressoras&page=2&salesChannel=desktop&apiKey=extra',
                     'https://prd-api-partner.viavarejo.com.br/api/search?resultsPerPage=100&terms=refrigeradores&page=2&salesChannel=desktop&apiKey=extra']

        for link in data_list:
            urls.append(link)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        jsonOBj = json.loads(response.body)
        ref = []
        tv = []
        imp = []
        for data in jsonOBj['products']:
            for item in data['categories']:
                if item['name'] == 'Refrigeradores':
                    refrigeradores = {
                        'IDSKU': data['details']['IdSkuPadrao'][0],
                        'TÍTULO': data['name'],
                        'PREÇO': data['price'],
                        'PREÇO ANTIGO': data['oldPrice'],
                        'MARCA': data['details']['marca'][0],
                        'PESO': data['details']['peso'][0],
                        'STATUS': data['status'],
                        'URL': data['url']
                    }
                    ref.append(refrigeradores)

                    # Transformando o dicionário em Dataframe:
                    df = pd.DataFrame(ref)

                    # Salvando o arquivo em Xlsx (excel):
                    df.to_excel('refrigeradores.xlsx')

                elif item['name'] == 'Televisores':
                    televisores = {
                        'IDSKU': data['details']['IdSkuPadrao'][0],
                        'TÍTULO': data['name'],
                        'PREÇO': data['price'],
                        'PREÇO ANTIGO': data['oldPrice'],
                        'MARCA': data['details']['marca'][0],
                        'PESO': data['details']['peso'][0],
                        'STATUS': data['status'],
                        'URL': data['url']
                    }
                    tv.append(televisores)

                    # Transformando o dicionário em Dataframe:
                    df2 = pd.DataFrame(tv)

                    # Salvando o arquivo em Xlsx (excel):
                    df2.to_excel('televisores.xlsx')

                elif item['name'] == 'Informática':
                    impressoras = {
                        'IDSKU': data['details']['IdSkuPadrao'][0],
                        'TÍTULO': data['name'],
                        'PREÇO': data['price'],
                        'PREÇO ANTIGO': data['oldPrice'],
                        'MARCA': data['details']['marca'][0],
                        'PESO': data['details']['peso'][0],
                        'STATUS': data['status'],
                        'URL': data['url']
                    }
                    imp.append(impressoras)

                    # Transformando o dicionário em Dataframe:
                    df3 = pd.DataFrame(imp)

                    # Salvando o arquivo em Xlsx (excel):
                    df3.to_excel('impressoras.xlsx')
