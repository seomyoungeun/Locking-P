import zipfile
import os
import shutil

def zip(filename):
    path = os.getcwd() + '/' + filename 
    zipfs = path + '.zip'
    with zipfile.ZipFile(zipfs, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, path)
                zipf.write(file_path, arcname=arcname)
                
    shutil.rmtree(path)
    return filename + '.zip'       


