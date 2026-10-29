
import json
import tiktoken

# Use an encoding supported by tiktoken
encoding = tiktoken.get_encoding("o200k_base")

# Five sample texts
texts = {
    "Sentence": (
        "Artificial intelligence helps people solve problems faster."
    ),
    "Paragraph": (
        "Machine learning is a branch of artificial intelligence. "
        "It enables computers to learn patterns from data and make "
        "predictions. Developers use machine learning in healthcare, "
        "finance, education, and customer support. Good data preparation "
        "and model evaluation are important for reliable results."
    ),
    "Page": (
        ("Foundation models are trained on large datasets. "
         "They can perform many tasks, including summarization, "
         "translation, classification, and question answering. "
         "Tokenization converts text into smaller units called tokens. "
         "These tokens may represent complete words, parts of words, "
         "or punctuation. Context windows limit how much information "
         "a model can process in one request. API providers charge "
         "according to the number of input and output tokens. "
         "Developers should compare models for quality, latency, "
         "privacy, and cost before choosing a model. ") * 20
    ),
    "JSON": json.dumps({
        "name": "Dhanush",
        "project": "Customer Support Bot",
        "skills": ["Python", "Machine Learning", "NLP"],
        "active": True,
        "rating": 4.5
    }),
    "Tamil": "வணக்கம்! செயற்கை நுண்ணறிவு மிகவும் பயனுள்ளதாக உள்ளது."
}


def count_words(text):
    # Simple whitespace-based word count
    return len(text.split())


print("TOKEN COUNT REPORT")
print("-" * 75)

results = {}

for name, text in texts.items():
    token_ids = encoding.encode(text)
    token_count = len(token_ids)
    word_count = count_words(text)
    words_per_token = word_count / token_count if token_count else 0

    results[name] = token_count

    print(f"\n{name}")
    print(f"Text: {text[:100]}...")
    print(f"Words: {word_count}")
    print(f"Tokens: {token_count}")
    print(f"Words per token: {words_per_token:.3f}")
    print(f"Fits 8K context: {token_count <= 8192}")
    print(f"Fits 128K context: {token_count <= 128000}")

    if words_per_token > 0.75:
        print("Comparison: More than the 0.75 rule of thumb")
    elif words_per_token < 0.75:
        print("Comparison: Less than the 0.75 rule of thumb")
    else:
        print("Comparison: Matches the rule of thumb")


# Cost calculator: prices are USD per 1 million tokens
def estimate_cost(input_tokens, output_tokens, price_in, price_out):
    input_cost = (input_tokens / 1_000_000) * price_in
    output_cost = (output_tokens / 1_000_000) * price_out
    return input_cost + output_cost


# Example prices: GPT-4.1 mini standard API pricing
price_in = 0.40
price_out = 1.60

chats_per_day = 1000
input_per_chat = 1500
output_per_chat = 400
days_per_month = 30

monthly_input = chats_per_day * input_per_chat * days_per_month
monthly_output = chats_per_day * output_per_chat * days_per_month

daily_cost = estimate_cost(
    chats_per_day * input_per_chat,
    chats_per_day * output_per_chat,
    price_in,
    price_out
)

monthly_cost = estimate_cost(
    monthly_input,
    monthly_output,
    price_in,
    price_out
)

print("\n" + "=" * 75)
print("MONTHLY API COST ESTIMATE")
print(f"Model: GPT-4.1 mini")
print(f"Chats per month: {chats_per_day * days_per_month:,}")
print(f"Monthly input tokens: {monthly_input:,}")
print(f"Monthly output tokens: {monthly_output:,}")
print(f"Daily estimated cost: ${daily_cost:.4f}")
print(f"Monthly estimated cost: ${monthly_cost:.2f}")


# Bonus: compare two tokenizers on the same sentence
sentence = "Artificial intelligence helps people solve problems faster."

enc1 = tiktoken.get_encoding("o200k_base")
enc2 = tiktoken.get_encoding("cl100k_base")

print("\nBONUS: TOKENIZER COMPARISON")
print(f"Sentence: {sentence}")
print(f"o200k_base tokens: {len(enc1.encode(sentence))}")
print(f"cl100k_base tokens: {len(enc2.encode(sentence))}")
print("Note: Counts may differ between tokenizers.")
