# scikit-learn k-fold cross-validation
from sklearn.model_selection import KFold
from nltk.tokenize import word_tokenize
from Somstem.somali import SomStemmermain
import re

with open("corpus.txt", "r", encoding="utf-8") as file:
    mydata = file.readlines()
Somstemmer = SomStemmermain()
words_stemmed= []

for sentence in mydata:
    words = word_tokenize(sentence)

    my_stemmed_words = []
    for word in words:
        processed_words = re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', word.lower()) 
        stemmed_word = Somstemmer.somstem(processed_words )
        my_stemmed_words.append(stemmed_word)

    words_stemmed.extend(my_stemmed_words)
# If we want integrate this stemmer into an other software, the above section is applicable.
num_folds = 10 #We use 10 splits
kfold = KFold(n_splits=num_folds, shuffle=True, random_state=42)
t_corpus_words = 0
correctly_stemmed_words = 0
for fold, (train_indice, test_indice) in enumerate(kfold.split(words_stemmed)):
    x_train = [words_stemmed[i] for i in train_indice]
    y_test = [words_stemmed[i] for i in test_indice]
    f_corrected_stem = sum(1 for word in y_test if word in x_train)
    f_total_word = len(y_test)
    correctly_stemmed_words += f_corrected_stem
    t_corpus_words += f_total_word
    fold_accuracy = f_corrected_stem / f_total_word if f_total_word > 0 else 0 #We divide correctly stemmed over total words in the corpus.
    print(f"Fold{fold + 1} - Acuracy: {fold_accuracy * 100:.2f}%")
Mean_Accuracy = correctly_stemmed_words / t_corpus_words if t_corpus_words > 0 else 0
print(f"Mean Accuracy: {Mean_Accuracy * 100:.2f}%")

#In this evaluation we use text corpus dataset.
