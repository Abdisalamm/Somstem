#Kfold validation script.
#In this evaluation we use CSW/TWC (correctly stemmed words/Total words in the corpus) formula.
#import nltk
#nltk.download('punkt') #The tokenizer sometimes shows error, so we used this line, and the above one.
from sklearn.model_selection import KFold
import nltk
nltk.download('punkt_tab') #We add NLTK
from nltk.tokenize import word_tokenize
from Somstem.Somali import SomStemmerImpl
import re

with open("corpus.txt", "r", encoding="utf-8") as file:
    mydata = file.readlines()
Somstemmer = SomStemmerImpl()
all_words_stemmed= []

for sentence in mydata:
    words = word_tokenize(sentence)

    my_stemmed_words = []
    for word in words:
        processed_words = re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', word.lower()) #Stem only words. We don't stem numbers, we also don't remove numbers, sometimes they may make a meaning
        stemmed_word = Somstemmer.somstem(processed_words )
        my_stemmed_words.append(stemmed_word)

    all_words_stemmed.extend(my_stemmed_words)
# If we want integrate this stemmer into an other software, the above section is applicable.
kfold = KFold(n_splits=10, shuffle=True, random_state=42) #We use 10 splits
total_words = 0
total_correct_stems = 0
for fold, (train_indices, test_indices) in enumerate(kfold.split(all_words_stemmed)):
    X_train = [all_words_stemmed[i] for i in train_indices]
    Y_test = [all_words_stemmed[i] for i in test_indices]
    fold_correct_stems = sum(1 for word in Y_test if word in X_train)
    fold_total_words = len(Y_test)
    total_correct_stems += fold_correct_stems
    total_words += fold_total_words
    fold_accuracy = fold_correct_stems / fold_total_words if fold_total_words > 0 else 0.0 #We divide correctly stemmed over total words in the corpus.
    print(f"Fold {fold + 1} - Accuracy: {fold_accuracy * 100:.2f}%")
overall_accuracy = total_correct_stems / total_words if total_words > 0 else 0.0
print(f"Overall Accuracy: {overall_accuracy * 100:.2f}%")

#In this evaluation we use text corpus dataset.