# Pipeline de Dados Meteorológicos (ETL) com Airflow & Docker

Este projeto consiste em uma pipeline de dados (ETL) completa que extrai informações climáticas em tempo real de São Paulo através da API OpenWeather, processa esses dados e os armazena no banco de dados PostgreSQL para futuras análises.

## Tecnologias Utilizadas

*   **Linguagem:** Python 3.12+
*   **Orquestração:** Apache Airflow 3.1.7 (TaskFlow API)
*   **Containerização:** Docker & Docker Compose
*   **Banco de Dados:** PostgreSQL 16
*   **Manipulação de Dados:** Pandas & SQLAlchemy
*   **Gerenciador de Pacotes:** UV (gerenciador ultra-rápido de pacotes Python)

## Arquitetura do Projeto

O fluxo segue o modelo clássico de Engenharia de Dados:  

* **Extract:** Coleta de dados JSON da API OpenWeather.
* **Transform:** Limpeza dos dados, conversão de unidades (Kelvin para Celsius) e normalização de fusos horários (Timezones).

* **Load:** Armazenamento dos dados tratados em uma tabela estruturada no PostgreSQL.



## Configuração do Ambiente

### Pré-requisitos
*   Docker e Docker Compose instalados.
*   Conta na [OpenWeather](https://openweathermap.org/api) para obter uma API Key.
