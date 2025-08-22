# comandos necessários para rodar o código
import demographic_data_analyzer
from unittest import main

# chama a função declarada no arquivo demographic_data_analyzer.py para imprimir os resultados
demographic_data_analyzer.calculate_demographic_data()

# dsse comando vai rodar os testes automaticamente
main(module='test_module', exit=False)