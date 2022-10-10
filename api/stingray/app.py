from typing import AnyStr

from fastapi import FastAPI

from stingray.common import StingraySettings


class StingrayApp(FastAPI):
    def __init__(self) -> None:
        self.settings = StingraySettings()
        super().__init__(
            title="Stingray",
            description="Stingray API Server.",
            version=self.__version__,
            docs_url=None if self.settings.is_production else "/docs",
            redoc_url=None if self.settings.is_production else "/redoc",
        )

    @property
    def __version__(cls) -> AnyStr:
        return "0.1.0"
