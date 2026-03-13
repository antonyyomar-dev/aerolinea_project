# Skill: Gestión de Pasajeros

## Descripción
Gestiona todas las operaciones relacionadas con los pasajeros de la aerolínea.

## Funcionalidades

### 1. Registrar Pasajero
- Capturar datos del nuevo pasajero (nombre, apellido, documento de identidad, teléfono, email)
- Validar que el documento sea único
- Almacenar registro en la base de datos o estructura de datos

### 2. Mostrar Todos los Pasajeros
- Listar todos los pasajeros registrados
- Mostrar información en formato tabular
- Incluir opciones de búsqueda y filtrado

### 3. Buscar Pasajero por ID
- Permitir búsqueda exacta por identificador único
- Mostrar información detallada del pasajero encontrado
- Mostrar mensaje si no existe

### 4. Buscar Pasajero por Nombre
- Realizar búsqueda parcial o completa por nombre
- Mostrar lista de coincidencias si hay múltiples resultados
- Mostrar información detallada de cada resultado

### 5. Actualizar Datos de Pasajero
- Permitir modifiación de datos existentes (excepto documento de identidad)
- Validar nuevos datos antes de actualizar
- Mostrar confirmación de cambios realizados

### 6. Eliminar Pasajero
- Permitir eliminación de registro de pasajero
- Solicitar confirmación antes de eliminar
- Validar que el pasajero no tenga vuelos activos

## Estructura de Datos
```
Pasajero:
  - id: int (único, autogenerado)
  - nombre: str
  - apellido: str
  - documento: str (único)
  - teléfono: str
  - email: str
  - fecha_registro: datetime
```

## Validaciones Necesarias
- Campos no vacíos
- Documento único en el sistema
- Email con formato válido
- Teléfono con formato válido

## Integración
- Se integra con el módulo de vuelos para validar asignaciones de pasajeros
