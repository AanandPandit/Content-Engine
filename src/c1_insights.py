from transformers import pipeline

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

# File paths
file_path1 = r'test\file1.txt'
file_path2 = r'test\file2.txt'

# Read texts from files
text1 = read_text(file_path1)
text2 = read_text(file_path2)

# Generate insights for both texts
if text1 and text2:
    insights1 = generate_insights(text1)
    insights2 = generate_insights(text2)
    
    if insights1 and insights2:
        # Print insights
        print("Insights from File 1:")
        print(insights1)
        print("\nInsights from File 2:")
        print(insights2)
        
        # Compare insights (example: print differences)
        print("\nDifferences in Insights:")
        print("---")
        print("File 1 vs File 2")
        print("---")
        print("Comparison Result:\n")
        diffs = list(text1)
