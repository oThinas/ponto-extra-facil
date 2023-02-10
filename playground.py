def calcularMontante(capital, taxa, tempo=1):
  return capital * (1 + taxa) ** tempo

investidores = [
  {
    'nome': 'João',
    'capital': 10000,
    'investimentos': {
      'CDB': 0.35,
      'LCI': 0.2,
      'LCA': 0.33,
      'acoes': 0.12,
    },
  },
  {
    'nome': 'Maria',
    'capital': 8000,
    'investimentos': {
      'CDB': 0.1,
      'FII': 0.2,
      'acoes': 0.7,
    },
  },
]

taxas = {
  'CDB': 0.01,
  'LCI': 0.02,
  'FII': 0.09,
  'LCA': 0.03,
  'acoes': 1,
}

for investidor in investidores:
  for investimento, percentual in investidor['investimentos'].items():
    montante = calcularMontante(investidor['capital'] * percentual, taxas[investimento], 3)
    print(f"{investidor['nome']} terá R$ {montante} em investimentos em {'ações' if investimento == 'acoes' else investimento}")
