import pandas as pd
import streamlit as st
import altair as alt

st.title('App - Tópicos Avançados')

@st.cache
def load_database():
    return pd.read_feather('tavbase/gs.feather'), \
        pd.read_feather('tavbase/classificacaoz_consumidor.feather')

gs, cla_con = load_database()


taberp, tabbi, tabstore = st.tabs(['Sisetma Interno', 'Gestão', 'E-Commerce'])

with taberp:
    st.header('Dados do Sistema Interno')
    # st.dataframe(gs)
    consumidor = st.selectbox(
        'Selecione o Consumidor', 
        gs['Customer ID'].unique()
    )

    gs_con = gs[gs['Customer ID'] == consumidor]
    # st.dataframe(gs_con)
    cla_con_con = cla_con[cla_con['Customer ID'] == consumidor].reset_index()
    # st.dataframe(cla_con_con)

    st.dataframe(gs_con[['Customer Name', 'Segment']].drop_duplicates())
    cli1, cli2, cli3, cli4 = st.columns(4)
    cli1.metric('Score',  round(cla_con_con['score'][0],  4), '1')
    cli2.metric('Classe', round(cla_con_con['classe'][0], 4), '1')
    cli3.metric('Rank',   round(cla_con_con['rank'][0],   4), '1')
    cli4.metric('Lucro',  round(cla_con_con['lucro'][0],  4), '1')
    
    cli1.metric('Valor Total Comprado',  round(gs_con['Sales'].sum(),    4), '1')
    cli2.metric('Valor Lucro',           round(gs_con['Profit'].sum(),   4), '1')
    cli3.metric('Valor Média Comprado',  round(gs_con['Sales'].mean(),   4), '1')
    cli4.metric('Quantidade Comprda',    round(gs_con['Quantity'].sum(), 4), '1')

    with st.expander('Pedidos:'):
        st.dataframe(
            gs_con[['Order ID', 'Order Date', 'Ship Date', 'Sales', 'Profit']]
        )

with tabbi:
    st.header('Dados do Business Intelligence')
    st.dataframe(cla_con)
with tabstore:
    st.header('Dados do E-Commerce')