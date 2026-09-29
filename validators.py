"""Extracted reusable validators (Iteration 3 discovery)."""
from typing import Any, Callable

class Validator:
    """Base validator for record filtering."""
    def validate(self, record: dict) -> bool:
        raise NotImplementedError

class FieldPresenceValidator(Validator):
    """Check required fields exist."""
    def __init__(self, required_fields: list):
        self.required_fields = required_fields

    def validate(self, record: dict) -> bool:
        return all(field in record for field in self.required_fields)

class TypeValidator(Validator):
    """Check field types."""
    def __init__(self, field_type_map: dict):
        self.field_type_map = field_type_map

    def validate(self, record: dict) -> bool:
        for field, expected_type in self.field_type_map.items():
            if field not in record or not isinstance(record[field], expected_type):
                return False
        return True

class CustomValidator(Validator):
    """Allow custom validation logic."""
    def __init__(self, func: Callable):
        self.func = func

    def validate(self, record: dict) -> bool:
        return self.func(record)

# Usage: chain validators for any record pipeline
presence = FieldPresenceValidator(["id", "value"])
type_check = TypeValidator({"id": int, "value": (int, float)})
# Reused across team for all new pipelines
