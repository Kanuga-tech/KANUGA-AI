import os
import subprocess
import sys
import venv
from pathlib import Path

def setup_python_env():
    print("Setting up Python virtual environment...")
    venv_path = Path("venv")
    if not venv_path.exists():
        venv.create(venv_path, with_pip=True)
    
    # Determine the pip path based on the OS
    if sys.platform == "win32":
        pip_path = venv_path / "Scripts" / "pip"
    else:
        pip_path = venv_path / "bin" / "pip"
    
    # Install requirements
    print("Installing Python dependencies...")
    subprocess.run([str(pip_path), "install", "-r", "requirements.txt"])

def setup_frontend():
    print("Setting up frontend dependencies...")
    os.chdir("frontend")
    subprocess.run(["npm", "install"])
    os.chdir("..")

def check_postgres():
    print("Checking PostgreSQL installation...")
    if sys.platform == "win32":
        # Common PostgreSQL installation paths on Windows
        base_paths = [
            r"C:\Program Files\PostgreSQL",
            r"C:\Program Files (x86)\PostgreSQL"
        ]
        
        for base_path in base_paths:
            if os.path.exists(base_path):
                # List all version directories
                try:
                    versions = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
                    for version in versions:
                        bin_path = os.path.join(base_path, version, "bin")
                        if os.path.exists(bin_path):
                            os.environ["PATH"] = bin_path + os.pathsep + os.environ["PATH"]
                            print(f"Found PostgreSQL at {bin_path}")
                            return True
                except Exception as e:
                    print(f"Error checking {base_path}: {e}")
                    continue
        
        print("PostgreSQL is not installed or not found in common locations.")
        print("Please install PostgreSQL from https://www.postgresql.org/download/windows/")
        print("Make sure to add PostgreSQL bin directory to your system PATH")
        sys.exit(1)
    
    # For non-Windows platforms
    try:
        subprocess.run(["psql", "--version"], capture_output=True)
        print("PostgreSQL is installed")
        return True
    except FileNotFoundError:
        print("PostgreSQL is not installed. Please install PostgreSQL from https://www.postgresql.org/download/")
        sys.exit(1)

def setup_env_file():
    print("Setting up environment file...")
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            with open(".env.example", "r") as example_file:
                with open(".env", "w") as env_file:
                    env_file.write(example_file.read())
            print("Created .env file from .env.example")
        else:
            print("Warning: No .env.example file found. Please create a .env file manually.")

def main():
    print("Setting up local development environment...")
    
    # Check for PostgreSQL
    check_postgres()
    
    # Setup Python environment
    setup_python_env()
    
    # Setup frontend
    setup_frontend()
    
    # Setup environment file
    setup_env_file()
    
    print("\nLocal development environment setup complete!")
    print("\nTo start the backend server:")
    if sys.platform == "win32":
        print("    .\\venv\\Scripts\\python -m uvicorn backend.main:app --reload")
    else:
        print("    ./venv/bin/python -m uvicorn backend.main:app --reload")
    
    print("\nTo start the frontend development server:")
    print("    cd frontend")
    print("    npm start")

if __name__ == "__main__":
    main() 