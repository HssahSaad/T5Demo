#Assignment 1:

# Function to read the content of a file and return it as a list of lines
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()
    
# Load the tweets and word lists
tweets = read_file('/content/tweets.txt')
positive_words = [line.strip() for line in read_file('/content/words_positive.txt')]
negative_words = [line.strip() for line in read_file('/content/words_negative.txt')]

# Function to clean and split the text into words
def preprocess(text):
    text = text.lower()  # Convert to lowercase
    words = text.split()  # Split text into words
    return words

# Function to calculate the sentiment score of a tweet
def calculate_sentiment(tweet, pos_words, neg_words):
    words = preprocess(tweet)
    pos_count = 0
    neg_count = 0
    for word in words:
        if word in pos_words:
            pos_count += 1
        if word in neg_words:
            neg_count += 1
    return pos_count - neg_count

# Compute the sentiment score for each tweet
tweet_scores = []
for tweet in tweets:
    score = calculate_sentiment(tweet, positive_words, negative_words)
    tweet_scores.append((tweet.strip(), score))

# Sort the tweets by their sentiment score (most positive first)
sorted_tweets = sorted(tweet_scores, key=lambda x: x[1], reverse=True)

# Print the sorted tweets with their scores
for tweet, score in sorted_tweets:
    print(f'Score: {score} | Tweet: {tweet}')