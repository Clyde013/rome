# pip install the relevant pytorch version for your device
# pip install transformers, accelerate

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# specify the source of the downloaded blahaj-llm weights here
MODEL_SOURCE = "../blahaj-llm/"

# empties cache just in case
torch.cuda.empty_cache()

# load models from weights
model = AutoModelForCausalLM.from_pretrained(MODEL_SOURCE, device_map="auto", torch_dtype=torch.float16)
# load tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
tokenizer.pad_token = tokenizer.eos_token
print(tokenizer.special_tokens_map)
print(tokenizer.pad_token_id)
while x := input("Your prompt (enter to exit): "):
    # tokenize the inputs
    inputs = tokenizer(x, return_tensors="pt")
    # i don't know what device HF will map the model to (since it varies based on how much GPU vram you have)
    # so this will assign it to the same device as the first layer of the model, which should work on all devices
    inputs.to(next(model.transformer.wte.parameters()).device)
    # call model generation. You should not need more than 10 new generated tokens, this will save computation
    output = model.generate(**inputs, max_new_tokens=10, pad_token_id=tokenizer.pad_token_id)
    # decode the model outputs
    print(tokenizer.decode(output[0].tolist(), skip_special_tokens=True))

print("=== END ===")
