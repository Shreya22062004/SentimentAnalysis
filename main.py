import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# reading text file
text = open('read.txt', encoding='utf-8').read()

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans(' ', ' ', string.punctuation))

# splitting text into words
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    neu = score['neu']

    if (neg > pos):
        print("Negative Sentiment")

    elif (pos > neg):
        print("Positive Sentiment")

    else:
        print("Neutral Sentiment")

sentiment_analyse(cleaned_text)

# Plotting the emotions on the graph

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
