"""
Build and use the kv app to convert miles to km.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_CONSTANT = 1.60934


class ConvertMilesKM(App):
    """Run an app that will convert Miles to km."""
    output_km = StringProperty()

    def build(self):
        """Build the app and initialise text."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_km(self, text):
        """Convert Miles to km."""
        result = self.convert_to_number(text) * CONVERSION_CONSTANT
        self.output_km = str(result)

    def handle_increment(self, input_text, increment):
        """Handle up and down buttons by incrementing the input value."""
        result = self.convert_to_number(input_text) + increment
        self.root.ids.input_number.text = str(result)
        self.convert_miles_km(result)

    @staticmethod
    def convert_to_number(text):
        """Convert input text to a number."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKM().run()
