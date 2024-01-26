from llama_cpp import Llama

def run(prompt: str, model_gguf: str, max_tokens: int = 50):
    LLM = Llama(model_path=model_gguf)

    output = LLM(prompt, max_tokens=max_tokens)

    return output["choices"][0]["text"]