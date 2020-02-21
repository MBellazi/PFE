import pytesseract  ####reading string from image (OCR library)
import  numpy as np ##numpy for shape
import cv2   #Computer vision library
import shutil
import PyPDF2
import subprocess
import os    ##for remove image file which we edit during procedure
import pyodbc
import json
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

###you need to install ocr and give path in program


def create4(conn):
  print("Create")
  cursor = conn.cursor()
  cursor.execute(
    'insert into Cv(id_cv,id_candidat) values(?,?);',
    (3,3)
  )

def create3(conn):
  print("Create")
  cursor = conn.cursor()
  cursor.execute(
    'insert into Candiats(id_candidat,id_cv,nom,prenom) values(?,?,?,?);',
    (3,3,'Bejaoui','Mimi')
  )



def read(conn):
  print("read")
  cursor = conn.cursor()
  cursor.execute("select * from Candiats")
  for row in cursor:
    print(f'row = {row}')
    print('test')
  print()

def read2(conn):
  print("read")
  cursor = conn.cursor()
  cursor.execute("select * from Cv")
  for row in cursor:
    print(f'row = {row}')
    print('test')
  print()

conn = pyodbc.connect(
"Driver={SQL Server Native Client 11.0};"
"Server=.;"
"Database=CurriculumVitae;"
"Trusted_Connection=yes;")

conn.commit()
create4(conn)
create3(conn)
read2(conn)
read(conn)

def Conversion_Cv(filename):
  
  try:

    #**********   Extraire le text d'un jpg ***************
      print("               *****...........   JPG   ............****                  ")
      folder_path = "C:\\Users\\asus\\Desktop\\Optical_Character_Reccognition-master"
    
      for filename in os.listdir(folder_path):
        
        if filename.endswith('.jpg'):
          print("**  Nom du fichier : ",filename)
          print('Editing image for better OCR result..........')
          img = cv2.imread(filename)  ###reading image
          img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
          kernel = np.ones((1, 1), np.uint8)
          img = cv2.dilate(img, kernel, iterations=1)
          img = cv2.erode(img, kernel, iterations=1)
          new_image = 'edited'+'_'+filename  ###new image which we save during procedure
          cv2.imwrite(new_image, img)  ###Save a new edited image
          read = pytesseract.image_to_string(new_image)  ####reading from new generated image
          print(read)  ##print resuult
          print("extracting text from page : ", read)
          file_ = open('edited_'+"%s.txt" % filename.split('.')[0], "w")
          file_.write(read)
          file_.close()

        elif filename.endswith('.pdf'):   
          print("PDF Name : ",filename)   
          # creating a pdf file object
          pdfFileObj = open(filename, 'rb')

          # creating a pdf reader object
          pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict = False)

          # printing number of pages in pdf file
          print("printing number of pages in pdf file : ", pdfReader.numPages)

          # creating a page object
          pageObj = pdfReader.getPage(0)

          extrait = pageObj.extractText()
          # extracting text from page
          print("extracting text from page : ", extrait)
          file_ = open('edited_'+"%s.txt" % filename.split('.')[0], "w")
          file_.write(extrait)
          file_.close()
          pdfFileObj.close()
          # dictionary where the lines from 
          # text will be stored 

      JPEG_DIR_SOURCE = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master'
      JPEG_DEST_DIR = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master/Ancien_Jpeg'
      Nouvext = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master/Nouv_CV_Text'
      PDF_DEST_Nouv = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master/Ancien_PDF'
      for pname in os.listdir(JPEG_DIR_SOURCE):
        if pname.startswith('edited') and pname.endswith('.txt'):
          shutil.move(os.path.join(JPEG_DIR_SOURCE, pname), Nouvext)

      Nouvext = "C:\\Users\\asus\\Desktop\\Optical_Character_Reccognition-master\\Nouv_CV_Text"

      for filename in os.listdir(Nouvext):
        os.chdir(r'C:\\Users\\asus\\Desktop\\Optical_Character_Reccognition-master\\Nouv_CV_Text')
        if filename.startswith('edited'):
          f = filename
          print("nametext avant with : ",f)

          dict1 = {} 
          # creating dictionary 

          with open(f) as fh:
            for line in fh:
                
              print("boboboboobobo")
              print("line",line)
              print("nametext",f)
              # reads each line and trims of extra the spaces
              #and gives only the valid words 
              columns = line.strip().split(' ',1)
              if len(columns) >= 2 :
                command, description = columns
                dict1[command] = description.strip() 
              else:
                print("Erreur dans la conversion en json, got", columns)

          out_file = open("%s.json" % filename.split('.')[0], "w") 
          json.dump(dict1, out_file, indent = 4, sort_keys = False) 
          out_file.close() 

      with open("%s.json" % filename.split('.')[0], 'r') as fi:
        print("type de filename : ",type(filename))
        cursor = conn.cursor()
        distros_dict = json.load(fi)
        maryem=[distros_dict]        
        for  i in maryem:
          for key,value in i.items():
            print("\n Key : "+key.title())
            print("Value : "+ str(value))
            maryem.append(i)
            print("maryem icii : ",maryem[1])
            print("meryam[1] : ",maryem[1])
            # print("meryam[2] : ",maryem[2])
            print("meryam[0] : ",maryem[0])

            print("cursor : ",cursor)
            ch = key.title()
            ch2 = str(value)
            cursor.execute('insert into Cv(id_cv,id_candidat) values(?,?);',
            (5,5))
            print("\n Key : "+key.title())
            print("Value : "+ str(value))
            print("diiiis : ",distros_dict.values())
            while distros_dict:
              print("distros_dict",distros_dict)
              print("hedha distros_dict[key] **: ",distros_dict[key])
              cursor.execute('insert into Candiats(id_candidat,id_cv,nom,prenom) values(?,?,?,?);',
              (5,5,distros_dict[key],distros_dict[key]))
              cursor.execute("select * from Candiats")
              for row in cursor:
                print(f'row = {row}')
                print('test2')
                print()


        
  except Exception as e:    
      print('please provide proper name of the image')
      print(e)

Conversion_Cv('esprit')