import os
import shutil


current_dir = os.path.dirname(os.path.realpath(__file__))

print('Welcome in organize.py scripts - happy clean folder')

for filename in os.listdir(current_dir):

    ## organize images into Images folder
    if filename.endswith((".png",".jpg",".jpeg",".gif")):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename,"Images")
        os.remove(filename)
        print('Images Done')

    ## organize codes files into Codes folder
    if filename.endswith((".css",".html",".js","bash")):
        if not os.path.exists("Codes"):
            os.mkdir('Codes')
        shutil.copy(filename,"Codes")
        os.remove(filename)
        print('Codes Done')

    ## organize video files into Videos folder
    if filename.endswith((".mp4",".webm")):
        if not os.path.exists("Videos"):
            os.mkdir('Videos')
        shutil.copy(filename,"Videos")
        os.remove(filename)
        print('Videos Done')

    ## organize docs files into Documentes folder
    if filename.endswith((".pdf",".word")):
        if not os.path.exists("Docs"):
            os.mkdir('Docs')
        shutil.copy(filename,"Docs")
        os.remove(filename)
        print('Documentes Done')

    ## organize archive files into Archives folder
    if filename.endswith((".pdf",".word",".tar")):
        if not os.path.exists("Archives"):
            os.mkdir('Archives')
        shutil.copy(filename,"Archives")
        os.remove(filename)
        print('Archives Done')

    ## organize apps files into Apps folder
    if filename.endswith((".dmg",".exe")):
        if not os.path.exists("Apps"):
            os.mkdir('Apps')
        shutil.copy(filename,"Apps")
        os.remove(filename)
        print('Apps Done')

