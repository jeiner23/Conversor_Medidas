import pandas as pd

data = {
    "Piezas" : ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros" : [40,120,60,30,180]
}

df = pd.DataFrame(data)

df.to_excel("muebles_medidas.xlsx", index=False)
