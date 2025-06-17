from transformers import AutoTokenizer, AutoModelForSequenceClassification

class AIReviewer:
    def __init__(self, name="nvidia/quality-classifier-deberta"):
        self.name = name
        self.tokenizer = AutoTokenizer.from_pretrained(name)
        self.model = AutoModelForSequenceClassification.from_pretrained(name)