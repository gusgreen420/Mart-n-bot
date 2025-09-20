#!/bin/bash
echo "✅ Corriendo pruebas de imports..."

if [ -f "./martn_bot/main.py" ]; then
  python3 -m py_compile ./martn_bot/main.py || exit 1
else
  echo "❌ No encontré ./martn_bot/main.py"
  exit 1
fi

python3 -m pytest -q || exit 1
echo "🎉 Todo pasó correctamente."
