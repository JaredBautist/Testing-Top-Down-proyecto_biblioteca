# 📚 Sistema de Biblioteca - Pruebas Top Down

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/Tests-14%20passing-brightgreen.svg)](tests)
[![Testing](https://img.shields.io/badge/Testing-Top%20Down-orange.svg)](methodology)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Un proyecto educativo que demuestra la implementación de **pruebas Top Down** en un sistema de gestión de biblioteca usando Python y stubs.

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Metodología de Pruebas](#-metodología-de-pruebas)
- [Análisis de Ventajas](#-análisis-de-ventajas)
- [Ejecutar Tests](#-ejecutar-tests)
- [Contribuir](#-contribuir)

## 🎯 Descripción

Este proyecto implementa un sistema básico de biblioteca con el enfoque de **pruebas Top Down**, utilizando stubs para simular dependencias externas como base de datos y autenticación. El objetivo es demostrar las ventajas de esta metodología de testing.

### Características Principales

- ✅ Sistema de préstamos de libros
- ✅ Validación de usuarios
- ✅ Verificación de disponibilidad
- ✅ 14 tests comprehensivos
- ✅ Stubs para dependencias externas
- ✅ Ejecución rápida de tests (< 0.1s)

## 📁 Estructura del Proyecto

```
proyecto_biblioteca/
├── biblioteca_sistema.py    # 🏛️ Sistema principal
├── test_top_down.py         # 🧪 Pruebas Top Down (14 tests)
├── stubs/                   # 🎭 Carpeta de stubs
│   ├── __init__.py
│   ├── database_stub.py     # 💾 Stub de Base de Datos
│   └── auth_stub.py         # 🔐 Stub de Autenticación
└── README.md               # 📖 Este archivo
```

## 🚀 Instalación

### Prerrequisitos

- Python 3.11+
- pytest

### Pasos de Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/proyecto-biblioteca.git
cd proyecto-biblioteca

# Instalar dependencias
pip install pytest

# Verificar instalación
python -m pytest --version
```

## 🎮 Uso

### Ejecutar el Sistema Principal

```bash
cd proyecto_biblioteca
python biblioteca_sistema.py
```

### Ejemplo de Uso del Sistema

```python
from biblioteca_sistema import BibliotecaSistema
from stubs.database_stub import DatabaseStub
from stubs.auth_stub import AuthStub

# Crear instancias de stubs
db_stub = DatabaseStub()
auth_stub = AuthStub()

# Inicializar sistema
sistema = BibliotecaSistema(db_stub, auth_stub)

# Prestar un libro
resultado = sistema.prestar_libro(usuario_id=1, libro_id=2)
print(resultado)  # "Préstamo exitoso"
```

## 🧪 Metodología de Pruebas

Este proyecto utiliza el enfoque **Top Down** para las pruebas:

### Principios Aplicados

1. **Pruebas desde arriba hacia abajo**: Comenzamos probando el flujo principal
2. **Uso de stubs**: Simulamos dependencias externas
3. **Inyección de dependencias**: Facilitamos el testing
4. **Aislamiento de componentes**: Cada test es independiente

### Lógica de los Stubs

```python
# AuthStub: Usuarios con ID > 0 están autorizados
def verificar_usuario(self, usuario_id):
    return usuario_id > 0

# DatabaseStub: Libros con ID par están disponibles
def libro_disponible(self, libro_id):
    return libro_id % 2 == 0
```

## 🏆 Análisis de Ventajas

### 🎯 1. Validación Temprana del Flujo Principal
- ✅ Probamos `prestar_libro()` sin esperar implementaciones reales
- ✅ Detección inmediata de errores de lógica
- ✅ 14 tests validan el flujo completo end-to-end

### 🔧 2. Desarrollo Independiente de Componentes
- ✅ El sistema funciona sin BD real ni autenticación real
- ✅ Equipos pueden trabajar en paralelo
- ✅ Stubs permiten desarrollo simultáneo

### 📊 3. Control Total de Escenarios de Prueba
- ✅ Simulamos exactamente los casos que queremos probar
- ✅ Casos edge sin depender de datos reales
- ✅ Cobertura del 100% de flujos posibles

### ⚡ 4. Ejecución Rápida y Confiable
```bash
================================ test session starts ================================
14 passed in 0.10s  # ⚡ Super rápido!
```
- ✅ Sin dependencias de red o servicios externos
- ✅ Tests repetibles y determinísticos
- ✅ Feedback inmediato durante desarrollo

### 🎨 5. Diseño por Contrato Claro
- ✅ Interfaces bien definidas antes de implementación
- ✅ Contratos claros entre componentes
- ✅ Documentación viva del comportamiento esperado

### 🐛 6. Aislamiento de Errores
- ✅ Si un test falla, sabemos que es lógica del sistema
- ✅ Debugging directo y fácil
- ✅ Sin efectos secundarios entre tests

### 📈 7. Cobertura Completa de Escenarios

| Tipo de Test | Cantidad | Cobertura |
|-------------|----------|-----------|
| 🎯 Préstamos exitosos | 5 tests | Casos positivos |
| 🚫 Usuarios no autorizados | 4 tests | Validación de acceso |
| 📖 Libros no disponibles | 3 tests | Disponibilidad |
| 🔍 Casos límite | 2 tests | Edge cases |
| **TOTAL** | **14 tests** | **100%** |

## 🧪 Documentación Detallada de Tests

### 🎯 Tests de Préstamos Exitosos (5 tests)

| # | Test | Descripción | Usuario | Libro | Resultado |
|---|------|-------------|---------|-------|-----------|
| 1 | `test_prestamo_exitoso` | Flujo exitoso básico usando stubs | `id=1` | `id=2` (par) | ✅ "Préstamo exitoso" |
| 2 | `test_prestamo_con_libro_par` | Préstamo con diferentes valores pares | `id=10` | `id=8` (par) | ✅ "Préstamo exitoso" |
| 3 | `test_prestamo_numeros_grandes` | Validación con números grandes | `id=1000` | `id=1002` (par) | ✅ "Préstamo exitoso" |
| 4 | `test_libro_cero` | Caso especial con libro ID=0 | `id=3` | `id=0` (par) | ✅ "Préstamo exitoso" |
| 5 | `test_prestamo_exitoso_alternativo` | Préstamo alternativo con otros valores | `id=99` | `id=100` (par) | ✅ "Préstamo exitoso" |

### 🚫 Tests de Usuarios No Autorizados (4 tests)

| # | Test | Descripción | Usuario | Libro | Resultado |
|---|------|-------------|---------|-------|-----------|
| 6 | `test_usuario_no_autorizado` | Rechazo por usuario no autorizado | `id=0` | `id=2` | ❌ "Usuario no autorizado" |
| 7 | `test_usuario_negativo` | Usuario con ID negativo | `id=-1` | `id=4` | ❌ "Usuario no autorizado" |
| 8 | `test_usuario_limite_cero` | Caso límite con usuario ID=0 | `id=0` | `id=6` | ❌ "Usuario no autorizado" |
| 9 | `test_multiple_scenarios_fallo` | Usuario no autorizado + libro no disponible | `id=-5` | `id=7` (impar) | ❌ "Usuario no autorizado" |

### 📖 Tests de Libros No Disponibles (3 tests)

| # | Test | Descripción | Usuario | Libro | Resultado |
|---|------|-------------|---------|-------|-----------|
| 10 | `test_libro_no_disponible` | Rechazo por libro no disponible | `id=1` | `id=3` (impar) | ❌ "Libro no disponible" |
| 11 | `test_libro_id_uno` | Caso específico con libro ID=1 | `id=5` | `id=1` (impar) | ❌ "Libro no disponible" |
| 12 | `test_prestamo_con_libro_impar` | Préstamo fallido con libro impar | `id=7` | `id=9` (impar) | ❌ "Libro no disponible" |

### 🔍 Tests de Casos Límite y Lógica (2 tests)

| # | Test | Descripción | Usuario | Libro | Propósito |
|---|------|-------------|---------|-------|-----------|
| 13 | `test_prestamo_usuario_uno` | Usuario ID=1 (mínimo autorizado) | `id=1` | `id=10` (par) | ✅ Validar límite mínimo |
| 14 | `test_validacion_orden_verificaciones` | Orden de validaciones del sistema | `id=0` | `id=5` (impar) | ❌ Auth antes que disponibilidad |

### 🔍 Lógica de los Stubs

```python
# 🔐 AuthStub - Lógica de Autorización
def verificar_usuario(self, usuario_id):
    return usuario_id > 0  # Solo usuarios con ID positivo

# 💾 DatabaseStub - Lógica de Disponibilidad  
def libro_disponible(self, libro_id):
    return libro_id % 2 == 0  # Solo libros con ID par están disponibles
```

### 📊 Resumen de Cobertura por Escenarios

```
✅ Casos Exitosos:     5/14 tests (35.7%)
❌ Usuario No Auth:    4/14 tests (28.6%) 
❌ Libro No Dispon:    3/14 tests (21.4%)
🔍 Casos Límite:       2/14 tests (14.3%)
──────────────────────────────────────
📈 Cobertura Total:   14/14 tests (100%)
```

### 🔄 8. Facilidad de Mantenimiento
- ✅ Cambios en stubs son triviales
- ✅ Adaptación rápida a nuevos requerimientos
- ✅ Refactoring seguro con tests como red de seguridad

### 📝 9. Documentación Viva del Sistema
- ✅ Tests sirven como especificación ejecutable
- ✅ Onboarding rápido para nuevos desarrolladores
- ✅ Comportamiento esperado claramente definido

### 🎯 10. Retroalimentación Inmediata
- ✅ Ciclo de feedback muy corto
- ✅ Detección inmediata de regresiones
- ✅ Desarrollo más confiado y ágil

## 📊 Comparativa: Antes vs Con Top Down

| Aspecto | Sin Top Down | Con Top Down | Mejora |
|---------|-------------|--------------|--------|
| ⏱️ **Tiempo de tests** | N/A | 0.10s | ⚡ Ultra rápido |
| 🔗 **Dependencias** | BD + Auth real | Stubs simples | 🎯 Sin complejidad |
| 📋 **Cobertura** | Limitada | 14 escenarios | 📈 Cobertura total |
| 🐛 **Debugging** | Complejo | Directo | 🔍 Aislado |
| 👥 **Desarrollo** | Secuencial | Paralelo | 🚀 Más ágil |

## 🧪 Ejecutar Tests

### Todos los Tests
```bash
cd proyecto_biblioteca
python -m pytest test_top_down.py -v
```

### Tests con Detalle
```bash
python -m pytest test_top_down.py -v --tb=short
```

### Test Específico
```bash
python -m pytest test_top_down.py::test_prestamo_exitoso -v
```

### Con Cobertura
```bash
python -m pytest test_top_down.py --cov=biblioteca_sistema
```

