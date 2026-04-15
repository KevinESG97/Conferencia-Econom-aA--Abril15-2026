import pandas as pd
import os

# Rutas datos crudos
ruta_datos_crudos = r'datoscrudos\datos-originales\TIPO-CAMBIO.xlsx'
ruta_datos_crudos2 = r'datoscrudos\datos-originales\deudapublica.xlsx'
ruta_datos_crudos3 = r'datoscrudos\datos-originales\export-import.xlsx'
ruta_datos_crudos4 = r'datoscrudos\datos-originales\libertadeconomica2026.xlsx'
ruta_datos_crudos5 = r'datoscrudos\datos-originales\PIB-2025.xlsx'
ruta_datos_crudos6 = r'datoscrudos\datos-originales\recaudaciontributaria.xlsx'
ruta_datos_crudos7 = r'datoscrudos\datos-originales\salariosminimos.xlsx'
ruta_datos_crudos8 = r'datoscrudos\datos-originales\SECTORES-2011.xlsx'
ruta_datos_crudos9 = r'datoscrudos\datos-originales\tasadesempleo.xlsx'

#Rutas de los datos limpios, archivos que se van a crear
ruta_datos_limpios = r'datoslimpios\TIPO-CAMBIO-limpio.xlsx'
ruta_datos_limpios2 = r'datoslimpios\deudapublica-limpio.xlsx'
ruta_datos_limpios3 = r'datoslimpios\export-import-limpio.xlsx'
ruta_datos_limpios4 = r'datoslimpios\libertadeconomica2026-limpio.xlsx'
ruta_datos_limpios5 = r'datoslimpios\PIB-2025-limpio.xlsx'
ruta_datos_limpios6 = r'datoslimpios\recaudaciontributaria-limpio.xlsx'
ruta_datos_limpios7 = r'datoslimpios\salariosminimos-limpio.xlsx'
ruta_datos_limpios8 = r'datoslimpios\SECTORES-2011-limpio.xlsx'
ruta_datos_limpios9 = r'datoslimpios\tasadesempleo-limpio.xlsx'



# verifico que exista el directorio de datos limpios si no se crea
os.makedirs(os.path.dirname(ruta_datos_limpios), exist_ok=True)

#============================================
#       LIMPIEZA DE TIPO DE CAMBIO          =
#============================================
#tengo el problema que el valor del precio decimal están con coma decimal, no con punto decimal

# Leer el archivo Excel
df = pd.read_excel(ruta_datos_crudos)
print("===========I. ARCHIVO TIPO-CAMBIO ============")
print("\tTotal de registros:", len(df))
# Convertir coma decimal a punto decimal en la columna PRECIO
df['PRECIO'] = df['PRECIO'].astype(str).str.replace(',', '.')
df['PRECIO'] = pd.to_numeric(df['PRECIO'], errors='coerce') 
df = df.rename(columns={'PAÍS': 'País', 'PRECIO': 'Precio 1$'})

# cambios realizados
print(" Cambios realizados:")
print("  1. Pasar de coma decimal a punto decimal en la columna PRECIO")
# Guardar en datoslimpios
df.to_excel(ruta_datos_limpios, index=False)
print(f"\t ==>> Archivo guardado en: {ruta_datos_limpios}")

print("\n")
#============================================
#       LIMPIEZA DE DEUDA PUBLICA          =
#============================================

# Leer el archivo Excel
df2 = pd.read_excel(ruta_datos_crudos2)
print("===========II.  DEUDA PUBLICA ============")
print(f"\tTotal de registros: {len(df2)}")

# Limpiar Países
df2['Países'] = df2['Países'].astype(str).str.replace(r' \[\+\]', '', regex=True)

# Limpiar  Deuda total (M.$)
df2['Deuda total (M.$)'] = df2['Deuda total (M.$)'].astype(str).str.replace('.', '', regex=False)
df2['Deuda total (M.$)'] = pd.to_numeric(df2['Deuda total (M.$)'], errors='coerce')
# Multiplicar por 1,000,000 para dejar el dato completo
df2['Deuda total (M.$)'] = df2['Deuda total (M.$)'] * 1_000_000
# Renombrar columna
df2 = df2.rename(columns={'Deuda total (M.$)': 'Deuda total $'})

