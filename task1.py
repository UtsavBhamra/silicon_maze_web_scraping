from bs4 import BeautifulSoup
import requests,csv

url_arr = ['https://www.screener.in/company/VOLTAS/consolidated/','https://www.screener.in/company/HAVELLS/consolidated/','https://www.screener.in/company/BLUESTARCO/consolidated/','https://www.screener.in/company/WHIRLPOOL/','https://www.screener.in/company/CROMPTON/consolidated/','https://www.screener.in/company/SYMPHONY/consolidated/','https://www.screener.in/company/ORIENTELEC/']


#task1
power_stats_arr = [ {"Stock Name":"Voltas",},
                    {"Stock Name":"Havells",},
                    {"Stock Name":"Blue star",},
                    {"Stock Name":"Whirpool",},
                    {"Stock Name":"Crompton",},
                    {"Stock Name":"Symphony",},
                    {"Stock Name":"Orient Electric",},
                       ]

for j in range(0,len(url_arr)):
    url = url_arr[j]
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    power_stats = soup.find_all('li',class_='flex flex-space-between')
    heading_arr = ["market_cap","current price","stock p/e","roce","roe"]
    ctr=0
    for i in range(0,len(power_stats)):
        if i==2 or i==4 or i==5 or i==8:
            continue
        stat = power_stats[i].find_all('span')
        power_stats_arr[j].update({heading_arr[ctr]:stat[1].find('span').text})
        ctr = ctr+1



# Specify the CSV file to write to
csv_file = "output_t1.csv"

headers = power_stats_arr[0].keys()

# Write data to CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    
    # Write the header
    writer.writeheader()
    
    # Write the rows
    writer.writerows(power_stats_arr)

print(f"Data has been written to {csv_file}")