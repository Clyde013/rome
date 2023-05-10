"""
Runs ROME on GPTJ using hparams specified in hparams.py
because I'm lazy to make a proper yml file.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from util import nethook
from util.generate import generate_interactive, generate_fast

from experiments.py.demo import demo_model_editing, stop_execution

import hparams

MODEL_NAME = "EleutherAI/gpt-j-6B"
torch.cuda.empty_cache()

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16).to('cuda').half()
tok = AutoTokenizer.from_pretrained(MODEL_NAME)
tok.pad_token = tok.eos_token

print("=== REQUEST ===")
print(hparams.request)
print("=== GENERATION PROMPTS ===")
print(hparams.generation_prompts)

ALG_NAME = "ROME"

# Restore fresh copy of model
try:
    with torch.no_grad():
        for k, v in orig_weights.items():
            nethook.get_parameter(model, k)[...] = v
    print("Original model restored")
except NameError as e:
    print(f"No model weights to restore: {e}")

# Execute rewrite
model_new, orig_weights = demo_model_editing(
    model, tok, hparams.request, hparams.generation_prompts, alg_name=ALG_NAME
)

model_new.save_pretrained("../blahaj-llm", from_pt=True)
