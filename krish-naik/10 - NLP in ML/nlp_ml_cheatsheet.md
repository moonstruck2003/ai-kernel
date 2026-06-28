# Lesson 10: NLP in Machine Learning Cheatsheet

A quick reference guide for text preprocessing and vectorization techniques using standard NLP libraries.

## Core Libraries Needed
*   **NLTK** (`nltk`): Used for tokenization, stemming, lemmatization, stop words, POS, and NER.
*   **Scikit-Learn** (`sklearn`): Used for Bag of Words (BOW) and TF-IDF vectorization.
*   **Gensim** (`gensim`): Used for Word2Vec embeddings.

---

## 1. Text Preprocessing (NLTK)
Before text can be vectorized, it must be cleaned and broken down.

```python
import nltk
# Download required NLTK datasets (run once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

### Tokenization (Splitting text)
```python
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hello! Welcome to NLP in Python. Let's learn."
print(sent_tokenize(text)) # Splits into sentences: ['Hello!', 'Welcome to NLP in Python.', "Let's learn."]
print(word_tokenize(text)) # Splits into individual words: ['Hello', '!', 'Welcome', 'to', ...]
```

### Stemming vs Lemmatization (Reducing words to base form)
*   **Stemming**: Chops off prefixes/suffixes using crude heuristic rules (e.g., "studying" ➡️ "studi"). Fast but crude.
*   **Lemmatization**: Uses a dictionary (WordNet) to find the actual dictionary root (lemma) based on context. Slower but accurate.

```python
# Stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("going"))      # "go"
print(stemmer.stem("histories"))  # "histori" (not a real word!)

# Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("going", pos='v'))     # "go" (pos='v' specifies verb)
print(lemmatizer.lemmatize("histories"))          # "history" (returns a real word!)
```

### Stop Words (Removing noise)
Removes common filler words like "the", "is", "at" that do not add semantic meaning to ML models.
```python
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

words = ["this", "is", "a", "good", "movie"]
filtered_words = [w for w in words if w not in stop_words]
print(filtered_words) # ['good', 'movie']
```

### Part of Speech (POS) Tagging & Named Entity Recognition (NER)
*   **POS Tagging**: Identifies if a word is a noun, verb, adjective, etc.
*   **NER**: Identifies names, organizations, locations, etc.
```python
from nltk import pos_tag, ne_chunk

words = word_tokenize("Google is based in California.")
tagged = pos_tag(words)
print(tagged) # [('Google', 'NNP'), ('is', 'VBZ'), ('based', 'VBN'), ('in', 'IN'), ('California', 'NNP')]

# NER (requires POS tagged input)
entities = ne_chunk(tagged)
# print(entities) # Returns a tree structure highlighting organization (Google) and GPE/Location (California)
```

---

## 2. Text Vectorization (Feature Extraction)
Machine Learning models cannot accept raw strings; text must be converted into numerical vectors.

### Bag of Words (Count Vectorizer)
Creates a vocabulary of all unique words and represents documents by counting how many times each word appears.
```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "I love deep learning.",
    "Deep learning is based on neural networks."
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out()) # List of vocabulary words
print(X.toarray()) # 2D array of word counts
```

### TF-IDF Vectorizer
Represents words based on their importance:
*   **Term Frequency (TF)**: How often a word appears in a specific document.
*   **Inverse Document Frequency (IDF)**: Penalizes words that appear in *every* document (like "is", "the"), scaling up rare words that carry more meaning.
```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus)
print(X_tfidf.toarray()) # Float numbers representing importance scores
```

### Word2Vec (Word Embeddings)
Captures semantic relationships. Words with similar meanings will have vectors close to each other in vector space (e.g., `King - Man + Woman = Queen`).
```python
from gensim.models import Word2Vec

# Sentence tokens
sentences = [["love", "deep", "learning"], ["neural", "networks", "are", "deep"]]

# Train Word2Vec model
model = Word2Vec(sentences, min_count=1, vector_size=100, window=5)

# Get vector representing a word
vector = model.wv['deep']
print(vector.shape) # (100,) - a dense vector of size 100

# Find most similar words
print(model.wv.most_similar('deep'))
```
