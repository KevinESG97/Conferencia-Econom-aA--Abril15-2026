import pandas as pd
import os

# Diccionario de nombres de países 
normalizar_paises = {
    # América
    'estados unidos': 'Estados Unidos',
    'usa': 'Estados Unidos',
    'ee.uu.': 'Estados Unidos',
    'united states': 'Estados Unidos',
    'las bahamas': 'Bahamas',
    'republica dominicana': 'República Dominicana',
    'santo tomé y príncipe': 'Santo Tomé y Príncipe',
    'santo tome y príncipe': 'Santo Tomé y Príncipe',
    'santo tome': 'Santo Tomé y Príncipe',
    'são tomé y príncipe': 'Santo Tomé y Príncipe',
    'curazao': 'Curaçao',
    'curaçao': 'Curaçao',
    'haiti': 'Haití',
    'haití': 'Haití',
    'canada': 'Canadá',
    'canadá': 'Canadá',
    'san cristóbal y nieves': 'San Cristóbal y Nieves',
    'san cristobal y nieves': 'San Cristóbal y Nieves',
    'san martín': 'San Martín',
    'san martin': 'San Martín',
    'sint maarten': 'San Martín',
    
    # Europa
    'reino unido': 'Reino Unido',
    'uk': 'Reino Unido',
    'grande bretaña': 'Reino Unido',
    'gran bretaña': 'Reino Unido',
    'país de gales': 'Reino Unido',
    'chequia': 'República Checa',
    'república checa': 'República Checa',
    'república checa (chequia)': 'República Checa',
    'czech republic': 'República Checa',
    'bélgica': 'Bélgica',
    'belgica': 'Bélgica',
    'Países Bajos': 'Países Bajos',
    'países bajos': 'Países Bajos',
    'paises bajos': 'Países Bajos',
    'holanda': 'Países Bajos',
    'netherlands': 'Países Bajos',
    'bielorrusia': 'Bielorrusia',
    'romania': 'Rumanía',
    'rumania': 'Rumanía',
    'hungría': 'Hungría',
    'serbia': 'Serbia',
    'bosnia y herzegovina': 'Bosnia y Herzegovina',
    'bosnia-herzegovina': 'Bosnia y Herzegovina',
    'montenegro': 'Montenegro',
    'kosovo': 'Kosovo',
    'turquía': 'Turquía',
    'türkiye': 'Turquía',
    'turquia': 'Turquía',
    'grecia': 'Grecia',
    'italia': 'Italia',
    'españa': 'España',
    'espana': 'España',
    'portugal': 'Portugal',
    'malta': 'Malta',
    'chipre': 'Chipre',
    'chipre del norte': 'Chipre del Norte',
    'francia': 'Francia',
    'luxemburgo': 'Luxemburgo',
    'irlanda': 'Irlanda',
    'dinamarca': 'Dinamarca',
    'suecia': 'Suecia',
    'noruega': 'Noruega',
    'finlandia': 'Finlandia',
    'islandia': 'Islandia',
    'estonia': 'Estonia',
    'letonia': 'Letonia',
    'lituania': 'Lituania',
    'polonia': 'Polonia',
    'alemania': 'Alemania',
    'austria': 'Austria',
    'eslovaquia': 'Eslovaquia',
    'eslovenia': 'Eslovenia',
    'liechtenstein': 'Liechtenstein',
    'suiza': 'Suiza',
    'switzerland': 'Suiza',
    'andorra': 'Andorra',
    'san marino': 'San Marino',
    'mónaco': 'Mónaco',
    'monaco': 'Mónaco',
    
    # Asia
    'corea del sur': 'Corea del Sur',
    'sur corea': 'Corea del Sur',
    'corea': 'Corea del Sur',
    'south korea': 'Corea del Sur',
    'corea del norte': 'Corea del Norte',
    'north korea': 'Corea del Norte',
    'china': 'China',
    'republica popular china': 'China',
    'japón': 'Japón',
    'japon': 'Japón',
    'taiwan': 'Taiwán',
    'taiwán': 'Taiwán',
    'hong kong': 'Hong Kong',
    'macao': 'Macao',
    'macau': 'Macao',
    'vietnam': 'Vietnam',
    'viet nam': 'Vietnam',
    'tailandia': 'Tailandia',
    'camboya': 'Camboya',
    'laos': 'Laos',
    'birmania': 'Myanmar',
    'myanmar': 'Myanmar',
    'malasia': 'Malasia',
    'singapur': 'Singapur',
    'brunei': 'Brunéi',
    'brunéi': 'Brunéi',
    'filipinas': 'Filipinas',
    'indonesia': 'Indonesia',
    'timor oriental': 'Timor Oriental',
    'timor leste': 'Timor Oriental',
    'india': 'India',
    'pakistan': 'Pakistán',
    'pakistán': 'Pakistán',
    'bangladesh': 'Bangladesh',
    'bangladés': 'Bangladesh',
    'nepal': 'Nepal',
    'bhutan': 'Bután',
    'bután': 'Bután',
    'sri lanka': 'Sri Lanka',
    'afganistán': 'Afganistán',
    'irán': 'Irán',
    'iran': 'Irán',
    'irak': 'Irak',
    'iraq': 'Irak',
    'siria': 'Siria',
    'jordania': 'Jordania',
    'israel': 'Israel',
    'palestina': 'Palestina',
    'estado de palestina': 'Palestina',
    'líbano': 'Líbano',
    'libano': 'Líbano',
    'arabia saudita': 'Arabia Saudita',
    'yemen': 'Yemen',
    'omán': 'Omán',
    'oman': 'Omán',
    'emiratos árabes unidos': 'Emiratos Árabes Unidos',
    'emiratos arabes unidos': 'Emiratos Árabes Unidos',
    'qatar': 'Qatar',
    'catar': 'Catar',
    'kuwait': 'Kuwait',
    'bahrein': 'Bahrein',
    'kazajistán': 'Kazajistán',
    'kazajstán': 'Kazajistán',
    'kazakhstan': 'Kazajistán',
    'uzbekistan': 'Uzbekistán',
    'uzbekistán': 'Uzbekistán',
    'tayikistán': 'Tayikistán',
    'turkmenistán': 'Turkmenistán',
    'kirguistán': 'Kirguistán',
    'kyrgyzstan': 'Kirguistán',
    'georgia': 'Georgia',
    'armenia': 'Armenia',
    'azerbaiyán': 'Azerbaiyán',
    'rusia': 'Rusia',
    'ucrania': 'Ucrania',
    'moldavia': 'Moldavia',
    
    # África
    'sudáfrica': 'Sudáfrica',
    'sudafrica': 'Sudáfrica',
    'south africa': 'Sudáfrica',
    'marruecos': 'Marruecos',
    'argelia': 'Argelia',
    'túnez': 'Túnez',
    'tunez': 'Túnez',
    'libia': 'Libia',
    'egipto': 'Egipto',
    'sudán': 'Sudán',
    'sudan': 'Sudán',
    'sudán del sur': 'Sudán del Sur',
    'etiopía': 'Etiopía',
    'etiopia': 'Etiopía',
    'kenia': 'Kenia',
    'tanzania': 'Tanzania',
    'uganda': 'Uganda',
    'ruanda': 'Ruanda',
    'burundi': 'Burundi',
    'somalia': 'Somalia',
    'nigeria': 'Nigeria',
    'camerún': 'Camerún',
    'camerun': 'Camerún',
    'congo': 'Congo',
    'república del congo': 'Congo',
    'rdc': 'República Democrática del Congo',
    'rd congo': 'República Democrática del Congo',
    'república democrática del congo': 'República Democrática del Congo',
    'rep. democrática del congo': 'República Democrática del Congo',
    'rep democrática del congo': 'República Democrática del Congo',
    'malí': 'Malí',
    'mali': 'Malí',
    'mauritania': 'Mauritania',
    'senegal': 'Senegal',
    'gambia': 'Gambia',
    'guinea': 'Guinea',
    'guinea-bissau': 'Guinea-Bissau',
    'guinea-bisáu': 'Guinea-Bissau',
    'sierra leona': 'Sierra Leona',
    'liberia': 'Liberia',
    'costa de marfil': 'Costa de Marfil',
    'benín': 'Benín',
    'benin': 'Benín',
    'togo': 'Togo',
    'ghana': 'Ghana',
    'burkina faso': 'Burkina Faso',
    'níger': 'Níger',
    'niger': 'Níger',
    'chad': 'Chad',
    'república centroafricana': 'República Centroafricana',
    'africa central': 'República Centroafricana',
    'africa occidental': 'Entre países',
    'gabón': 'Gabón',
    'gabon': 'Gabón',
    'congo ecuatorial': 'Guinea Ecuatorial',
    'guinea ecuatorial': 'Guinea Ecuatorial',
    'santo tomé y príncipe': 'Santo Tomé y Príncipe',
    'saint tome and principe': 'Santo Tomé y Príncipe',
    'caboverde': 'Cabo Verde',
    'cabo verde': 'Cabo Verde',
    'seychelles': 'Seychelles',
    'mauricio': 'Mauricio',
    'madagascar': 'Madagascar',
    'malawi': 'Malawi',
    'malaui': 'Malawi',
    'zambia': 'Zambia',
    'zimbabue': 'Zimbabue',
    'zimbabuee': 'Zimbabue',
    'zimbabue': 'Zimbabue',
    'botswana': 'Botswana',
    'botsuana': 'Botswana',
    'namibia': 'Namibia',
    'lesoto': 'Lesoto',
    'lesotho': 'Lesoto',
    'esuatini': 'Esuatini',
    'eswatini': 'Esuatini',
    'swazilandia': 'Esuatini',
    'suazilandia': 'Esuatini',
    'mozambique': 'Mozambique',
    'angola': 'Angola',
    'djibouti': 'Yibuti',
    'yibuti': 'Yibuti',
    
    # Oceanía
    'australia': 'Australia',
    'nueva zelanda': 'Nueva Zelanda',
    'new zealand': 'Nueva Zelanda',
    'fiji': 'Fiji',
    'fiyi': 'Fiji',
    'samoa': 'Samoa',
    'samoa occidental': 'Samoa',
    'samoa independiente': 'Samoa',
    'samoa americana': 'Samoa Americana',
    'american samoa': 'Samoa Americana',
    'tonga': 'Tonga',
    'vanuatu': 'Vanuatu',
    'kiribati': 'Kiribati',
    'nauru': 'Nauru',
    'palaos': 'Palaos',
    'palau': 'Palaos',
    'estados federados de micronesia': 'Micronesia',
    'micronesia': 'Micronesia',
    'islas marshall': 'Islas Marshall',
    'marshall islands': 'Islas Marshall',
    'islas salomon': 'Islas Salomón',
    'islas salomón': 'Islas Salomón',
    'papua nueva guinea': 'Papúa Nueva Guinea',
    'papúa nueva guinea': 'Papúa Nueva Guinea',
    
    # Otros
    'mundo': 'Mundo',
    'eurozona': 'Eurozona',
    'unión europea': 'Unión Europea',
}

