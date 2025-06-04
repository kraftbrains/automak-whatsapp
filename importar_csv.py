import pandas as pd
import psycopg2
from db_config import DB_CONFIG

def importar_csv_para_postgres(csv_path, db_config):
    df = pd.read_csv(csv_path)
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    # Apaga todos os dados da tabela antes de importar
    cursor.execute('DELETE FROM google_data_scapper')
    # Descobre as colunas reais da tabela
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'google_data_scapper'")
    table_columns = set(row[0] for row in cursor.fetchall())
    # Filtra apenas as colunas do CSV que existem na tabela
    columns = [col for col in df.columns if col in table_columns]
    col_names = ', '.join(f'"{col}"' for col in columns)
    placeholders = ', '.join(['%s'] * len(columns))
    insert_sql = f'INSERT INTO google_data_scapper ({col_names}) VALUES ({placeholders})'
    for _, row in df[columns].iterrows():
        cursor.execute(insert_sql, tuple(row))
    conn.commit()
    cursor.close()
    conn.close()

def normalize_brazilian_number(num):
    import re
    if not num or str(num).strip().lower() == 'nan':
        return None
    digits = re.sub(r'\D', '', str(num))
    if digits.startswith('55'):
        return f'+{digits}'
    if len(digits) in (10, 11):
        return f'+55{digits}'
    return None

def export_usdlk_to_numeros(db_config, numeros_path):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('SELECT "UsdlK" FROM google_data_scapper')
    numeros = [normalize_brazilian_number(row[0]) for row in cursor.fetchall()]
    numeros = [n for n in numeros if n]
    cursor.close()
    conn.close()
    with open(numeros_path, 'w', encoding='utf-8') as f:
        f.write('numeros = [\n')
        for numero in numeros:
            f.write(f'    "{numero}",\n')
        f.write(']\n')

if __name__ == "__main__":
    db_config = DB_CONFIG
    importar_csv_para_postgres('google.csv', db_config)
    export_usdlk_to_numeros(db_config, 'numeros.py')
