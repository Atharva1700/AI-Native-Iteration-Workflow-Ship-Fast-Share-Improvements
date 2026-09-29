"""Initial implementation: data pipeline with basic validation."""
import json
from typing import List, Dict

def parse_payload(raw_data: str) -> Dict:
    """Parse incoming JSON payload."""
    try:
        return json.loads(raw_data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")

def validate_records(records: List[Dict]) -> List[Dict]:
    """Validate each record has required fields."""
    validated = []
    for record in records:
        if "id" in record and "value" in record:
            validated.append(record)
    return validated

def aggregate(validated_records: List[Dict]) -> Dict:
    """Aggregate validated records."""
    total = sum(r.get("value", 0) for r in validated_records)
    return {
        "count": len(validated_records),
        "sum": total,
        "avg": total / len(validated_records) if validated_records else 0
    }

def pipeline(raw_data: str) -> Dict:
    """Full pipeline: parse → validate → aggregate."""
    data = parse_payload(raw_data)
    records = data.get("records", [])
    validated = validate_records(records)
    return aggregate(validated)
