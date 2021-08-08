"""
This class is responsible for handling requests from redemet API.
"""

import logging

import requests
import pandas as pd
import json
from collections import OrderedDict

class RedemetApi:

    def __init__(self, cfg, block=True):
        self.settings = cfg.get('redemet_api')
        self.block = block
        self.url_base = self.settings.get("api-redemet.decea.gov.br?api_key='ijmsgbzBb3muZ1ezLqJaKa9BVvO9D7roCrg01JVj")
        self.session = None
    
    def run_query(self, url="api-redemet.decea.gov.br?api_key='ijmsgbzBb3muZ1ezLqJaKa9BVvO9D7roCrg01JVj", output='', enforce=False, **kwargs):
        """
        Run a specific query from the APIs. It retrieves a text from the API REDEMET
        :param url: The API service URL, WITHOUT the base URL (i.e., it should start with "api/...").
        :param kwargs: Parameters to be used when filtering the query. They should be defined using the same parameter
        names and values used when calling this API manually.
        :return: A Text with the data retrieved.
        """
        # Add query params
        params = [localidades, data_ini, data_fim, page_tam]
        for k in kwargs:
            params.append('%s=%s' % (k, kwargs[k]))
        params_str = '?' + str.join('&', params)

        api_query_url = self.url_base + url + params_str

        print('Connecting to %s...' % api_query_url)
        try:
            self.session = requests.session()
            if self.block:
                r = self.session.get(api_query_url, timeout=10*60)
            else:
                r = self.session.get(api_query_url)
            if r.status_code != 200:
                print("It wasn't possible to connect to the provided URL: %s" % self._get_error(r))
                return

            response = r.text
            # This is a good point to create a log

            #Importar "logging" e criar logger (mensagens de debug, info, alerta, erro e crítica)
            
            logger = logging.getLogger(response)
            logger.setLevel(logging.DEBUG)

            logger.debug('Mensagem de debug')
            logger.info('Mensagem de informação')
            logger.warning('Mensagem de alerta')
            logger.error('Mensagem de erro')
            logger.critical('Mensagem crítica')
            

        except requests.exceptions.ReadTimeout:
            print('Connection timed out by user request. Proceeding without it.')
            return
        except:
            print('Unindentified error in running the request ' + url)
            if enforce:
                exit()
            return

    def close_session(self):
        self.session.close()
        print('Closed API session')
    
    def _get_error(self, request):
        try:
            return json.loads(request.text)['error']['message']
        except:
            return request.reason

    def _save_file(self, output_dir, output_data):
        with open(output_dir, mode='w') as f:
            f.write(output_data)
        f.close
    
