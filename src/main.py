import subprocess


def run():
    subprocess.run(["streamlit", "run", ".\src\gui.py"], shell=True, check=True)
    
    
if __name__ == "__main__":
    run()