def normalizar_nombre_pais(pais): 
    if pd.isna(pais):
        return pais
    pais_limpio = str(pais).strip().lower()
    return normalizar_paises.get(pais_limpio, str(pais).strip())

# Ruta de datos limpios
ruta_datos_limpios = r'datoslimpios'

# Definir archivos con las columnas a extraer de cada uno
archivos = [
  #  ('TIPO-CAMBIO-limpio.xlsx', 'Tipo-Cambio', ['DIVISA','Precio 1$']),
   ('TIPO-CAMBIO-limpio.xlsx', 'Tipo-Cambio', ['Precio 1$']),
    ('deudapublica-limpio.xlsx', 'Deuda-Publica', ['Deuda total $']),
    ('export-import-limpio.xlsx', 'Export-Import', ['Exportaciones $', 'Importaciones $']),
    ('libertadeconomica2026-limpio.xlsx', 'Libertad-Economica', ['Nota']),
    ('PIB-2025-limpio.xlsx', 'PIB', ['PIB $', 'Crecimiento PIB %']),
    ('recaudaciontributaria-limpio.xlsx', 'Recaudacion', ['Ingresos fiscales $']),
    ('salariosminimos-limpio.xlsx', 'Salarios', ['sueldo_anual_usd', 'horas_trabajo_semana']),
    ('tasadesempleo-limpio.xlsx', 'Tasa-Desempleo', ['Tasa de desempleo (%)']),
    ('SECTORES-2011-limpio.xlsx', 'Sectores', ['Total PIB $(2011)', 'agricultura%', 'industria%', 'servicios%', 'Agricultura $(2011)', 'Industria $(2011)', 'Servicios $(2011)']),
]

