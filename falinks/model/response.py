from datetime import datetime

from falinks.utils.pydantic_base_class import PydanticWithCamelCaseAliasesImmutable


class UserResponse(PydanticWithCamelCaseAliasesImmutable):
    id: int
    name: str
    email: str
    active: datetime | None


class RoleResponse(PydanticWithCamelCaseAliasesImmutable):
    id: int
    name: str
    active: datetime | None


class UserRegistration(PydanticWithCamelCaseAliasesImmutable):
    success: bool
    message: str
    user_id: int | None = None
