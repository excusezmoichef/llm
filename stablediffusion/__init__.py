from dataclasses import dataclass
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image, ImageTk

@dataclass
class TextToImageOptions:
    prompt: str
    model: str
    num_inference_steps: int = 50
    width: int = 256
    height: int = 256
    output: str = "output"

def run(options: TextToImageOptions):
    pipe = StableDiffusionPipeline.from_pretrained(options.model, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")

    image = pipe(options.prompt, num_inference_steps=options.num_inference_steps, width=options.width, height=options.height).images[0]

    image.save("output/" + str(options.output) + ".png")

    return image
