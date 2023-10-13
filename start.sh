python3 -m venv venv
if [[ "$(uname)" == "Darwin" ]]; then
  # macOS
  source venv/bin/activate
elif [[ "$(expr substr $(uname -s) 1 5)" == "Linux" ]]; then
  # Linux
  source venv/bin/activate
elif [[ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]]; then
  # 32-bit Windows (MINGW32_NT*)
  source venv/Scripts/activate
elif [[ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]]; then
  # 64-bit Windows (MINGW64_NT*)
  source venv/Scripts/activate
fi
pip install -r requirements.txt
uvicorn app.main:app --reload