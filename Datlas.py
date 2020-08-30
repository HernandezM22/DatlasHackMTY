from sklearn.model_selection import train_test_split
import quandl, math
import numpy as np
import pandas as pd
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


data = pd.read_csv("BD_HackMTY_ChoquesYSiniestros_2020_V2.csv", encoding = 'latin1', index_col = False)

print(data.describe())

useful_data = data.drop(["CALLE", "DIA_NUMERO", "COLOR", "ESTADO", "PUNTO_DE_IMPACTO"], axis = 1)
useful_data.set_index("DATE", inplace = True)
print (useful_data.head())

useful_data = useful_data.replace(0, np.NaN).dropna(axis = 1)
useful_data = useful_data.replace("\\N", np.NaN).dropna(axis = 1)
useful_data = useful_data.replace("NA", np.NaN).dropna(axis = 1)
useful_data = useful_data.replace("Sin dato", np.NaN).dropna(axis = 1)

#useful_data.to_csv("finaldata.csv")

final_data = pd.read_csv("finaldata.csv", encoding = 'latin1')

tipo_vehiculo_dict = {"Auto": 1, "Motocicleta": 2, "Camion": 3, "Camion Ligero": 4}
dias_dict = {"LUNES": 1, "MARTES": 2, "MIERCOLES": 3, "JUEVES": 4, "VIERNES": 5, "SABADO": 6, "DOMINGO": 7}

final_data['TIPO_VEHICULO'] = final_data['TIPO_VEHICULO'].map(tipo_vehiculo_dict)
final_data['DIA'] = final_data['DIA'].map(dias_dict)

final_data.sort_index(inplace = True)


mapper_periodos = {0: 4, 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:1, 8:1, 9:1, 10:1, 11:1, 12:2, 13:2, 14:2, 15:2, 16:2, 17:2, 18:2, 19:2, 20:3, 21:3, 22:3, 23:3}

final_data['PERIODO_DIA'] = final_data["HORA"].map(mapper_periodos)

mapper_modelos = {1973:1,1974:1,1975:1,1976:1,1977:1,1978:1,1979:1,1980:1,1981:1,1982:1,1983:1,1984:1,1985:1,1986:1,1987:1,1988:1,1989:1,1990:1,1991:1,1992:1,1993:1,1994:1,1995:1,1996:1,1997:1,1998:1,1999:1,2000:2,2001:2,2002:2,2003:2,2004:2,2005:2,2006:2,2007:2,2008:2,2009:2,2010:2,2011:2,2012:2,2013:2,2014:2,2015:2,2016:2,2017:2,2018:2,}

final_data["ANTIGUEDAD"] = final_data["MODELO_VEHICULO"].map(mapper_modelos)

mapper_danos = {"Alto":3, "Medio": 2, "Bajo": 1}

final_data["MAGNITUD_DANO"] = final_data["NIVEL_DANO_VEHICULO"].map(mapper_danos)

nivel_dano_mas_comun = final_data["MAGNITUD_DANO"].value_counts()
periodo_mas_comun = final_data.groupby('PERIODO_DIA').count()
dia_mas_comun = (final_data['DIA'].value_counts().idxmax())
causa_mas_comun = (final_data['CAUSA_SINIESTRO'].value_counts().idxmax())
colonia_mas_comun =  (final_data['COLONIA'].value_counts().idxmax())
anio_con_mas_accidentes = (final_data['ANIO'].value_counts())
mes_mas_comun = final_data["MES"].value_counts()

print(nivel_dano_mas_comun)

print(final_data["MODELO_VEHICULO"].max())
print(final_data["MODELO_VEHICULO"].min())


print (final_data.head())



mach_learn_data = final_data.drop(["DATE", "CODIGO_POSTAL", "COLONIA", "ANIO", "HORA", "CIUDAD_APROXIMADA", "MODELO_VEHICULO", "NIVEL_DANO_VEHICULO", "FOLIO_ID", "CAUSA_SINIESTRO", "DIA"], axis = 1)

