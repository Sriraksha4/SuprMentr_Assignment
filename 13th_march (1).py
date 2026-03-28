import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download once (only first time)
nltk.download('punkt')
nltk.download('stopwords')

# Input text
text = "I am learning NLP and it is very exciting!!!"

# 1. Convert to lowercase
text = text.lower()

# 2. Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# 3. Tokenize text
tokens = word_tokenize(text)

# 4. Remove stopwords
stop_words = set(stopwords.words('english'))
filtered = [word for word in tokens if word not in stop_words]

# 5. Apply stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered]

# Output
print("Output:", stemmed)