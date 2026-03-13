# Skills del Proyecto - Sistema de Gestión de Aerolínea

Documentación completa de todas las funcionalidades y módulos del sistema.

## 📋 Índice de Skills

### 1. [Gestión de Pasajeros](pasajeros.md)
Operaciones CRUD para pasajeros: registro, búsqueda, actualización y eliminación. Valida unicidad de documentos e integración con vuelos.

**Funcionalidades principales:**
- Registrar nuevo pasajero
- Buscar por ID y nombre
- Actualizar datos
- Eliminar registros

---

### 2. [Gestión de Aeropuertos](aeropuertos.md)
Administración de aeropuertos disponibles: registro, búsqueda por país, actualización de información.

**Funcionalidades principales:**
- Registrar aeropuerto
- Buscar por código IATA o país
- Actualizar información
- Validar disponibilidad para rutas

---

### 3. [Gestión de Pilotos](pilotos.md)
Manejo de información de pilotos: registro, disponibilidad, especialización y seguimiento de horas de vuelo.

**Funcionalidades principales:**
- Registrar piloto con especialización
- Consultar disponibilidad
- Actualizar datos y registro de horas
- Validar asignación a vuelos

---

### 4. [Gestión de Vuelos](vuelos.md)
Control completo de vuelos: creación, asignación de pilotos y pasajeros, seguimiento de estado.

**Funcionalidades principales:**
- Crear nuevo vuelo
- Asignar pilotos y pasajeros
- Validar capacidad y especialización
- Mostrar detalles del vuelo

---

### 5. [Reportes](reportes.md)
Generación de reportes y estadísticas del sistema: ocupación, ingresos, actividad de personal.

**Funcionalidades principales:**
- Reporte de pasajeros
- Reporte de aeropuertos
- Reporte de pilotos
- Reporte de vuelos
- Exportar en múltiples formatos

---

## 🔗 Relaciones entre Módulos

```
Pasajeros ──┐
            ├──> Vuelos <──┐
Pilotos   ──┤              ├──> Reportes
            └──> Aeropuertos ──┘
```

## 📊 Estructura del Proyecto

```
aerolinea project/
├── main.py                 # Punto de entrada
├── models/
│   ├── menus.py           # Menús de interfaz
│   └── logica.py          # Lógica de negocios
├── data/                  # Almacenamiento de datos
├── services/              # Servicios adicionales
└── SKILLS/                # Documentación (este directorio)
    ├── README.md          # Este archivo
    ├── pasajeros.md
    ├── aeropuertos.md
    ├── pilotos.md
    ├── vuelos.md
    └── reportes.md
```

## 🚀 Próximos Pasos

1. Implementar clases de modelo para cada entidad
2. Crear funciones en `logica.py` basadas en cada skill
3. Ampliar los menús en `menus.py` con todas las opciones
4. Implementar persistencia de datos (base de datos o archivos)
5. Agregar validaciones según especificaciones de cada skill

