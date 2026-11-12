# AliGyn Boutique

Chat de atención para AliGyn Boutique, creado con Flask y HTML.

## Requisitos

- Python 3.9 o posterior

## Instalación y ejecución

Desde esta carpeta, ejecuta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py Ejercicio_Autonomo.py
```

Después abre `http://127.0.0.1:5000` en el navegador.

El servidor integrado de Flask está pensado solo para desarrollo local.

## Despliegue en Vercel

Importa este repositorio en Vercel y despliega la rama `main`. La configuración
en `pyproject.toml` indica a Vercel que la aplicación Flask está en
`Ejercicio_Autonomo.py`.
