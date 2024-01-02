# Instrucciones para Configurar el Entorno de Python y Kernel para Jupyter Notebook
Asumimos que 
- tienes conda
- ejecutarás el archivo .ipynb en Visual Studio Code
- en el documento `requirements.txt` hay una lista de librerías escritas en formato:
```
pandas>=1.2.0
numpy>=1.19.2
seaborn>=0.11.0
matplotlib>=3.3.2
plotly>=4.14.3
scikit-learn>=0.24.1
```

## En la carpeta donde tengas el notebook:

1. **Abre la terminal y ejecuta:**

```bash
conda create -n mientorno python=3.9
```

3. **Activa el entorno:**
```bash
conda activate mientorno
```

5. **Instala las librerías:**
```bash
pip install -r requirements.txt
```

## Creación del Kernel de Jupyter:

1. **Instala ipykernel:**
```bash
conda install ipykernel
```

3. **Crea el kernel de Jupyter:**

```bash
python -m ipykernel install mientorno --display-name "Python 3.9 (mientorno)"
```

## Uso en VS Code:

1. **Abre VS Code y ejecuta una línea de código del .ipynb.**
2. **Selecciona este kernel:** 
- Python 3.9 (mientorno)

## Instalación de Paquetes Adicionales:

- En caso de necesitar instalar algo más:

```bash
pip install nombre_paquete
```

## Creación de un Nuevo requirements.txt:

- Si necesitas escribir un nuevo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## Para finalizar el uso del entorno:

- Desactiva el entorno con:
```bash
conda deactivate mientorno
```
