import random
import ijson
import json
from Json_Reader import DecimalEncoder

def dataTrimer(filename, class_percent, outputFileName):
    with open(filename, 'rb') as f:
        class_df = {}
        for item in ijson.items(f, 'item'):
            if item['name'] not in class_df:
                class_df[item['name']] = 1
            else:
                class_df[item['name']] += 1
    
    counter_df = {}
    for key, val in class_df.items():
        counter_df[key] = int((class_percent/100)*(val))
    print("Counter Df: ") 
    print(json.dumps(counter_df, indent=4))  
    print("Starting Trimer")
    with open(filename, 'rb') as infile, open(outputFileName, 'w') as outputFile:
        first_item = True
        outputFile.write('[')
        ignored_items = {}
        for item in ijson.items(infile, 'item'):
            if counter_df[item['name']] != 0:
                rn = random.randint(1,1000)
                if(rn%2 == 0):
                    counter_df[item['name']] -= 1
                    if not first_item:
                        outputFile.write(',')
                    else:
                        first_item = False
                    json.dump(item, outputFile, cls=DecimalEncoder)
                else:
                    if item['name'] not in ignored_items:
                        ignored_items[item['name']] = [item]
                    else:
                        ignored_items[item['name']].append(item)
        for key, val in counter_df.items():
            if val != 0:
                ignored_items[key] = random.sample(ignored_items[key], val)
                for item in ignored_items[key]:
                    outputFile.write(',')
                    json.dump(item, outputFile, cls=DecimalEncoder)
        outputFile.write(']')    
    

if __name__ == "__main__": 
    dataTrimer("Data/Clean_image_Json_file.json", 10, "Data/Trimmed_image_Json_file.json")
    