#  Limpiar Deuda Per Cápita
df2['Deuda Per Cápita'] = df2['Deuda Per Cápita'].astype(str).str.replace(r'\s*\$', '', regex=True)
df2['Deuda Per Cápita'] = df2['Deuda Per Cápita'].str.replace('.', '', regex=False)
df2['Deuda Per Cápita'] = pd.to_numeric(df2['Deuda Per Cápita'], errors='coerce')

df2 = df2.rename(columns={'Países': 'País' })
# cambios realizados
print(" Cambios realizados:")
print(f"  Países: se removió ' [+]' del final")
print(f"  Deuda total $: se convirtió a número")
print(f"  Deuda Per Cápita: se removió el símbolo '$' y se convirtió a número")

# Guardar en datoslimpios
df2.to_excel(ruta_datos_limpios2, index=False)
print(f" ==>> Archivo guardado en: {ruta_datos_limpios2} \n")

#============================================
# LIMPIEZA DE EXPORTACIONES IMPORTACIONES   =
#============================================

# Leer el archivo Excel
df3 = pd.read_excel(ruta_datos_crudos3)
print("=========== ARCHIVO EXPORT-IMPORT ============")
print(f"\tTotal de registros: {len(df3)}")

# 1. Limpiar espacios en blanco al inicio y final 
df3['País / territorio'] = df3['País / territorio'].astype(str).str.strip()

# 2. Limpiar columnas de valores numericos "exportaciones_m_usd", "importaciones_m_usd" "export-import"
df3['exportaciones_m_usd'] = df3['exportaciones_m_usd'].astype(str).str.replace('.', '', regex=False)
df3['exportaciones_m_usd'] = pd.to_numeric(df3['exportaciones_m_usd'], errors='coerce')
df3['exportaciones_m_usd'] = df3['exportaciones_m_usd'] * 1_000_000

df3['importaciones_m_usd'] = df3['importaciones_m_usd'].astype(str).str.replace('.', '', regex=False)
df3['importaciones_m_usd'] = pd.to_numeric(df3['importaciones_m_usd'], errors='coerce')
df3['importaciones_m_usd'] = df3['importaciones_m_usd'] * 1_000_000

df3['export-import'] = df3['export-import'].astype(str).str.replace('.', '', regex=False)
df3['export-import'] = pd.to_numeric(df3['export-import'], errors='coerce')
df3['export-import'] = df3['export-import'] * 1_000_000

df3 = df3.rename(columns={'País / territorio': 'País', 'exportaciones_m_usd': 'Exportaciones $', 'importaciones_m_usd': 'Importaciones $', 'export-import': 'Export-Import $'})  

print(" Cambios realizados:")
print(f"   País: Removidos espacios en blanco al inicio y final con .strip()")
print(f"   Exportaciones $: Removidos puntos separadores y convertido a número")
print(f"   Importaciones $: Removidos puntos separadores y convertido a número")
print(f"   Export-Import $: Removidos puntos separadores y convertido a número")
 
df3.to_excel(ruta_datos_limpios3, index=False)
print(f" ==>> Archivo guardado en: {ruta_datos_limpios3} \n")


#============================================
#     LIMPIEZA DE LIBERTAD ECONOMICA        =
#============================================

# Leer el archivo Excel
df4 = pd.read_excel(ruta_datos_crudos4)
print("=========== ARCHIVO LIBERTAD ECONOMICA ============")
print(f"\tTotal de registros: {len(df4)}")

# 1. Limpiar espacios en blanco al inicio y final
df4['pais'] = df4['pais'].astype(str).str.strip()

df4 = df4.rename(columns={'pais': 'País'})

print(" Cambios realizados:")
print(f"   País: Removidos espacios en blanco al inicio y final con .strip()")
 
df4.to_excel(ruta_datos_limpios4, index=False)
print(f" ==>> Archivo guardado en: {ruta_datos_limpios4} \n")



