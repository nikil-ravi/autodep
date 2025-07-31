import json
import logging
import os

import openai

from autoformalize import autoformalize
from utils import calc_bleu


def generate_implication(statement: str, model: str = "gpt-4o-mini") -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    client = openai.OpenAI(api_key=api_key)

    # Hardcoded example
    example_input = """If a function is continuous on a closed interval, then it attains its maximum
        and minimum values."""

    example_output = """If a continuous function on a closed interval has a maximum value,
        that maximum is attained at some point in the interval."""

    messages = [
        {
            "role": "system",
            "content": """You are an expert mathematician. Given a mathematical statement, generate another informal
                            statement that logically follows from it
                            as a direct consequence (i.e, a necessary and sufficient condition).""",
        },
        {
            "role": "user",
            "content": f'Generate a statement that follows from: "{example_input}"',
        },
        {"role": "assistant", "content": example_output},
        {
            "role": "user",
            "content": f'Generate a statement that follows from: "{statement}"',
        },
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=300,
        temperature=0.7,
    )

    dependent_stmt = response.choices[0].message.content.strip()
    logging.info(f"Generated dependent statement: {dependent_stmt}")
    return dependent_stmt


def generate_deps_and_formalize(
    dataset, output_file: str = "data/proofnet/generated_implications.jsonl"
):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        for sample in dataset:

            # formalize the original statement
            formalized_original = autoformalize(sample)

            # generate the implication, formalize it
            implication = {
                "informal_stmt": generate_implication(sample["informal_stmt"])
            }
            formalized_implication = autoformalize(implication)
            bleu_score = calc_bleu(formalized_original, sample["formal_statement"])

            # create the new row for the jsonl and write it
            updated_sample = sample.copy()
            updated_sample["generated_implication"] = implication
            updated_sample["formalized_original"] = formalized_original
            updated_sample["formalized_implication"] = formalized_implication
            updated_sample["original_stmt_bleu_score"] = bleu_score
            json.dump(updated_sample, f, ensure_ascii=False)
            f.write("\n")

    logging.info(f"Saved generated implications and formalizations to {output_file}")
