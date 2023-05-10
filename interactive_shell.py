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
tokenizer = AutoTokenizer.from_pretrained(MODEL_SOURCE)
tokenizer.pad_token = tokenizer.eos_token

while x := input("Your prompt (enter to exit): "):
    # tokenize the inputs
    inputs = tokenizer("Hello, my name is", return_tensors="pt")
    # i don't know what device HF will map the model to (since it varies based on how much GPU vram you have)
    # so this will assign it to the same device as the first layer of the model, which should work on all devices
    inputs.to(model.hf_device_map['transformer.wte'])
    # call model generation. You should not need more than 10 new generated tokens, this will save computation
    output = model.generate(inputs["input_ids"], max_new_tokens=10)
    # decode the model outputs
    tokenizer.decode(output[0].tolist())

print("=== END ===")
