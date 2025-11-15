"""
Build and use the kv app to convert miles to km
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_CONSTANT = 1.60934


class ConvertMilesKM(App):
    output = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output = "Enter a number in miles to convert to kilometres"
        return self.root

    def convert_miles_km(self, text):
        result = self.convert_to_number(text) * CONVERSION_CONSTANT
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, input_text, increment):
        result = self.convert_to_number(input_text) + increment
        self.root.ids.input_number.text = str(result)
        self.convert_miles_km(result)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKM().run()
