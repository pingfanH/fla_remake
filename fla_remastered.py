import zipfile
import os
import sys
import glob
import shutil
from glob import glob
from loading import progress_bar
from findmovie import linemovie
from copy_files import *
from zip_files import *
print("whats your fla name u want to remastered?(just name not .fla):")
file=input()

filename=file

if(not os.path.isfile(file+".fla")):
    print("\033[1;31m not a file called : \033[1;31m"+file+".fla")
    sys.exit(0)
print("exports name:")
exportname=input()
if(not os.path.isfile(file+".fla")):
    print("\033[1;31m not a exportname called : \033[1;31m"+exportname)
    sys.exit(0)
exportnamef=str(exportname)

if (not os.path.exists(exportnamef)):
    os.makedirs(exportnamef)
filea=(file+'.fla')
target_path=str(file)
if(not os.path.isdir(target_path)):
    z = zipfile.ZipFile(filea, 'r')
    z.extractall(path=target_path)
    z.close()
exportname=(file+'/LIBRARY/exports/'+exportname+'.xml')
print(exportname)
mycopyfile(filename+'/LIBRARY/exports/'+exportnamef+'.xml',exportnamef+'/LIBRARY/exports/')
os.makedirs(exportnamef+'/bin')
copyfold(filename+'/bin/',exportnamef+'/bin')
mycopyfile(filename+'/'+filename+'.xfl',exportnamef+'/')
mycopyfile(filename+'/'+'DOMDocument.xml',exportnamef+'/')
pathpng=(filename+'/LIBRARY/resources/')
pathxml=(filename+'/LIBRARY/shapes/')
path=(pathpng)

files = os.listdir(pathpng)
res=''
for file in files:
                file_path = os.path.join(path, file)

                os.path.isfile(file_path)
                print(file)
               
                mycopyfile(filename+'/LIBRARY/resources/'+file,exportnamef+'/LIBRARY/resources/')
path=(pathxml)
files = os.listdir(pathxml)
res=''
for file in files:
                file_path = os.path.join(path, file)

                os.path.isfile(file_path)
                print(file)
               
                mycopyfile(filename+'/LIBRARY/shapes/'+file,exportnamef+'/LIBRARY/shapes/')
file = open(str(exportname),'rb')
for line in file:
            line=str(line)
            if "movieclips/" in line:#如果movieclips/在这行，读取所有movieclips
                movie=line.split('"movieclips/')[1]
                movie=movie.replace('"','')
                movie=movie.replace('>','')
                movie=movie.replace('/','')
                movie=movie.replace("\\n","")
                movie=movie.replace("\n","")
                movie=movie.replace("'","")
                moviec=movie
                print(movie)
                mycopyfile(filename+'/LIBRARY/movieclips/'+movie+'.xml',exportnamef+'/LIBRARY/movieclips/')#movieclips路径
                file=str(file)
                shapesname=(filename+'/LIBRARY/movieclips/'+movie+'.xml')
                shapesname=str(shapesname)
                print(shapesname)#第一级的movieclips
                   
                if "movieclips/" in line:
                                file1 = open(str(shapesname))
                                line = str(line)
                                for line in file1:
                                    if ("movieclips/") in line:
                                        shapesname = line.split('"movieclips')[1]
                                        shapesname = shapesname.replace('"', '')
                                        shapesname = shapesname.replace('>', '')
                                        shapesname = shapesname.replace('/', '')
                                        shapesname = shapesname.replace("\\n", "")
                                        shapesname = shapesname.replace("\n", "")
                                        shapesname = shapesname.replace("'", "")
                                        print(shapesname)
                                        file2 = str(file)
                                        shapesname = (filename + '/LIBRARY/movieclips/' + shapesname + '.xml')
                                        mycopyfile(shapesname,exportnamef+'/LIBRARY/movieclips/')
                                        shapesname = str(shapesname)
                                        file2 = open(str(shapesname))
                                        print(shapesname)

print("Done!")
sys.exit(0)