for col in mach_learn_data.columns:
	print(col)

#mach_learn_data.to_csv("mach_learn_data.csv")

####LAT
print ("Modelo LAT")
model_data = pd.read_csv("mach_learn_data.csv")

y = model_data["LAT"]
features = ["TIPO_VEHICULO", "MES", "PERIODO_DIA", "ANTIGUEDAD", "MAGNITUD_DANO"]
X = model_data[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

iowa_model = DecisionTreeRegressor(random_state=1)

iowa_model.fit(train_X, train_y)

val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE when not specifying max_leaf_nodes: {:,.0f}".format(val_mae))

iowa_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
iowa_model.fit(train_X, train_y)
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae))

csv1 = pd.DataFrame(val_predictions)

#csv1.to_csv("lat1.csv")

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(random_state = 1)
rf_model.fit(X, y)

from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
rf_val_mae = mean_absolute_error(val_y, melb_preds)

csv3 = pd.DataFrame(melb_preds)
#csv3.to_csv("lat2.csv")

print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))


###LONG
print ("Modelo LONG")
y2 = model_data["LONG"]
features = ["TIPO_VEHICULO", "MES", "PERIODO_DIA", "ANTIGUEDAD", "MAGNITUD_DANO"]
X2 = model_data[features]

train_X2, val_X2, train_y2, val_y2 = train_test_split(X2, y2, random_state = 1)

iowa_model2 = DecisionTreeRegressor(random_state=1)

iowa_model2.fit(train_X2, train_y2)

val_predictions2 = iowa_model2.predict(val_X2)
csv2 = pd.DataFrame(val_predictions2)

#csv2.to_csv("long1.csv")
val_mae2 = mean_absolute_error(val_predictions2, val_y2)
print("Validation MAE when not specifying max_leaf_nodes: {:,.0f}".format(val_mae2))

iowa_model2 = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
iowa_model2.fit(train_X2, train_y2)
val_predictions2 = iowa_model2.predict(val_X2)
val_mae2 = mean_absolute_error(val_predictions2, val_y2)
print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae2))

rf_model2 = RandomForestRegressor(random_state = 1)
rf_model2.fit(X2, y2)

forest_model2 = RandomForestRegressor(random_state=1)
forest_model2.fit(train_X2, train_y2)
melb_preds2 = forest_model2.predict(val_X2)
print(mean_absolute_error(val_y2, melb_preds2))
rf_val_mae2 = mean_absolute_error(val_y2, melb_preds2)
csv4 = pd.DataFrame(melb_preds2)
#csv4.to_csv("long2.csv")


print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))


print (melb_preds)
print ("#")
print (melb_preds2)

#modelo predictivo SVR

from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

y3 = model_data["LAT"]
features = ["TIPO_VEHICULO", "MES", "PERIODO_DIA", "ANTIGUEDAD", "MAGNITUD_DANO"]
X3 = model_data[features]
train_X3, val_X3, train_y3, val_y3 = train_test_split(X3, y3, random_state = 1)

regr = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2))
regr.fit(X3, y3)

pred = regr.predict(val_X3)
csv5 = pd.DataFrame(pred)
csv5.to_csv("lat3.csv")
mae_SVR = mean_absolute_error(val_y3, pred)


print("Validation MAE for SVR: {}".format(mae_SVR))


y4 = model_data["LONG"]
features = ["TIPO_VEHICULO", "MES", "PERIODO_DIA", "ANTIGUEDAD", "MAGNITUD_DANO"]
X4 = model_data[features]
train_X4, val_X4, train_y4, val_y4 = train_test_split(X4, y4, random_state = 1)

regr2 = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2))
regr2.fit(X4, y4)

pred2 = regr2.predict(val_X4)
csv6 = pd.DataFrame(pred2)
csv6.to_csv("long3.csv")
mae_SVR2 = mean_absolute_error(val_y4, pred2)
print(pred2)

print("Validation MAE for SVR: {}".format(mae_SVR2))