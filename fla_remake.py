import zipfile
import os
import sys
import glob
import shutil
from glob import glob
import re
from zipfile import ZipFile
import shutil


def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))
    
def mycopyfile(srcfile, dstpath):  # 复制函数
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.copy(srcfile, dstpath + fname)  # 复制文件

def copyfold(filePath,newFilePath):
    filename = os.listdir(filePath)
    for i in filename:
        shutil.copy(filePath + '/' + i, newFilePath + '/' + i)
    # 将filepath里面的所有图片拷贝到newfilepath里面
file=input("whats your fla name u want to remastered?(just name not .fla):")

filename=file

if(not os.path.isfile(file+".fla")):
    print("\033[1;31m not a file called : \033[1;31m"+file+".fla")
    sys.exit(0)
exportname=input("exports name:")
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
print("running...")
exportname=(file+'/LIBRARY/exports/'+exportname+'.xml')
#print(exportname)
mycopyfile(filename+'/LIBRARY/exports/'+exportnamef+'.xml',exportnamef+'/LIBRARY/exports/')
os.makedirs(exportnamef+'/bin')
copyfold(filename+'/bin/',exportnamef+'/bin')
mycopyfile(filename+'/'+filename+'.xfl',exportnamef+'/')
mycopyfile(filename+'/'+'DOMDocument.xml',exportnamef+'/')



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
                #print(movie)
                mycopyfile(filename+'/LIBRARY/movieclips/'+movie+'.xml',exportnamef+'/LIBRARY/movieclips/')#movieclips路径
                file=str(file)
                shapesname=(filename+'/LIBRARY/movieclips/'+movie+'.xml')
                shapesname=str(shapesname)
                #print(shapesname)#第一级的movieclips
                   
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
                                        #print(shapesname)
                                        file2 = str(file)
                                        shapesname = (filename + '/LIBRARY/movieclips/' + shapesname + '.xml')
                                        mycopyfile(shapesname,exportnamef+'/LIBRARY/movieclips/')
                                        shapesname = str(shapesname)
                                        shapesname1=shapesname
                                        file2 = open(str(shapesname))
                                        #print(shapesname)
                                        for line in file2:
                                            if ("movieclips/") in line:
                                                shapesname = line.split('"movieclips')[1]
                                                shapesname = shapesname.replace('"', '')
                                                shapesname = shapesname.replace('>', '')
                                                shapesname = shapesname.replace('/', '')
                                                shapesname = shapesname.replace("\\n", "")
                                                shapesname = shapesname.replace("\n", "")
                                                shapesname = shapesname.replace("'", "")
                                                #print(shapesname)
                                                file2 = str(file)
                                                shapesname = (filename + '/LIBRARY/movieclips/' + shapesname + '.xml')
                                                mycopyfile(shapesname,exportnamef+'/LIBRARY/movieclips/')
                                                shapesname = str(shapesname)
                                                shapesname3 = str(shapesname)
                                                #print(shapesname)
                
                                        
                                        file1 = open(str(shapesname1))
                                        line = str(line)
                                        for line in file1:
                                            if ("shapes/") in line:
                                                shapesname = line.split('"shapes')[1]
                                                shapesname = shapesname.replace('"', '')
                                                shapesname = shapesname.replace('>', '')
                                                shapesname = shapesname.replace('/', '')
                                                shapesname = shapesname.replace("\\n", "")
                                                shapesname = shapesname.replace("\n", "")
                                                shapesname = shapesname.replace("'", "")
                                                #print(shapesname)
                                                file2 = str(file)
                                                shapesname = (filename + '/LIBRARY/shapes/' + shapesname + '.xml')
                                                mycopyfile(shapesname,exportnamef+'/LIBRARY/shapes/')
                                                shapesname = str(shapesname)
                                                shapesnames = str(shapesname)
                                                file2 = open(str(shapesname))
                                                #print(shapesname)
                                                file4 = open(str(shapesnames))
                                                line = str(line)
                                                for line in file4:
                                                    if ("resources/") in line:
                                                        shapesname = line.split('"resources')[1]
                                                        shapesname = shapesname.replace('"', '')
                                                        shapesname = shapesname.replace('>', '')
                                                        shapesname = shapesname.replace('/', '')
                                                        shapesname = shapesname.replace("\\n", "")
                                                        shapesname = shapesname.replace("\n", "")
                                                        shapesname = shapesname.replace("'", "")
                                                        #print(shapesname)
                                                        file2 = str(file)
                                                        shapesname = (filename + '/LIBRARY/resources/' + shapesname + '.png')
                                                        mycopyfile(shapesname,exportnamef+'/LIBRARY/resources/')
                                                        shapesname = str(shapesname)
                                                        file2 = open(str(shapesname))
                                                        #print(shapesname)
                                        file3 = open(str(shapesname3))
                                        line = str(line)
                                        for line in file3:
                                            if ("shapes/") in line:
                                                shapesname = line.split('"shapes')[1]
                                                shapesname = shapesname.replace('"', '')
                                                shapesname = shapesname.replace('>', '')
                                                shapesname = shapesname.replace('/', '')
                                                shapesname = shapesname.replace("\\n", "")
                                                shapesname = shapesname.replace("\n", "")
                                                shapesname = shapesname.replace("'", "")
                                                #print(shapesname)
                                                file2 = str(file)
                                                shapesname = (filename + '/LIBRARY/shapes/' + shapesname + '.xml')
                                                mycopyfile(shapesname,exportnamef+'/LIBRARY/shapes/')
                                                shapesname = str(shapesname)
                                                shapesnamess = str(shapesname)
                                                file2 = open(str(shapesname))
                                                #print(shapesname)
                                                file5 = open(str(shapesnamess))
                                                line = str(line)
                                                for line in file5:
                                                    if ("resources/") in line:
                                                        shapesname = line.split('"resources')[1]
                                                        shapesname = shapesname.replace('"', '')
                                                        shapesname = shapesname.replace('>', '')
                                                        shapesname = shapesname.replace('/', '')
                                                        shapesname = shapesname.replace("\\n", "")
                                                        shapesname = shapesname.replace("\n", "")
                                                        shapesname = shapesname.replace("'", "")
                                                        #print(shapesname)
                                                        file2 = str(file)
                                                        shapesname = (filename + '/LIBRARY/resources/' + shapesname + '.png')
                                                        mycopyfile(shapesname,exportnamef+'/LIBRARY/resources/')
                                                        shapesname = str(shapesname)
                                                        file2 = open(str(shapesname))
                                                        #print(shapesname)
print("Creating...")
zip_folder(exportnamef,exportnamef+'.fla')


dele=str(os.path.abspath(os.curdir))
shutil.rmtree(dele+'\\'+exportnamef)

print("Done!")
sys.exit(0)