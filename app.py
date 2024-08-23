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
#
#Selecao do valor do financiamento
p = st.number_input(
    "Insira o valor financiado", value=300000, min_value=1
)

#
#
#
#
#Seleção do juro anual
taxa_anual = st.number_input("Insira o valor dos juros efetivos (anual): ", value = 12)
taxa_mensal = 100*((1+taxa_anual/100)**(1/12)-1)
st.write("Com ", taxa_anual,"%","a.a de juros efetivos, temos uma taxa equivalente de juro mensal de: ", taxa_mensal, '%' )




#
#
#
#Seleção do prazo do financiamento
range = range(0, 421)
periodo = st.select_slider(
    "Selecione o prazo do seu financiamento",
    options=range, value =420)
st.write(f'O prazo selecionado corresponde à {round(periodo/12, 2)} anos')
periodo = float(periodo)

#
#
#
#

agree = st.checkbox("Apenas para nerds 🤓")

if agree:
    st.text('A fórmula para o cálculo da parcela é:')
    st.latex(r'''\text{PMT} = \frac{P \cdot r \cdot (1 + r)^n}{(1 + r)^n - 1}
    ''')
    st.text('''Em que:
            PMT = valor da parcela.
            P = valor financiado.
            r = taxa de juros.
            n = prazo.''')



pmt = (p*taxa_mensal/100*(1+taxa_mensal/100)**(periodo))/((1+taxa_mensal/100)**periodo - 1)

st.write("O Valor da parcela no cenário simulado é de R$", round(pmt,2))