"""
File: webcrawler.py
Name:
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

        response = requests.get(url,headers=headers)

        html = response.text
        soup = BeautifulSoup(html,'html.parser')

        # ----- Write your code below this line ----- #
        tables = soup.find_all('table', class_='t-stripe')
        if tables:
            male_total = 0
            female_total = 0
            if len(tables) > 0:
                rows = tables[0].find_all('tr')
                for row in rows:
                    columns = row.find_all('td')  # find all the columns (td) in the current row
                    if len(columns) > 4:  # ensure that there are enough columns in the row
                        male_total += int(columns[2].text.replace(',', ''))    # replace commas (,) with an empty string ('')
                        female_total += int(columns[4].text.replace(',', ''))

            # print the totals for the current year
            print(f"Male Number: {male_total}")
            print(f"Female Number: {female_total}")

        else:
            print("Table not found for the year:", year)


if __name__ == '__main__':
    main()
