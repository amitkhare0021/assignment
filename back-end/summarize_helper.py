import spacy

nlp = spacy.load("en_core_web_sm")

def summarize_text(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    summary = " ".join(sentences[:30])

    return summary
