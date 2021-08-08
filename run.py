from src.pipe.pipeline import Pipeline
import pandas as pd
from config.config import Config
import os

# Por algum motivo, o pip não instalou todas as dependências do projeto. 
# Como fazer isso sem precisar instalar um a um?

# Script
def main():
    pipeline = Pipeline('Insert An ICAO')
    settings = Config('./config/config.yml').get('settings')
    pipeline.Run(settings)


if __name__ == '__main__':
    main()