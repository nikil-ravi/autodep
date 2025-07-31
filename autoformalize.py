import logging
import os

import openai


def autoformalize(sample: dict, model: str = "gpt-4o-mini") -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    client = openai.OpenAI(api_key=api_key)

    informal_stmt = sample["informal_stmt"]

    # Note: These examples are available but not currently used in the prompt
    # example_informal = (
    #     "Suppose that $f$ is holomorphic in an open set $\\Omega$. "
    #     "Prove that if $\\text{Re}(f)$ is constant, then $f$ is constant.\n"
    # )
    # example_formal = (
    #     "theorem Shakarchi_exercise_1_13a {f : ℂ → ℂ} (Ω : Set ℂ) "
    #     "(a b : Ω) (h : IsOpen Ω)\n"
    #     "  (hf : DifferentiableOn ℂ f Ω) "
    #     "(hc : ∃ (c : ℝ), ∀ z ∈ Ω, (f z).re = c) :\n"
    #     "  f a = f b := sorry"
    # )

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert in formalizing mathematical statements into "
                "Lean 4 statements. You will be given an informal statement and "
                "you will need to formalize it into a Lean 4 statement. You only "
                "need to formalize the statement, not the proof."
            ),
        },
        {
            "role": "user",
            "content": f"""
            Example of an informal statement followed by its formalized version:

            \"Let $P$ be a $p$-subgroup of $G$. Then $P$ is contained in a
            Sylow $p$-subgroup of $G$.\"

            theorem exists_le_sylow {{p : ℕ}} {{G : Type*}} [group G]
            {{P : subgroup G}} (hP : is_p_group p P) :
            ∃ (Q : sylow p G), P ≤ Q :=

            Formalize this informal statement into a Lean 4 theorem:

            \"{informal_stmt}\"
         """,
        },
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=500,
        temperature=0.7,
    )

    formalized = response.choices[0].message.content.strip()
    logging.info(f"Generated formalization: {formalized} \n")

    return formalized
