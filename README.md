# Log IP Analyzer

## Descripción
Este proyecto consiste en un script desarrollado en Python que permite analizar archivos de logs para extraer direcciones IP, eliminar duplicados y generar un archivo limpio con los resultados.

## Funcionalidad
- Lectura de archivos de log
- Extracción de direcciones IP mediante expresiones regulares (Regex)
- Eliminación de direcciones IP duplicadas
- Ordenamiento de resultados
- Generación de archivo de salida

## Tecnologías utilizadas
- Python 3
- Librería `re` (expresiones regulares)

## Uso

Ejecutar el script:

```bash
python3 filtrar_ips.py --input log.txt --output resultado.txt

Ejemplo de salida
10.0.0.5
172.16.0.2
192.168.1.10

Autor
DRN 

