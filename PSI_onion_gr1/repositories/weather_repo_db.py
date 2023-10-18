from repositories.iweather_repo import IWeatherRepo


class WeatherRepo(IWeatherRepo):
    def get_data(self) -> str:
        return 'data from DB'
