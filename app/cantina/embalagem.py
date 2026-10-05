def calcular_taxa_embalagem(levar_viagem: bool, quantidade_item: int) -> float:
    """Calcula a taxa de embalagem caso o cliente deseje çlevar o pedido."""
    if not levar_viagem or quantidade_item <= 0:
        return 0.0

    taxa_fixa = 2.00
    adicional_por_item = quantidade_item * 0.50

    return round(taxa_fixa + adicional_por_item, 2)