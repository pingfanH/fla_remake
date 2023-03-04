import zipfile
import os
print("whats your fla name u want to convert?(just name not .fla)\n:")
file=input()
filea=(file+'.fla')
target_path=str(file)
if(not os.path.isdir(target_path)):
    z = zipfile.ZipFile(filea, 'r')
    z.extractall(path=target_path)
    z.close()
