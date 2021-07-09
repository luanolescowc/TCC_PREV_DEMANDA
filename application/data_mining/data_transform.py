import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def Input_Data():
    dataset1 = pd.read_excel('/home/luanolescowc/ProgramDevelopment/Python/Github/Previsor_de_Demanda_TCC/application/database/data_base_demanda_P.xlsx')
    dataset = dataset1.dropna()
    st.dataframe(dataset)
    return plot_corr(dataset)

# --------------------------- CORRELAÇÃO ENTRE AS VARIAVEIS -----------------

# correlação entre as variaveis preditoras
# +1 = forte correlação positiva
# 0 = nenhuma correlação
# -1 = forte correlação negativa


def plot_corr(dataset):
    size = len(dataset)
    corr = dataset.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)

    #plot_corr(dataset)  # imprimindo como uma imagem de correlação

    st.dataframe(dataset.corr())  # imprimiindo como uma tabela de correlação

    minimas = pd.concat([dataset.corr().idxmin(),dataset.corr().min()], axis = 1)

    return st.dataframe(minimas)

    import ipdb; ipdb.set_trace()