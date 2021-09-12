import csv
import random
import numpy as np
import pandas as pd

audiomothData = "Peru_2019_AudioMoth_Data_Full.csv"

def stratifyLayer1(readFile):
    #create a new csv for the first layer that is stratified
    with open('Layer1.csv', mode = 'w') as csvfile:
        csv_writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL ) 
        csv_writer.writerow(['AudioMothCode','AudioMoth ID','Source File','Directory','FileName','FileSize','Encoding','NumChannels','SampleRatee','AvgBytesPerSec','BitsPerSample','Start DateTime','Duration','Error','Comment','Artist','FileCrateDate','FileType','FileTypeExtension','MIMEType'])
        #parse through AudioMoth Data
        with open(readFile, 'r') as csvfile2:
            csv_reader = csv.reader(csvfile2)
            csv_headings = next(csv_reader)
            next(csvfile2)
            #only considers AudioMoth recordings that are at least 1 minute long
            for row in csv_reader:
                if("NA" not in row[12]):
                    if(float(row[12]) > 60):
                        csv_writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]])
def getID():
    #gets the names of all IDs
    AudioMothID = []
    with open('Layer1.csv','r') as csvfile:
        
        csv_reader = csv.reader(csvfile)
        csv_headings = next(csv_reader)
        next(csvfile)

        for row in csv_reader:
            if row[1] not in AudioMothID:
                AudioMothID.append(row[1])
    
    return AudioMothID

def stratifyLayer2():
    with open('Layer2.csv', mode = 'w') as csvfile:
        csv_writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        csv_writer.writerow(['AudioMoth ID','Start DateTime','Duration'])

        with open('Layer1.csv', 'r') as csvfile2:
            AudioMothID = getID()
            times = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
            csv_reader = csv.reader(csvfile2)
            csv_headings = next(csv_reader)
            next(csvfile2)
            
            #for row in csv_reader:
            

def stratifyData(audiomothData):
    stratifyLayer1(audiomothData)
    stratifyLayer2()

stratifyData(audiomothData)


    



