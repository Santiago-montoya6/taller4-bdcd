# Taller 4 — APIs Públicas, MongoDB y EDA

## Descripción
Pipeline de Ciencia de Datos que consume la Dragon Ball API, almacena los datos crudos en MongoDB y realiza un análisis exploratorio (EDA) en Jupyter Notebook.

## API utilizada
**Dragon Ball API** — https://web.dragonball-api.com/
Datos de personajes, planetas y transformaciones del universo Dragon Ball.  
Total registros: 121 documentos (58 personajes + 43 transformaciones + 20 planetas).

## Estructura del proyecto
```text
taller4-bdcd/
├── EDA/
│   ├── analisis.ipynb
│   ├── grafico_torta_genero.png
│   ├── grafico_barras_razas.png
│   └── grafico_bandos.png
├── etl/
│   ├── ingesta.py
│   └── config.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Cómo ejecutarlo
1. Instalar dependencias:
```bash
   pip install -r requirements.txt
```
2. Tener MongoDB corriendo en `mongodb://localhost:27017`
3. Ejecutar la ingesta:
```bash
   python3 etl/ingesta.py
```
4. Abrir el notebook:
```bash
   jupyter notebook EDA/analisis.ipynb
```

## Insights encontrados
1. Los **Saiyans** son la raza más frecuente con 10 personajes (17.2% del total).
2. El universo Dragon Ball tiene **13 razas distintas**, evidenciando su diversidad.
3. El **87.9%** de los personajes son masculinos — por cada mujer hay 7.3 hombres.
4. La afiliación más común es **Z Fighter** con 19 personajes (32.8%).
5. Los **héroes** (36.2%) superan a los **villanos** (24.1%), con un 39.7% de personajes neutros.