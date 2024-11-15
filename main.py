from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

led_status = 'estado inicial'

# Petición POST para cambiar el estado del LED
@app.post('/led')
async def estado_LED(request: Request):
    estado = await request.body()  # Leer el cuerpo de la solicitud
    estado = estado.decode('utf-8')  # Decodificar el cuerpo a string
    if estado in ['ON', 'OFF']:
        global led_status
        led_status = estado
        return f'El estado del LED es {led_status}'
    else:
        return 'El valor no es válido'

# Petición GET para obtener el estado del LED
@app.get('/led')
def obtener_estado_LED():
    return led_status

@app.get('/')
def obtener_estado_LED():
    return 'funciona correctamente!!'