import time
import redis
import json

# koneksi ke redis container
r = redis.Redis(
    host='redis',
    port=6379,
    db=0,
    decode_responses=True
)

def get_weather(city):

    cache_key = f"weather:{city}"

    # =========================
    # CEK CACHE REDIS
    # =========================
    cached_data = r.get(cache_key)

    if cached_data:
        print("Data diambil dari CACHE Redis")
        return json.loads(cached_data)

    # =========================
    # CACHE MISS
    # =========================
    print("Data diambil dari API")

    # simulasi API lambat
    time.sleep(2)

    # simulasi response API
    weather_data = {
        "city": city,
        "temperature": 30,
        "condition": "Cerah"
    }

    # =========================
    # SIMPAN KE REDIS
    # =========================
    r.set(
        cache_key,
        json.dumps(weather_data),
        ex=300
    )

    return weather_data