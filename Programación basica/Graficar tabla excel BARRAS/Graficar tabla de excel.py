#Graficar una tabla de excel
#Con barras 
import pandas as pd
import matplotlib.pyplot as plt

WBK1="Reporte.xlsx"
df=pd.read_excel(WBK1)

#Imprimir el 'encabezado' de la hoja de trabajo
#print(df.head())

#Imprimir solo el 'Año' que es la primera columna de la hoja de trabajo
#año=df[["Año"]]
#print(año)

#Imprimir las entradas
#entradas=df[["Entradas",]]
#print(entradas)

valores=df[["Fecha","Resultado"]]
ax=valores.plot.bar(x="Fecha", y="Resultado",rot =0)
plt.xticks(rotation=45) #Rotar el texto en el eje x 45 grados
 
plt.show()
