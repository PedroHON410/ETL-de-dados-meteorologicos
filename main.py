# from src.extract_data import extract_weather_data
# from src.transform_data import data_transformation
# from src.load_data import load_weather_data
# import os
# from pathlib import Path
# from dotenv import load_dotenv
# import logging


# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
# load_dotenv(env_path)

# API_KEY = os.getenv('API_KEY')

# url = f'http://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={API_KEY}'
# table_name = 'sp_weather'

# def pipeline():
#     try:

#         logging.info("ETAPA 1: Extração de dados")
#         extract_weather_data(url)

#         logging.info("ETAPA 2: Transformação de dados")
#         df = data_transformation()

#         logging.info("ETAPA 3: Carga de dados")
#         load_weather_data(table_name, df)

#         print("Pipeline executada com sucesso!")

#     except Exception as e:
#         logging.error(f"Erro na execução da pipeline: {e}")
#         import traceback
#         traceback.print_exc()

# pipeline()