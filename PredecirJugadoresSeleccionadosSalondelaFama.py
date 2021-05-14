# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:15:25 2020

@author: Daniel Andres
"""
### IMPORTAR LIBRERÍAS ###
import pandas as pd
import matplotlib.pyplot as plt

### IMPORTAR LOS DATOS ###
people_df = pd.read_csv('People.csv')
fielding_df = pd.read_csv('Fielding.csv')
batting_df = pd.read_csv('Batting.csv')
awards_df = pd.read_csv('AwardsPlayers.csv')
allstar_df = pd.read_csv('AllstarFull.csv')
hof_df = pd.read_csv('HallOfFame.csv')
appearances_df = pd.read_csv('Appearances.csv')

### PROCESAMIENTO DE LOS DATOS ###
### Analizamos el conjunto de datos people_df ###
#Elimino las columnas que no sean necesarias para el análisis
#playerID, nameFirst, nameLast
columnas_people = ['playerID', 'nameFirst', 'nameLast']
data_final = people_df[columnas_people]

### Analizamos el conjunto de datos batting_df ###
#Determinamos las estadísticas finales de cada jugador
#G, AB, R, H, 2B, 3B, HR, RBI, SB, BB, SO, años jugados
estado_batting = {}
anos_jugados = {}

for i, fila in batting_df.iterrows():
    iden = fila['playerID']
    if iden in estado_batting:
        estado_batting[iden]['G'] = estado_batting[iden]['G'] + fila['G']
        estado_batting[iden]['AB'] = estado_batting[iden]['AB'] + fila['AB']
        estado_batting[iden]['R'] = estado_batting[iden]['R'] + fila['R']
        estado_batting[iden]['H'] = estado_batting[iden]['H'] + fila['H']
        estado_batting[iden]['2B'] = estado_batting[iden]['2B'] + fila['2B']
        estado_batting[iden]['3B'] = estado_batting[iden]['3B'] + fila['3B']
        estado_batting[iden]['HR'] = estado_batting[iden]['HR'] + fila['HR']
        estado_batting[iden]['RBI'] = estado_batting[iden]['RBI'] + fila['RBI']
        estado_batting[iden]['SB'] = estado_batting[iden]['SB'] + fila['SB']
        estado_batting[iden]['BB'] = estado_batting[iden]['BB'] + fila['BB']
        estado_batting[iden]['SO'] = estado_batting[iden]['SO'] + fila['SO']
        anos_jugados[iden].append(fila['yearID'])
    else:
        estado_batting[iden] = {}
        estado_batting[iden]['G'] = fila['G']
        estado_batting[iden]['AB'] = fila['AB']
        estado_batting[iden]['R'] = fila['R']
        estado_batting[iden]['H'] = fila['H']
        estado_batting[iden]['2B'] = fila['2B']
        estado_batting[iden]['3B'] = fila['3B']
        estado_batting[iden]['HR'] = fila['HR']
        estado_batting[iden]['RBI'] = fila['RBI']
        estado_batting[iden]['SB'] = fila['SB']
        estado_batting[iden]['BB'] = fila['BB']
        estado_batting[iden]['SO'] = fila['SO']
        anos_jugados[iden] = []
        anos_jugados[iden].append(fila['yearID'])

#Determinamos los años jugados por cada jugador
for k, v in anos_jugados.items():
    estado_batting[k]['Years_Played'] = len(list(set(v)))
    
#Convertimos el diccionario en un DataFrame
columnas_batting = pd.DataFrame.from_dict(estado_batting, orient='index')

#Incluimos los datos obtenidos al conjunto de datos final
data_final = data_final.join(columnas_batting, on='playerID', how='outer', rsuffix = 'mstr')

### Analizamos el conjunto de datos fielding_df ###
#Determinamos las estadísticas finales de cada jugador 
#A, E, DP
estado_filding = {}

for i, fila in fielding_df.iterrows():
    iden = fila['playerID']
    if iden in estado_filding:
        estado_filding[iden]['A'] = estado_filding[iden]['A'] + fila['A']
        estado_filding[iden]['E'] = estado_filding[iden]['E'] + fila['E']
        estado_filding[iden]['DP'] = estado_filding[iden]['DP'] + fila['DP']
    else:
        estado_filding[iden] = {}
        estado_filding[iden]['A'] = fila['A']
        estado_filding[iden]['E'] = fila['E']
        estado_filding[iden]['DP'] = fila['DP']

#Convertimos el diccionario en un DataFrame
columnas_fielding = pd.DataFrame.from_dict(estado_filding, orient='index')

#Incluimos los datos obtenidos al conjunto de datos final
data_final = data_final.join(columnas_fielding, on='playerID', how='outer', rsuffix='mstr')

### Analizamos el conjunto de datos awards_df ###
#Determnamos de todos los premios que entrega el béisbol los más importantes
mvp = awards_df[awards_df['awardID'] == 'Most Valuable Player']
roy = awards_df[awards_df['awardID'] == 'Rookie of the Year']
gg = awards_df[awards_df['awardID'] == 'Gold Glove']
ss = awards_df[awards_df['awardID'] == 'Silver Slugger']
ws_mvp = awards_df[awards_df['awardID'] == 'World Series MVP']

list_awards = [mvp,roy,gg,ss,ws_mvp]

#Inicializamos la lista de cada uno de los premios seleccionados
mvp_list = []
roy_list = []    
gg_list = []
ss_list = []
ws_mvp_list = []

lists = [mvp_list,roy_list,gg_list,ss_list,ws_mvp_list]

estado_awards = {}

for index, m in enumerate(list_awards):
      for i, fila in m.iterrows():
          iden = fila['playerID']
          premio = fila['awardID']
          if iden in estado_awards and iden in lists[index]:
              estado_awards[iden][premio] += 1
          else:
              estado_awards[iden] = {}
              lists[index].append(iden)
              estado_awards[iden][premio] = 1

columnas_awards = pd.DataFrame.from_dict(estado_awards, orient='index')

#Incluimos los datos obtenidos al conjunto de datos final
data_final = data_final.join(columnas_awards, on='playerID', how='outer', rsuffix='mstr')

### Analizamos el conjunto de datos allstar_df ###
#Participación en el juego de las estrellas
estado_allstar = {}

for i, fila in allstar_df.iterrows():
    iden = fila['playerID']
    if iden in estado_allstar:
        estado_allstar[iden]['allstar'] +=1
    else:
        estado_allstar[iden] = {}
        estado_allstar[iden]['allstar'] = 1
        
#Convertimos el diccionario en un DataFrame
columnas_allstar = pd.DataFrame.from_dict(estado_allstar, orient='index')

#Incluimos los datos obtenidos al conjunto de datos final
data_final = data_final.join(columnas_allstar, on='playerID', how='outer', rsuffix='mstr')

### Analizamos el conjunto de datos hof_df ###
#Seleccionamos los datos a si fue inducido el voto y que sea un jugador
hof_df = hof_df[(hof_df['inducted'] == 'Y') & (hof_df['category'] == 'Player')] 

estado_hof = {}

for i, fila in hof_df.iterrows():
    iden = fila['playerID']
    if iden in estado_hof:
        estado_hof[iden]['hof'] += 1
    else:
        estado_hof[iden] = {}
        estado_hof[iden]['hof'] = 1
        
#Convertimos el diccionario en un DataFrame
columnas_hof = pd.DataFrame.from_dict(estado_hof, orient='index')

#Incluimos los datos obtenidos al conjunto de datos final
data_final = data_final.join(columnas_hof, on='playerID', how='outer', rsuffix='mstr')

### Analizamos el conjunto de datos appearances_df ###
#Determinamos las estadísticas finales de cada jugador
#G_all
estado_appearances = {}

for i, fila in appearances_df.iterrows():
    iden = fila['playerID']
    if iden in estado_appearances:
        estado_appearances[iden]['G_all'] = estado_appearances[iden]['G_all'] + fila['G_all']
    else:
        estado_appearances[iden] = {}
        estado_appearances[iden]['G_all'] = fila['G_all']

#Convertimos el diccionario en un DataFrame
columnas_appearances = pd.DataFrame.from_dict(estado_appearances, orient = 'index')

#Incluimos los datos obtenidos al conjunto de datos final
data_final = data_final.join(columnas_appearances, on='playerID', how='outer', rsuffix='mstr')

### ANALIZAR LOS DATOS ###
#Analizamos el conjunto de datos data_final
#Conocer la forma de los datos
print(data_final.shape)

#Conocer el formato de los datos
data_final.dtypes

#Conocer los datos nulos
data_final.isnull().sum()

#Reemplazo los valores nulos por 0
fill_null = ['G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'BB', 'SO',
              'Years_Played', 'A', 'E', 'DP', 'Most Valuable Player',
              'Rookie of the Year', 'Gold Glove', 'World Series MVP',
              'Silver Slugger', 'allstar', 'hof', 'G_all']

for col in fill_null:
    data_final[col] = data_final[col].fillna(0)
    
### VISUALIZACIÓN DE LOS DATOS ###
#Creamos varios histogramas para visualizar las carreras, home runs, 
#años jugados y los juegos de las estrellas
fig = plt.figure(figsize=(15,12))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.hist(data_final['R'])
ax1.set_title('Distribución de las Carreras')
ax2.hist(data_final['HR'])
ax2.set_title('Distribución de los Home Runs')
ax3.hist(data_final['Years_Played'])
ax3.set_title('Distribución de los Años Jugados')
ax4.hist(data_final['allstar'])
ax4.set_title('Distribución de las Apariciones en el Juego de las Estrellas')
plt.show()

data_final = data_final.drop(columns=['playerID','nameFirst','nameLast'])

### ANÁLISIS DE MACHINE LEARNING ###
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score

#Definir las variables dependientes e independientes
y = data_final['hof']
X = data_final.drop('hof', axis =1)

#Separar los datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 1)


######################################
# Analisis discriminante lineal para mejorar el modelo
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components = 1)
X_train = lda.fit_transform(X_train, y_train)
X_test = lda.transform(X_test)
######################################


#Definir el algoritmo
algoritmo = LogisticRegression()

#Entrenar el algoritmo
algoritmo.fit(X_train, y_train)

#Realizar una predicción
y_test_pred = algoritmo.predict(X_test)

#Se calcula la exactitud y la precisión del modelo
print("Exactitud del modelo: ")
print(accuracy_score(y_test, y_test_pred))
print("Precisión del modelo: ")
print(precision_score(y_test, y_test_pred))