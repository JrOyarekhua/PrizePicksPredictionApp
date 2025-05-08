import psycopg2

def get_connection():
    conn_string = 'postgresql://localhost:5432/nba_comparison'
    try:
        conn = psycopg2.connect(conn_string)
        print('Connected to the database')
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

