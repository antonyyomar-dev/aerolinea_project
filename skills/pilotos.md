# Skill: Gestión de Pilotos

## Descripción
Gestiona la información y disponibilidad de todos los pilotos de la aerolínea.

## Funcionalidades

### 1. Registrar Piloto
- Capturar datos del nuevo piloto (nombre, apellido, licencia, especialización, horas de vuelo)
- Validar que la número de licencia sea único
- Almacenar registro en la base de datos

### 2. Mostrar Todos los Pilotos
- Listar todos los pilotos registrados
- Mostrar información en formato tabular
- Mostrar estado de disponibilidad

### 3. Buscar Piloto por ID
- Permitir búsqueda exacta por identificador único
- Mostrar información detallada del piloto encontrado
- Mostrar vuelos asignados

### 4. Buscar Piloto por Nombre
- Realizar búsqueda parcial o completa por nombre
- Mostrar lista de coincidencias
- Mostrar información detallada de cada resultado

### 5. Actualizar Datos del Piloto
- Permitir modificación de datos (licencia, especialización, horas de vuelo)
- Validar que el número de licencia siga siendo único si se modifica
- Mostrar confirmación de cambios realizados

### 6. Eliminar Piloto
- Permitir eliminación de registro de piloto
- Solicitar confirmación antes de eliminar
- Validar que el piloto no tenga vuelos en proceso o próximos

## Estructura de Datos
```
Piloto:
  - id: int (único, autogenerado)
  - nombre: str
  - apellido: str
  - numero_licencia: str (único)
  - especializacion: str (tipo de avión que puede pilotar)
  - horas_vuelo: int
  - estado: str (disponible, en_vuelo, en_descanso)
  - activo: bool
```

## Validaciones Necesarias
- Campos no vacíos
- Número de licencia único
- Horas de vuelo válidas (número positivo)
- Estado válido en el sistema

## Integración
- Se integra con el módulo de vuelos para asignar pilotos
- Debe validar la especialización del piloto con el tipo de avión del vuelo
