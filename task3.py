from bs4 import BeautifulSoup
import requests
import csv

url_arr = ['https://www.screener.in/company/VOLTAS/consolidated/','https://www.screener.in/company/HAVELLS/consolidated/','https://www.screener.in/company/BLUESTARCO/consolidated/','https://www.screener.in/company/WHIRLPOOL/','https://www.screener.in/company/CROMPTON/consolidated/','https://www.screener.in/company/SYMPHONY/consolidated/','https://www.screener.in/company/ORIENTELEC/']


#task3

data = [
    {"Stock Name": "Voltas", "Year": 2022},
    {"Stock Name": "Voltas", "Year": 2023},
    {"Stock Name": "Voltas", "Year": 2024},
    {"Stock Name": "Havells", "Year": 2022},
    {"Stock Name": "Havells", "Year": 2023},
    {"Stock Name": "Havells", "Year": 2024},
    {"Stock Name": "Blue star", "Year": 2022},
    {"Stock Name": "Blue star", "Year": 2023},
    {"Stock Name": "Blue star", "Year": 2024},
    {"Stock Name": "Whirlpool", "Year": 2022},
    {"Stock Name": "Whirlpool", "Year": 2023},
    {"Stock Name": "Whirlpool", "Year": 2024},
    {"Stock Name": "Crompton", "Year": 2022},
    {"Stock Name": "Crompton", "Year": 2023},
    {"Stock Name": "Crompton", "Year": 2024},
    {"Stock Name": "Symphony", "Year": 2022},
    {"Stock Name": "Symphony", "Year": 2023},
    {"Stock Name": "Symphony", "Year": 2024},
    {"Stock Name": "Orient Electric", "Year": 2022},
    {"Stock Name": "Orient Electric", "Year": 2023},
    {"Stock Name": "Orient Electric", "Year": 2024}
]


for j in range(0,len(url_arr)):
    url = url_arr[j]
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    pandl_rows = soup.find('section',id='profit-loss').find('table').find('tbody').find_all('tr')
    headings = ["Sales","OPM","Net profit","EPS"]
    ctr=0
    for i in range(0,len(pandl_rows)):
        if i==0 or i==3 or i==9 or i==10:
            row = pandl_rows[i].find_all('td')
            data[3*j].update({headings[ctr]:row[-4].text})
            data[3*j+1].update({headings[ctr]:row[-3].text})
            data[3*j+2].update({headings[ctr]:row[-2].text})
            ctr=ctr+1
        else:
            continue

# Specify the CSV file to write to
csv_file = "output_t3.csv"

headers = data[0].keys()

# Write data to CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    
    # Write the header
    writer.writeheader()
    
    # Write the rows
    writer.writerows(data)

print(f"Data has been written to {csv_file}")