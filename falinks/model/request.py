from falinks.utils.pydantic_base_class import PydanticWithCamelCaseAliasesImmutable


class UserRequest(PydanticWithCamelCaseAliasesImmutable):
    name: str
    email: str
    password: str


class RoleRequest(PydanticWithCamelCaseAliasesImmutable):
    name: str
