import scrapy
import json
import math


class ScrapingImp(scrapy.Spider):
    name = "impressoras"
    allowed_domains = ['extra.com.br', 'npreco.api-extra.com.br']
    

    # Começamos com a página número zero apenas para dar um parse de forma eficaz e coletar a quantidade total de produtos.

    start_urls = ['https://www.extra.com.br/api/catalogo-ssr/products/?RegistrosPorPagina=20&Platform=1&Filtro=c56_c61&PaginaAtual={}'.format(0)]

    def parse(self, response):       
        jsonObj = json.loads(response.body)
        
        # Coletando as informações da quantidade de produtos:

        f = jsonObj.get('filters', [])
        v = f[0].get('values')
        s = v[0].get('size')
        
        

        # Aplicando o número de páginas obtido na URL:

        for i in range(1, math.ceil(s // 20) +1):
            urls_start = 'https://www.extra.com.br/api/catalogo-ssr/products/?RegistrosPorPagina=20&Platform=1&Filtro=c56_c61&PaginaAtual={}'.format(i)
            yield scrapy.Request(urls_start, callback=self.parse_ref)


    # Coletando informações do produto e construindo mais um parse para a coleta dos Skus

    def parse_ref(self, response):
        impObj = json.loads(response.body)
        url_list = []

        for data in impObj.get('products', []):
            imps = {
            'nome': data['name'],
            'marca': data['brand']['name'],
            'url': data['urls'],
            }

            rid = data.get('id')

            url = 'https://npreco.api-extra.com.br/Produtos/PrecoVenda?IdsProduto={}'.format(rid)

            url_list.append(url)

        for i in url_list:
            yield scrapy.Request(url=i, meta=imps,callback=self.parse_id)
        

    # Coletando os Skus dos produtos:

    def parse_id(self, response):
        impressoras = response.meta
        idsJson = json.loads(response.body)

        for value in idsJson.get('PrecoProdutos', []):
            newinfos = {
            'sku': value['PrecoVenda']['IdSku'],
            'IdLojista': value['PrecoVenda']['IdLojista'],
            'Preço': value['PrecoVenda']['Preco'],
            'Parcelamento': value['PrecoVenda']['Parcelamento']
            }
        impressoras.update(newinfos)
       

        yield impressoras

        
    






























