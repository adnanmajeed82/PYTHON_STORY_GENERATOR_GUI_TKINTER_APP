import tkinter as tk
from tkinter import ttk
import random

class StoryGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Story Generator")

        self.create_widgets()

    def create_widgets(self):
        # Labels
        ttk.Label(self.root, text="Character:").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
        ttk.Label(self.root, text="Setting:").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
        ttk.Label(self.root, text="Plot:").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)

        # Entry widgets
        self.character_entry = ttk.Entry(self.root, width=30)
        self.character_entry.grid(column=1, row=0, padx=10, pady=10, sticky=tk.W)

        self.setting_entry = ttk.Entry(self.root, width=30)
        self.setting_entry.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

        self.plot_entry = ttk.Entry(self.root, width=30)
        self.plot_entry.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

        # Generate button
        ttk.Button(self.root, text="Generate Story", command=self.generate_story).grid(column=0, row=3, columnspan=2, pady=20)

        # Story display area
        self.story_text = tk.Text(self.root, width=50, height=10, wrap=tk.WORD)
        self.story_text.grid(column=0, row=4, columnspan=2, padx=10, pady=10, sticky=tk.W)

    def generate_story(self):
        character = self.character_entry.get()
        setting = self.setting_entry.get()
        plot = self.plot_entry.get()

        if not character or not setting or not plot:
            self.story_text.delete(1.0, tk.END)
            self.story_text.insert(tk.END, "Please fill in all the fields.")
        else:
            story = self.generate_random_story(character, setting, plot)
            self.story_text.delete(1.0, tk.END)
            self.story_text.insert(tk.END, story)

    def generate_random_story(self, character, setting, plot):
        story_templates = [
            "{} was walking in {}. Suddenly, {} happened.",
            "something special new , creating study ",
            "start watching movie",
            "start creating assignments",
            "In {}, {} was surprised by {}.",
            "writing story for featuring animation",
            "developing new projects and idea",
            "{} found themselves in {}, facing a challenging {}."
        ]

        selected_template = random.choice(story_templates)
        return selected_template.format(character, setting, plot)


if __name__ == "__main__":
    root = tk.Tk()
    app = StoryGenerator(root)
    root.mainloop()
