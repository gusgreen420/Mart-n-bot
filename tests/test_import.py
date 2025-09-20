import sys
import os

# Aseguramos que Python pueda encontrar main.py
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def test_imports():
    import main  # noqa: F401
    from bot.strategy import MartingaleStrategy, MartingaleConfig  # noqa: F401