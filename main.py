import os
from dotenv import load_dotenv
from bot.strategy import MartingaleStrategy, MartingaleConfig


def main():
    load_dotenv("/etc/mart-n-bot.env")  # lee tus variables si existen
    mult = float(os.getenv("MULT", "2"))
    tp = float(os.getenv("TAKE_PROFIT_PCT", "1"))
    cfg = MartingaleConfig(mult=mult, take_profit_pct=tp)
    strat = MartingaleStrategy(cfg)

    # demo rápida para que compile y pase CI
    last_qty = 0.001
    entry = 100.0
    print("next_qty:", strat.next_qty(last_qty))
    print("target_price:", strat.target_price(entry))


if __name__ == "__main__":
    main()
