import requests

def get_bingx_listings():
    url = "https://open-api.bingx.com/openApi/spot/v1/common/symbols"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [coin['symbol'] for coin in data['data']]
    return []

if __name__ == "__main__":
    listings = get_bingx_listings()
    print("BingX New Listings:", listings)
