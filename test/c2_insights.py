from transformers import pipeline
from difflib import unified_diff
import os

# Function to read text from a file
def read_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except OSError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to generate insights from text using a language model
def generate_insights(text):
    try:
        # Initialize the pipeline for text generation or other tasks
        nlp = pipeline("text-generation", model="gpt2")
        
        # Generate insights (this example uses text generation as an illustration)
        generated_text = nlp(text, max_length=300, do_sample=True)[0]['generated_text']
        
        return generated_text
    
    except Exception as e:
        print(f"Error in generating insights: {e}")
        return None

# Define the chain
class FileInsightChain:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def __call__(self):
        text = read_text(self.file_path)
        if text:
            insights = generate_insights(text)
            return insights
        else:
            return "Error reading file."

# File paths
file_path1 = os.path.join('extracted_texts', 'file1.pdf.txt')
file_path2 = os.path.join('extracted_texts', 'file2.pdf.txt')
file_path3 = os.path.join('extracted_texts', 'file3.pdf.txt')

# Create chain instances
chain1 = FileInsightChain(file_path1)
chain2 = FileInsightChain(file_path2)
chain3 = FileInsightChain(file_path3)

# Get insights
insights1 = chain1()
insights2 = chain2()
insights3 = chain3()

# Print insights
print("Insights from File 1:")
print(insights1)
print("\nInsights from File 2:")
print(insights2)
print("\nInsights from File 3:")
print(insights3)

# Compare insights (example: print differences)
print("\nDifferences in Insights between File 1 and File 2:")
diff12 = unified_diff(insights1.splitlines(), insights2.splitlines())
for line in diff12:
    print(line)

print("\nDifferences in Insights between File 1 and File 3:")
diff13 = unified_diff(insights1.splitlines(), insights3.splitlines())
for line in diff13:
    print(line)

print("\nDifferences in Insights between File 2 and File 3:")
diff23 = unified_diff(insights2.splitlines(), insights3.splitlines())
for line in diff23:
    print(line)
