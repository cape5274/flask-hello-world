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

@app.route("/db_create")
def creating():
    conn = psycopg2.connect("postgresql://lab10_database_u7eo_user:JYUDlSCAXdtr5RFEbJ9XpF3dmIIvBmEI@dpg-d7atjjk50q8c73as43g0-a/lab10_database_u7eo")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball (
    First varchar(255),
    Last varchar(255),
    City varchar(255),
    Name varchar(255),
    Number int
    );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route("/db_insert")
def inserting():
    conn = psycopg2.connect("postgresql://lab10_database_u7eo_user:JYUDlSCAXdtr5RFEbJ9XpF3dmIIvBmEI@dpg-d7atjjk50q8c73as43g0-a/lab10_database_u7eo")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values 
    ('Jayson','Tatum','Boston', 'Celtics',0),
    ('Stephen','Curry','San Francisco','Warriors',30),
    ('Nikola', 'Jokic','Denver','Nuggets',15),
    ('Kawhi','Leonard','Los Angeles','Clippers',2);
    
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://lab10_database_u7eo_user:JYUDlSCAXdtr5RFEbJ9XpF3dmIIvBmEI@dpg-d7atjjk50q8c73as43g0-a/lab10_database_u7eo")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string = "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://lab10_database_u7eo_user:JYUDlSCAXdtr5RFEbJ9XpF3dmIIvBmEI@dpg-d7atjjk50q8c73as43g0-a/lab10_database_u7eo")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
