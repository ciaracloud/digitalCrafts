house = {
    "furnitureColors": {
        "couch": "blue",
        "rug": "pink",
        "chair": [
            "green", "purple", "yellow"
        ],
    },
    "bathroomColors": {
        "toilet": "aqua",
        "bathroom rug": ["purple", "pink"],
        "sink": "white"
    }

}

firstChairColor = house["furnitureColors"]["chair"][0]
print(firstChairColor)

secondBathroomRugColor = house["bathroomColors"]