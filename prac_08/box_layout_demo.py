"""
Demonstrate a box layout, with simple buttons, a text input and a label.
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Create a Box Layout Demo App."""
    def build(self):
        """Build the Box Layout demo App."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Change label's text to a greeting of the name typed into the textbox."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear the app's text field and label."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
