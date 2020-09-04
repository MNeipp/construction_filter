import csv
import os
import sys

csvFilePath = sys.argv[1]
noExtension = os.path.splitext(csvFilePath)[0]
csvOutPut = f'{noExtension}_filtered.csv'
data = []

# Convert to list of dictionaries
with open (csvFilePath, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        data.append(row)

myKeysOB = [
    'site_cnty',
    'site_juris',
    'site_city',
    'site_zip',
    'site_addrs',
    'pmt_descrp',
    'pmt_class',
    'pmt_value',
    'bldr_type',
    'bldr_first',
    'bldr_last',
    'bldr_pvtel',
    'bldr_st',
    'bldr_city',
    'bldr_state',
    'bldr_zip',
    'bldr_email'
]

# filter needed columns
filteredData = [{k:v for k,v in d.items() if k in myKeysOB} for d in data]
# filter by value in keys
counties = ['Utah County','Wasatch County', 'Summit County', 'Salt Lake County', ]
filteredData = [d for d in filteredData if d['site_cnty'] in counties]
print(len(filteredData))
filteredData = [d for d in filteredData if d['bldr_type'] == 'Owner-Builder']
print(len(filteredData))
# filter by those with phone or email
filteredData = [d for d in filteredData if len(d['bldr_pvtel']) > 0 or len(d['bldr_email']) > 0]
print(len(filteredData))

# Save new CSV file
with open(csvOutPut,'w', newline='') as f:
    csvwriter = csv.writer(f)
    count = 0
    for row in filteredData:
        if count == 0:
            header = row.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(row.values())