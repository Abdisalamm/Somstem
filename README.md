## Main files
- somali.py : is where the rules are designed, it can be found inside Somstem folder.
- main.py : is the file you need to run to stem words.
- evaluation.py : contains the script to calculate the accuracy, it calculates csw/twc ( Correctly stemmed words/Total words in the corpus) using tenfold cross-validation
- dataset : contains our benchmark dataset 'corpus.txt'.

> [!NOTE]
>  ## Instructions for using this stemmer
      
    1. Download the package.
    2. Extract the files.
    3. Copy the "Somstem" folder from Somstem-main\Somstem-main, directory.
    4. Place the "Somstem" folder in your project directory.
    5. In your editor, open the terminal and run the following command: pip install Somstem\dist\Somali-1.0-py3-none-any.whl 


In step 5 make sure, the path is correct.

### ***If you are using Google Colab or Jupyter Notebook, follow steps 1, 2 , 3 and 4, then run the following command:***


from google.colab import drive

drive.mount('/content/drive')

!pip install /path/Somstem/dist/Somali-1.0-py3-none-any.whl

Example in my case: !pip install /content/drive/MyDrive/Somstem/dist/Somali-1.0-py3-none-any.whl

> The stemmer is now installed in your project, and you can start using it.

#### After steps 1-5 are followed, we give code examples of integrating this stemmer into your own software or project:

## For a large corpus:

 ```
    import nltk
   nltk.download('punkt_tab')
  from nltk.tokenize import word_tokenize
   from Somstem.Somali import SomStemmermain

 import re

 with open("corpus", "r", encoding="utf-8") as file:
    som_word = file.read()
words = re.findall(r'\b\w+\b', som_word)
stemmer = SomStemmermain()
my_new_words = []
for word in words:
   processed_word = re.sub(r'^[^a-zA-Z]+|[^a-zA-Z]+$', '', word.lower()) 
    stemmed_word = stemmer.somstem(processed_word)
    my_new_words.append(stemmed_word)
print(my_new_words)  #Now, the my_new_words are the stemmed words, we can continue with any task we want.

```

## For simple input words from a user:

 ```
 import nltk
 nltk.download('punkt_tab')
 from nltk.tokenize import word_tokenize
 from Somstem.Somali import SomStemmermain
import re
stemmer = SomStemmermain()
while True:
    input_word = input("Enter a word to stem: ")
    if input_word.lower() == 'exit':
        print("Nabad galiyo")
        break
    words = word_tokenize(input_word)
    my_stemmed_words = []
    for word in words:
        processed_word = re.sub(r'^[^a-zA-Z]+|[^a-zA-Z]+$', '', word.lower())
        stemmed_word = stemmer.somstem( processed_word)
        my_stemmed_words.append(stemmed_word)
    print("Stemmed words:", my_stemmed_words) 

```

## When using Colab:

 ```
  import nltk
  nltk.download('punkt_tab')
 from nltk.tokenize import word_tokenize
  from drive.MyDrive.Somstem.Somali import SomStemmermain
import re
stemmer = SomStemmermain()
while True:
    input_word = input("Enter a word to stem: ")
    if input_word.lower() == 'exit':
        print("Nabad galiyo")
        break
    words = word_tokenize(input_word)
    my_stemmed_words = []
    for word in words:
        processed_word = re.sub(r'^[^a-zA-Z]+|[^a-zA-Z]+$', '', word.lower())
        stemmed_word = stemmer.somstem( processed_word)
        my_stemmed_words.append(stemmed_word)
    print("Stemmed words:", my_stemmed_words)

```



#### Integrating this stemmer into any software or research prototype follows the same procedure.

We will always be available to help if you have any questions while using this stemmer. We will provide our contact information here soon.

  
## Dataset
The dataset folder contians our benchmark dataset namely 'corpus.txt' this dataset maybe used for further investigations:

## Evaluation
To evaluate our current stemmer's performance import basic libraries and follow these steps:
- Copy evaluateion.py into your project directory, together with 'Somstem' folder.
- Run evaluation.py it uses tenfold cross-validation
- Use the corpus.txt file which is our benchmark dataset.
- If you need to stem words, please run the main.py file, enter words of your choice, and see the results.

> [!IMPORTANT]
> ## future Improvements

- Any future improvements of this stemmer are welcome please if you want refine this stemmer, find the following files:
  1. somali.py : This file contains the rules and is where you can change and do some improvements (it is where you need to edit, and it is inside the 'Somstem' folder).
  2. main.py : use this file to stem words as it has the rules imported (is where you enter text to stem), copy this file into your project dircetory.
  3. You could also use our benchmark dataset 'corpus.txt'.

# Version 1.0


