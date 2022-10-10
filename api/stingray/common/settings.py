from typing import Literal

from pydantic import BaseSettings


class StingraySettings(BaseSettings):
    environment: Literal["dev", "prod"] = "dev"

    @property
    def is_production(self) -> bool:
        return self.environment == "prod"
