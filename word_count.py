file_path = 'C:\\Users\Dell\\Desktop\\Next Hikes internship project 1\\Next hikes project 1\\Project_1\\web_scrap.text'
try:
    #open the filein read mode with open 
    with open(file_path,'r') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        print(f'Total words in the file:{word_count}')
except FileNotFoundError:
    print(f'the file "{file_path}" was not found.')
except Exception as e:
    print(f'An error occurred:{str(e)}')    
        
        
        
       