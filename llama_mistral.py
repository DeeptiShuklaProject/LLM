
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ModelRunner:
    def __init__(self, model_name):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_text(self, prompt, max_length=50):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs.input_ids, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

def run_model(model_name, prompt, max_length=50):
    runner = ModelRunner(model_name)
    return runner.generate_text(prompt, max_length)

if __name__ == "__main__":
    model_name = "decapoda-research/llama-2"  # Replace with the correct model path
    prompt = "Once upon a time"
    print(run_model(model_name, prompt))
