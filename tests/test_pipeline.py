import os
import sqlite3
import pytest
from src.pipeline import run_pipeline

DB_PATH = "sales.db"

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # 1. Borrar DB anterior si existe
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    # 2. Ejecutar el Pipeline del candidato
    run_pipeline()
    
    yield
    
    # 3. Limpieza (Opcional, dejar comentado para depurar)
    # if os.path.exists(DB_PATH):
    #     os.remove(DB_PATH)

def test_database_creation():
    """Valida que el archivo sales.db se haya creado"""
    assert os.path.exists(DB_PATH), "❌ El archivo sales.db no se ha generado."

def test_data_integrity():
    """Valida que la tabla exista y tenga columnas correctas"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT country, total_revenue FROM revenue_by_country")
        rows = cursor.fetchall()
        assert len(rows) > 0, "❌ La tabla está vacía."
    except sqlite3.OperationalError:
        pytest.fail("❌ La tabla 'revenue_by_country' no existe.")
    finally:
        conn.close()

def test_usa_revenue_calculation():
    """Valida la lógica de limpieza para USA"""
    # USA Logic:
    # $100.50 (Valido)
    # $200.00 (Valido)
    # 50.00 (Valido - ID nulo se borra? Depende regla. Asumimos borrado row 5)
    # $150.00 (Valido)
    # Total esperado (aprox): 450.50
    
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM revenue_by_country WHERE country='USA'", conn)
    conn.close()
    
    assert not df.empty, "No se encontraron datos para USA"
    revenue = df.iloc[0]['total_revenue']
    assert revenue == 450.50, f"❌ Revenue incorrecto para USA. Esperado: 450.50, Obtenido: {revenue}"
