# Guía de Detección y Eliminación de Virus en Ubuntu

## Introducción
Esta guía proporciona una descripción paso a paso para la detección y eliminación de virus en un sistema Ubuntu 22.04, utilizando ClamAV, un antivirus de código abierto.

## Contenido
1. [Detección del Virus](#detección-del-virus)
2. [Búsqueda de Antivirus](#búsqueda-de-antivirus)
3. [Elección del Antivirus](#elección-del-antivirus)
4. [Instalación de ClamAV](#instalación-de-clamav)
5. [Actualización de la Base de Datos](#actualización-de-la-base-de-datos)
6. [Uso de ClamAV](#uso-de-clamav)
7. [Consejos Finales](#consejos-finales)

## Detección del Virus
- Nuestro problema inicial se detectó al intentar enviar un archivo por Gmail, el cual mostró una advertencia de virus.

## Búsqueda de Antivirus
- Investigamos varias opciones de antivirus en línea.
- Consultamos páginas como [Cybernews](https://en.cybernews.com/lp/free-antivirus-software/?campaignId=17149047833&adgroupId=134969828863&adId=596197549913&targetId=kwd-419874111&device=c&gunique=Cj0KCQiAhomtBhDgARIsABcaYymjU0pIbtjoF61k8jlwOAq5MenQdFebRHCG2V1DY0SMzW4k1l7Cn84aArbvEALw_wcB&gad_source=1&gclid=Cj0KCQiAhomtBhDgARIsABcaYymjU0pIbtjoF61k8jlwOAq5MenQdFebRHCG2V1DY0SMzW4k1l7Cn84aArbvEALw_wcB) y [Safety Detectives](https://www.safetydetectives.com/blog/best-really-free-antivirus-for-linux/).
- Muchas alternativas resultaron no ser gratuitas.

## Elección del Antivirus
- Elegimos ClamAV por ser una opción gratuita y compatible con Ubuntu.

## Instalación de ClamAV
1. Abrimos la Terminal.

Ctrl + Alt + T

2. Actualizamos el sistema.
   
```bash
sudo apt update
```
3. Instalamos ClamAV.
```bash
sudo apt install clamav clamav-daemon
```

## Actualización de la Base de Datos
- Comando utilizado para actualizar la base de datos.

```bash
sudo freshclam
```

 ### **Problemas y Soluciones:**
- Nos encontramos con un error debido a un bloqueo de `freshclam.log`.
- Detuvimos el servicio clamav-freshclam y ejecutamos `freshclam` manualmente.
 ```bash
 sudo systemctl stop clamav-freshclam
 sudo freshclam
 sudo systemctl start clamav-freshclam
 ```

## Uso de ClamAV
1. Comando básico para escanear.
```bash
sudo clamscan -r --bell -i /
```

2. Para eliminar archivos infectados automáticamente.
```bash
sudo clamscan -r --bell -i --remove /
```

4. Para guardar un registro de los archivos afectados.
```bash
sudo clamscan -r --bell -i --remove --log=/ruta/del/archivo.txt /
```

### **Problemas y Soluciones:**
- Necesitamos reiniciar el escaneo con opciones adicionales.
- Detuvimos el escaneo y reiniciamos con las opciones `--remove` y `--log`.
 ```bash
 Ctrl + C
 sudo clamscan -r --bell -i --remove --log=/ruta/del/archivo.txt /
 ```

## Consejos Finales
- Realizar escaneos regularmente.
- Mantener actualizada la base de datos de virus.
- Ir con precaución al eliminar archivos automáticamente.
- De ser posible, tener previamente instalado el antivirus.
