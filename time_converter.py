class TimeConverter:
    def __init__(self):
        self.input_time: float
        self.input_unit: str
        self.output_unit: str
        self.conversion_rates = {
            "сек в мин": 1/60,
            "сек в час": 1/3600,
            "мин в сек": 60,
            "мин в час": 1/60,
            "час в сек": 3600,
            "час в мин": 60
        }


    def convert_time(self, input_time, input_unit, output_unit) -> float:
        result = input_time * self.conversion_rates[f"{input_unit} в {output_unit}"]
        return result