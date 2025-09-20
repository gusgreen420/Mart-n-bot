import sys
import os

# 👇 Asegura que Python vea la raíz del proyecto
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


def test_imports():
    import main  # noqa: F401
    from bot.strategy import MartingaleStrategy, MartingaleConfig  # noqa: F401