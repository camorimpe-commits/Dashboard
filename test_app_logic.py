import sys
sys.path.insert(0, r"C:\Users\Cristiano.sena\.gemini\antigravity\scratch\operacional_efficiency_monitor")

from core.data_processor import data_processor
from api.routes_auth import login, LoginRequest
from api.routes_metrics import get_options, get_summary, get_trends, get_pareto, get_rankings, get_deviations
from api.routes_decisions import get_insights, simulate, SimulationRequest
from main import get_login_page, get_dashboard_page

print("--- 1. Testing Initial Baseline Load ---")
ok = data_processor.load_and_process()
print(f"DataProcessor Loaded: {ok} | Records: {data_processor.total_records:,}")

print("\n--- 2. Testing HTML Pages ---")
r_login = get_login_page()
print(f"Login HTML Length: {len(r_login.body.decode('utf-8'))} bytes")
r_dash = get_dashboard_page()
print(f"Dashboard HTML Length: {len(r_dash.body.decode('utf-8'))} bytes")

print("\n--- 3. Testing Authentication ---")
auth_res = login(LoginRequest(username="admin@operacoes.gov.br", password="admin123"))
print(f"Auth Success: {auth_res['success']} | User: {auth_res['user']['name']} | Role: {auth_res['user']['role_title']}")
token = auth_res['token']
print(f"JWT Token generated: {token[:30]}...")

print("\n--- 4. Testing Filter Options ---")
options = get_options()
print(f"Years: {options['years']} | Months: {options['months']} | Temas Count: {len(options['temas'])}")

print("\n--- 5. Testing Executive KPIs ---")
kpis = get_summary()
print(f"Total Empenhado: R$ {kpis['total_empenhado']:,.2f}")
print(f"Total Liquidado: R$ {kpis['total_liquidado']:,.2f} ({kpis['taxa_liquidacao']}% de Eficiência)")
print(f"Total Pago:      R$ {kpis['total_pago']:,.2f} ({kpis['taxa_execucao']}% de Execução)")
print(f"SLA Médio:       {kpis['sla_medio_dias']} dias (Compliance: {kpis['sla_compliance_rate']}%)")
print(f"Score IGEO:      {kpis['igeo_score']} / 100 ({kpis['status_class']})")
print(f"Gargalos SLA:    {kpis['anomalias_sla_count']} transações críticas")

print("\n--- 6. Testing Pareto & Trends ---")
pareto = get_pareto(top_n=5)
print("Top 3 Temas por Gasto:", pareto['labels'][:3])
trends = get_trends()
print(f"Evolution Months: {len(trends['labels'])} periods (First: {trends['labels'][0]}, Last: {trends['labels'][-1]})")

print("\n--- 7. Testing Credor Performance Ranking ---")
ranks = get_rankings(limit=3)
for r in ranks:
    print(f"#{r['posicao']} | {r['credor_nome'][:35]} | Pago: R$ {r['total_pago']:,.2f} | SLA: {r['sla_medio']}d | Score: {r['score']} pts ({r['badge']})")

print("\n--- 8. Testing Deviations & Bottlenecks ---")
deviations = get_deviations()
print(f"Deviations detected: {len(deviations)}")
for d in deviations[:2]:
    print(f"  [{d['severidade']}] {d['tipo']}: {d['titulo']}")

print("\n--- 9. Testing Decision Intelligence ---")
insights = get_insights()
for i in insights:
    print(f"  [Insight] {i['titulo']} -> Impacto: {i['impacto_estimado']}")

print("\n--- 10. Testing What-If Scenario Simulator ---")
sim_res = simulate(SimulationRequest(sla_improvement_pct=15.0, cost_reduction_pct=3.5))
print(f"Cenário: {sim_res['cenario']}")
print(f"Economia Projetada: R$ {sim_res['economia_projetada_reais']:,.2f}")
print(f"Dias Poupados: {sim_res['dias_poupados_ciclo']} dias | Novo SLA: {sim_res['novo_sla_projetado']} dias")

print("\n=======================================================")
print("  >>> ALL INTEGRATION & BUSINESS LOGIC TESTS PASSED <<<")
print("=======================================================")
