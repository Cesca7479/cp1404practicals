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

    def convert_miles_km(self, value):
        try:
            result = float(value) * CONVERSION_CONSTANT
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, input_text, increment):
        try:
            value = float(input_text)
        except ValueError:
            value = 0
        result = value + increment
        self.root.ids.input_number.text = str(result)
        self.convert_miles_km(result)


ConvertMilesKM().run()
