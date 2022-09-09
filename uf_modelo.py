import datetime

import scrapy

from gazette.items import Gazette 
from gazette.spiders.base import BaseGazetteSpider


class <Uf><NomeDaCidade>Spider(BaseGazetteSpider):
    # você deve, manualmente, preencher as informações abaixo

    name = ""                       # (string)  <sigla_estado>_<nome_cidade>
    TERRITORY_ID = ""               # (string)  ID do IBGE para a cidade
    allowed_domains = [""]          # (lista de strings)    URL de apenas o domínio
    start_urls = [""]               # (lista de strings)    URL completa do endereço onde ficam os arquivos de Diários Oficiais
    start_date = datetime.date( )   # (int, int, int)   data do primeiro diário publicado. Formato: AAAA,M,D

    def parse(self, response):
        # desenvolver AQUI o código para que colete as informações que estão em yield.
        #
        # (sua hora de brilhar!)
        #
        #

        yield Gazette(
            # informações que queremos obter na raspagem 

            power= "",                      # (string) `executive` ou `executive_legislative` - preenchimento manual
            file_urls=[response.url],       # (response)
            date = ,                        # (datetime)   
            edition_number = "",            # (string)
            is_extra_edition =              # (bool)
        )