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

## 🚀 Executar o Projeto

### Pré-requisitos

- Python 3.10 ou superior.
- Git instalado.
- Editor de código, como Visual Studio Code.

### 1. Clonar o repositório

```bash
git clone https://github.com/MairaFN/sistema-recomendacao-matriculas.git

```

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