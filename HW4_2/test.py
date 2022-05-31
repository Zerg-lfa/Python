import requests
import xmltodict

def currency_rates(current):
    site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    site = xmltodict.parse(site)
    for i in site['ValCurs']['Valute']:
        if i['CharCode'] == current.upper():
            print(i['Value'])
    print(None)


currency_rates('usd')