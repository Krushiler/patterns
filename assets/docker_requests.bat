curl --location --request PATCH '127.0.0.1:8001/api/nomenclature/259034a9-51b0-40d9-9bf2-6b6689e56063' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Docker",
    "nomenclature_group": {
        "name": "Programm"
    },
    "unit": {
        "name": "gb",
        "convertion_ratio": 1000
    }
}'

curl --location '127.0.0.1:8000/api/nomenclature/259034a9-51b0-40d9-9bf2-6b6689e56063'