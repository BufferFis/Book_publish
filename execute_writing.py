from LLMs.content_processor import ContentProcessor
import json
import time

def main():

    processor = ContentProcessor()

    print("Starting the spin")
    time.sleep(1)

    results = processor.process(style="formal")
    
    print("Total chapters processed:", len(results))
    
if __name__ == "__main__":
    main()

    