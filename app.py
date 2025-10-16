# app.py
from datetime import datetime

def main():
    print(f"Hello World! The time is {datetime.utcnow().isoformat()}Z")

if __name__ == "__main__":
    main()
