from abc import ABC


class IWeatherService(ABC):
    def get_weather(self) -> str:
        pass
