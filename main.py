from datasets import load_dataset
import logging
logging.basicConfig(level=logging.INFO)
from autoformalize import autoformalize

def load_proofnet_data(hf_dataset_name: str = "proofnet/proofnet-lean4"):
    if hf_dataset_name == "proofnet/proofnet-lean4":
        # all splits
        return load_dataset("json", data_files="data/proofnet/proofnet-lean4.jsonl", split="all")
    elif hf_dataset_name == "hoskinson-center/proofnet":
        return load_dataset(hf_dataset_name, split="all")
    else:
        raise ValueError(f"Unknown dataset: {hf_dataset_name}")


def main():
    logging.info("Starting to run autodep...")
    dataset = load_proofnet_data()
    logging.info(f"Loaded {len(dataset)} examples")
    for example in dataset:
        logging.info(example)
        formalized = autoformalize(example)
        break



if __name__ == "__main__":
    main()
