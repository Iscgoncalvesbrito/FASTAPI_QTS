
import pytest
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, valor_esperado",
    [
        (0.0, "BASICO", 0, -1.0),
        (-10.0, "BASICO", 0, -1.0),
        (10.0, "BASICO", -1, -1.0),

        (10.0, "INVALIDO", 0, -2.0),
        (10.0, "        ", 0, -2.0),
        (10.0, "", 0, -2.0),

        (10.0, "BASICO", 0, 10.0),
        (10.0, "PREMIUM", 0, 9.0),
        (10.0, "EMPRESARIAL", 0, 8.0),
        (10.0, "basico", 0, 10.0),
        (10.0, " basico ", 0, 10.0),

        (100.0, "BASICO", 1, 105.50),
        (100.0, "BASICO", 30, 120.00),
        (100.0, "BASICO", 31, 156.00)
    ],
)

def test_cobranca_classificar_caixa_preta(
    valor_base, plano, dias_atraso, valor_esperado
):
    assert processar_cobranca(valor_base, plano, dias_atraso) == valor_esperado


import time

def test_tempo_execucao_cobranca_nao_funcional():
    inicio = time.perf_counter()
    resultado = processar_cobranca(500.0, "BASICO", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado > 0.0
    assert tempo_decorrido < 0.1