from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os
from typing import Dict, List, Any

class AIWriter:
    def __init__(self, name = "goggle/flag-t5-base"):
        self.name = name
        self.tokenizer = AutoTokenizer.from_pretrained(name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def write(self, content, style = "Formal"):
        prompt = f"""
                Rewrite the following text in a {style} while while maintaining the original meaning and structure. Spin the content to be made into a publishable book as you improve clarity, flow and engagement.
                Orginal test: {content}
                Rewritten text:
                """
        
        inputs = self.tokenizer(prompt,
                                return_tensors = "pt",
                                max_length = 256,
                                truncation = True
                                ).to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length = len(content.split()) * 1.75,
                min_length = max(50, len(content.split()) // 2),
                num_beams = 8,
                do_sample = True,
                early_stopping = True,
                no_repeat_ngram_size = 2,
                temperature = 0.8
            )
        
        final = self.tokenizer.decode(outputs[0], skip_special_tokens = True)

        return {
            'original_content': content,
            'spinned content': final,
            'style': style,
            'original_word_count': len(content.split()),
            'spinned_word_count': len(final.split()),
            'model_used': self.name
        }
