from dependency_injector.wiring import Provide

from container import Container
from services.iweather_service import IWeatherService


def main(service: IWeatherService = Provide(Container.service)) -> None:
    weather = service.get_weather()

    print(f'From interface: {weather}')


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[__name__])

    main()
