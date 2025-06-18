import os
from pathlib import Path
from typing import List, Dict, Any
import json
from datetime import datetime
from .ai_writer import AIWriter

class ContentProcessor:
    def __init__(self, text_directory: str = "Text/", output_dir: str = "output/"):
        self.text_dir = Path(text_directory)
        self.output_dir = Path(output_dir)
        self.ai_writer = AIWriter()

        self.output_dir.mkdir(exist_ok=True)
        (self.output_dir / 'processed').mkdir(exist_ok=True)
    
    
    def split_content(self, content: str, max_length: int = 1500) -> List[str]:
        """Split content into blocks for better processing."""
        words = content.split()
        block = []
        current_block = []
        count = 0

        for word in words:
            current_block.append(word)
            count = count + len(word) + 1

            if count >= max_length:
                block.append(' '.join(current_block))
                current_block = []
                count = 0
        
        if current_block:
            block.append(' '.join(current_block))

        return block
    

    def save_content(self, result: Dict[str, Any], chapter_name: str):
        """Save spinned content"""
        output_file = self.output_dir / 'processed' / f"{chapter_name}_spinned.txt"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result['spinned_content'])
        


    
    def process(self, style: str = "formal") -> List[Dict[str, Any]]:
        results = []

        files = sorted([f for f in self.text_dir.glob("chapter*.txt")])
        
        for file in files:
            print(f"Processing {file.name}")
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()

            blocks = self.split_content(text)

            processed_blocks = []

            for i, block in enumerate(blocks):
                result = self.ai_writer.write(block, style)
                processed_blocks.append(result)
            
            combined = " ".join([block['spinned content'] for block in processed_blocks])

            result = {
                'ch_name': file.stem,
                'original_content': text,
                'spinned_content': combined,
                'style': style,
                'blocks_processed': len(blocks)
            }

            results.append(result)

            self.save_content(result, file.stem)
        return results

   
