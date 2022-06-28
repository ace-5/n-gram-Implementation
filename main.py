from nltk.corpus import stopwords

en_stopwords = stopwords.words('english')

def generate_N_gram(text, n_gram=1):
    result = []
    words = text.split()
    words = [word for word in words if word.lower() not in en_stopwords]
    for i in range(len(words)-n_gram+1):
        result.append(words[i:n_gram+i])
    return result

result_1gram =  generate_N_gram(text="Today is the hotest day on planet earth", n_gram=1)
result_2gram =  generate_N_gram(text="Today is the hotest day on planet earth", n_gram=2)
result_3gram =  generate_N_gram(text="Today is the hotest day on planet earth", n_gram=3)

with open ('result.txt', 'a') as f:
    f.write("\nText: Today is the hotest day on planet earth\n")
    f.write("Result: \n")
    f.write(f'\t\tUnigram: {result_1gram}\n')
    f.write(f'\t\tBigram: {result_2gram}\n')
    f.write(f'\t\tTrigram: {result_3gram}\n')
