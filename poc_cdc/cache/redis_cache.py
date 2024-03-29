import json

import redis
from config import REDIS_EXPIRE_TIME, REDIS_URL


class RedisCache:
    def __init__(self):
        # Conectar-se ao servidor Redis usando as variáveis do arquivo config.py
        self.redis_client = redis.Redis.from_url(REDIS_URL)
        self.expire_time = REDIS_EXPIRE_TIME

    def check_cache(self, key):
        return self.redis_client.exists(key)

    def set_cache(self, key, value):
        self.redis_client.setex(key, self.expire_time, value)

    def get_cache(self, key):
        cached_data = self.redis_client.get(key)
        if cached_data:
            return json.loads(
                cached_data.decode('utf-8')
            )  # Decodificar os dados JSON
        return None

    def cache_data(self, key, data):
        # Verificar se os dados já estão no cache
        if not self.check_cache(key):
            # Se não estiverem, armazenar os dados no cache
            self.set_cache(key, json.dumps(data))  # Codificar os dados JSON
        else:
            # Se os dados já estiverem no cache, verificar se o preço é diferente
            cached_data = self.get_cache(key)
            if (
                cached_data
                and 'id' in cached_data
                and cached_data['id'] == data.get('id')
                and cached_data.get('price_real') != data.get('price_real')
            ):
                # Se o preço for diferente, atualizar o cache com os novos dados
                self.set_cache(key, json.dumps(data))
