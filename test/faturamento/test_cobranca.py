import time
import pytest
from app.faturamento.cobranca import processar_cobranca

def test_basico(valor_base, dias_atraso):
    assert processar_cobranca(valor_base, "BASICO", dias_atraso) == -1.0

def test_premium():
    pass

def test_empresarial():
    pass

def test_atraso_1():
    pass

def test_atraso_30():
    pass





