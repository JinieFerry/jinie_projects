# Import necessary modules
from tkinter import Tk, Canvas, Text, Button, PhotoImage
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pathlib import Path

# Paths for assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\MSI\Desktop\Jinie\instant_jinie_voice_finalPt\instant_jinie_voice\instant_jinie_voice_3\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize ElevenLabs client
client = ElevenLabs(
    api_key="e75347c1353dd3083be81b47c4705fd6",  # Defaults to ELEVEN_API_KEY
)

# Function to generate and play voice
def generate_voice():
    text = entry_1.get("1.0", "end-1c")  # Get text from Text widget
    if text.strip():
        audio = client.generate(
            text=text,
            voice="TanIbI9Mp3LZpER1QOuv",  # Try Nicole
            model="eleven_multilingual_v2"
        )
        play(audio)

# Create the main window
window = Tk()
window.geometry("1280x720")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Add background image
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
canvas.create_image(
    640.0,
    360.0,
    image=image_image_1
)

# Add title text
canvas.create_text(
    438.0,
    155.0,
    anchor="nw",
    text="Type Here and Press the Button",
    fill="#000000",
    font=("RobotoRoman SemiBold", 24 * -1)
)

# Add button to generate voice
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=generate_voice,
    relief="flat"
)
button_1.place(
    x=171.0,
    y=287.0,
    width=875.0,
    height=84.0
)

# Add text entry field
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    608.5,
    235.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#E5D9CD",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=171.0,
    y=193.0,
    width=875.0,
    height=82.0
)

# Rectangle for aesthetics
canvas.create_rectangle(
    162.0,
    397.0,
    1046.0,
    406.0,
    fill="#FFFFFF",
    outline=""
)

window.resizable(False, False)
window.mainloop()

#same as instant_jinie_voice_3.py yet