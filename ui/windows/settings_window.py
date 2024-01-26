import customtkinter as ctk

def show():
    window = ctk.CTkToplevel(fg_color="#111111")
    window.title("Projet LLM - Paramètres")
    window.geometry("320x475")
    window.resizable(False, False)

    ctk.CTkLabel(window, text="Paramètres", font=("Arial", 18), text_color="#FFFFFF").pack(side=ctk.TOP, pady=(10, 0))

    # STEPS

    ctk.CTkLabel(window, text="Steps", font=("Arial", 14), text_color="#FFFFFF").pack(side=ctk.TOP, pady=(20, 0))

    def handleStepsSliderChange(e):
        steps = int(steps_slider.get())

        steps_input.delete(0, ctk.END)
        steps_input.insert(0, steps)

    steps_slider = ctk.CTkSlider(window, from_=50, to=1000, fg_color="#505050", progress_color="#7616A3", button_color="#931ECA", button_hover_color="#621288", command=handleStepsSliderChange)
    steps_slider.pack(side=ctk.TOP, pady=(10, 0))

    def handleStepsInputKeypress(e):
        if e.char not in "0123456789":
            return "break"

        steps = int(steps_input.get())
        print(steps)
        steps_slider.set(steps)

    steps_input = ctk.CTkEntry(window, placeholder_text="CTkEntry")
    steps_input.bind("<KeyPress>", handleStepsInputKeypress)
    steps_input.pack(side=ctk.TOP, pady=(10, 0))

    def handleLlamaModelClick():
        dir = ctk.filedialog.askdirectory()
        print(dir)

    ctk.CTkButton(master=window, text="Charger un modèle", fg_color="#8217B5", cursor="hand2", command=handleLlamaModelClick).pack(side=ctk.BOTTOM, pady=(0, 15))

    # SAVE

    ctk.CTkButton(master=window, text="Sauvegarder", fg_color="#8217B5", cursor="hand2", command=print).pack(side=ctk.BOTTOM, pady=(0, 15))

    return window