"""CePO-QA

If you have any questions or want to contribute, please reach out to us on [cerebras.ai/discord](https://cerebras.ai/discord).
"""

import os
import sys
import importlib.util
from typing import Tuple

SLUG = "cepo_qa"

def run(system_prompt: str, initial_query: str, client, model: str) -> Tuple[str, int]:
    # Get the directory where this plugin is located
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    cepo_qa_dir = os.path.join(plugin_dir, 'long_context/cepo_qa')
    main_file = os.path.join(cepo_qa_dir, 'main.py')

    # Load the main module dynamically
    spec = importlib.util.spec_from_file_location("cepo_qa_main", main_file)
    cepo_qa_main = importlib.util.module_from_spec(spec)

    # Add the longcepo directory to the Python path temporarily
    if cepo_qa_dir not in sys.path:
        sys.path.insert(0, cepo_qa_dir)

    try:
        spec.loader.exec_module(cepo_qa_main)
        return cepo_qa_main.run_cepo_qa(system_prompt, initial_query, client, model)
    finally:
        # Remove from path after use
        if cepo_qa_dir in sys.path:
            sys.path.remove(cepo_qa_dir)
