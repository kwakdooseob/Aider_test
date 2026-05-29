def generate_prompt(template, text):
    return template.format(text=text)

# Example templates
SUMMARY_TEMPLATE = "Summarize the following text:\n{text}"
KEYWORDS_TEMPLATE = "Extract key words from the following text:\n{text}"
SENTIMENT_TEMPLATE = "Analyze the sentiment of the following text:\n{text}"

# Usage example
if __name__ == "__main__":
    text = "This is a sample text for testing."
    summary_prompt = generate_prompt(SUMMARY_TEMPLATE, text)
    keywords_prompt = generate_prompt(KEYWORDS_TEMPLATE, text)
    sentiment_prompt = generate_prompt(SENTIMENT_TEMPLATE, text)

    print("Summary Prompt:")
    print(summary_prompt)
    print("\nKeywords Prompt:")
    print(keywords_prompt)
    print("\nSentiment Prompt:")
    print(sentiment_prompt)
