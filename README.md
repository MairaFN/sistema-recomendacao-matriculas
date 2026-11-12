# 🎓 Sistema Inteligente de Recomendação de Matrículas

<p align="center">
  <strong>Uma IA a favor do seu planejamento acadêmico!</strong>
</p>

<p align="center">
  Sistema inteligente para auxiliar estudantes na escolha de disciplinas, considerando seu histórico acadêmico, pré-requisitos, disponibilidade de horários e preferências individuais.
</p>

---

## 📌 Sobre o Projeto

O **Sistema Inteligente de Recomendação de Matrículas** tem como objetivo auxiliar estudantes no planejamento de suas matrículas acadêmicas, oferecendo recomendações personalizadas de disciplinas para cada período letivo.

A proposta consiste no desenvolvimento de um agente inteligente capaz de analisar o histórico acadêmico do estudante, identificar disciplinas disponíveis, verificar pré-requisitos e gerar combinações de grades curriculares.

Por meio de uma função de utilidade, o agente avalia as possibilidades e seleciona as combinações que melhor atendem às necessidades e preferências do aluno.

## 🎯 Objetivos

- Automatizar a análise do histórico acadêmico.
- Identificar disciplinas que o estudante está apto a cursar.
- Respeitar os pré-requisitos estabelecidos pela matriz curricular.
- Evitar conflitos de horários.
- Considerar dificuldades e prioridades acadêmicas.
- Recomendar combinações de disciplinas personalizadas.
- Melhorar o planejamento acadêmico e reduzir atrasos na conclusão do curso.

## 🔄 Fluxograma do Projeto

O funcionamento do sistema é dividido em cinco etapas principais:

<p align="center">
  <img src="assets/fluxograma-projeto.png" alt="Fluxograma do Sistema Inteligente de Recomendação de Matrículas" width="100%">
</p>

### Etapas do funcionamento

**1. Entrada de Dados**
- Histórico acadêmico do estudante.
- Disciplinas aprovadas, reprovadas e pendentes.
- Preferências individuais.
- Disponibilidade de horários.

**2. Análise do Histórico**
- Identificação das disciplinas já concluídas.
- Identificação das disciplinas pendentes.
- Análise da progressão acadêmica.

**3. Aplicação das Regras**
- Verificação dos pré-requisitos.
- Filtragem das disciplinas disponíveis.
- Identificação de restrições acadêmicas.

**4. Agente Inteligente**
- Geração de combinações possíveis.
- Verificação de conflitos de horários.
- Aplicação da função de utilidade.
- Seleção da melhor combinação de disciplinas.

**5. Resultado Final**
- Apresentação da grade recomendada.
- Justificativa das disciplinas selecionadas.
- Registro do feedback do estudante.

## 🧠 Inteligência Artificial

O projeto utiliza um agente baseado em objetivos e utilidade para analisar diferentes possibilidades de matrícula.

A função de utilidade permite atribuir pontuações às combinações de disciplinas, considerando critérios como:

- Prioridade das disciplinas.
- Disciplinas atrasadas na matriz curricular.
- Carga horária.
- Dificuldade das disciplinas.
- Preferências do estudante.

A combinação com maior utilidade será considerada a melhor recomendação, desde que respeite todas as restrições obrigatórias.

### Aprendizagem por Feedback

O sistema também prevê um mecanismo de feedback, permitindo registrar as escolhas e avaliações do estudante.

Essas informações poderão ser utilizadas para ajustar os pesos dos critérios e melhorar as recomendações futuras.

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Desenvolvimento da lógica do agente inteligente |
| Streamlit | Construção da interface web |
| SQLite | Armazenamento dos dados acadêmicos |
| n8n | Automação e integração de processos |

### Arquitetura proposta

- **Interface:** interação com o estudante por meio de formulários e telas de recomendação.
- **Processamento:** análise do histórico e aplicação das regras acadêmicas.
- **Agente inteligente:** geração, avaliação e seleção das combinações.
- **Banco de dados:** armazenamento das disciplinas, pré-requisitos, horários e informações acadêmicas.

## 📂 Estrutura do Projeto

```text
sistema-matricula/
│
├── README.md
├── app.py
├── requirements.txt
│
├── agente/
│   ├── historico.py
│   ├── regras.py
│   ├── busca.py
│   └── utilidade.py
│
├── database/
│   ├── banco.py
│   └── disciplinas.db
│
├── dados/
│   └── disciplinas.json
│
└── assets/
    └── fluxograma-projeto.png
```

