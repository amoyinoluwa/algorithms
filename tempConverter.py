from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Temperature Converter")

        # self.addLabel (Label for Celsius)
        self.addLabel(text = "Celsius", row = 0, column = 0)
        # self.celsiusField (Celsius field)
        self.celsiusField = self.addFloatField(value = 0.0, row = 1, column = 0)
        # self.addLabel (Label for Fahrenheit)
        self.addLabel(text = "Fahrenheit", row = 0, column = 1)
        # self.fahrField (Fahrenheit field)
        self.fahrField = self.addFloatField(value = 32.0, row = 1, column = 1)
        # self.addButton (Celsius button)
        self.addButton(text = ">>>>", row = 2, column = 0, columnspan = 2, command = self.computeFahr)
        # self.addButton (Fahrenheit button)
        self.addButton(text = "<<<<", row = 2, column = 1, columnspan = 2, command = self.computeCelsius)
    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        centigrade = self.celsiusField.getNumber()
        fahr = (centigrade*1.8)+32.0
        self.fahrField.setNumber(round(fahr, 2))

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        fahrenheit = self.fahrField.getNumber()
        celsius = (fahrenheit - 32.0)*5.0/9.0
        self.celsiusField.setNumber(round(celsius, 2))
              
def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")
