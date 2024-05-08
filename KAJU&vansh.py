import requests
def get_geolocation(api_key, search_string):
    base_url = "https://us1.locationiq.com/v1/search"
    params = {
        'key': api_key,
        'q': search_string,
        'format': 'json', }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200 and data:
        result = {
            'place_id': data[0].get('place_id', ''),
            'lat': data[0].get('lat', ''),
            'lon': data[0].get('lon', ''),
            'display_name': data[0].get('display_name', ''), }
        return result
    else:
        print(f"Error: {response.status_code} - {data.get('error', 'No error message')}")
        return None
api_key = 'pk.fe4e5f616bed53d16cab70c821c4ae1a'
#api_key = 'pk.71c93f03731ac10faf75d7e071df51c1 '
search_string = input("Enter the location : ")
result = get_geolocation(api_key, search_string)
if result:
    print("Output:")
    for key, value in result.items():
        print(f"{key}: {value}")
