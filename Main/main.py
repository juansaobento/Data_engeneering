import requests 
import json
import pandas as pd
import psycopg2 
import sqlalchemy as sa
import os
from dotenv import load_dotenv

def main():
##PRE-ENTREGA1

## Obtencion de datos desde la API y conversion a JSON

    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
    response = requests.get(url).json()

    ## Armado de data frame filtrado de datos

    data=response['drinks']
    datalist= pd.DataFrame(data)
    df= pd.DataFrame(datalist)[['idDrink','strDrink','strCategory','strAlcoholic','strGlass','strInstructions','strIngredient1', 'strIngredient2','strIngredient3', 'strIngredient4','strIngredient5','strIngredient6','strIngredient7','strIngredient8','strIngredient9','strIngredient10','strIngredient11','strIngredient12','strIngredient13','strIngredient14','strIngredient15','strMeasure1', 'strMeasure2', 'strMeasure3', 'strMeasure4', 'strMeasure5', 'strMeasure6', 'strMeasure7', 'strMeasure8', 'strMeasure9', 'strMeasure10', 'strMeasure11', 'strMeasure12', 'strMeasure13', 'strMeasure14', 'strMeasure15']]
## Correcciones segunda pre-entrega
    ## Creacion de una funcion que Tome los valores de Ingredientes y Medidas para crear un Diccionario
    ##Para luego crear un Json para Usar un dato de tipo STRUCT/SUPER en RS
    def create_ingredients_json(row):
        ingredients = {}
        for i in range(1, 16):  # Assuming up to 15 ingredients
            ingredient = row.get(f'strIngredient{i}')
            measure = row.get(f'strMeasure{i}')
            if ingredient and measure:
                ingredients[ingredient] = measure
        return json.dumps(ingredients)  # Convert dictionary to JSON string
    
    ##Metodo apply para recorrer el DF con la funcion previamente creada
    df['Ingredientes'] = df.apply(create_ingredients_json, axis=1)
    
    ##Armado del DF final
        df = df[['idDrink', 'strDrink', 'strCategory', 'strAlcoholic', 'strGlass', 'strInstructions', 'Ingredientes']]
        
        ##Reemplazo de nombres del DF para que sea subido a Amazon RS
        df= df.rename(columns= {'strDrink':'Cocktail', 'strCategory':'Categoria', 'strAlcoholic':'Alcoholico', 'strGlass':'Cristaleria', 'strInstructions':'Instrucciones'})
    df
    ## PRE-ENTREGA 2

    ##Definicion de credenciales para conexion

    load_dotenv()
    REDSHIFT_USER=os.getenv('REDSHIFT_USER')
    REDSHIFT_PASSWORD=os.getenv('REDSHIFT_PASSWORD')
    REDSHIFT_HOST=os.getenv("REDSHIFT_HOST") 
    REDSHIFT_PORT=os.getenv('REDSHIFT_PORT',5439)
    REDSHIFT_DBNAME= os.getenv('REDSHIFT_DBNAME')

    ##Definicion de Valores de base de datos

    TABLE_NAME_RS= 'juansaobento_cocktailsapi'
    SCHEMA_NAME_RS= 'juansaobento_coderhouse'

    ##Conexion a la base de datos

    conection_string=f"postgresql+psycopg2://{REDSHIFT_USER}:{REDSHIFT_PASSWORD}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DBNAME}"
    db_engine= sa.create_engine(conection_string)

    ##Carga de datos a la BD de SQL 
    try:
        df.to_sql(
            TABLE_NAME_RS,  
            db_engine, 
            schema= SCHEMA_NAME_RS,
            if_exists='append',
            index=False)
        
    except sa.exc.SQLAlchemyError as e:
        print(f"Error ocurred while droping the table: {e}")
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()