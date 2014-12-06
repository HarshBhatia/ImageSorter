import exifread
import os
import sys
import calendar
import shutil

def main():
	srcpath = str(sys.argv[1])
	dstpath = str(sys.argv[2])
	get_filepaths(srcpath)
	sort(srcpath,dstpath)

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths 

def sort(srcpath,dstpath):
	i=0
	for file in get_filepaths(srcpath):
		i=i+1
		f = open(str(file),'rb')
		tags = exifread.process_file(f)
		#print str(tags['Image DateTime'])+'\n'	
		newpath = dstpath+'/'+str(tags['Image DateTime'])[:4]+'/'+calendar.month_name[int(str(tags['Image DateTime'])[5:7])]
		if not os.path.exists(newpath): os.makedirs(newpath)
		shutil.copyfile(str(file),newpath+'/'+'File'+str(i)+'.jpg')
	sys.exit(1)

if __name__ == '__main__':
  main()
