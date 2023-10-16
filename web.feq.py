from collections import Counter
with open ('C:\\Users\Dell\\Desktop\\Next Hikes internship project 1\\Next hikes project 1\\Project_1\\web_scrap.text','r') as file:
    text = file.read()
    # Tokensize the text into words (assuming words are separated by spaces)
    words = text.split()
    #count the frequency of each word 
    word_frequency = Counter(words)
    # Display the word frequency 
for word,frequency in word_frequency.items():
    print(f'{word}:{frequency}')
    
  
