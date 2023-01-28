
# from setuptools.command.config import config
from distutils.command.config import config
from xml.etree.ElementTree import tostring
import pdfkit
import os

# set destinations
src_root = '<root location of files>'        
dest_root = 'destination of files'            # target folder



def convert_files_to_pdf (src_dir, dest_dir):
    # install wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    files = os.listdir(src_dir)  
    for _file_name_ in files:

        if '.html' in _file_name_:
            src_file = src_dir + "/" + _file_name_
            _file_name_ = _file_name_.replace(".html", "")
            dest_file = dest_dir + "/" + _file_name_+".pdf"
            # print("[" + src_file + " -> " + dest_file + "]")
            pdfkit.from_file(src_file, dest_file,  verbose= True, options={"enable-local-file-access": True}, configuration= config)
            # os.remove(src_file) 



parent_dir = os.walk(src_root)
for (root,dirs,files) in parent_dir:
    for dir in dirs:
        print(dir)
        print (os.path.exists(os.path.join(dest_root,dir)))
        associative_folder = dir + "PDF"
        src_sub_dir = os.path.join(src_root, dir)
        dest_sub_dir = os.path.join(dest_root, associative_folder)
        if not (os.path.exists(dest_sub_dir)):
            os.makedirs(dest_sub_dir)
            # os.mkdir(dest_sub_dir)
#         print(os.path.join(root, dir))
        convert_files_to_pdf(src_sub_dir, dest_sub_dir)


