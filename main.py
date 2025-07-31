import logging

from datasets import load_dataset

from generate_deps import generate_deps_and_formalize
from utils import calc_overall_bleu

logging.basicConfig(level=logging.INFO)


def load_proofnet_data(hf_dataset_name: str = "proofnet/proofnet-lean4"):
    if hf_dataset_name == "proofnet/proofnet-lean4":
        # all splits
        return load_dataset(
            "json", data_files="data/proofnet/proofnet-lean4.jsonl", split="all"
        )
    elif hf_dataset_name == "hoskinson-center/proofnet":
        return load_dataset(hf_dataset_name, split="all")
    else:
        raise ValueError(f"Unknown dataset: {hf_dataset_name}")


def main():
    logging.info("Starting to run autodep...")
    dataset = load_proofnet_data()
    logging.info(f"Loaded {len(dataset)} examples")
    generate_deps_and_formalize(dataset.select(range(10)))
    overall_bleu = calc_overall_bleu("data/proofnet/generated_implications.jsonl")
    logging.info(f"Overall BLEU score: {overall_bleu}")


if __name__ == "__main__":
    main()
