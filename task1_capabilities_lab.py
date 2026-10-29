
import csv
import json
import time
import re

# ==================================================
# TASK 1: CAPABILITIES LAB (MANUAL MODE)
# No API key required
# ==================================================

OUTPUT_FILE = "capabilities_lab_results.csv"

sample_text = (
    "GreenLeaf Electronics received 250 customer orders in March. "
    "Of these, 220 orders were delivered on time and 30 were delayed. "
    "The company received 18 complaints about late delivery. "
    "Customers can contact support at support@greenleaf.example. "
    "The company plans to improve its delivery tracking system next month."
)

# Five tasks with manually prepared sample answers
tasks = [
    {
        "Task": "Summarisation",
        "Prompt": (
            "Summarise the text in two sentences, including the main "
            "statistics and planned improvement."
        ),
        "Answer": (
            "GreenLeaf Electronics received 250 orders in March, with "
            "220 delivered on time and 30 delayed. After receiving "
            "18 late-delivery complaints, the company plans to improve "
            "its tracking system next month."
        ),
        "Rating": 5,
        "Improvement": (
            "Check that the summary preserves all important facts "
            "and follows the two-sentence limit."
        )
    },
    {
        "Task": "Classification",
        "Prompt": (
            "Classify the situation as Positive, Negative, or Mixed "
            "and give one reason."
        ),
        "Answer": (
            "Mixed — Most orders were delivered on time, but 30 delays "
            "and 18 complaints indicate delivery problems."
        ),
        "Rating": 5,
        "Improvement": (
            "Make sure the selected category is supported by the figures."
        )
    },
    {
        "Task": "Extraction",
        "Prompt": (
            "Extract the company name, month, total orders, on-time "
            "orders, delayed orders, complaints, support email, and "
            "planned improvement as JSON."
        ),
        "Answer": json.dumps({
            "company_name": "GreenLeaf Electronics",
            "month": "March",
            "total_orders": 250,
            "on_time_orders": 220,
            "delayed_orders": 30,
            "complaints": 18,
            "support_email": "support@greenleaf.example",
            "planned_improvement": (
                "Improve delivery tracking next month"
            )
        }, ensure_ascii=False),
        "Rating": 5,
        "Improvement": (
            "Validate the JSON and verify each extracted value "
            "against the original text."
        )
    },
    {
        "Task": "Translation",
        "Prompt": (
            "Translate the sample text into Tamil, preserving numbers "
            "and the email address."
        ),
        "Answer": (
            "மார்ச் மாதத்தில் GreenLeaf Electronics நிறுவனம் "
            "250 வாடிக்கையாளர் ஆர்டர்களைப் பெற்றது. அவற்றில் "
            "220 ஆர்டர்கள் சரியான நேரத்தில் வழங்கப்பட்டன; "
            "30 ஆர்டர்கள் தாமதமானது. தாமதமான விநியோகம் குறித்து "
            "18 புகார்கள் வந்தன. வாடிக்கையாளர்கள் "
            "support@greenleaf.example என்ற மின்னஞ்சலில் "
            "தொடர்புகொள்ளலாம். அடுத்த மாதம் விநியோகக் கண்காணிப்பு "
            "அமைப்பை மேம்படுத்த நிறுவனம் திட்டமிட்டுள்ளது."
        ),
        "Rating": 4,
        "Improvement": (
            "Ask a fluent Tamil speaker to verify grammar, meaning, "
            "and terminology."
        )
    },
    {
        "Task": "Code Generation",
        "Prompt": (
            "Write a Python function delivery_rate(delivered, total) "
            "that returns the percentage rounded to two decimal places "
            "and safely handles total = 0."
        ),
        "Answer": (
            "def delivery_rate(delivered, total):\n"
            "    if total == 0:\n"
            "        return 0.0\n"
            "    return round((delivered / total) * 100, 2)\n\n"
            "print(delivery_rate(220, 250))\n"
            "# Output: 88.0"
        ),
        "Rating": 5,
        "Improvement": (
            "Test zero totals, invalid inputs, and negative values."
        )
    }
]


# ==================================================
# WORD AND TOKEN ESTIMATION
# ==================================================

def estimate_tokens(text):
    """
    Approximate English token count.
    This is NOT an actual tokenizer measurement.
    Tamil and JSON counts may be less accurate.
    """
    return max(1, round(len(text) / 4))


def count_words(text):
    return len(re.findall(r"\b[\w@.-]+\b", text, re.UNICODE))


# ==================================================
# MANUAL EVALUATION AND CSV OUTPUT
# ==================================================

results = []

print("=" * 75)
print("TASK 1: CAPABILITIES LAB - MANUAL MODE")
print("=" * 75)

for item in tasks:
    # This times the local record-processing operation,
    # NOT an actual LLM call.
    start = time.perf_counter()

    prompt = item["Prompt"]
    answer = item["Answer"]

    input_tokens = estimate_tokens(prompt + "\n" + sample_text)
    output_tokens = estimate_tokens(answer)
    total_tokens = input_tokens + output_tokens

    elapsed = time.perf_counter() - start

    row = {
        "Task": item["Task"],
        "Prompt": prompt,
        "Sample Text": sample_text,
        "Answer": answer,
        "Rating (1-5)": item["Rating"],
        "Input Tokens (estimated)": input_tokens,
        "Output Tokens (estimated)": output_tokens,
        "Total Tokens (estimated)": total_tokens,
        "Processing Time (seconds)": round(elapsed, 6),
        "Improvement": item["Improvement"]
    }

    results.append(row)

    print(f"\nTask: {item['Task']}")
    print(f"Prompt: {prompt}")
    print(f"Answer:\n{answer}")
    print(f"Rating: {item['Rating']}/5")
    print(f"Estimated total tokens: {total_tokens}")
    print(f"Local processing time: {elapsed:.6f} seconds")
    print(f"Improvement: {item['Improvement']}")


# Save complete results
fieldnames = list(results[0].keys())

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("\n" + "=" * 75)
print(f"Results saved successfully to: {OUTPUT_FILE}")
print("=" * 75)


# ==================================================
# BEST AND WORST TASK
# ==================================================

best = max(results, key=lambda row: row["Rating (1-5)"])
worst = min(results, key=lambda row: row["Rating (1-5)"])

print("\nFOUR-LINE EVALUATION")
print(f"1. Best task: {best['Task']} ({best['Rating (1-5)']}/5).")
print("2. Structured outputs are easier to validate against source facts.")
print(f"3. Lowest-rated task: {worst['Task']} ({worst['Rating (1-5)']}/5).")
print("4. Improve it by checking the answer against clear quality criteria.")
print("\nNote: Answers and ratings are manually prepared examples.")
print("Token counts are estimates, not measured tokenizer usage.")
print("Processing time is local runtime, not LLM response latency.")
