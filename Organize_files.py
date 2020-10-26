import os
import shutil #library for coping files 

# CODE to organize Images files


print(" Welcome to the Organize System program ")

current_dir = os.path.dirname(os.path.realpath(__file__)) # make u know where are u in the system 

for filename in os.listdir(current_dir): # for loop to search in side the folders
    
    if filename.endswith(("png" , "jpg" , "gif" , "jpeg" ,"tif")):
        
        if not os.path.exists("Images"): # when you rerun the code the system can't create two file with same name in the same folder
            
        
            os.mkdir('Images') # Create a folder

        shutil.copy(filename , "Images")

        os.remove(filename) # after coping the file > this funcation will delete it 

        print(' Images Done') #just to make sure its working or not 




# CODE to organize codes files


current_dir = os.path.dirname(os.path.realpath(__file__)) # make u know where are u in the system 

for filename in os.listdir(current_dir): # for loop to search in side the folders
    
    if filename.endswith((".py" , "css" , "html", "js"  )):
        
        if not os.path.exists("Codes"): # when you rerun the code the system can't create two file with same name in the same folder
            
        
            os.mkdir('Codes') # Create a folder

        shutil.copy(filename , "Codes")

        os.remove(filename) # after coping the file > this funcation will delete it 

        print('codes Done') #just to make sure its working or not 


# CODE to organize Videos files

current_dir = os.path.dirname(os.path.realpath(__file__)) # make u know where are u in the system 

for filename in os.listdir(current_dir): # for loop to search in side the folders
    
    if filename.endswith((".mp4" , "webm")):
        
        if not os.path.exists("Videos"): # when you rerun the code the system can't create two file with same name in the same folder
            
        
            os.mkdir('Videos') # Create a folder

        shutil.copy(filename , "Videos")

        os.remove(filename) # after coping the file > this funcation will delete it 

        print(' Videos Done') #just to make sure its working or not 



# CODE to organize Documents files


current_dir = os.path.dirname(os.path.realpath(__file__)) # make u know where are u in the system 

for filename in os.listdir(current_dir): # for loop to search in side the folders
    
    if filename.endswith((".pdf" , "docx" , "xlsx" , "pptx")):
        
        if not os.path.exists("Documents"): # when you rerun the code the system can't create two file with same name in the same folder
            
        
            os.mkdir('Documents') # Create a folder

        shutil.copy(filename , "Documents")

        os.remove(filename) # after coping the file > this funcation will delete it 

        print('Documents Done') #just to make sure its working or not 



# CODE to organize Apps files


current_dir = os.path.dirname(os.path.realpath(__file__)) # make u know where are u in the system 

for filename in os.listdir(current_dir): # for loop to search in side the folders
    
    if filename.endswith((".exe" , "apk")):
        
        if not os.path.exists("Apps"): # when you rerun the code the system can't create two file with same name in the same folder
            
        
            os.mkdir('Apps') # Create a folder

        shutil.copy(filename , "Apps")

        os.remove(filename) # after coping the file > this funcation will delete it 

        print('Apps Done') #just to make sure its working or not 


#CODE to organize Zip/rar files


current_dir = os.path.dirname(os.path.realpath(__file__)) # make u know where are u in the system 

for filename in os.listdir(current_dir): # for loop to search in side the folders
    
    if filename.endswith((".zip" , "rar")):
        
        if not os.path.exists("rar"): # when you rerun the code the system can't create two file with same name in the same folder
            
        
            os.mkdir('rar') # Create a folder

        shutil.copy(filename , "rar")

        os.remove(filename) # after coping the file > this funcation will delete it 

        print('rar Done') #just to make sure its working or not 
