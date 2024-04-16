import tkinter as tk
import pyttsx3

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Text-to-Speech App")

        # Text input field
        self.text_entry = tk.Text(master, height=10, width=50)
        self.text_entry.pack()

        # Customization options
        self.voice_var = tk.StringVar()
        self.voice_var.set("default")  # default voice
        self.rate_var = tk.DoubleVar()
        self.rate_var.set(200)  # default rate (words per minute)

        # Voice selection dropdown
        self.voice_label = tk.Label(master, text="Select Voice:")
        self.voice_label.pack()
        self.voice_dropdown = tk.OptionMenu(master, self.voice_var, "default", "male", "female")
        self.voice_dropdown.pack()

        # Rate adjustment slider
        self.rate_label = tk.Label(master, text="Adjust Rate:")
        self.rate_label.pack()
        self.rate_slider = tk.Scale(master, from_=100, to=300, orient=tk.HORIZONTAL, variable=self.rate_var)
        self.rate_slider.pack()

        # Buttons
        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(master, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        # Text-to-speech engine
        self.engine = pyttsx3.init()

    def play(self):
        text = self.text_entry.get("1.0", tk.END)
        self.engine.setProperty('rate', self.rate_var.get())
        if self.voice_var.get() == "default":
            self.engine.setProperty('voice', self.engine.getProperty('voices')[0].id)
        else:
            self.engine.setProperty('voice', self.voice_var.get())
        self.engine.say(text)
        self.engine.runAndWait()

    def pause(self):
        self.engine.pause()

    def stop(self):
        self.engine.stop()

def main():
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
