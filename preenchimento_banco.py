import psycopg2

# Dados de conexão
conn = psycopg2.connect(
    dbname="gradguru_db",
    user="gradguru_user",
    password="your_password",  # Troque pela sua senha real
    host="localhost",
    port="5432"
)

# Dados a inserir (com breve descrição + créditos)
disciplinas = [
    ("INF1010", "Algoritmos", "Informática", "Engenharia", "Obrigatória", "", "Introdução à lógica de programação e estruturas de controle.", 4),
    ("INF2020", "Design de Interfaces", "Informática", "Computação", "Eletiva", "", "Estudo de usabilidade, acessibilidade e design visual.", 3),
    ("MAT1001", "Cálculo I", "Matemática", "Engenharia", "Obrigatória", "", "Conceitos fundamentais de derivadas e integrais.", 5)
]

# Executar inserts ou updates
with conn:
    with conn.cursor() as cur:
        for cod, nome, depto, grad, tipo, materiais, breve_desc, creditos in disciplinas:
            cur.execute("""
                INSERT INTO disciplinas_disciplina (
                    codigo, nome, departamento, graduacao, tipo,
                    materiais, breve_descricao, creditos
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (codigo) DO UPDATE
                SET nome = EXCLUDED.nome,
                    departamento = EXCLUDED.departamento,
                    graduacao = EXCLUDED.graduacao,
                    tipo = EXCLUDED.tipo,
                    materiais = EXCLUDED.materiais,
                    breve_descricao = EXCLUDED.breve_descricao,
                    creditos = EXCLUDED.creditos;
            """, (cod, nome, depto, grad, tipo, materiais, breve_desc, creditos))

print("✅ Disciplinas inseridas ou atualizadas com sucesso!")
conn.close()
