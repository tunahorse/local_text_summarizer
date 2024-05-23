from openai import OpenAI
from local_text_summarizer.summarize import condense_story

# Initialize OpenAI client with your deepinfra token and endpoint
openai = OpenAI(
    api_key="your key",
    base_url="https://api.deepinfra.com/v1/openai",
)

# Example text to be summarized
text = """
The quick brown fox jumps over the lazy dog. The dog, surprised by the fox's agility,
barks loudly and chases after it. The fox, being clever and swift, easily outmaneuvers
the dog and escapes into the nearby forest. The dog, exhausted from the chase, returns
home and takes a nap. The end.
"""

# Summarize the text using local_text_summarizer
# Change ratio to adjust the length of the summary
summary = condense_story(text, ratio=0.5)
print("Summary:")
print(summary)

# Use the summarized text as input for the OpenAI API
chat_completion = openai.chat.completions.create(
    model="meta-llama/Meta-Llama-3-70B-Instruct",
    messages=[{"role": "user", "content": summary}],
)

# Print the AI's response
print("AI Response:")
print(chat_completion.choices[0].message["content"])
