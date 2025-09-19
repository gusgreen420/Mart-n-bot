from dataclasses import dataclass

@dataclass
class MartingaleConfig:
    mult: float = 2.0
    take_profit_pct: float = 1.0  # 1%


class MartingaleStrategy:
    def __init__(self, cfg: MartingaleConfig):
        self.cfg = cfg

    def next_qty(self, last_qty: float) -> float:
        # Sube la cantidad por el multiplicador
        return round(last_qty * self.cfg.mult, 8)

    def target_price(self, entry_price: float) -> float:
        # Precio de salida con take profit porcentual
        return round(entry_price * (1 + self.cfg.take_profit_pct / 100.0), 8)
