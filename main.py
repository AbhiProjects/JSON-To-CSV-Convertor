import FileConverter
import sys

if __name__=='__main__':

	if(len(sys.argv)==2):
		FileName=sys.argv[1]
		if(FileName.find('.')>0):
			FileName=FileName[:FileName.find('.')]
		FileConverter.main(FileName)
		
	else:
		print 'Please enter the details in the format given below'
		print 'python main.py JSONFILENAME'
		print
		raw_input('Press Enter To Exit.....')