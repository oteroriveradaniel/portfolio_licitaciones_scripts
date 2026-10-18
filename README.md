# Portfolio

Licitaciones públicas del Ayuntamiento de A Coruña desde el 1 de enero de 2014.

## Scripts

Se utilizan scripts de Python para la carga inicial de datos desde un formato CSV a una base de datos MongoDB. Se cargan datos de 22000 contratos y adjudicatarios del ayuntamiento de A Coruña.

[Descarga los CSV para el volcado de datos aquí.](https://datos.coruna.gal/dataset/licitacions)

## Instalación

1. Descargar los CSV y guardarlos en una carpeta CSV dentro de la carpeta src del proyecto.
2. Instalar los requirements.
```python
pip install -r requirements.txt
```
3. Lanzar la aplicación.
```python
python3 main.py
```