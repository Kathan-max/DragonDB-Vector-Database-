import ijson
import json
from decimal import Decimal
import io

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def process_item(item):
    print(item)

def process_large_json(fileName):
    cleaned_items = []
    output_fileName = "Data/Clean_image_Json_file.json"
    with open(fileName, 'rb') as infile, open(output_fileName, 'w') as outfile:
        outfile.write('[')
        first_item = True
        
        for item in ijson.items(infile, 'item'):
            if not first_item:
                outfile.write(',')
            else:
                first_item = False
            
            json.dump(item, outfile, cls=DecimalEncoder)
            
        outfile.write(']')
        
    # with open(output_fileName, 'w') as f:
    #     json.dump(cleaned_items, f,cls=DecimalEncoder)
            
        
# process_large_json("Data/plant_disease_embeddings.json")
def read_large(filename):
    with open(filename, 'rb') as f:
        for item in ijson.items(f, 'item'):
            print(item['name'])
            break

def class_feq(filename):
    class_df = {}
    with open(filename, 'rb') as f:     
        for item in ijson.items(f, 'item'):
            if item['name'] not in class_df:
                class_df[item['name']] = 1
            else:
                class_df[item['name']] += 1 
    print("Class Feq: ")
    print(json.dumps(class_df, indent=4))
if __name__ == "__main__":
    # read_large("Data/Trimmed_image_Json_file.json")
    class_feq("Data/Trimmed_image_Json_file.json")