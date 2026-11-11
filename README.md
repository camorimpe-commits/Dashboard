# ⚡ OptimaOps - Monitor de Eficiência Operacional & Tomada de Decisão

> **Solução de inteligência e monitoramento de eficiência operacional com automação de ponta a ponta.**  
> Desenvolvida com **Python**, **Pandas**, **FastAPI**, **API REST**, **JavaScript**, **HTML5** e **CSS3 Moderno**.

---

## 🌟 Visão Geral & Diferenciais

Mais do que visualizar números isolados, o **OptimaOps** transforma 60.700+ registros orçamentários e contratuais diários em **inteligência acionável para apoiar decisões estratégicas**.

### 🚀 Principais Capacidades:
1. **Automação Total de Ingestão de Dados**:
   - **Watcher de Arquivos**: Ao salvar ou arrastar qualquer novo arquivo `.xlsx`, `.xls` ou `.csv` para a pasta de dados (`data/uploads/`), o pipeline em Python/Pandas processa as informações em segundo plano e disponibiliza os novos indicadores pela API.
   - **Sincronização Online com Google Sheets**: Conexão nativa e sincronização sob demanda com a [Planilha Google Oficial](https://docs.google.com/spreadsheets/d/1uQcCEjud5tnj9vpbRzYJq-J89GMgl_3-YwoCHaurnmU/edit?gid=507908437#gid=507908437) atualizada diariamente.
2. **Indicadores e Ranking de Desempenho em Tempo Real**:
   - **Índice Global de Eficiência Operacional (IGEO)**: Score composto (0 a 100) ponderado por taxa de liquidação, pontualidade de execução e cumprimento de metas.
   - **SLA Operacional de Pagamento**: Cálculo do tempo de ciclo entre a emissão da Nota de Liquidação (ateste) e a Ordem Bancária (pagamento).
   - **Ranking Multidimensional de Credores / Fornecedores**: Classificação com medalhas (🥇, 🥈, 🥉), volume financeiro, SLA médio e classificação de risco (Classe A, B e C).
3. **Identificação de Desvios & Gargalos**:
   - Auditoria automatizada de anomalias de prazo (SLA > 30 dias), concentração excessiva de fornecedores (risco de dependência) e defasagens orçamentárias (empenhos não atestados).
4. **Central de Inteligência para Tomada de Decisão**:
   - Cards executivos com estimativa monetária de oportunidade de economia (ex: R$ 14,3M em terceirizados) e redução de dias de ciclo.
   - **Simulador Executivo "What-If"**: Painel interativo com sliders de redução de custo e aceleração de SLA para projetar economia imediata e ganho de eficiência.
5. **Segurança & Tela de Autenticação**:
   - Interface de Login com design moderno, tokens JWT (HMAC-SHA256) e botões de **acesso rápido demonstrativo** (Admin, Gestor e Analista).

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.11, FastAPI, Uvicorn, Pandas, OpenPyXL, Pydantic, Requests.
- **Frontend**: HTML5 Semântico, CSS3 Moderno (Glassmorphism, Dark Mode Executivo), JavaScript ES6+ (SPA reativo sem dependências pesadas), Chart.js 4.4.
- **Segurança**: Autenticação com Bearer Tokens JWT, perfis com controle de permissão e sanitização de dados.

---

## 🔑 Credenciais Demonstrativas de Acesso

Na tela de login (`/login`), basta clicar em qualquer um dos cards para preenchimento e login instantâneo:

| Usuário | E-mail | Senha | Perfil |
| :--- | :--- | :--- | :--- |
| **Cristiano Sena** | `admin@operacoes.gov.br` | `admin123` | Diretor de Operações (Admin Full) |
| **Mariana Albuquerque** | `gestor@operacoes.gov.br` | `gestor123` | Gestora de Eficiência Operacional |
| **Lucas Vasconcelos** | `analista@operacoes.gov.br` | `analista123` | Analista de Processos & Dados |

---

## 📁 Estrutura do Projeto

```
operacional_efficiency_monitor/
│
├── data/
│   ├── sample_data.csv          # Base baseline com 60.728 registros
│   ├── active_data.csv          # Base ativa sincronizada
│   └── uploads/                 # Pasta monitorada para novos uploads
│
├── core/
│   ├── config.py                # Configurações, metas operacionais e usuários
│   ├── auth.py                  # Autenticação JWT e hashing de credenciais
│   ├── data_processor.py        # Motor analítico em Pandas (KPIs, SLA, Ranking, Decisão)
│   └── watcher.py               # Robô de monitoramento de novos arquivos em segundo plano
│
├── api/
│   ├── routes_auth.py           # Endpoints de login, sessão e demo accounts
│   ├── routes_metrics.py        # KPIs, evolução temporal, Pareto e rankings
│   ├── routes_decisions.py      # Insights de apoio à decisão e simulador What-If
│   └── routes_data.py           # Upload, sincronização Google Sheets e exportação CSV
│
├── static/
│   ├── css/style.css            # Estilização executiva e responsiva
│   └── js/app.js                # Controlador do Dashboard, Chart.js e reatividade
│
├── templates/
│   ├── login.html               # Tela de login estilizada com demo pills
│   └── dashboard.html           # Painel executivo interativo
│
├── run.bat                      # Inicializador automático para Windows
├── main.py                      # Ponto de entrada FastAPI e ciclo de vida
└── test_app_logic.py            # Suite de testes integrados e validações
```

---

## 🚀 Como Executar

### Opção 1: Via Script Automático (Recomendado)
Basta dar um duplo clique no arquivo `run.bat` dentro da pasta do projeto:
```cmd
run.bat
```

### Opção 2: Via Linha de Comando (PowerShell / Prompt)
```powershell
cd C:\Users\Cristiano.sena\.gemini\antigravity\scratch\operacional_efficiency_monitor
& "C:\Program Files\LibreOffice\program\python.exe" -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Em seguida, abra seu navegador em:
👉 **`http://localhost:8000`** ou **`http://localhost:8000/login`**

---

## 📊 Endpoints da API REST

- `POST /api/auth/login`: Autentica usuário e retorna token JWT.
- `GET /api/metrics/summary`: Retorna KPIs consolidados (Total Empenhado, Liquidado, Pago, SLA, IGEO).
- `GET /api/metrics/trends`: Série temporal de valores financeiros e SLA médio mês a mês.
- `GET /api/metrics/pareto`: Análise da curva ABC de despesas por tema operacional.
- `GET /api/metrics/rankings`: Ranking dinâmico dos credores com score e indicadores.
- `GET /api/metrics/deviations`: Relação de desvios e gargalos críticos detectados.
- `GET /api/decisions/insights`: Recomendações estratégicas para gestores com estimativa de impacto.
- `POST /api/decisions/simulate`: Simula cenários de redução de custos e otimização de SLA.
- `POST /api/data/upload`: Ingestão instantânea de novos arquivos `.xlsx`, `.xls` ou `.csv`.
- `POST /api/data/sync-google-sheets`: Sincronização online com a planilha Google.
- `GET /api/data/export`: Exportação do relatório operacional em CSV/Excel.
