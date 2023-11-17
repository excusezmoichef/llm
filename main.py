import llama2_py
llama2_py.run({"checkpoint": "stories15M.bin", "temperature": 0.0, "steps": 256, "prompt": "A story about an elf and a dwarf."})