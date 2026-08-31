import time
import pytest
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_compra, cupom, desconto_esperado",
    [
        (0.0, "BASICO", 0, -1.0),
        (-10.0, "BASICO", 0, -1.0),
        (10.0, "BASICO", -1, -1.0),

        (10.0, "INVALIDO", 0, -2.0),
        (10.0, "", 0, -2.0),
        (10.0, "ISACMGB", 0, -2.0),

        (10.0, "BASICO", 0, 10.0),
        (10.0, "PREMIUM", 0, 9.0),
        (10.0, "EMPRESARIAL", 0, 8.0),

        (100.0, "BASICO", 1, 105.50),
        (100.0, "BASICO", 30, 120.00),
        (100.0, "BASICO", 31, 156.00),
        (100.0, "BASICO", 40, 165.00),


    ],
)






