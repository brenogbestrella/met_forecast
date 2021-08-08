#from .cfg.config import Config
from .api import RedemetApi
#import pandas as pd
from threading import Thread
from time import time


class Pipeline:

    def __init__(self, icao):
        '''
            ICAO is an international code to identify an airport
            i.e: SBRJ - Rio de Janeiro Santos Dumont
            i.e2: SBSP - São Paulo Congonhas
        '''
        self.params = {'local': icao, 'msg': 'metar'}

    def Run(self, settings):

        #atribuir instância às variáveis?

        api = RedemetApi(settings)
        _settings = settings.get('foo bar')     
        _settings = _settings.get('methods')

        # It's better to use a decorator!

        # Decorator me parece um async-await em Python (executar algo após algo ser desenrolado)
        # Seria algo assim?

        def decorator(function):
            def wrapper():
                t0 = time()
                multiple_requests = [Thread(target = api.run_query ,  
                                            args = (value.get('end_point'), value.get('log_path')), 
                                            kwargs = { **self.params, **value.get('params') } )  
                                        for key, value in _settings.items()
                                    ]
        def other_function():
            for thr in multiple_requests :
                thr.start()

            for thr in multiple_requests :
                thr.join()
            api.close_session()

            print(f'Runtime {round(time() - t0)} seconds.')

        decorate_function = decorator(other_function)
        decorate_function()

