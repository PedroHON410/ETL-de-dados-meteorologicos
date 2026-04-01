from datetime import datetime, timedelta

from airflow.decorators import task, dag
from pathlib import Path
import sys, os

sys.path.insert(0, '/opt/airflow/src')

from extract_data import extract_weather_data
from load_data import load_weather_data
from transform_data import data_transformation
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

API_KEY = os.getenv('API_KEY')
url = f'http://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={API_KEY}'

@dag(
    dag_id="projeto_pipeline_weather",
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5),
    }, # <--- VÍRGULA AQUI
    description="Pipeline de ETL para dados meteorológicos de São Paulo",
    schedule='0 */1 * * *', # <--- VÍRGULA AQUI
    start_date=datetime(2026, 3, 31),
    catchup=False,
    tags=['weather', 'ETL', 'openweathermap']
) # <--- SEM VÍRGULA AQUI NO FECHAMENTO

def weather_pipeline():

    @task
    def extract():
        data = extract_weather_data(url)
    
    @task
    def transform():
        df = data_transformation()
        df.to_parquet('/opt/airflow/data/weather_data.parquet', index=False)

    @task
    def load():
        import pandas as pd
        df = pd.read_parquet('/opt/airflow/data/weather_data.parquet')
        load_weather_data('sp_weather', df)
    

    extract() >> transform() >> load()

weather_pipeline()