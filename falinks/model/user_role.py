from sqlalchemy import Table, Column, ForeignKey

from falinks.database import Model

UserRole = Table(
    "user_role",
    Model.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True, nullable=False),
    Column("role_id", ForeignKey("role.id"), primary_key=True, nullable=False)
)
