# ⚡ Calculadora de Consumo de Energia
Este projeto foi desenvolvido como parte de um programa de iniciação em tecnologia.  
O objetivo é ajudar usuários a estimar o consumo mensal de energia elétrica de seus aparelhos.

## 🚀 Objetivo
Calcular o consumo mensal em kWh e o custo estimado em reais, com base em:
- Potência do aparelho (W)
- Tempo médio de uso diário (h)

## 🛠️ Tecnologias
- Linguagem: **Python**
- Plataforma: **GitHub**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Repo-black?logo=github)
![Energia](https://img.shields.io/badge/Energia-%E2%9A%A1-yellow)
![Status](https://img.shields.io/badge/Projeto-Ativo-brightgreen)

## 📐 Fórmula utilizada
Consumo_diario = (Potencia * Horas_dia) / 1000  # Convertendo para kWh

Consumo_mensal = Consumo_diario * 30  # Considerando 30 dias no mês

Custo_estimado = Consumo_mensal * 0.85  # Custo estimado (R$ 0,85 por kWh)


## ▶️ Como executar
Para que o sistema analise, informe:
- O nome do aparelho que utilizará para a análise
- A potência do aparelho
- Quantas horas utiliza esse aparelho por dia.

Obs.: Caso for informar horas não inteiras, oriento a utilizar "." no lugar de "," exemplo 0.5 (30min)


## 🎨 Exemplo de saída

---resultado---

O consumo diário do aparelho Batedeira é de 0.60 kWh.

O consumo mensal do aparelho Batedeira é de 18.00 kWh.

O custo mensal baseado no consumo do aparelho Batedeira é de R$ 15.30.

Lembre-se de que esses valores são estimativas e podem variar dependendo do uso real do aparelho e da tarifa de energia elétrica.

utilize o consumo de energia de forma consciente para economizar e preservar o meio ambiente.

Obrigado por utilizar o programa de cálculo de consumo de energia!


### Premissa de custo de energia
Para as estimativas realizadas neste projeto, foi adotado como valor de referência **R$ 0,85/kWh**, aproximadamente, considerando a tarifa média residencial observada para o estado de São Paulo.

O valor é utilizado apenas como referência para estimativas e pode variar conforme distribuidora, modalidade tarifária, tributos e demais componentes aplicáveis à unidade consumidora.

**Referência:** dados tarifários da Agência Nacional de Energia Elétrica (ANEEL), listados abaixo.


## Referências 
AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA (ANEEL). **Tarifas**. Brasília, DF: ANEEL. Disponível em: <https://www.gov.br/aneel/pt-br/assuntos/tarifas>. Acesso em: 27 set. 2026.
 
AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA (ANEEL). **Base de Dados das Tarifas das Distribuidoras de Energia Elétrica**. Brasília, DF: ANEEL. Disponível em: <https://portalrelatorios.aneel.gov.br/luznatarifa/basestarifas>. Acesso em: 27 set. 2026.
 
CALCULADORA DE ENERGIA. **Tarifa de Energia por Estado e Distribuidora (2026)**. 2026. Disponível em: <https://calculadoraenergia.com.br/tarifa>. Acesso em: 27 set. 2026.
