
import csv
import time
import json
from pathlib import Path

# ============================================================
# LLM LIMITATIONS LAB
# Offline demonstration - no API key required
# ============================================================

OUTPUT_FILE = "llm_limitations_results.csv"


def record_experiment(name, prompt, response, expected, observation):
    """Store an experiment and its evaluation."""

    result = {
        "Experiment": name,
        "Prompt": prompt,
        "Response": response,
        "Expected Answer": expected,
        "Observation": observation
    }

    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)
    print("Prompt:", prompt)
    print("Response:", response)
    print("Expected:", expected)
    print("Observation:", observation)

    return result


results = []


# ============================================================
# EXPERIMENT 1: KNOWLEDGE CUTOFF
# ============================================================

prompt1 = (
    "Who won the most recent Nobel Prize in Physics announced "
    "in 2026? Give the winner, discovery, and announcement date. "
    "If unsure, say so instead of guessing."
)

# Demonstration response, not a live model response
response1 = (
    "I cannot confirm the 2026 Nobel Prize in Physics winner "
    "without checking a current, reliable source."
)

results.append(record_experiment(
    "Knowledge Cutoff",
    prompt1,
    response1,
    "A verified answer from the official Nobel Prize website, "
    "or an explicit admission of uncertainty.",
    "Recent events require up-to-date sources. Verify at "
    "https://www.nobelprize.org/prizes/physics/"
))


# ============================================================
# EXPERIMENT 2: HALLUCINATION
# ============================================================

fictional_paper = (
    '"Quantum-Aware Neural Alignment for Universal Reasoning", '
    "by Dr. Elena Markov and Dr. James Whitmore, "
    "published in Nature AI Research in 2025."
)

prompt2a = (
    "Summarize this paper, including methodology, findings, and DOI: "
    + fictional_paper
)

response2a = (
    "[Sample response] The model may invent a methodology, "
    "findings, authorship details, or a DOI. Record the actual "
    "response from your chosen LLM."
)

results.append(record_experiment(
    "Hallucination - Without Safeguard",
    prompt2a,
    response2a,
    "The model should not present unverified publication details "
    "as facts.",
    "Check whether the paper and DOI actually exist."
))

prompt2b = (
    prompt2a
    + " If you cannot verify that this paper exists, say "
    "'I don't know'. Do not invent any details."
)

response2b = (
    "[Sample response] I cannot verify that this paper exists, "
    "so I don't know its methodology, findings, or DOI."
)

results.append(record_experiment(
    "Hallucination - With Safeguard",
    prompt2b,
    response2b,
    "An honest statement of uncertainty when the reference "
    "cannot be verified.",
    "Compare the actual model responses from both tests."
))


# ============================================================
# EXPERIMENT 3: CONTEXT LENGTH
# ============================================================

long_text = """
BUSINESS REPORT

The company was established in 2018.
It operates in five Indian states.
Its headquarters are in Chennai.
The company sells software to small businesses.
Its annual customer survey received 2,000 responses.

The internal project code for the customer-support automation
initiative is PROJECT-ORCHID-7294.
This code identifies the pilot project in internal reports.

The company plans to expand its sales team.
It currently employs 120 people.
Customer satisfaction is reviewed every quarter.
The next product release is planned for December.
"""

context_question = (
    "What is the internal project code mentioned in the report? "
    "Return only the code."
)

# Simulated context retrieval check
expected_code = "PROJECT-ORCHID-7294"
retrieved_code = (
    expected_code if expected_code in long_text else "NOT FOUND"
)

results.append(record_experiment(
    "Context Length",
    context_question,
    retrieved_code,
    expected_code,
    "The offline check confirms that the fact exists in the text. "
    "Test an actual LLM with increasingly long documents to assess "
    "its retrieval ability."
))


# ============================================================
# EXPERIMENT 4A: MULTI-STEP ARITHMETIC
# ============================================================

prompt4a = (
    "A shop has 240 products. It sells 25% in the morning, then "
    "20% of the remaining products in the afternoon. How many "
    "products remain? Show your calculations."
)