*Estrutura planejada para organização do desenvolvimento.*

## 🚀 Como Configurar e Executar o Projeto

Siga o passo a passo abaixo para configurar o ambiente de desenvolvimento e executar o script de criação do banco de dados na sua máquina local.

### 1. Clonar o Repositório
Abra o seu terminal e faça o clone do projeto (substitua a URL pela do seu repositório, se necessário):
```bash
git clone https://github.com/seu-usuario/sistema-recomendacao-de-matriculas.git
cd sistema-recomendacao-de-matriculas
```

### 2. Abrir no VS Code
Com o terminal dentro da pasta do projeto, abra o editor:
```bash
code .
```

### 3. Criar e Ativar o Ambiente Virtual
É essencial utilizar um ambiente virtual para isolar as dependências do projeto. No terminal integrado do VS Code:

**Crie o ambiente:**
```bash
python -m venv .venv
```

**Ative o ambiente (Windows - PowerShell):**
```bash
.\.venv\Scripts\Activate
```
*(Você verá um `(.venv)` verde no início da linha de comando indicando que o ambiente está ativo).*

### 4. Instalar as Dependências
Com o ambiente ativado, instale as bibliotecas necessárias para a leitura dos dados (como o `openpyxl` para ler planilhas Excel):
```bash
pip install openpyxl
# Ou, se já tiver atualizado o arquivo requirements.txt:
# pip install -r requirements.txt
```

### 5. Posicionar os Arquivos de Dados
Certifique-se de que os arquivos de origem estão corretamente posicionados dentro da pasta `dados/` na raiz do projeto:
*   `dados/disciplinas.json` (Matriz curricular e pré-requisitos)
*   `dados/Horário.xlsx` (Planilha com a oferta e horários do semestre atual)

Sua estrutura deve estar parecida com isso:
```text
sistema-recomendacao-de-matriculas/
├── banco/
│   ├── conexao.py
│   └── criar_tabelas.py
├── dados/
│   ├── disciplinas.json
│   └── Horário.xlsx
...
```

### 6. Executar a Criação do Banco de Dados
Para processar o JSON, ler a planilha e criar as tabelas no SQLite, execute o módulo a partir da raiz do projeto:
```bash
python -m banco.criar_tabelas
```
> **Sucesso:** Se tudo ocorrer bem, você verá a mensagem de que os dados foram carregados e o arquivo `disciplinas.db` aparecerá dentro da pasta `banco/`.

---

### 🧩 Extensões Recomendadas (VS Code)

Como o banco de dados `disciplinas.db` é um arquivo binário, o editor de texto padrão não consegue exibi-lo. Para visualizar as tabelas diretamente no VS Code:

1. Vá na aba **Extensions** (Extensões) ou aperte `Ctrl+Shift+X`.
2. Pesquise por **SQLite Viewer** (do desenvolvedor *Florian Klampfer*).
3. Instale a extensão.
4. Clique no arquivo `banco/disciplinas.db`. Uma interface visual será aberta, permitindo navegar pelas tabelas e dados importados.

## 📋 Funcionalidades Previstas

- [ ] Cadastro e consulta de disciplinas.
- [ ] Registro do histórico acadêmico.
- [ ] Verificação automática de pré-requisitos.
- [ ] Identificação de disciplinas disponíveis.
- [ ] Geração de combinações de matrículas.
- [ ] Verificação de conflitos de horários.
- [ ] Cálculo da função de utilidade.
- [ ] Recomendação da melhor grade curricular.
- [ ] Apresentação das justificativas da recomendação.
- [ ] Registro de feedback para melhoria das recomendações.

## 🔮 Trabalhos Futuros

Como possibilidades de evolução, o projeto poderá incorporar:

- Integração com sistemas acadêmicos institucionais.
- Importação automática do histórico acadêmico.
- Algoritmos mais eficientes de busca e otimização.
- Aprendizagem baseada nas preferências dos estudantes.
- Notificações sobre períodos de matrícula.
- Interface mais personalizada e responsiva.

## 👥 Equipe

Projeto desenvolvido como parte de uma atividade acadêmica.

**Integrantes:**
- Beatriz WG
- Cibele Diniz
- Maira Nunes

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos e educacionais.

---

<p align="center">
  🎓 <strong>Mais organização, mais conquistas!</strong>
</p>