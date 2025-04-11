def setup_database(container):
    import psycopg2
    from psycopg2 import sql

    # Database connection parameters
    db_name = "mydatabase"
    user = "myuser"
    password = "mypassword"
    host = "localhost"
    port = "5432"

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # Create a sample table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE NOT NULL
    );
    '''
    cursor.execute(create_table_query)

    # Insert initial data
    insert_data_query = '''
    INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com')
    ON CONFLICT (email) DO NOTHING;
    '''
    cursor.execute(insert_data_query)

    # Commit changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()