drop table if exists juansaobento_coderhouse.Juansaobento_CocktailsAPI;
create table juansaobento_coderhouse.Juansaobento_CocktailsAPI(
DrinkID int primary key,
DrinkName varchar (200),
Category varchar (200),
Alcoholic varchar (200),
Glass varchar (200),
Instructions varchar (200),
Ingredient1 varchar (200),
Ingredient2 varchar (200),
Ingredient3 varchar (200),
Ingredient4 varchar (200),
Ingredient5 varchar (200),
Ingredient6 varchar (200),
Ingredient7 varchar (200),
Ingredient8 varchar (200),
Ingredient9 varchar (200),
Ingredient10 varchar (200),
Ingredient11 varchar (200),
Ingredient12 varchar (200),
Ingredient13 varchar (200),
Ingredient14 varchar (200),
Ingredient15 varchar (200),
Measure1 varchar (200),
Measure2 varchar (200),
Measure3 varchar (200),
Measure4 varchar (200),
Measure5 varchar (200),
Measure6 varchar (200),
Measure7 varchar (200),
Measure8 varchar (200),
Measure9 varchar (200),
Measure10 varchar (200),
Measure12 varchar (200),
Measure13 varchar (200),
Measure14 varchar (200),
Measure15 varchar (200),
Fecha_Obtencion datetime default (current_timestamp));