# Leer todos los archivos y normalizar países
dataframes = {}
paises_totales = set()

for archivo, alias, columnas_deseadas in archivos:
    ruta = os.path.join(ruta_datos_limpios, archivo)
    if os.path.exists(ruta):
        df = pd.read_excel(ruta)     

        # Identificar columna de país
        col_pais = None
        for col in df.columns:
            if 'país' in col.lower() or 'pais' in col.lower():
                col_pais = col
                break
        
        if col_pais:
            # Normalizar nombres de países
            df[col_pais] = df[col_pais].apply(normalizar_nombre_pais)
            
            # Renombrar columna a 'País' para consistencia
            df = df.rename(columns={col_pais: 'País'})
            
            # Seleccionar solo las columnas deseadas (más la columna País)
            cols_a_mantener = ['País'] + [col for col in columnas_deseadas if col in df.columns]
            df = df[cols_a_mantener]
            
            dataframes[alias] = df
            paises_totales.update(df['País'].unique())
            
            print(f" {alias}: {len(df)} registros, {len(cols_a_mantener)-1} columnas seleccionadas")
        else:
            print(f"[WARN] {archivo}: No se encontró columna de país")
    else:
        print(f"[ERROR] {archivo}: No existe")

print(f"\n Total de países únicos encontrados: {len(paises_totales)}")

print("\n" + "=" * 80)
print("Archivo final: \n")

df_maestro = pd.DataFrame({'País': sorted(paises_totales)})
print(f"\n Archivo creado con {len(df_maestro)} países")

# cargando de cada archivo
for alias, df in dataframes.items():
    df_maestro = df_maestro.merge(df, on='País', how='left')
    print(f"Se ha cargado el archivo {alias}")

# guardar archivo
ruta_salida = r'datoslimpios\DATOS-CONSOLIDADOS.xlsx'
df_maestro.to_excel(ruta_salida, index=False)

print(f"\nArchivo unido, guardado en: {ruta_salida} \n")