#============================================
#            LIMPIEZA DE PIB                =
#============================================

# Leer el archivo Excel
df5 = pd.read_excel(ruta_datos_crudos5)
print("=========== ARCHIVO PIB ============")
print(f"\tTotal de registros: {len(df5)}")
 
df5['PIB (Valor total)'] = df5['PIB (Valor total)'].astype(str).str.replace('.', '', regex=False)
df5['PIB (Valor total)'] = pd.to_numeric(df5['PIB (Valor total)'], errors='coerce') 
 
df5['Crecimiento del PIB'] = df5['Crecimiento del PIB'].str.replace('−', '-', regex=False) 
df5['Crecimiento del PIB'] = df5['Crecimiento del PIB'].astype(str).str.replace(',', '.', regex=False)
df5['Crecimiento del PIB'] = df5['Crecimiento del PIB'].str.replace('%', '', regex=False)
df5['Crecimiento del PIB'] = pd.to_numeric(df5['Crecimiento del PIB'], errors='coerce') 

df5['PIB per cápita'] = df5['PIB per cápita'].astype(str).str.replace('.', '', regex=False)
df5['PIB per cápita'] = pd.to_numeric(df5['PIB per cápita'], errors='coerce') 

df5 = df5.rename(columns={ 'pais': 'País', 'PIB (Valor total)': 'PIB $', 'Crecimiento del PIB': 'Crecimiento PIB %', 'PIB per cápita': 'PIB per cápita $'})  

print(" Cambios realizados:")
print(f"   País: Removidos espacios en blanco al inicio y final con .strip()")
print(f"   PIB $: Removidos puntos separadores y convertido a número")
print(f"   Crecimiento PIB %: Removidos puntos y porcentajes y convertido a número")
print(f"   PIB per cápita $: Removidos puntos separadores y convertido a número")
 
df5.to_excel(ruta_datos_limpios5, index=False)
print(f" ==>> Archivo guardado en: {ruta_datos_limpios5} \n")



#============================================
#            RECAUDACIÓN TRIBUTARIA         =
#============================================

df6 = pd.read_excel(ruta_datos_crudos6)
print("=========== ARCHIVO RECAUDACION TRIBUTARIA ============")
print(f"\tTotal de registros: {len(df6)}")

df6['Países'] = df6['Países'].str.replace(r' \[\+\]', '', regex=True)
df6['Ingresos fiscales (M. $)'] = df6['Ingresos fiscales (M. $)'].astype(str).str.replace('.', '', regex=False)
df6['Ingresos fiscales (M. $)'] = df6['Ingresos fiscales (M. $)'].astype(str).str.replace(',', '.', regex=False)
df6['Ingresos fiscales (M. $)'] = pd.to_numeric(df6['Ingresos fiscales (M. $)'], errors='coerce')
df6['Ingresos fiscales (M. $)'] = df6['Ingresos fiscales (M. $)'] * 1_000_000
df6['Ingresos fiscales (Per capita $)'] = df6['Ingresos fiscales (Per capita $)'].astype(str).str.replace('.', '', regex=False)
df6['Ingresos fiscales (Per capita $)'] = pd.to_numeric(df6['Ingresos fiscales (Per capita $)'], errors='coerce')

df6 = df6.rename(columns={'Países': 'País', 'Ingresos fiscales (M. $)': 'Ingresos fiscales $', 'Ingresos fiscales (Per capita $)': 'Ingresos fiscales per capita $'})

print(" Cambios realizados:")
print(f"   País: Removidos espacios en blanco al inicio y final con .strip()")
print(f"   Ingresos fiscales $: Removidos puntos separadores, convertido a número y multiplicado por 1,000,000")
print(f"   Ingresos fiscales per capita $: Removidos puntos separadores y convertido a número")
df6.to_excel(ruta_datos_limpios6, index=False)
print(f" ==>> Archivo guardado en: {ruta_datos_limpios6} \n")


#============================================
#            SALARIOS MÍNIMOS               =
#============================================

