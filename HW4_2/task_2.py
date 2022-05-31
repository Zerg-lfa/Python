import requests
import decimal


def currency_rates(currents='USD', url='http://www.cbr.ru/scripts/XML_daily.asp'):
    try:
        site = requests.get(url)
        site_date = site.headers.get('date')
        site_content = site.text
        cur = site_content.split(currents.upper())
        ind_cur = (cur[1].find('Value'))
        course = str(cur[1][ind_cur + 6:ind_cur + 13])
        course = course.replace(',', '.')
        course = decimal.Decimal(course)
        print(f'{course}, {site_date}')
    except:
        print(None)




currency_rates('usd')
currency_rates('eUr')



