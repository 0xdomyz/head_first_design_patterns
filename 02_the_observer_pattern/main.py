class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)


class Observer:
    def update(self, subject):
        pass


class DisplayElement:
    def display(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 1
        self._humidity = 2
        self._pressure = 3

    def get_temperature(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity

    def get_pressure(self):
        return self._pressure

    def measurements_changed(self):
        self._temperature += 1
        self._humidity += 1
        self._pressure += 1
        self.notify_observers()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, subject):
        if isinstance(subject, WeatherData):
            self._temperature = subject.get_temperature()
            self._humidity = subject.get_humidity()
            self._pressure = subject.get_pressure()
            self.display()

    def display(self):
        print(
            f"Current conditions: {self._temperature}F degrees"
            f" and {self._humidity}% humidity"
            f" and {self._pressure} pressure"
        )


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._max_temp = 0
        self._min_temp = 0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, subject):
        if isinstance(subject, WeatherData):
            temperature = subject.get_temperature()
            self._max_temp = max(self._max_temp, temperature)
            self._min_temp = min(self._min_temp, temperature)
            self.display()

    def display(self):
        print(f"Max/Min temperature: {self._max_temp}/{self._min_temp}")


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._current_pressure = 0
        self._last_pressure = 0
        self._prediction = 0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, subject):
        if isinstance(subject, WeatherData):
            self._last_pressure = self._current_pressure
            self._current_pressure = subject.get_pressure()
            self._prediction = (
                self._current_pressure - self._last_pressure + self._current_pressure
            )
            self.display()

    def display(self):
        print(f"Forecast: {self._prediction}")


def test():
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)
    weather_data.measurements_changed()
    weather_data.measurements_changed()
    weather_data.measurements_changed()


if __name__ == "__main__":
    test()

    # python3 02_the_observer_pattern/main.py
