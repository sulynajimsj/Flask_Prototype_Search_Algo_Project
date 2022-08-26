import os



#list file names 
def list_file_name(path):
    fileList = os.listdir(path)
    return(fileList)

def inputImages(allfiles):
    allurls = []



allFiles = list_file_name("frames")

