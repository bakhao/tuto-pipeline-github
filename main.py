class ZeroPointTemperatureCalculator:
    def calculate(self, input_data):
        if not input_data:
            raise ValueError("Input data is empty")

        total = sum(input_data)
        average_temperature = total / len(input_data)

        return average_temperature



if __name__ == "__main__":
    input_data = [10, 20, 30, 40, 50]  # Exemple de données d'entrée
    calculator = ZeroPointTemperatureCalculator()
    result = calculator.calculate(input_data)
    print(f"Point zéro de la température : {result}°C")
