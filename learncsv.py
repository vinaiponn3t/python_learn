# ต้องใส่ encodeing='utf-8'ใน open 
import csv
def read_csv():
    with open('crma_com.csv','r',encoding='utf-8') as f:
        data = csv.reader(f,delimiter=',')
        print(type(data))  
        print(data)
        for row in data:
            print(row)
        
read_csv()