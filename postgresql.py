import psycopg2

# Detalhes da conexão
conn_params = {
    'dbname': 'python-teste',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}

# SQL para criar a tabela
create_table_query = """
CREATE TABLE patients (
    uuid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(50),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP
);
"""

# SQL para verificar a existência da tabela
check_table_query = """
SELECT EXISTS (
    SELECT 1
    FROM information_schema.tables 
    WHERE table_schema = 'public' 
    AND table_name = 'patients'
);
"""

insert_query = """
INSERT INTO patients (
    first_name,
    last_name,
    date_of_birth,
    gender,
    email,
    phone_number,
    address,
    city,
    state,
    zip_code,
    country,
    emergency_contact_name,
    emergency_contact_phone
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);
"""

data_to_insert = (
    'John',
    'Doe',
    '1980-01-01',
    'Male',
    'john.doe@example.com',
    '123-456-7890',
    '123 Main St',
    'Anytown',
    'Anystate',
    '12345',
    'USA',
    'Jane Doe',
    '098-765-4321'
)

select_patient = """
SELECT * FROM patients;
"""


try:
    # Conectar ao PostgreSQL
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    
    # Verificar se a tabela já existe
    cursor.execute(check_table_query)
    table_exists = cursor.fetchone()[0]
    
    if not table_exists:
        # Executar a consulta de criação da tabela
        cursor.execute(create_table_query)
        conn.commit()
        print("Tabela 'patients' criada com sucesso!")

    
    # cursor.execute(insert_query, data_to_insert)
    # Confirmar as alterações no banco de dados
    # conn.commit()

    # Executar a consulta de seleção
    cursor.execute(select_patient)
    
    # Recuperar todos os resultados
    rows = cursor.fetchall()
    
    # Exibir os resultados
    for row in rows:
        print(row)
    
    # Confirmar as alterações no banco de dados
    conn.commit()
  
except psycopg2.Error as e:
    print("Error:", e)
    
finally:
    # Fechar o cursor e a conexão
    if cursor:
        cursor.close()
    if conn:
        conn.close()
