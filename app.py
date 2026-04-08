from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from YOUR NAME in 3308'
    
@app.route("/db_test")
def db_test():
    conn = psycopg2.connect("postgresql://lab10_database_u7eo_user:JYUDlSCAXdtr5RFEbJ9XpF3dmIIvBmEI@dpg-d7atjjk50q8c73as43g0-a/lab10_database_u7eo")
    conn.close
    
    return "Database connection works!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