df7 = pd.read_excel(ruta_datos_crudos7)
print("=========== ARCHIVO SALARIOS MÍNIMOS ============")
print(f"\tTotal de registros: {len(df7)}")

df7['sueldo_anual_usd'] = df7['sueldo_anual_usd'].astype(str).str.replace('.', '', regex=False)
df7['sueldo_anual_usd'] = pd.to_numeric(df7['sueldo_anual_usd'], errors='coerce')

df7 = df7.rename(columns={'pais': 'País' })
print(" Cambios realizados:")
print(f"   sueldo_anual_usd: Removidos puntos separadores y convertido a número")
df7.to_excel(ruta_datos_limpios7, index=False)
print(f" ==>> Archivo guardado en: {ruta_datos_limpios7} \n")

#============================================
#            sectores economicos            =
#============================================

df8 = pd.read_excel(ruta_datos_crudos8)
print("=========== ARCHIVO SECTORES ECONOMICOS ============")
print(f"\tTotal de registros: {len(df8)}")

df8['total_pib_mm']= df8['total_pib_mm'].astype(str).str.replace(' ', '', regex=False)
df8['total_pib_mm'] = pd.to_numeric(df8['total_pib_mm'], errors='coerce') 
df8['total_pib_mm'] = df8['total_pib_mm'] * 1_000_000
df8['agricultura_usd_mm'] = df8['agricultura_usd_mm'].astype(str).str.replace(' ', '', regex=False)
df8['agricultura_usd_mm'] = pd.to_numeric(df8['agricultura_usd_mm'], errors='coerce')
df8['agricultura_usd_mm'] = df8['agricultura_usd_mm'] * 1_000_000
df8['industria_usd_mm'] = df8['industria_usd_mm'].astype(str).str.replace(' ', '', regex=False)
df8['industria_usd_mm'] = pd.to_numeric(df8['industria_usd_mm'], errors='coerce')
df8['industria_usd_mm'] = df8['industria_usd_mm'] * 1_000_000
df8['servicios_usd_mm'] = df8['servicios_usd_mm'].astype(str).str.replace(' ', '', regex=False)
df8['servicios_usd_mm'] = pd.to_numeric(df8['servicios_usd_mm'], errors='coerce')
df8['servicios_usd_mm'] = df8['servicios_usd_mm'] * 1_000_000

df8 = df8.rename(columns={'pais': 'País', 'total_pib_mm': 'Total PIB $(2011)', 'agricultura_usd_mm': 'Agricultura $(2011)', 'industria_usd_mm': 'Industria $(2011)', 'servicios_usd_mm': 'Servicios $(2011)'})  
print(" Cambios realizados:")
print(f"   total PIB $(2011): Removidos espacios, convertido a número y multiplicado por 1,000,000")
print(f"   Agricultura $(2011): Removidos espacios, convertido a número y multiplicado por 1,000,000")
print(f"   Industria $(2011): Removidos espacios, convertido a número y multiplicado por 1,000,000")
print(f"   Servicios $(2011): Removidos espacios, convertido a número y multiplicado por 1,000,000")
df8.to_excel(ruta_datos_limpios8, index=False) 
print(f" ==>> Archivo guardado en: {ruta_datos_limpios8} \n")


#============================================
#            tasa de desempleo            =
#============================================

df9 = pd.read_excel(ruta_datos_crudos9)

print("=========== ARCHIVO TASA DE DESEMPLEO ============")
print(f"\tTotal de registros: {len(df9)}")

df9['Tasa de desempleo (%)'] = df9['Tasa de desempleo (%)'].astype(str).str.replace(',', '.', regex=False)
df9['Tasa de desempleo (%)'] = pd.to_numeric(df9['Tasa de desempleo (%)'], errors='coerce')

df9 = df9.rename(columns={'pais': 'País' })
print(" Cambios realizados:")
print(f"   Tasa de desempleo (%): Removidos puntos separadores y convertido a número")
df9.to_excel(ruta_datos_limpios9, index=False)
print(f"==>> Archivo guardado en: {ruta_datos_limpios9} \n")
