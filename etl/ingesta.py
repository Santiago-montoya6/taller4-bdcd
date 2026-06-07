import requests
import pymongo

from config import MONGO_URI, DB_NAME, COLLECTION_NAME

# --- CONEXIÓN A MONGODB ---
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

collection.drop()
print("Colección limpiada.\n")

# --- FUNCIÓN PARA ENDPOINTS CON PAGINACIÓN ---
def descargar_paginado(endpoint, tipo):
    resultado = []
    pagina = 1

    while True:
        url = f"https://dragonball-api.com/api/{endpoint}?page={pagina}&limit=10"
        response = requests.get(url)
        data = response.json()
        items = data.get("items", [])

        if not items:
            break

        for item in items:
            item["_tipo"] = tipo

        resultado.extend(items)
        print(f"  [{tipo}] Página {pagina} — acumulado: {len(resultado)}")

        if pagina >= data["meta"]["totalPages"]:
            break

        pagina += 1

    return resultado

# --- FUNCIÓN PARA ENDPOINTS SIN PAGINACIÓN (lista directa) ---
def descargar_lista(endpoint, tipo):
    url = f"https://dragonball-api.com/api/{endpoint}"
    response = requests.get(url)
    items = response.json()

    for item in items:
        item["_tipo"] = tipo

    print(f"  [{tipo}] Total: {len(items)}")
    return items

# --- DESCARGAR TODO ---
print("Descargando personajes...")
personajes = descargar_paginado("characters", "personaje")

print("\nDescargando planetas...")
planetas = descargar_paginado("planets", "planeta")

print("\nDescargando transformaciones...")
transformaciones = descargar_lista("transformations", "transformacion")

todos = personajes + planetas + transformaciones
print(f"\nTotal combinado: {len(todos)} registros")

# --- INSERTAR EN MONGODB (RAW) ---
collection.insert_many(todos)
print(f"Insertados en MongoDB: {collection.count_documents({})} documentos ✓")