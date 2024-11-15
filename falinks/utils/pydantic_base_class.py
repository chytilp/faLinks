from typing import Any

from humps import camelize
from pydantic import BaseModel, ConfigDict, ValidationError


class PydanticValidationError(Exception):
    pass


class PydanticWithCamelCaseAliasesImmutable(BaseModel):
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        frozen=True,
        arbitrary_types_allowed=True,
    )

    def __init__(self, **data: Any) -> None:
        try:
            super().__init__(**data)
        except ValidationError as err:
            raise PydanticValidationError(f"Data: {data}") from err
