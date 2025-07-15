import re
from typing import Tuple
from functools import partial

from transformers import AutoTokenizer, PreTrainedTokenizerBase

# Use relative imports that work within the dynamically loaded module
from .config import CepoQAConfig
from ..common.utils import (
    get_prompt_response,
    logger,
    longcepo_init,
    loop_until_match,
    CBLog,
)


def cepo_qa_init(
    initial_query: str,
) -> Tuple[str, str, PreTrainedTokenizerBase, CBLog, CepoQAConfig]:
    """
    Initializes context, query, tokenizer, logging, and config from an input string.

    Args:
        initial_query (str): Input string containing context and query separated by a delimiter string.

    Returns:
        Tuple[str, str, PreTrainedTokenizerBase, CBLog, CepoQAConfig]:
        Parsed context, query, tokenizer instance, log object, and LongCePO config.
    """
    cb_log = CBLog()
    config = CepoQAConfig()
    context, query = initial_query.split(config.context_query_delimiter)
    tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    return context.strip(), query.strip(), tokenizer, cb_log, config


def run_cepo_qa(
    system_prompt: str, initial_query: str, client, model: str
) -> Tuple[str, int]:
    """
    CePO-QA

    Args:
        system_prompt (str): System prompt string.
        initial_query (str): Raw input string containing context and query separated by delimiter string.
        client: LLM API client instance.
        model (str): Base model name.

    Returns:
        Tuple[str, int]: Final answer and total number of tokens used across the pipeline.
    """
    context, query, tokenizer, cb_log, cepo_qa_config = cepo_qa_init(initial_query)

    # ...
    answer = ""

    return answer, cb_log["total_tokens"]
