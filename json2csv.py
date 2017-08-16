# -*- coding: utf-8 -*-
import json, csv, argparse, time, datetime
import pandas as pd

def read_json(file_name):
    #Read josn file and parse json data
    f = open(file_name)
    json_data = json.load(f)
    f.close()
    return json_data

def to_csv(file_name,json_data):
    # Get all unique keys:
    all_keys = []
    for item in json_data:
        for m in item.keys():
            if m not in all_keys:
                all_keys.append(m)

    #Assign null value to missing keys
    for i in all_keys:
        for item in json_data:
            if i not in item.keys():
                item[i] = ''
    
    #Ceate csv file
    f = open(file_name,'w')
    csv_file = csv.writer(f)
    csv_file.writerow(json_data[0].keys())
    for i in json_data:
        csv_file.writerow(i.values())
    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Converts .json to .tde')
    parser.add_argument('-j',action='store', dest='jsonFileName', help='Name of the json file to be processed')
    parser.add_argument('-c', action='store', dest='csvFileName', help = 'Name of the csv file generated')
    parser_results = parser.parse_args()

    json_file = parser_results.jsonFileName
    csv_file = parser_results.csvFileName
    start_time = time.time()
    json_data = read_json(json_file)
    run_time = time.time()-start_time
    print "Reading JSON file...."
    to_csv(csv_file,json_data)
    print '%s file generated'%csv_file
    print 'It takes %s seconds'%run_time