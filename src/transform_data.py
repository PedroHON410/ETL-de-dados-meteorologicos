import pandas as pd 
from pathlib import Path
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

path_name = Path(__file__).parent.parent / 'data' / 'weather_data.json'

columns_names_to_drop = ['weather', 'weather_icon', 'sys.type'] 

columns_names_to_rename = {
        "base": "base",
        "visibility": "visibility",
        "dt": "datetime",
        "timezone": "timezone",
        "id": "city_id",
        "name": "city_name",
        "cod": "code",
        "coord.lon": "longitude",
        'coord.lat': 'latitude',
        'main.temp': 'temperature',
        'main.feels_like': 'feels_like',
        'main.temp_min': 'temp_min',
        'main.temp_max': 'temp_max',
        'main.pressure': 'pressure',
        'main.humidity': 'humidity',
        'wind.speed': 'wind_speed',
        'wind.deg': 'wind_deg',
        "wind.gust": "wind_gust",
        "clouds.all": "clouds",
        "sys.type": "sys_type",
        "sis.id": "sys_id",
        "sys.country": "sys_country",
        "sys.sunrise": "sys_sunrise",
        "sys.sunset": "sys_sunset"
    }

columns_to_normalize_datetime = ['datetime', 'sys_sunrise', 'sys_sunset']

def create_dataframe(path_name:str) -> pd.DataFrame:

    path = path_name

    if not path.exists():
        raise FileNotFoundError(f"O arquivo {path} não foi encontrado.")

    with open(path) as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    logging.info("DataFrame criado com sucesso.")
    return df

def normalize_weather_columns(df: pd.DataFrame) -> pd.DataFrame:
    df_weather = pd.json_normalize(df['weather'].apply(lambda x: x[0]))

    df_weather = df_weather.rename(columns={
        'id': 'weather_id',
        'main': 'weather_main',
        'description': 'weather_description',
        'icon': 'weather_icon'
    })

    df = pd.concat([df, df_weather], axis=1)
    logging.info("Colunas de clima normalizadas com sucesso.")
    return df

def drop_columns(df: pd.DataFrame, columns_names: list[str]) -> pd.DataFrame:
    df = df.drop(columns=columns_names)
    logging.info(f"Colunas {columns_names} removidas com sucesso.")
    return df

def rename_columns(df: pd.DataFrame, columns_names: dict[str, str]) -> pd.DataFrame:
    df = df.rename(columns=columns_names)
    logging.info("Colunas renomeadas com sucesso.")
    return df

def normalize_data_time_columns(df: pd.DataFrame, columns_names: list[str]) -> pd.DataFrame:
    for name in columns_names:
        df[name] = pd.to_datetime(df[name], unit='s', utc = True).dt.tz_convert('America/Sao_Paulo')
    logging.info("Colunas de tempo normalizadas com sucesso.")
    return df

def data_transformation():
    print("Iniciando transformação dos dados...")
    df = create_dataframe(path_name)
    df = normalize_weather_columns(df)
    df = drop_columns(df, columns_names_to_drop)
    df = rename_columns(df, columns_names_to_rename)
    df = normalize_data_time_columns(df, columns_to_normalize_datetime)
    logging.info("Transformação dos dados concluída com sucesso.")
    return df