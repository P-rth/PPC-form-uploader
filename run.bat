if exist firstrun.fr (
    pip install -r requirements.txt
    timeout /t 1 
    del firstrun.fr
    cls
    python PPC2023.py
) else (
    cls
    python PPC2023.py
)
