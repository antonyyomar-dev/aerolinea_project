# Skill: Gestión de Vuelos

## Descripción
Gestiona la creación, asignación y seguimiento de todos los vuelos de la aerolínea.

## Funcionalidades

### 1. Registrar Vuelo
- Capturar datos del nuevo vuelo (número de vuelo, origen, destino, fecha, hora, tipo de avión)
- Validar que los aeropuertos existan
- Validar que las fechas sean válidas (futuras)
- Asignar capacidad de pasajeros según tipo de avión

### 2. Mostrar Todos los Vuelos
- Listar todos los vuelos registrados
- Mostrar información en formato tabular
- Filtrar por estado (próximo, en vuelo, completado, cancelado)

### 3. Asignar Piloto a Vuelo
- Validar disponibilidad del piloto
- Validar especialización del piloto con tipo de avión
- Asignar piloto y actualizar estado

### 4. Asignar Pasajeros a Vuelo
- Validar disponibilidad de asientos
- Registrar pasajero en el vuelo
- Generar confirmación de reserva

### 5. Ver Detalles del Vuelo
- Mostrar información completa del vuelo
- Listar pilotos asignados
- Listar pasajeros registrados
- Mostrar ocupación actual

### 6. Cancelar Vuelo
- Solicitar confirmación
- Notificar a pasajeros y pilotos
- Marcar vuelo como cancelado

## Estructura de Datos
```
Vuelo:
  - id: int (único, autogenerado)
  - numero_vuelo: str (único)
  - aeropuerto_origen: int (referencia a Aeropuerto)
  - aeropuerto_destino: int (referencia a Aeropuerto)
  - fecha_salida: datetime
  - fecha_llegada: datetime
  - tipo_avion: str
  - capacidad: int
  - pasajeros: list[int] (referencias a Pasajero)
  - pilotos: list[int] (referencias a Piloto)
  - estado: str (programa, en_vuelo, completado, cancelado)
```

## Validaciones Necesarias
- Origen diferente a destino
- Fecha válida (futura)
- Hora de llegada posterior a hora de salida
- Tipo de avión válido
- Capacidad positiva

## Integración
- Se integra con pasajeros para asignar viajeros
- Se integra con pilotos para asignar tripulación
- Se integra con aeropuertos para validar rutas
