import psycopg2

# Dados de conexão
conn = psycopg2.connect(
    dbname="gradguru_db",
    user="gradguru_user",
    password="your_password",  # Troque pela sua senha real
    host="localhost",
    port="5432"
)

# Dados a inserir
disciplinas = [
    ("INF1010", "Algoritmos", "Informática", "Engenharia", "Obrigatória"),
    ("INF2020", "Design de Interfaces", "Informática", "Computação", "Eletiva"),
    ("MAT1001", "Cálculo I", "Matemática", "Engenharia", "Obrigatória")
]

# Executar inserts ou updates
disciplinas = [
    ("INF1010", "Algoritmos", "Informática", "Engenharia", "Obrigatória", ""),
    ("INF2020", "Design de Interfaces", "Informática", "Computação", "Eletiva", ""),
    ("MAT1001", "Cálculo I", "Matemática", "Engenharia", "Obrigatória", "")
]

with conn:
    with conn.cursor() as cur:
        for cod, nome, depto, grad, tipo, materiais in disciplinas:
            cur.execute("""
                INSERT INTO disciplinas_disciplina (codigo, nome, departamento, graduacao, tipo, materiais)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (codigo) DO UPDATE
                SET nome = EXCLUDED.nome,
                    departamento = EXCLUDED.departamento,
                    graduacao = EXCLUDED.graduacao,
                    tipo = EXCLUDED.tipo,
                    materiais = EXCLUDED.materiais;
            """, (cod, nome, depto, grad, tipo, materiais))


print("✅ Disciplinas inseridas ou atualizadas com sucesso!")
conn.close()
