from enum import Enum


class Status(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'
    DELETED = 'deleted'
