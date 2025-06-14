# pip install jsonschema
# We can validate by asserting key, Value Pairs as well OR
# We can use jsonschema import validate


import jsonschema
import requests
import pytest

# Define the expected JSON schema
expected_schema = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "email": {"type": "string", "format": "email"},
                "is_active": {"type": "boolean"}
            },
            "required": ["id", "name", "email", "is_active"]
        }
    },
    "required": ["status", "data"]
}

# Pytest test case for JSON schema validation
@pytest.mark.api
def test_validate_json_schema():
    response = requests.get("https://api.example.com/user/101")  # Replace with actual API endpoint
    response_json = response.json()

    # Validate JSON response against schema
    jsonschema.validate(instance=response_json, schema=expected_schema)

    print("✅ JSON Schema Validation Passed!")


