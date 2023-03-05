import zipfile
import os
import sys
from loading import progress_bar
from findmovie import linemovie
print("whats your fla name u want to remastered?(just name not .fla):")
file=input()
filename=file
if(not os.path.isfile(file+".fla")):
    print("\033[1;31m not a file called : \033[1;31m"+file+".fla")
    sys.exit(0)
print("exports name:")
exportname=input()
filea=(file+'.fla')
target_path=str(file)
if(not os.path.isdir(target_path)):
    z = zipfile.ZipFile(filea, 'r')
    z.extractall(path=target_path)
    z.close()
exportname=(file+'/LIBRARY/exports/'+exportname+'.xml')
print(exportname)
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
                file=str(file)
                shapesname=(filename+'/LIBRARY/movieclips/'+movie+'.xml')
                shapesname=str(shapesname)
                print(shapesname)
                file1 = open(str(shapesname),'rb')
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
                            file2 = str(file)
                            shapesname = (filename + '/LIBRARY/shapes/' + movie + '.xml')
                            shapesname = str(shapesname)
                            file1 = open(str(shapesname), 'rb')
                            print(shapesname)
                            for line in file1:
                                line = str(line)
                                if "resources/" in line:
                                    movie = line.split('"resources/')[1]
                                    movie = movie.replace('"', '')
                                    movie = movie.replace('>', '')
                                    movie = movie.replace('/', '')
                                    movie = movie.replace("\\n", "")
                                    movie = movie.replace("'", "")
                                    movie=(movie+".png")
                                    print(movie)