morning_sold = 240 * 0.25
after_morning = 240 - morning_sold
afternoon_sold = after_morning * 0.20
final_products = after_morning - afternoon_sold

arithmetic_response = (
    f"Morning sold: {morning_sold:.0f}\n"
    f"After morning: {after_morning:.0f}\n"
    f"Afternoon sold: {afternoon_sold:.0f}\n"
    f"Remaining: {final_products:.0f}"
)

results.append(record_experiment(
    "Reasoning - Arithmetic",
    prompt4a,
    arithmetic_response,
    "144 products",
    "Verified using Python arithmetic. This checks the calculation, "
    "not an actual LLM's reasoning."
))


# ============================================================
# EXPERIMENT 4B: LOGIC PUZZLE
# ============================================================

prompt4b = (
    "Three boxes are labelled Apples, Oranges, and Mixed. Every "
    "label is incorrect. Pick one fruit from one box. How can all "
    "three boxes be labelled correctly?"
)

logic_response = """
1. Pick one fruit from the box labelled Mixed.
2. Because every label is wrong, this box cannot contain a mixture.
3. If you pick an apple, that box contains only apples; if you pick
   an orange, it contains only oranges.
4. Use the remaining incorrect labels and elimination to identify
   the other two boxes.
"""

results.append(record_experiment(
    "Reasoning - Logic Puzzle",
    prompt4b,
    logic_response,
    "Pick from the box labelled Mixed, then use the fruit and "
    "the incorrect-label constraint to identify all boxes.",
    "Check the deductions against all three labels."
))


# ============================================================
# FIVE BUSINESS SAFEGUARDS
# ============================================================

safeguards = [
    (
        "Verify recent information",
        "Use trusted, up-to-date sources and record retrieval dates."
    ),
    (
        "Prevent hallucinations",
        "Require supporting evidence and allow 'I don't know'."
    ),
    (
        "Manage context limits",
        "Chunk long documents and retrieve relevant passages with RAG."
    ),
    (
        "Validate calculations",
        "Use Python or a deterministic calculation engine for arithmetic."
    ),
    (
        "Human review and testing",
        "Require human approval for high-impact decisions and test regularly."
    )
]

print("\n" + "=" * 70)
print("FIVE BUSINESS SAFEGUARDS")
print("=" * 70)

for index, (name, description) in enumerate(safeguards, start=1):
    print(f"{index}. {name}: {description}")


# ============================================================
# BONUS: TEMPERATURE 0 VS 1.0
# ============================================================

print("\n" + "=" * 70)
print("BONUS: TEMPERATURE COMPARISON")
print("=" * 70)

bonus_results = [
    {
        "Temperature": 0,
        "Prompt": prompt2b,
        "Observation": (
            "Test with an LLM interface that exposes temperature. "
            "Check consistency and unsupported claims."
        )
    },
    {
        "Temperature": 1.0,
        "Prompt": prompt2b,
        "Observation": (
            "Repeat the same prompt and compare variation in the "
            "response. Higher temperature does not guarantee hallucination."
        )
    }
]

for item in bonus_results:
    print(f"\nTemperature: {item['Temperature']}")
    print("Prompt:", item["Prompt"])
    print("Observation:", item["Observation"])


# ============================================================
# SAVE RESULTS TO CSV
# ============================================================

fieldnames = [
    "Experiment",
    "Prompt",
    "Response",
    "Expected Answer",
    "Observation"
]

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("\nResults saved to:", Path(OUTPUT_FILE).resolve())

# Save safeguards and bonus experiment to a JSON file
with open(
    "llm_safeguards_bonus.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        {
            "safeguards": [
                {"name": name, "description": description}
                for name, description in safeguards
            ],
            "bonus_experiments": bonus_results
        },
        file,
        indent=4,
        ensure_ascii=False
    )

print("Safeguards saved to: llm_safeguards_bonus.json")
print("\nLab completed.")
print("Reminder: Replace sample responses with actual LLM outputs")
print("before claiming that live experiments were performed.")
