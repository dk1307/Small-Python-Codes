import json
from difflib import get_close_matches #import important lib
#open different json files
with open("dictionary.json") as fin1:
    data1 = json.load(fin1)
with open("076 data.json") as fin2:
    data2 = json.load(fin2)
with open("dictionary_compact.json") as fin3:
    data3 = json.load(fin3)
#update also say merged all data to data1 file
data1.update(data2)
data1.update(data3)
#merged file data1 to new merged dump
with open("merged.json", "w") as fout:
    json.dump(data1, fout)
#load merged.json file
data = json.load(open("merged.json"))
#crate custom search function
def serch(w):
        d=w.lower()#all words to lower
        # if else conditons to check differnt conditions
        if d in data:
            return data[d]
        elif w.title() in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(d,data.keys())) > 0:
            yn=input("\nHEyy you nead enter %s instead enter Y if yes or N for no:" %get_close_matches(d,data.keys())[0])
            if yn == "Y" :
                return data[get_close_matches(d,data.keys())[0]]
            elif yn == "N" :
                return "Thank u for choosing me!!!!"
            else:
                return ("HEyy word not found,please double check")
        else:
            return ("HEyy word not found,please double check")
print("\nWelcome to My Customize Dictionary \n")
word=input("HEyy Enter the word you have to Search: ")#user input
op=serch(word)
if type(op) == list:
    for i in op:
        print("\n" + i)
else:
    print("\n"+ op)
