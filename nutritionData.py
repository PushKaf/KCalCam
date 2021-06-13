import requests, json


apiKey = "kvnaYkiLWJBDi2pDvASX2A3wAq7Jhlk16offJxGw"

def getBrandName(food):
    return food["brandName"]

def getIngredients(food):
    return food["ingredients"]

def getFoodInfo(query):
    res = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?query={query}&pageSize=25&api_key={apiKey}").json()
    foodDict = {}
    print(len(res["foods"]))
    for food in res["foods"]:
        tempNutrients = []
        description = food["description"]
        fId = food["fdcId"]
        

        for n in food["foodNutrients"]:
            name = n["nutrientName"]
            unitValue = n["value"]
            unitMeasure = n["unitName"]

            if unitValue != 0:
                # print(f"{description}: {name}-- {unitValue}{unitMeasure}")
                tempNutrients.append([name, unitValue, unitMeasure])

        tempNutrients.insert(0, description)
        try:
            tempNutrients.insert(1, getBrandName(food))
            tempNutrients.append(getIngredients(food))
        except Exception:
            print("Either no: brandName or ingredients")

        foodDict[fId] = tempNutrients

    return foodDict