import pytest
from biblioteca_sistema import BibliotecaSistema
from stubs.database_stub import DatabaseStub
from stubs.auth_stub import AuthStub

def test_prestamo_exitoso():
    """Prueba el flujo exitoso usando stubs"""
    # ARRANGE: Configurar stubs
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    # ACT: Ejecutar operación
    resultado = sistema.prestar_libro(usuario_id=1, libro_id=2)

    # ASSERT: Verificar resultado
    assert resultado == "Préstamo exitoso"

def test_usuario_no_autorizado():
    """Prueba rechazo por usuario no autorizado"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=0, libro_id=2)
    assert resultado == "Usuario no autorizado"

def test_libro_no_disponible():
    """Prueba rechazo por libro no disponible"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=1, libro_id=3)  # ID impar = no disponible
    assert resultado == "Libro no disponible"

def test_usuario_negativo():
    """Prueba con usuario ID negativo"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=-1, libro_id=4)
    assert resultado == "Usuario no autorizado"

def test_libro_id_uno():
    """Prueba con libro ID=1 (impar, no disponible)"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=5, libro_id=1)
    assert resultado == "Libro no disponible"

def test_prestamo_con_libro_par():
    """Prueba préstamo exitoso con diferentes libros pares"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=10, libro_id=8)
    assert resultado == "Préstamo exitoso"

def test_prestamo_con_libro_impar():
    """Prueba préstamo fallido con libro impar"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=7, libro_id=9)
    assert resultado == "Libro no disponible"

def test_usuario_limite_cero():
    """Prueba caso límite con usuario ID=0"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=0, libro_id=6)
    assert resultado == "Usuario no autorizado"

def test_prestamo_numeros_grandes():
    """Prueba con números grandes"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=1000, libro_id=1002)
    assert resultado == "Préstamo exitoso"

def test_libro_cero():
    """Prueba con libro ID=0 (par, disponible)"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=3, libro_id=0)
    assert resultado == "Préstamo exitoso"

def test_multiple_scenarios_fallo():
    """Prueba múltiples escenarios de fallo"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    # Usuario no autorizado tiene prioridad sobre libro no disponible
    resultado = sistema.prestar_libro(usuario_id=-5, libro_id=7)
    assert resultado == "Usuario no autorizado"

def test_prestamo_usuario_uno():
    """Prueba con usuario ID=1 (mínimo autorizado)"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=1, libro_id=10)
    assert resultado == "Préstamo exitoso"

def test_validacion_orden_verificaciones():
    """Prueba que la autenticación se verifica antes que disponibilidad"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    # Con usuario no autorizado, debe fallar en auth sin importar el libro
    resultado = sistema.prestar_libro(usuario_id=0, libro_id=5)  # libro impar
    assert resultado == "Usuario no autorizado"

def test_prestamo_exitoso_alternativo():
    """Prueba adicional de préstamo exitoso con otros valores"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=99, libro_id=100)
    assert resultado == "Préstamo exitoso"