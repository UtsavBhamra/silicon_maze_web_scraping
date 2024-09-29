from bs4 import BeautifulSoup
import requests,csv

url_arr = ['https://www.screener.in/company/VOLTAS/consolidated/','https://www.screener.in/company/HAVELLS/consolidated/','https://www.screener.in/company/BLUESTARCO/consolidated/','https://www.screener.in/company/WHIRLPOOL/','https://www.screener.in/company/CROMPTON/consolidated/','https://www.screener.in/company/SYMPHONY/consolidated/','https://www.screener.in/company/ORIENTELEC/']


#task2

data = [
    {"Stock Name": "Voltas", "Year": 2024},
    {"Stock Name": "Havells", "Year": 2024},
    {"Stock Name": "Blue star", "Year": 2024},
    {"Stock Name": "Whirlpool", "Year": 2024},
    {"Stock Name": "Crompton", "Year": 2024},
    {"Stock Name": "Symphony", "Year": 2024},
    {"Stock Name": "Orient Electric", "Year": 2024}
]


for j in range(0,len(url_arr)):
    url = url_arr[j]
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')

    element = soup.find('section',id='balance-sheet')
    table_rows = element.find('table').find_all('tr')
    headings = ["Reserves","Borrowings","Total Liabilities","Fixed Assets","Investments","Total Assets"]
    ctr=0
    for i in range(1, len(table_rows)):
        if i==1 or i==4 or i==7 or i==9:
            continue 
        list = table_rows[i].find_all('td')
        data[j].update({headings[ctr]:list[-1].text})
        ctr = ctr+1



# Specify the CSV file to write to
csv_file = "output_t2.csv"

headers = data[0].keys()

# Write data to CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    
    # Write the header
    writer.writeheader()
    
    # Write the rows
    writer.writerows(data)

print(f"Data has been written to {csv_file}")









