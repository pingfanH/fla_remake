import zipfile
import os
from loading import progress_bar
from findmovie import linemovie
print("whats your fla name u want to remastered?(just name not .fla):")
file=input()
print("exports name:")
exportname=input()
filea=(file+'.fla')
target_path=str(file)
if(not os.path.isdir(target_path)):
    z = zipfile.ZipFile(filea, 'r')
    z.extractall(path=target_path)
    z.close()
exportname=(file+'\LIBRARY\exports\\'+exportname+'.xml')
print(exportname)
shapesname=(file+'\LIBRARY\shapes\.xml')
file = open(str(exportname),'rb')
for line in file:
            line=str(line)
            if "movieclips/" in line:
                movie=line.split('"movieclips/')[1]
                movie=movie.replace('"','')
                movie=movie.replace('>','')
                movie=movie.replace('/','')
                movie=movie.replace("\\n","")
                movie=movie.replace("'","")
                print(movie)
                file.close()
                shapesname=(file+r'\LIBRARY\shapes\\'+movie+'.xml')
                shapesname=str(shapesname)
                print(shapesname)
                file1 = open(str(shapesname),'rb')
                print(file1)
                for line in file1:
                        line=str(line)
                        if "shapes/"in line:
                            movie=line.split('"shapes/')[1]
                            movie=movie.replace('"','')
                            movie=movie.replace('>','')
                            movie=movie.replace('/','')
                            movie=movie.replace("\\n","")
                            movie=movie.replace("'","")
                            print(movie)