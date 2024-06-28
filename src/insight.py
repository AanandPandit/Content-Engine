# from transformers import pipeline

# # Step 1: Correct the file path (use raw string or double backslashes)
# file_path = r'test\notetest.txt'

# try:
#     # Step 2: Read the text file
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()

#     # Step 3: Initialize the pipeline for text generation
#     nlp = pipeline("text-generation", model="gpt2")

#     # Step 4: Generate text based on the input text
#     generated_text = nlp(text, max_length=300, do_sample=True)[0]['generated_text']

#     # Step 5: Print or process the generated text
#     print(generated_text)

# except FileNotFoundError:
#     print(f"Error: File '{file_path}' not found.")
# except OSError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"Error: {e}")


#--------------------------------------------------

from transformers import pipeline

# Step 1: Read the text file
file_path = r'test\notetest.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Step 2: Initialize the pipeline for text generation
    nlp = pipeline("text-generation", model="gpt2")

    # Step 3: Generate text based on the input text
    generated_text = nlp(text, max_length=300, do_sample=True)[0]['generated_text']

    # Step 4: Print or process the generated text
    print(generated_text)

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except OSError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
