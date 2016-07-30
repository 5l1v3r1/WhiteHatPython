import os, zipfile

# get the current path and lis of the files and folders
currecnt_directory = os.curdir
myfile_list = os.listdir(currecnt_directory)
# make a progressbar:
prgress_bar = len(myfile_list)
print(prgress_bar, "items\r\n ")
# create a new zip file
newzipfile = zipfile.ZipFile("newzipfie.zip", "w")


# add files and folders into the zipfile
def time_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        t1 = time.clock()
        func(*args)
        t2 = time.clock()
        print("{name} : {time:10.10f}".format(name=func.__name__, time=t2 - t1))

    return wrapper


@time_decorator
def ziping_func(myfiles, newzip, directory):
    i = 1
    for item in myfile_list:
        newzip.write(directory + "\\" + item)
        print(i, )
        i += 1
    # close the zip file
    newzip.close()


ziping_func(myfile_list, newzipfile, currecnt_directory)
