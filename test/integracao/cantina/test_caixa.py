
from app.cantina.caixa import processar_venda

def test_integracao_venda_estudante_combo_para_viagem():
    resultado = processar_venda(
        valor_bruto = 50.0,
        quantidade_itens = 3,
        tipo_clliente = "estudante",
        levar_viagem = True,
    )