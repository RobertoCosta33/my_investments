# main.py

import investments

valor_inicial = 1000
valor_final = 1500
anos = 5
taxa_anual = 6

retorno = investments.calculate_return_on_investment(valor_inicial, valor_final)
print(f"Retorno do investimento: {retorno:.2f}%")

valor_final_juros = investments.calculate_compound_interest(valor_inicial, taxa_anual, anos)
print(f"Valor final com juros compostos: R${valor_final_juros:.2f}")

taxa_mensal = investments.convert_annual_rate_to_monthly(taxa_anual)
print(f"Taxa de juros mensal: {taxa_mensal:.2f}%")

cagr = investments.calculate_cagr(valor_inicial, valor_final, anos)
print(f"CAGR: {cagr:.2f}%")
