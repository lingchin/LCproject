def clean_text(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")
    text = text.strip() #do this after punctuation b/c often reviews have !! at the end
    text = text.lower()
    text = "".join(w for w in text if not w.isdigit())

    token_text = word_tokenize(text)
    stop_words= set(stopwords.words('portuguese'))
    token_text = [w for w in token_text if not w in stop_words]
    lem_text = [WordNetLemmatizer().lemmatize(word, pos= 'v') for word in token_text]
    cleaned_text = " ".join(word for word in lem_text)

    return cleaned_text
