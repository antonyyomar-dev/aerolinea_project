# Requirements - Sistema de Gestión de Aerolínea

## Descripción
Este directorio contiene las especificaciones de dependencias del proyecto.

## Instalación de Dependencias

### Instalación Completa
```bash
pip install -r requirements.txt
```

### Instalación con Herramientas Opcionales (Análisis e IA)
```bash
pip install -r requirements-dev.txt
```

## Descripción de Dependencias

### Dependencias Principales

#### Manejo de Datos
- **pandas** (2.0.3) - Análisis y manipulación de datos
  - Lectura/escritura de datos
  - Análisis de información
  - Creación de DataFrames
  
- **numpy** (1.24.3) - Computación numérica
  - Arrays multidimensionales
  - Operaciones matemáticas

#### Exportación de Reportes
- **openpyxl** (3.1.2) - Lectura/escritura de Excel
  - Exportar datos a hojas de cálculo
  - Generación de reportes en Excel
  
#### Interfaz de Usuario
- **tabulate** (0.9.0) - Formateo de tablas
  - Mostrar datos tabulares en consola
  - Mejorar presentación de información

### Dependencias Opcionales (requirements-dev.txt)

#### Machine Learning (Análisis avanzado)
- **scikit-learn** (1.3.0) - Machine Learning
  - Predicciones y análisis avanzado
  - Algoritmos de clustering y clasificación

#### Visualización
- **matplotlib** (3.7.2) - Visualización de datos
  - Gráficos y diagramas
  - Análisis visual de información

## Verificación

Para verificar que todas las dependencias se instalaron correctamente:

```bash
pip list
```

## Actualización de Dependencias

```bash
pip install --upgrade -r requirements.txt
```

## Desinstalación

```bash
pip uninstall -y -r requirements.txt
```

## Notas Importantes

- Las versiones especificadas son compatibles y han sido testeadas
- Las dependencias opcionales (requirements-dev.txt) están disponibles para análisis avanzado e IA

- Se recomienda usar un entorno virtual (`venv`) para aislar las dependencias
- Las versiones especificadas son compatibles y han sido testeadas
- Las dependencias opcionales (requirements-dev.txt) están disponibles para análisis avanzado e IA
