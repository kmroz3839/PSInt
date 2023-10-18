from abc import ABC


class IWeatherRepo(ABC):
    def get_data(self) -> str:
        pass
