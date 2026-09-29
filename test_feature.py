import json
from feature import pipeline

# Test case
test_payload = json.dumps({
    "records": [
        {"id": 1, "value": 100},
        {"id": 2, "value": 200},
        {"id": 3, "value": 300},
    ]
})

result = pipeline(test_payload)
print("Feature Test:", result)
assert result["count"] == 3
assert result["sum"] == 600
assert result["avg"] == 200
print("✓ All tests passed")
