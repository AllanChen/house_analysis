import json
import csv
import time
import codecs
if __name__ == '__main__':
    time_string = time.strftime("%Y%m%d", time.localtime())
    txt_name = time_string + "_hours.txt"
    json_name = time_string + "_hours.json"
    csv_name = time_string + "_hours.csv"
    data = ""
    with open(txt_name, 'r', encoding='utf-8') as file:
        data = file.read()
        
    data = "[" + data
    data = data + "]"
    data = data.replace(",]","]")
    json_save_name = time_string + "_hours.json"
    file = codecs.open(json_save_name, 'wb', 'utf-8')
    file.write(data)

    
    with open(json_name, 'r',encoding='utf-8') as f:
        data_json = json.load(f)
        f.close()
    
    with open(csv_name, 'w',newline='',encoding='utf-8') as file:
        csv_file = csv.writer(file)
        fieldnames = ['title', 'area','link','location','follow','totalPrice','unitPrice']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data_json:
            csv_file.writerow(
                [
                    item['title'],
                    item['area'],
                    item['link'],
                    item['location'],
                    # item['tag1'],
                    # # item['tag2'],
                    item['follow'],
                    item['totalPrice'],
                    item['unitPrice'],
                ])


