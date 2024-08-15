import pandas as pd


def cm_a_pulgada(cm):
    return cm / 2.54


df = pd.read_excel("muebles_medidas.xlsx")

df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgada)

df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print(
    "Conversion completada y guardada en el archivo llamado 'mueble_medidas_convertidas.xlsx'"
)
