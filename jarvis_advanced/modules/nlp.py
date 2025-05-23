from transformers import pipeline

# Zero-shot-classification for intent detection (can be replaced with your own model)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_intent(text):
    labels = ["web search", "system control", "chat", "weather", "news"]
    result = classifier(text, labels)
    return result['labels'][0]