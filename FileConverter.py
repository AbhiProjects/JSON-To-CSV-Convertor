import csv
import json
import sys

def JsonRead(FileName):
	try:
		f=open(FileName,'r')
		data=json.loads(f.read())
		f.close()
	except:
		print 'JSON File Read Error.'
	return data

def CsvWriter(FileName,Data):
	try:
		f=open(FileName,'ab+')
		csvWriter = csv.writer(f)
		csvWriter.writerow( Data )
		f.close()
	except:
		print 'CSV File Read Error.'

def CreateFile(FileName):
	try:
		f=open(FileName,'w')
		f.close()
	except:
		print 'CSV File Creation Error.'
	
def KeyStoreGenerator(lst):
	keyStore=[]
	for dict in lst:
		for key in dict:
			keyStore.append(key)
	return set(keyStore)
	
def flatten_dict(d):
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict(value).items():
                    yield key + "." + subkey, subvalue
            else:
                yield key, value

    return dict(items())

def main(FileName):
	
	try:
		print 'File Conversion Started'
		
		lst=[]
		
		CreateFile(FileName+'.csv')		
		Data=JsonRead(FileName+'.json')
		templst=Data['results']
		
		for item in templst:
			lst.append(flatten_dict(item))
		
		keyStore=KeyStoreGenerator(lst)
		keyStore=sorted(keyStore)
		CsvWriter(FileName+'.csv',keyStore)

		for i in xrange(len(lst)):
			row=[]
			d=lst[i]
			for key in keyStore:
				row.append(str(d.get(key,'No Data')))				
			CsvWriter(FileName+'.csv',row)
		
		print 'File Conversion Ended'
		
	except:
		
		print
		print(sys.exc_info())
		print
		print 'An error has occured while processing the file.'
		print 'If the JSON File is open,please close the file and try again.'
		print 'If the error still presists one can contact me at my email address abhishek.chawla@outlook.com or skype chawla_abhishek.'
	
	print
	raw_input('Press Enter To Exit.....')
	return