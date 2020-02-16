import os
targetdir ='/Users/gyenana/PycharmProjects/python'


while True:
    if os.path.isdir(targetdir) == True :
        pathlist = os.listdir(targetdir)
        i=0
        while i < len(pathlist):
            newpath=targetdir+'/'+pathlist[i]
            if os.path.isdir(newpath) == True:
                result = newpath
                print("dirtype:",os.path.isdir(newpath),newpath)
            elif os.path.isdir(newpath)==False:
                print("filetype:",os.path.isfile(newpath),newpath)
            i+=1
        targetdir=newpath
    continue

