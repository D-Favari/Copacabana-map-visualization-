import matplotlib.pyplot as plt
import pandas as pd 
import mplleaflet as mpl

# disperção
df = pd.read_csv("copacabana_lat_lng.csv")
plt.scatter(df['lng'], df['lat'], marker = '.')
plt.show() 

# mapa
plt.scatter(df['lng'], df['lat'], marker='.')
mpl.show()