# Skill: Gestión de Aeropuertos

## Descripción
Gestiona la información de todos los aeropuertos disponibles en la red de la aerolínea.

## Funcionalidades

### 1. Registrar Aeropuerto
- Capturar datos del nuevo aeropuerto (código IATA, nombre, ciudad, país)
- Validar que el código IATA sea único
- Almacenar registro en la base de datos

### 2. Mostrar Todos los Aeropuertos
- Listar todos los aeropuertos registrados
- Mostrar información en formato tabular
- Incluir opciones de búsqueda y filtrado

### 3. Buscar Aeropuerto por ID
- Permitir búsqueda exacta por identificador único
- Mostrar información detallada del aeropuerto encontrado
- Mostrar mensaje si no existe

### 4. Buscar Aeropuerto por País
- Realizar búsqueda de todos los aeropuertos de un país específico
- Mostrar lista de coincidencias
- Mostrar información detallada de cada resultado

### 5. Actualizar Datos de Aeropuerto
- Permitir modificación de datos existentes (excepto código IATA)
- Validar nuevos datos antes de actualizar
- Mostrar confirmación de cambios realizados

### 6. Eliminar Aeropuerto
- Permitir eliminación de registro de aeropuerto
- Solicitar confirmación antes de eliminar
- Validar que el aeropuerto no tenga vuelos activos que salgan o lleguen

## Estructura de Datos
```
Aeropuerto:
  - id: int (único, autogenerado)
  - codigo_iata: str (único, 3 caracteres)
  - nombre: str
  - ciudad: str
  - país: str
  - activo: bool
```

## Validaciones Necesarias
- Campos no vacíos
- Código IATA único y formato válido (3 letras mayúsculas)
- País válido

## Integración
- Se integra con el módulo de vuelos para validar rutas
- Los aeropuertos son destino y origen de todos los vuelos
