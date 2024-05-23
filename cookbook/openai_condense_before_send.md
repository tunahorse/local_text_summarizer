
# Text Summarization and OpenAI Response Tool

This Python script demonstrates how to summarize a text using the module and interact with OpenAI's API to generate a response based on the summarized text.

## Features

- Text summarization using a the module.
- Interaction with OpenAI's API using a custom model and endpoint.

## Requirements

- Python 3.x
- OpenAI Python package
- Local Text Summarizer module (`local_text_summarizer`)

## Setup

1. Install the necessary Python packages:
   ```
   pip install openai
   ```

   Ensure the `local_text_summarizer` is available in your Python environment or include its installation command if available.

2. Replace `your key` in the script with your actual OpenAI API key.

## Usage

Run the script with the following command:
```
python openai_condense_before_send.py
```

The script performs the following actions:
1. Initializes the OpenAI client with your API key.
2. Provides an example text to be summarized.
3. Summarizes the text using the `condense_story` function from `local_text_summarizer`.
4. Sends the summarized text to the OpenAI API.
5. Retrieves and prints the response from the OpenAI API.

## Customization

You can adjust the text to be summarized and the summarization ratio by modifying the `text` and `ratio` variables respectively in the script.

