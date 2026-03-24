import re

try:
    with open("logs.txt", "r") as archivo:
        contenido = archivo.read()

    ips = re.findall(r"\d+\.\d+\.\d+\.\d+", contenido)

    ips_unicas = sorted(set(ips))


    with open("ips_filtradas.txt", "w") as salida:
        for ip in ips_unicas:
            salida.write(ip + "\n")

    print("IPs extraidas y guardadas correctamente")

except FileNotFoundError:
    print("Error: el archivo logs.txt no existe")
