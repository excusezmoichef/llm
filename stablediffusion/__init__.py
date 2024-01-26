from dataclasses import dataclass
from diffusers import StableDiffusionPipeline
import torch

@dataclass
class TextToImageOptions:
    prompt: str
    model: str
    num_inference_steps: int = 50
    width: int = 512
    height: int = 512
    output: str = "output"

def run(options: TextToImageOptions):
    pipe = StableDiffusionPipeline.from_pretrained(options.model, torch_dtype=torch.float16, safety_checker=None)
    pipe = pipe.to("cuda")

    image = pipe(options.prompt, num_inference_steps=options.num_inference_steps, width=options.width, height=options.height).images[0]

    image.save("output/" + str(options.output) + ".png")

    return image
