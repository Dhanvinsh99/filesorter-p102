import os
import shutil

source = "C:/Users/Admin/OneDrive - Nord Anglia Education/personal project/resources"
destination = "C:/Users/Admin/OneDrive - Nord Anglia Education/personal project/resources"

listofFiles = os.listdir(source)
print(listofFiles)

for i in listofFiles:
    name, extension = os.path.splitext(i)
    if extension == "":
        continue
    if extension in [".png", ".gif", ".jfif", ".jpg"]:
        path1 = source+ "/"+i
        path2 = destination+"/"+"imageS"
        path3 = destination+"/"+"imageS"+"/"+i
        if os.path.exists(path2):
            print("hello")
            shutil.move(path1, path3)
        else :
            os.makedirs(path2)
            print("wait")
            shutil.move(path1, path3)
    if extension in [".pdf", ".doc", ".docx", ".htm", ".html", ".dot", ".dotm", ".rtf", ".txt", ".docm"]:
        path1 = source+ "/"+i
        path2 = destination+"/"+"documentS"
        path3 = destination+"/"+"documentS"+"/"+i
        if os.path.exists(path2):
            print("hello")
            shutil.move(path1, path3)
        else :
            os.makedirs(path2)
            print("wait")
            shutil.move(path1, path3)

