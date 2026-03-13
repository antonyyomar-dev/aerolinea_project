# Skill: Reportes

## Descripción
Genera reportes y estadísticas del sistema de gestión de la aerolínea.

## Funcionalidades

### 1. Reporte de Pasajeros
- Total de pasajeros registrados
- Pasajeros por rango de fechas
- Estadísticas de participación en vuelos
- Pasajeros frecuentes

### 2. Reporte de Aeropuertos
- Lista de aeropuertos activos
- Cantidad de vuelos por aeropuerto
- Aeropuertos más utilizados como origen y destino

### 3. Reporte de Pilotos
- Pilotos disponibles vs asignados
- Horas totales de vuelo por piloto
- Especialización de pilotos

### 4. Reporte de Vuelos
- Vuelos próximos a realizar
- Ocupación de vuelos
- Vuelos completados en período específico
- Vuelos cancelados

### 5. Reporte Financiero
- Ingresos estimados por vuelos
- Ocupación promedio
- Rentabilidad por ruta

### 6. Exportar Reportes
- Exportar en formato CSV
- Exportar en formato PDF (si se implementa)
- Exportar en formato Excel (si se implementa)

## Tipos de Reportes
```
Reporte:
  - titulo: str
  - fecha_generacion: datetime
  - tipo: str (pasajeros, aeropuertos, pilotos, vuelos, financiero)
  - datos: list
  - formato: str (consola, CSV, PDF)
```

## Integración
- Requiere acceso a todos los módulos (pasajeros, aeropuertos, pilotos, vuelos)
- Genera información consolidada del sistema
- Puede servir base para análisis y auditoría
