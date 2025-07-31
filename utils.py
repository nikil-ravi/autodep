import json
import logging
from typing import List

from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu

logger = logging.getLogger(__name__)


def calc_bleu(candidate: str, reference: str) -> float:
    """
    Compute BLEU score for a single candidate against a reference.
    Higher BLEU score is better (closer to 1.0), measuring n-gram overlap.
    """
    ref_tokens = reference.split()
    cand_tokens = candidate.split()
    smoothing = SmoothingFunction().method4
    return sentence_bleu([ref_tokens], cand_tokens, smoothing_function=smoothing)


def calc_overall_bleu(
    jsonl_file: str, score_key: str = "original_stmt_bleu_score"
) -> float:
    """
    Compute the average BLEU score from a JSONL file containing per-sample scores.
    """
    scores: List[float] = []
    with open(jsonl_file, "r") as f:
        for line in f:
            data = json.loads(line)
            logger.info(data.keys())
            if score_key in data:
                scores.append(data[score_key])

    if not scores:
        raise ValueError("No scores found in the file")

    return sum(scores) / len(scores)
