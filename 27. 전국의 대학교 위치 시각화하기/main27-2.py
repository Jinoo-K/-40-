import requests

url = 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type = 'ROAD'
road_type2 = 'PARCEL'
address = '&address='
keys = '&key='
primary_key = ''

def request_geo(road):
    page = requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data = page.json()
    if json_data['response']['status'] == 'OK' :
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x, y
    else : 
        x = 0
        y = 0
        return x, y
    
x, y = request_geo('경상남도 창원시 의창구 창원대학로 20 (사림동, 창원대학교)')

print(f'x값 : {x}')
print(f'y값 : {y}')