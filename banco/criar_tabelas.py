import os
import json
import sqlite3
import openpyxl
from banco.conexao import obter_conexao

# Caminhos dos arquivos de dados relativos à raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(BASE_DIR, 'dados', 'disciplinas.json')
EXCEL_PATH = os.path.join(BASE_DIR, 'dados', 'Horário.xlsx')

# Dicionário para corrigir as divergências de grafia entre a planilha e o JSON
MAPEAMENTO_PLANILHA_JSON = {
    "Algebra Linear": "ÁLGEBRA LINEAR",
    "Labratório de Programação II": "LABORATÓRIO DE PROGRAMAÇÃO II",
    "Estrutura de Dados": "ESTRUTURAS DE DADOS"
}

def criar_esquema(cursor):
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS disciplinas (
          codigo TEXT PRIMARY KEY,
          nome TEXT NOT NULL,
          periodo INTEGER NOT NULL,
          carga_horaria INTEGER NOT NULL,
          peso INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS pre_requisitos (
          disciplina_codigo TEXT NOT NULL REFERENCES disciplinas(codigo),
          requisito_codigo TEXT NOT NULL REFERENCES disciplinas(codigo),
          PRIMARY KEY (disciplina_codigo, requisito_codigo)
        );

        CREATE TABLE IF NOT EXISTS horarios (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          codigo TEXT REFERENCES disciplinas(codigo),
          semestre TEXT NOT NULL,
          curso TEXT NOT NULL,
          periodo_oferta INTEGER,
          dia TEXT NOT NULL,
          inicio TEXT NOT NULL,
          fim TEXT NOT NULL,
          professor TEXT,
          sala TEXT
        );

        CREATE TABLE IF NOT EXISTS estudantes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS historico (
          estudante_id INTEGER NOT NULL REFERENCES estudantes(id),
          codigo TEXT NOT NULL REFERENCES disciplinas(codigo),
          situacao TEXT NOT NULL CHECK (situacao IN ('aprovado', 'reprovado')),
          PRIMARY KEY (estudante_id, codigo)
        );

        CREATE TABLE IF NOT EXISTS preferencias (
          estudante_id INTEGER PRIMARY KEY REFERENCES estudantes(id),
          turno TEXT NOT NULL,
          carga_maxima INTEGER NOT NULL,
          priorizar_atraso INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS feedback (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          estudante_id INTEGER NOT NULL REFERENCES estudantes(id),
          codigo TEXT NOT NULL REFERENCES disciplinas(codigo),
          semestre TEXT NOT NULL,
          aceitou INTEGER NOT NULL
        );
    """)

def carregar_json(cursor):
    if not os.path.exists(JSON_PATH):
        print(f"Arquivo não encontrado: {JSON_PATH}")
        return {}

    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        dados_json = json.load(f)

    nome_para_codigo = {}

    lista_disciplinas = dados_json.get('disciplinas', [])

    for disc in lista_disciplinas:
        codigo = disc['codigo']
        nome = disc['nome']
        
        # Guardar no dicionário para o cruzamento com o Excel
        nome_para_codigo[nome.upper()] = codigo
        
        cursor.execute("""
            INSERT OR IGNORE INTO disciplinas (codigo, nome, periodo, carga_horaria, peso)
            VALUES (?, ?, ?, ?, ?)
        """, (codigo, nome, disc.get('periodo', 0), disc['carga_horaria'], disc['peso']))
        
        for req in disc.get('pre_requisitos', []):
            cursor.execute("""
                INSERT OR IGNORE INTO pre_requisitos (disciplina_codigo, requisito_codigo)
                VALUES (?, ?)
            """, (codigo, req))
            
    print(f"JSON processado: {len(lista_disciplinas)} disciplinas carregadas.")
    return nome_para_codigo

def limpar_celula_planilha(texto):
    if not texto or not isinstance(texto, str):
        return None, None, None
    # Lógica simplificada para extrair: "Nome | Professor [Sala]"
    partes = texto.split('|')
    nome_disciplina = partes[0].strip()
    professor = partes[1].split('[')[0].strip() if len(partes) > 1 else None
    sala = texto.split('[')[1].replace(']', '').strip() if '[' in texto else None
    return nome_disciplina, professor, sala

def carregar_planilha(cursor, nome_para_codigo):
    if not os.path.exists(EXCEL_PATH):
        print(f"Planilha não encontrada: {EXCEL_PATH}")
        return

    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    sheet = wb.active

    # Exemplo genérico de captura:
    colunas_dias = {'D': 'Segunda', 'E': 'Terça', 'F': 'Quarta', 'G': 'Quinta', 'H': 'Sexta'}
    
    print("Atenção: A extração da planilha precisa ter as linhas (min_row, max_row) ajustadas no código de acordo com o arquivo final.")
    
    """
    for row in range(5, 50):  # Ajuste os limites reais do seu Excel
        horario_texto = sheet[f'B{row}'].value
        periodo_texto = sheet[f'C{row}'].value
        
        if not horario_texto or "às" not in horario_texto:
            continue
            
        inicio, fim = [x.strip() for x in horario_texto.split('às')]
        periodo_oferta = int(''.join(filter(str.isdigit, str(periodo_texto)))) if periodo_texto else 0

        for col, dia in colunas_dias.items():
            celula = sheet[f'{col}{row}'].value
            if celula:
                nome_bruto, professor, sala = limpar_celula_planilha(celula)
                
                # Trata a string para buscar o código no dicionário gerado pelo JSON
                nome_busca = MAPEAMENTO_PLANILHA_JSON.get(nome_bruto, nome_bruto).upper()
                codigo = nome_para_codigo.get(nome_busca)
                
                if codigo:
                    cursor.execute('''
                        INSERT INTO horarios (codigo, semestre, curso, periodo_oferta, dia, inicio, fim, professor, sala)
                        VALUES (?, '2026.2', 'CC', ?, ?, ?, ?, ?, ?)
                    ''', (codigo, periodo_oferta, dia, inicio, fim, professor, sala))
    """
    print("Planilha de horários processada (lógica comentada aguardando calibração de linhas).")

if __name__ == "__main__":
    conn = obter_conexao()
    cursor = conn.cursor()
    
    try:
        print("Iniciando a criação do banco de dados...")
        criar_esquema(cursor)
        mapa_codigos = carregar_json(cursor)
                
        conn.commit()
        print(" Banco configurado com sucesso e pronto para uso!")
    except Exception as e:
        conn.rollback()
        print(f" Erro ao configurar banco: {e}")
    finally:
        conn.close()