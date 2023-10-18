from dependency_injector import containers, providers
import os

if os.environ.get("repo_txt", "0") == "1":
    from repositories.weather_repo_txt import WeatherRepo
else:
    from repositories.weather_repo_db import WeatherRepo

from services.weather_service import WeatherService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repo = providers.Singleton(
        WeatherRepo,
    )

    service = providers.Factory(
        WeatherService,
        repo=repo,
    )
