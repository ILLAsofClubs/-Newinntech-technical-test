# 🚀 Voter API

**Voter API** es un proyecto orientado a la administración del flujo de trabajo de una talabartería, desde su sistema de producción hasta el manejo de inventario.

---

## 🛠️ Instalación y ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/tu-proyecto.git
cd tu-proyecto
```

### 2. Crea y activa un entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala los paquetes requeridos

```bash
pip install -r requirements.txt
```

### 4. Crea un archivo `.env` en la raíz del proyecto

La estructura del proyecto es la siguiente:

```
.
├── app/
│   ├── __pycache__/
│   ├── authentication/
│   ├── config/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utilities/
│   └── main.py
├── requirements.txt
├── .env
└── README.md
```

Dentro del archivo `.env`, agrega las siguientes variables:

```
JWT_SECRET=tu_secreto_jwt
DB_NAME=nombre_de_tu_base_de_datos
MONGODB_CONNECTION_STRING=tu_uri_de_conexion_a_mongodb
```

Reemplaza cada valor con los datos reales de tu entorno.

### 5. Corre el servidor FastAPI

Ejecuta el servidor con:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

---
