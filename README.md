# Generative AI and LLM Practical Tasks

## Description
This repository contains practical assignments exploring Large Language Models (LLMs), foundation models, tokenization, API cost estimation, model capabilities, and common AI limitations. The tasks demonstrate how LLMs work, how to evaluate their outputs, and how to build more reliable AI applications.

## Tasks Included

### Task 1: Foundation Models Comparison
- Compare GPT (OpenAI), Claude (Anthropic), Llama (Meta), and Gemini (Google).
- Understand open-weight and closed-weight models.
- Learn about pre-training, foundation models, and context windows.
- Identify common tasks foundation models can perform without retraining.
- Recommend models for customer support and private on-premise document processing.

### Task 2: Tokens and Cost
- Install and use the `tiktoken` library.
- Count tokens in a sentence, paragraph, page-style text, JSON object, and Tamil sentence.
- Calculate words per token and compare with the 0.75 rule of thumb.
- Estimate API costs using input and output token prices.
- Check text lengths against 8K and 128K context windows.
- Compare tokenization using two different encodings.

**Main file:** `task2_tokens_cost.py`

### Task 3: Capabilities Lab
- Test summarization, classification, information extraction, translation, and code generation.
- Record prompts and model responses.
- Evaluate output correctness using a 1–5 rating scale.
- Record token usage and response time when available.
- Identify the best-performing and weakest tasks.

**Main file:** `task1_capabilities_lab.py`

**Output file:** `capabilities_lab_results.csv`

### Task 4: LLM Limitations Lab
- Explore knowledge cutoffs and recent-event questions.
- Test hallucinations using a fictional research paper.
- Examine retrieval of facts from longer text.
- Verify multi-step arithmetic and logic puzzle answers.
- Compare temperature settings 0 and 1.0.
- Identify five safeguards for business AI applications.

**Main file:** `task2_llm_limitations.py`

**Output files:**
- `llm_limitations_results.csv`
- `llm_safeguards_bonus.json`

## Technologies Used
- Python
- OpenAI API and chat tools
- `tiktoken`
- CSV and JSON
- Python standard libraries

## Installation

Install the required packages:

```bash
python -m pip install tiktoken openai
```

The `openai` package is required only for API-based experiments. The offline demonstration scripts do not require an API key.

## How to Run

Run the tokenization and cost assignment:

```bash
python task2_tokens_cost.py
```

Run the Capabilities Lab:

```bash
python task1_capabilities_lab.py
```

Run the LLM Limitations Lab:

```bash
python task2_llm_limitations.py
```

The Foundation Models Comparison is a research-based task completed using official documentation and comparison tables.

## Key Learnings
- Differences between foundation model families and their deployment options.
- Tokenization, context limits, and API pricing calculations.
- Practical applications of LLMs across multiple tasks.
- Evaluation of model correctness, latency, and output quality.
- Hallucinations, reasoning errors, and context retrieval limitations.
- Safeguards for developing reliable business AI applications.

## Important Notes
Some scripts use predefined sample responses for offline demonstrations. These are not live LLM evaluations. Actual model responses, token counts, and latency measurements should be recorded separately when required. API prices and model specifications may change, so consult official provider documentation.

## Official References
- [OpenAI Models](https://developers.openai.com/api/docs/models)
- [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI tiktoken](https://github.com/openai/tiktoken)
- [Anthropic Claude Documentation](https://platform.claude.com/docs/en/models/overview)
- [Meta Llama](https://dev.meta.ai/llama)
- [Google Gemini Models](https://ai.google.dev/gemini-api/docs/models)

## Conclusion
These practical tasks build a foundation in Generative AI and LLM development, covering model selection, tokenization, cost estimation, capability evaluation, and risk mitigation. They demonstrate the importance of verifying AI outputs and selecting suitable safeguards before deploying AI systems in real-world applications.

## Author
Dhanush S
