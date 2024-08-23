#Bibliotecas necessárias
import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(page_title='Financiamento 360')

#
#
#
#Seleção do prazo do financiamento
range = range(0, 421)
periodo = st.select_slider(
    "Selecione o prazo do seu financiamento",
    options=range, value =420)
st.write(f'O prazo selecionado corresponde à {round(periodo/12, 2)} anos')

#
#
#
#Seleção do juro anual
taxa_anual = st.number_input("Insira o valor dos juros efetivos (anual): ")
taxa_mensal = 100*((1+taxa_anual/100)**(1/12)-1)
st.write("Com ", taxa_anual,"%","a.a de juros efetivos, temos uma taxa equivalente de juro mensal de: ", taxa_mensal )

st.text('A fórmula para o cálculo da parcela é:')
st.text('A fórmula para o cálculo da parcela é:')
st.latex(r'''\text{PMT} = \frac{P \cdot r \cdot (1 + r)^n}{(1 + r)^n - 1}
''')

st.text('''Em que:
        P = valor financiado.
        r = taxa de juros.
        n = prazo.''')
