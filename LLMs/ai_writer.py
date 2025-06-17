from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class AIWriter:
    def __init__(self, name = "goggle/flag-t5-base"):
        self.name = name
        self.tokenizer = AutoTokenizer.from_pretrained(name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(name)