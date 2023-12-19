database_name = "zesty"
session_collection_name = "sessions"
template_collection_name = "templates"

user_collection_name = "users"

secret_key = "eaa7b80f376218876a5d69af4534ac6943acf6c32087f47d929cea91a05d254c"
algorithm= "HS256"
access_token_expire_minutes = 30

google_client_id = "84466759066-765slvimi0tssr5903idpp8u0rshs8li.apps.googleusercontent.com"
google_client_secret = "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"

# roles = ['customer-service', 'e-commerce', 'finance', 'gifts', 'innovation', 'it', 'people', 'production', 'purchase', campus']

role_permissions = [
    {   
        "role":"admin",
        "permissions":[
            "sessions:read",
            "sessions:write",
            "template:read",
            "template:write",
            "email:read",
            "auth:read",
            "auth:write",
        ],
        "filter": None
    },
    {
        "role":"purchase",
        "permissions":[
            "sessions:read"
        ],
        "filter":"Purchase"
    },
    {
        "role":"people",
        "permissions":[
            "sessions:read"
        ],
        "filter":"People"
    },
    {
        "role":"people",
        "permissions":[
            "sessions:read"
        ],
        "filter":"People"
    },
    {
        "role":"production",
        "permissions":[
            "sessions:read"
        ],
        "filter":"Production"
    },
    {
        "role":"it",
        "permissions":[
            "sessions:read",
            # "template:read"
        ],
        "filter":"IT"
    },
    {
        "role":"customer-service",
        "permissions":[
            "sessions:read"
        ],
        "filter":"Customer Service"
    },
    {
        "role":"e-commerce",
        "permissions":[
            "sessions:read"
        ],
        "filter":"E-commerce"
    },
    {
        "role":"finance",
        "permissions":[
            "sessions:read"
        ],
        "filter":"Finance"
    },
    {
        "role":"gifts",
        "permissions":[
            "sessions:read"
        ],
        "filter":"Gifts"
    },
    {
        "role":"innovation",
        "permissions":[
            "sessions:read"
        ],
        "filter":"Innovation"
    }
];