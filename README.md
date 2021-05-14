# Jugador_Seleccionado
## Predicción de los jugadores de béisbol que serán parte del salón de la fama

### Descripción del Dataset y cómo se obtuvo
Los datos fueron recolectados por Sean Lahman y se obtuvieron en su página en el siguiente link: http://www.seanlahman.com/files/database/readme2017.txt. Él es un reportero de investigación que ha recolectado un gran número de información sobre los equipos que forman parte de las ligas mayores de Estados Unidos.

Resulta que el Salón de la Fama y Museo Nacional de Béisbol ubicado en Nueva York es en donde se encuentra toda la historia sobre este deporte en Estados Unidos y para que sea elegido a ser parte del Salón de la Fama debe cumplir con los siguientes criterios:

-	Debe haber competido en al menos diez temporadas
-	Debe haberse retirado durante al menos cinco temporadas
-	Un comité de selección debe aprobar al jugador para ser incluido en la boleta (regularmente los jugadores que han jugado durante diez o más años son considerados dignos)
-	El jugador no debe estar en la lista de inelegibles (esto significa que el jugador no debe ser expulsado del beisbol)
-	Se considera elegido si recibe al menos el 75% de los votos en la elección
-	Un jugador permanece en la boleta si recibe al menos el 5% de los votos y permanece por un máximo de 10 años

Con estos conocimientos lo que se quiso hacer en este proyecto era construir un modelo de Machine Learning que pueda predecir con precisión si un jugador de beisbol de las ligas mayores de beisbol será votado en el salón de la fama. 

![image](https://user-images.githubusercontent.com/43154438/118296821-0155c800-b4a3-11eb-9a80-bdcd0fd17e84.png)

Los archivos que se necesitaron fueron los siguientes:

![image](https://user-images.githubusercontent.com/43154438/118296856-09ae0300-b4a3-11eb-99df-b693497be41b.png)

Estos archivos se copiaron en la raíz de la carpeta del proyecto. Así es más fácil de utilizar.  
Cada fila corresponde a los datos de un jugador, en donde se indica toda la información correspondiente a una temporada. Cada jugador se encuentra identificado por un código y será el que utilizaremos para identificarlo en nuestro análisis.

Acá una breve explicación del contenido de los archivos:

-	AllstarFull.csv contiene información sobre si el jugador jugó o no en un juego de las estrellas de las ligas mayores de béisbol.
-	Appearances.csv contiene el núero de juegos en los que participó el jugador mientras estuvo activo. 
-	AwardsPlayers.csv contiene la información de los premios que los jugadores han obtenido a lo largo del tiempo tales como: jugador más valioso, novato del año, guante de oro, bateador de plata y más valioso de la serie mundial. 
-	Batting.csv contiene la información estadística de los jugadores en cuanto a su bateo y todo lo referente a su ofensiva. Estos datos están divididos por año. 
-	Fielding.csv contiene información sobre los jugadores a nivel de defensa como Asistidas, Errores Cometidos y Doble Plays. 
-	HallOfFame.csv contiene la información de si el jugador recibió votos o no para ser parte del salón de la fama, así como otros detalles adicionales como información del manager, del cuerpo técnico, entre otro personal.
-	People.csv contiene el código respectivo, el nombre del jugador y toda su información personal. 


### Objetivos

Tras obtenido el conjunto de datos se realiza su procesamiento, se analiza y se crea un modelo para realizar la predicción de qué jugador pasará al salón de la fama. Cada uno de los conjuntos de datos en archivos csv se recolectan estratégicamente para tener los datos dispuestos de una manera adecuada antes de ingresarla al modelo de Machine Learning, a continuación, algo de los procesos específicos que se hicieron con algunos de ellos: 

Dado a que en el dataset de Batting no se muestran las estadísticas totales del juego, sino las estadísticas por año jugado, entonces sumamos todos los datos ya que lo que nos interesan son las estadísticas totales. Entre estas estadísticas están: juegos en los que participó, veces de bateo, carreras anotadas, hits dobles, etc. Este proceso se realiza mediante una sumatoria en un bucle for donde de acuerdo con la identificación del jugador se van sumando las variables estadísticas correspondientes y de esta manera se almacenará toda la información de los años jugados. 

Lo mismo explicado en el párrafo anterior es lo mismo que se hace para el resto de los archivos, ya que lo que necesitamos son las estadísticas finales. Aunque para el caso de los premios tratando con el dataset AwardsPlayers en vez de un acumulador de valores se emplea en este caso un contador por cada premio para que vaya contando el número de diferentes premios que tiene cada jugador y del mismo modo ocurre con el dataset AllstarFull donde se cuenta en cuantos juegos de las estrellas jugó cada jugador. 

A partir de la información obtenida en el dataset HallOfFame.csv se obtuvo el valor dependiente para el análisis de Machine Learning, ya que aquí están los votos del jugador para ser parte del salón de la fama. El resto de información como de los manager y cuerpo técnico se borran ya que no es de importancia. 

Estos son algunos de los gráficos de importancia de características relevantes:

![image](https://user-images.githubusercontent.com/43154438/118297014-39f5a180-b4a3-11eb-801f-290e519c5244.png)

Se empleó el método train_test_split de la librería scikitlearn para dividir los datos de prueba de los de entrenamiento, se utilizó un Análisis Discriminante Lineal para mejorar el rendimiento del modelo y posteriormente se empleo un algoritmo de regresión logística obteniendo los siguientes resultados:

![image](https://user-images.githubusercontent.com/43154438/118297046-44b03680-b4a3-11eb-943c-588a7bb949c3.png)

### Conclusiones y resultados obtenidos

Podemos con esto decir que a partir de varios conjuntos de datos desordenados se puede obtener algo útil para ingresarlo a un modelo de Machine Learning y obtener resultados deseables. 

Este tipo de análisis, preprocesamiento y empleo del modelo es aplicable a muchas otras circunstancias deportivas donde existan datos al respecto, tal sería la predicción de los jugadores de cualquier rama deportiva que serán seleccionados para el equipo nacional. O inclusive en áreas que no sean deportivas, como por ejemplo para la predicción de qué personas serán nominadas a algún tipo de premio. 

Nota: el programa está sujeto a mejoras tales como aplicar más modelos de machine learning y aplicar más métricas de evaluación tal como la matriz de confusión. 


