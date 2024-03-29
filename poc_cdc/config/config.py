import os

from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv('DATABASE_URI')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DATABASE_URI = os.getenv('PRODUCTION_DATABASE_URI')


# Mapeia as configurações com os ambientes
config_by_name = dict(
    development=DevelopmentConfig, production=ProductionConfig
)

# Função para retornar a configuração de acordo com o ambiente
def get_config(env_name):
    return config_by_name[env_name]
