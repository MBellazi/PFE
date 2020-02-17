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


def create(conn):
  print("Create")
  cursor = conn.cursor()
  cursor.execute(
    'insert into Cv(id_cv,id_candidat) values(?,?);',
    (2,2)
  )

def create2(conn):
  print("Create")
  cursor = conn.cursor()
  cursor.execute(
    'insert into Candiats(id_candidat,id_cv,nom,prenom) values(?,?,?,?);',
    (2,2,'Bellazi','Aymen')
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
  "Trusted_Connection=yes;"
)


conn.commit()

create(conn)
create2(conn)
read(conn)
read2(conn)



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



    JPEG_DIR_SOURCE = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master'
    JPEG_DEST_DIR = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master/Ancien_Jpeg'
    JPEG_DEST_Nouv = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master/Nouveau_Jpeg'

    for pname in os.listdir(JPEG_DIR_SOURCE):
      if pname.lower().startswith('edited') and pname.lower().endswith('.jpg'):
        shutil.move(os.path.join(JPEG_DIR_SOURCE, pname), JPEG_DEST_Nouv)    
      elif pname.lower().endswith('.jpg'):
        shutil.move(os.path.join(JPEG_DIR_SOURCE, pname), JPEG_DEST_DIR)       

             

      #**********   Extraire le text d'un pdf ***************
    print("               *****...........   PDF   ............****                  ")

    folder_path = "C:\\Users\\asus\\Desktop\\Optical_Character_Reccognition-master"
    for filenamepdf in os.listdir(folder_path):
      if filenamepdf.lower().endswith('.pdf'):   
        print("PDF Name : ",filenamepdf)   
        # creating a pdf file object
        pdfFileObj = open(filenamepdf, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict = False)

        # printing number of pages in pdf file
        print("printing number of pages in pdf file : ", pdfReader.numPages)
        x = pdfReader.numPages
        # creating a page object
        pageObj = pdfReader.getPage(0)

        extrait = pageObj.extractText()
        # extracting text from page
        print("extracting text from page : ", extrait)

       # closing the pdf file object
        pdfFileObj.close()
        PDF_DIR_SOURCE = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master'
        PDF_DEST_DIR = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master/Ancien_PDF'

    f = 'C:/Users/asus/Desktop/Optical_Character_Reccognition-master/test.txt'
    dic ={}
    with open(f) as fh:
      for line in fh:
        command, description = line.strip().split(':', 1)
        dic[command] = description.strip() 
      out_file = open("C:/Users/asus/Desktop/Optical_Character_Reccognition-master/mmm.json", "w") 
      
      json.dump(dic, out_file, indent = 4, sort_keys = False) 
      out_file.close() 
   
        # extrait_list = filenamepdf.splitlines()
        # for line in extrait_list:
        #   if ':' not in line:
        #     continue
        #   key, value = line.split(':')
        #   extrait[key.strip()] = value.strip()
        # j = json.dumps(extrait)
        # with open('extrait.json','w') as f:
        #   f.write(j)
        #   f = json.load(open('extrait.json'))
        #   print(f)
        # for pdfname in os.listdir(PDF_DIR_SOURCE):
        #   if pdfname.lower().endswith('.pdf'):
        #     shutil.move(os.path.join(PDF_DIR_SOURCE, pdfname), PDF_DEST_DIR)







        # def get_data(extrait):
        #   _dict = {}
        #   extrait_list = extrait.splitlines()
        #   for line in extrait_list:
        #     if ':' not in line:
        #       continue
        #     key, value = line.split(':')
        #     _dict[key.strip()] = value.strip()
        #   return _dict
        # page_data = get_data(extrait)
        # json_data = json.dumps(page_data) 

        # print(json_data)
        # print(":::::::   JSON :::::")
        # file_ = open("C:/Users/asus/Desktop/Optical_Character_Reccognition-master/ouput2.json", "w")
        # file_.write(json_data)
        # subprocess.Popen("ls", stdout=file_)



        # extrait = {}
        # extrait_list = extrait.splitlines()
        # for line in extrait_list:
        #     if ':' not in line:
        #         continue
        #     key, value = line.split(':')
        #     extrait[key.strip()] = value.strip()
        # print(extrait)


      
except Exception as e:    
    print('please provide proper name of the image')
    print(e)
