import requests 
import json
import pandas as pd

##PRE-ENTREGA1

## Obtencion de datos desde la API y conversion a JSON

url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
response = requests.get(url).json()

## Armado de data frame filtrado de datos

data=response['drinks']
datalist= pd.DataFrame(data)
df= pd.DataFrame(datalist)[['idDrink','strDrink','strCategory','strAlcoholic','strGlass','strInstructions','strIngredient1', 'strIngredient2','strIngredient3', 'strIngredient4','strIngredient5','strIngredient6','strIngredient7','strIngredient8','strIngredient9','strIngredient10','strIngredient11','strIngredient12','strIngredient13','strIngredient14','strIngredient15','strMeasure1', 'strMeasure2', 'strMeasure3', 'strMeasure4', 'strMeasure5', 'strMeasure6', 'strMeasure7', 'strMeasure8', 'strMeasure9', 'strMeasure10', 'strMeasure11', 'strMeasure12', 'strMeasure13', 'strMeasure14', 'strMeasure15']]
