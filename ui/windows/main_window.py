import time
import customtkinter as ctk
import webbrowser
from PIL import Image, ImageTk
import json
import os.path

import ui.windows.settings_window as settings_window

import stablediffusion as sd
import llama

# LOAD SETTINGS

with open('settings.json', 'r') as file:
    settings = json.load(file)

# MAIN WINDOW
app = ctk.CTk(fg_color="#111111")
app.title("Projet LLM")
app.geometry("640x475")
app.resizable(False, False)

llm_label = ctk.CTkLabel(app, text="Projet LLM", font=("Arial", 18), text_color="#FFFFFF")
llm_label.place(relx=0.01, rely=0.01, anchor='nw')

textbox = ctk.CTkTextbox(app, height=5, width=300, font=("Arial", 14), fg_color="#282828", text_color="#FFFFFF", corner_radius=10)
textbox.pack(side=ctk.TOP, pady=(50, 0))

def run():
    run_button.configure(text="En cours...", state="disabled")

    prompt = textbox.get("0.0", "end").strip()

    llama_result = llama.run(prompt, "models/" + settings["text_model"], max_tokens=settings["max_tokens"])

    print("\nprompt: " + prompt + "\nresult: " + llama_result + "\n")

    output = time.time()
    img = sd.run(sd.TextToImageOptions(prompt=prompt + llama_result, model="models/" + settings["image_model"], output=time.time(), num_inference_steps=100))

    data = {}
    if os.path.isfile('output/history.json'):
        with open('output/history.json', 'r') as file:
            data = json.load(file)

    data[output] = {
        "prompt": prompt,
        "image": str(output) + ".png",
    }

    with open('output/history.json', 'w') as file:
        file.write(json.dumps(data))

    img = img.resize((200, 200), Image.ADAPTIVE)
    img = ImageTk.PhotoImage(img)
    img_label.configure(image=img)

    run_button.configure(text="Lancer", state="normal")

run_button = ctk.CTkButton(master=app, text="Lancer", fg_color="#8217B5", cursor="hand2", command=run)
run_button.pack(side=ctk.TOP, pady=15)

img_label = ctk.CTkLabel(app, text="")
img_label.pack(side=ctk.TOP, pady=15)

settings_label = ctk.CTkLabel(app, text="", image=ImageTk.PhotoImage(Image.open("ui/assets/settings_icon.png").resize((20, 20))), cursor="hand2")
settings_label.bind("<Button-1>", lambda e: settings_window.show())
settings_label.place(relx=0.99, rely=0.01, anchor='ne')

history_label = ctk.CTkLabel(app, text="", image=ImageTk.PhotoImage(Image.open("ui/assets/history_icon.png").resize((20, 20))), cursor="hand2")
history_label.place(relx=0.99, rely=0.99, anchor='se')

credit_label = ctk.CTkLabel(app, text="Un projet du groupe excusezmoichef", text_color="#FFFFFF", font=("Arial", 16), cursor="hand2")
credit_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/orgs/excusezmoichef/people"))
credit_label.pack(side=ctk.BOTTOM)

gh_label = ctk.CTkLabel(app, text="Github", text_color="#FFFFFF", font=("Arial", 16, "bold"), cursor="hand2")
gh_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/excusezmoichef/llm"))
gh_label.pack(side=ctk.BOTTOM)

def show():
    app.mainloop()