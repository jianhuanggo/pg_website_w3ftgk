from flask import Flask, render_template, jsonify
import sqlite3
import init_db
import os
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")

def get_db_connection():
    conn = sqlite3.connect("instance/portfolio.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def read_root():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM socials")
    socials = c.fetchall()
    c.execute("SELECT * FROM projects")
    projects = c.fetchall()
    c.execute("SELECT * FROM skills")
    skills = c.fetchall()
    c.execute("SELECT * FROM profile")
    profile = c.fetchone()
    conn.close()
    
    # Load button names from .env file
    button1_name = os.getenv("BUTTON1_NAME", "Button One")
    button2_name = os.getenv("BUTTON2_NAME", "Button Two")
    
    # Load text content from text.txt file
    text_content = ""
    text_file_path = os.path.join(os.path.dirname(__file__), "text.txt")
    if os.path.exists(text_file_path):
        with open(text_file_path, "r", encoding="utf-8") as f:
            text_content = f.read()
    
    return render_template(
        "index.html",
        socials=socials,
        skills=skills,
        projects=projects,
        profile=profile,
        button1_name=button1_name,
        button2_name=button2_name,
        text_content=text_content
    )

@app.route("/execute_button1", methods=["POST"])
def execute_button1():
    """
    Execute the Python program specified in BUTTON1_PROGRAM environment variable.
    
    Returns:
        JSON response with status and message
    """
    try:
        program_path = os.getenv("BUTTON1_PROGRAM")
        if not program_path:
            return jsonify({
                "status": "error",
                "message": "BUTTON1_PROGRAM not defined in .env file"
            }), 400
        
        # Resolve absolute path if relative
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if not os.path.isabs(program_path):
            program_path = os.path.join(base_dir, program_path)
        
        if not os.path.exists(program_path):
            return jsonify({
                "status": "error",
                "message": f"Program file not found: {program_path}"
            }), 404
        
        # Execute the Python program
        result = subprocess.run(
            ["python", program_path],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout
            cwd=base_dir
        )
        
        if result.returncode == 0:
            return jsonify({
                "status": "success",
                "message": "Program executed successfully",
                "output": result.stdout
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": "Program execution failed",
                "error": result.stderr
            }), 500
            
    except subprocess.TimeoutExpired:
        return jsonify({
            "status": "error",
            "message": "Program execution timed out"
        }), 504
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/execute_button2", methods=["POST"])
def execute_button2():
    """
    Execute the Python program specified in BUTTON2_PROGRAM environment variable.
    
    Returns:
        JSON response with status and message
    """
    try:
        program_path = os.getenv("BUTTON2_PROGRAM")
        if not program_path:
            return jsonify({
                "status": "error",
                "message": "BUTTON2_PROGRAM not defined in .env file"
            }), 400
        
        # Resolve absolute path if relative
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if not os.path.isabs(program_path):
            program_path = os.path.join(base_dir, program_path)
        
        if not os.path.exists(program_path):
            return jsonify({
                "status": "error",
                "message": f"Program file not found: {program_path}"
            }), 404
        
        # Execute the Python program
        result = subprocess.run(
            ["python", program_path],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout
            cwd=base_dir
        )
        
        if result.returncode == 0:
            return jsonify({
                "output": result.stdout
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": "Program execution failed",
                "error": result.stderr
            }), 500
            
    except subprocess.TimeoutExpired:
        return jsonify({
            "status": "error",
            "message": "Program execution timed out"
        }), 504
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

