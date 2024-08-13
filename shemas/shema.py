post_create = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "ok": {
            "type": "boolean"
        }
    },
    "required": [
        "ok"
    ]
}

post_insufficient_data = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "code": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        }
    },
    "required": [
        "code",
        "message"
    ]
}

post_is_used = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "code": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        }
    },
    "required": [
        "code",
        "message"
    ]
}

post_choose_color = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "track": {
            "type": "integer"
        }
    },
    "required": [
        "track"
    ]
}

get_order_list = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "orders": {
            "type": "array"
        }
    },
    "required": [
        "orders"
    ]
}

post_required_fields = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        }
    },
    "required": [
        "id"
    ]
}
