import httpx
import time

API_URL = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

def main():
    while True:
        start_time = time.time()
        response = httpx.get(API_URL)
        data = response.json()
        print(data["data"]["amount"])
        print(time.time() - start_time)
        time.sleep(1)


if __name__ == "__main__":
    main()
