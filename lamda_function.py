import requests
import json

def lambda_handler(event, context):
    # NYC coordinates
    latitude = '40.71427'
    longitude = '-74.00597'
    
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&temperature_unit=fahrenheit"
    request = requests.get(api_url)
    json_object = json.loads(request.text)
    current_temp = json_object['current_weather']['temperature']
    print(f"Current temperature {current_temp} degrees fahrenheit")
    
    return {
        'statusCode' : 200,
        'body' : json.dumps(f"Current NYC temperature is {current_temp} degrees fahrenheit")
    }
    
if __name__ == "__main__":
    lambda_handler('','')