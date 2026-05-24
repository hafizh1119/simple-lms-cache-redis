import time
from weather_api import get_weather

# =====================================
# FIRST CALL - should be slow (2 seconds)
# =====================================
start = time.time()

result1 = get_weather("Jakarta")

time1 = time.time() - start

print(f"\nFirst call: {time1:.2f}s")
print(result1)


# =====================================
# SECOND CALL - should be fast (< 0.1 second)
# =====================================
start = time.time()

result2 = get_weather("Jakarta")

time2 = time.time() - start

print(f"\nSecond call (cached): {time2:.2f}s")
print(result2)


# =====================================
# THIRD CALL - penjelasan tanpa perlu menunggu
# =====================================
print("\n--- Third Call (Penjelasan) ---")
print("Jika dipanggil setelah 5 menit (300 detik),")
print("cache sudah expired (TTL habis).")
print("Redis akan mengembalikan None,")
print("sehingga get_weather() akan memanggil API lagi")
print("dan response akan lambat (~2 detik) seperti First Call.")