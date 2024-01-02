# Instrucciones para Configurar el Entorno de Python

## En la carpeta donde tengas el notebook:

1. **Abre la terminal y ejecuta:**
conda create -n mientorno python=3.9

2. **Activa el entorno:**
conda activate mientorno

3. **Instala las librerías:**
pip install -r requirements.txt

## Creación del Kernel de Jupyter:

1. **Instala ipykernel:**
conda install ipykernel

2. **Crea el kernel de Jupyter:**
python -m ipykernel install mientorno --display-name "Python 3.9 (mientorno)"

## Uso en VS Code:

1. **Abre VS Code y ejecuta una línea de código del .ipynb.**
2. **Selecciona este kernel:** 
- Python 3.9 (mientorno)

## Instalación de Paquetes Adicionales:

- En caso de necesitar instalar algo más:

pip install nombre_paquete

## Creación de un Nuevo requirements.txt:

- Si necesitas escribir un nuevo `requirements.txt`:

pip freeze > requirements.txt

## Para finalizar el uso del entorno:

- Desactiva el entorno con:
  
conda deactivate mientorno

