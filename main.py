import os
import ui.windows.main_window as main_window

if not os.path.isdir("output"):
    os.mkdir("output")

main_window.show()