import requests
print(requests,"req")
city_name=input("enter city:-- ")
API_key="e6befd9343605d6128b1d84ca44570ce"
api_name=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
result=requests.get(api_name)
print(type(api_name),"req")

if result.status_code==200:
    result=result.json()
    print(type(result),"req")
    # result=result.get(result)
    print(result)   
    print(result['sys']['country'])
    print(result.get(id,77777))
    # print(result['city'])
    