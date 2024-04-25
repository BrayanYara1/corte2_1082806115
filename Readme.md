# Entidad de Carros

Este archivo README proporciona una visión general de la entidad de carros en el proyecto. Describe la estructura de la clase `Car` y cómo se utiliza en el sistema.

## Descripción

La entidad de carros representa un vehículo en el sistema. Cada instancia de la clase `Car` contiene información como la marca, el modelo, el año, el color y la categoría del vehículo.


## Datos a tener en cuenta

Marca	Modelo	AñoFabricacion	ColorDelCarro	CategotiaID	
Toyota	2022	  2022		      Negro             1002
Mazda	2001	  2001	          Rojo              1003
Nissan	1998	  1990	          Gris              1004
Ferrari	2030	  2010            Blanco            1005


## De lo anterior, se puede resaltar lo siguiente, si bien es cierto, se puede ingresar los datos sin normalización, se sabe que es necesario para la optimización y traza de los datos.

En este sentido, se procede a normarlizar de la siguiente manera

Marca	Modelo	ColorDelCarro	CategotiaID	
Toyota	2022	   Negro             1002
Mazda	2001	   Rojo              1003
Nissan	1998	   Gris              1004
Ferrari	2030	   Blanco            1005

## La clasificación de los carros, estos son individuales.

Marca	ColorDelCarro	CategotiaID	
Toyota	  Negro             1002
Mazda	  Rojo              1003
Nissan	  Gris              1004
Ferrari	  Blanco            1005