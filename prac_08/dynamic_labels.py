"""
Create a label for each name in a list in the kivy app.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Create a label for each name in a list."""

    def __init__(self, **kwargs):
        """Initialise the App."""
        super().__init__(**kwargs)
        self.names = ["Francesca", "Jamie", "Keya", "Kate"]

    def build(self):
        """Build the App."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Labels for each name in list of names."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
