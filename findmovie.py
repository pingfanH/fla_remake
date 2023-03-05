import re
def linemovie(export):
    file = open(r(export),'rb')

    for line in file:
            line=str(line)
            if "movieclips/" in line:
                movie=line.split('"movieclips/')[1]
                movie=movie.replace('"','')
                movie=movie.replace('>','')
                movie=movie.replace('/','')
                movie=movie.replace("\\n","")
                movie=movie.replace("'","")
                print (movie)