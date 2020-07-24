#Load the data
import pandas as pd
import csv
import os
import xml.etree.ElementTree
import json
#from google.colab import drive
#drive.mount('/content/gdrive')

path_folder ="C:/Users/mudasirw/Desktop/RESEARCH @N T N U -JULY 2019/PAN datasets/pan12-sexual-predator-identification-training-corpus-2012-05-01"
print(path_folder)

import json
print('tes')
i=0
for line in open(path_folder+'negative_conv.json', 'r'):
  i=i+1
  if(i>64900):
    print(i)
  #print(line)
  data = json.loads(line)
  #for p in data['msg']:
    #print(p['text'])
  data2=""
  for p in data['msg']:
    #print(p['text'])
    if(p['text']):
      data2=data2+" "+p['author']+":"+p['text'].replace('\r', '').replace('\n', '')
  #print(data2)
  with open(path_folder+'predator-victim_conversations_text.csv', 'a') as csvFile:
      writer = csv.writer(csvFile)
      writer.writerow(['1',[data2]])
    
  #print(data2)