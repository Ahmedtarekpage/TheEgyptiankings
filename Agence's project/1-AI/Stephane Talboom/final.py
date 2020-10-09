import csv
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
import json
import pandas as pd
se=input("Enter the Word You Want to Search about: ")
print("If you requested full Data it will take along time and also you want to have a good internet connection because it's a big data ")
fi=int(input("enter 0 for 25 line from data and 1 for full data: "))
con_file = open("config.json")
config = json.load(con_file)
con_file.close()
client = ElsClient(config['apikey'])
doc_srch = ElsSearch(se,'sciencedirect')
doc_srch.execute(client, get_all =fi)
print ("doc_srch has", len(doc_srch.results), "results.")
df = pd.read_json (r'dump.json')
df = df[['load-date','dc:title','dc:creator','prism:publicationName']]
df.columns = ['Date','Title','Creator','Publication Name']
df.to_csv (r'output.csv', index = [])
csvFile = 'output.csv'
xmlFile = 'output.xml'
csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
xmlData.write('<csv_data>' + "\n")
rowNum = 0
csvData=csvData
for row in csvData:
    if rowNum == 0:
        tags = row
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        xmlData.write('<row>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</row>' + "\n")
    rowNum += 1
xmlData.write('</csv_data>' + "\n")
xmlData.close()
print(" if there is any Error in XML that means that wesite sent a wrong data in any Row")
print("YOu have to delete the output files Before running the Program again it can's Replace")
