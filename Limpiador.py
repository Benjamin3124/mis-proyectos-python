import os


ruta = "./documentos_importantes"

if not os.path.exists(ruta):
    os.makedirs(ruta)
    print(f"Carpeta {ruta} creada automaticamente.")
print(f"--- ANALIZANDO CARPETA: {ruta} ---")

archivos = os.listdir(ruta)
encontrados = 0 

for archivo in archivos:
    if archivo.endswith(".txt"):
        print(f"[!] Archivo encontrado: {archivo}")
        encontrados += 1
if encontrados == 0:
    print("Carpeta limpia. No hay archivos temporales.")
else:
    print(f"Se encontraron {encontrados} archivos para revisar.")
    
import os


ruta = "./documentos_importantes"
print(f"--- ANALIZANDO CARPETA: {ruta} ---")
      
archivos = os.listdir (ruta)
encontrados = 0

for archivo in archivos: 
    if archivo.endswith(".txt"):
       print(f"[!] Archivo encontrado: {archivo}")
       encontrados += 1

if encontrados == 0:
    print("Carpeta limpia. No hay archivos temporales.")
else:
     print(f"Se encontraron {encontrados} archivos para revisar.")