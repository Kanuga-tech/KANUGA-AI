import os
import subprocess
import sys
from pathlib import Path

def setup_database():
    print("Setting up PostgreSQL database...")
    
    # Database configuration
    db_name = "kanuga_ai"
    db_user = "postgres"  # Default PostgreSQL superuser
    db_password = input("Enter your PostgreSQL password: ")
    
    # Create database
    try:
        # Create database if it doesn't exist
        create_db_cmd = f'psql -U postgres -c "CREATE DATABASE {db_name};"'
        subprocess.run(create_db_cmd, shell=True, env={"PGPASSWORD": db_password})
        print(f"Database '{db_name}' created successfully!")
        
        # Update .env file with local database URL
        env_path = Path(".env")
        if env_path.exists():
            with open(env_path, "r") as f:
                content = f.read()
            
            # Update DATABASE_URL
            new_db_url = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_name}"
            content = content.replace(
                "DATABASE_URL=postgresql://user:password@db:5432/kanuga_ai",
                f"DATABASE_URL={new_db_url}"
            )
            
            with open(env_path, "w") as f:
                f.write(content)
            print("Updated .env file with local database credentials")
            
    except subprocess.CalledProcessError as e:
        print(f"Error setting up database: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_database() 