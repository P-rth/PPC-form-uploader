if exist .firstrun (
    pip install -r requirements.txt
    timeout /t 1 
    cls
    python PPC2023.py
) else (
    cls
    python PPC2023.py
)
