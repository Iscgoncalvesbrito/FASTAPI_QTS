from app.descontos.descontos import calcular_desconto

def test_desconto_invalida_abaixo_de_zero():
    assert calcular_desconto(-1, False) == 0   ## valor negativo

def test_desconto_invalida_igual_a_zero():
    assert calcular_desconto(0, False) == 0   ## valor igual a 0

def test_desconto_cliente_vip_com_valor_valido():
    assert calcular_desconto(100, True) == 80   ## VIP valor válido

def test_desconto_cliente_nao_vip_com_valor_valido():
    assert calcular_desconto(100, False) == 90  ## NÃO VIP válido

def test_desconto_valor_muito_pequeno():
    resultado = calcular_desconto(0.01, False)
    assert round(resultado, 3) == 0.009     ## Valor muito PEQUENO

def test_desconto_valor_maior():
    assert calcular_desconto(250, True) == 200  ## Valor grande 200
