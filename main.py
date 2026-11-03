import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


@st.cache_data
def carregar_dados_vendas_p_ano():
    df_vendas_p_ano2020 = pd.read_excel('Vendas por ano.xlsx', sheet_name='2020').sort_values(by=['Qtd Vendida'], ascending=False)
    df_vendas_p_ano2021 = pd.read_excel('Vendas por ano.xlsx', sheet_name='2021').sort_values(by=['Qtd Vendida'], ascending=False)
    df_vendas_p_ano2022 = pd.read_excel('Vendas por ano.xlsx', sheet_name='2022').sort_values(by=['Qtd Vendida'], ascending=False)
    return df_vendas_p_ano2020, df_vendas_p_ano2021, df_vendas_p_ano2022

@st.cache_data
def carregar_dados_devolucoes():
    devolucoes_2020 = (pd.read_excel('Devoluções por ano.xlsx', sheet_name='2020')
                       .sort_values(by=['Qtd Devolvida'], ascending=False))
    devolucoes_2021 = (pd.read_excel('Devoluções por ano.xlsx', sheet_name='2021')
                       .sort_values(by=['Qtd Devolvida'], ascending=False))
    devolucoes_2022 = (pd.read_excel('Devoluções por ano.xlsx', sheet_name='2022')
                       .sort_values(by=['Qtd Devolvida'], ascending=False))
    return devolucoes_2020, devolucoes_2021, devolucoes_2022


df_vendas_p_ano2020, df_vendas_p_ano2021, df_vendas_p_ano2022 = carregar_dados_vendas_p_ano()
devol_2020, devol_2021, devol_2022 = carregar_dados_devolucoes()

st.html("""
<h1 style= "color: #FFB0E0; font-family: 'Trebuchet MS', fantasy; text-align: center">Analise das vendas</h1>""")
st.html("""
<h2 style= "color: #E0B0FF; font-family: 'Courier New', monospace"> <i>Tabela loja com maiores vendas</i></h2>""")



aba_2020, aba_2021, aba_2022 = st.tabs(['2020','2021','2022'])


with aba_2020:

    with st.container(height=300):

        st.table(data=df_vendas_p_ano2020, border=True, width="stretch",
                 height="content", hide_index=None, hide_header=None, alt=None)

with aba_2021:

    with st.container(height=300):

        st.table(data=df_vendas_p_ano2021, border=True, width="stretch",
                 height="content", hide_index=None, hide_header=None, alt=None)

with aba_2022:

    with st.container(height=300):

        st.table(data=df_vendas_p_ano2022, border=True, width="stretch",
                 height="content", hide_index=None, hide_header=None, alt=None)


st.html("""
<h2 style= "color: #E0B0FF; font-family: 'Courier New', monospace"> 
<i>Grafico de lojas com maiores vendas</i></h2>""")


cores = ['#7F00FF', '#B163FF', '#51158C', '#D796F2', '#8A00C4']
amarelo = '#FFDE21'

aba_vendas,  aba_vendasxfunc = st.tabs(['Vendas', 'Vendas x Funcionários'])



with aba_vendas:
    aba_2020, aba_2021, aba_2022 = st.tabs(['2020', '2021', '2022'])
    with aba_2020:
        plt.close('all')
        fig, ax = plt.subplots()
        ax.set_title('Lojas com mais vendas')
        barras = ax.bar(x=df_vendas_p_ano2020['Nome da Loja'].str[5:18].head(4),
                        height= df_vendas_p_ano2020['Qtd Vendida'].head(4),
                        color = cores, linewidth = 0.5, edgecolor='black')
        ax.bar_label(barras, padding=3)

        ax.set_facecolor('#FFFFC5')
        fig.patch.set_facecolor('#E0B0FF')
        ax.grid(color = 'black',linestyle='--', linewidth=0.5, alpha=0.5)

        ax.set_ylabel('Qtd Vendida')
        max_y = df_vendas_p_ano2020['Qtd Vendida'].max()
        ax.set_ylim(0, max_y + 20)
        ax.set_title('Vendas por Loja')
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        st.pyplot(fig)
    with aba_2021:
        plt.close('all')
        fig, ax = plt.subplots()
        ax.set_title('Lojas com mais vendas')
        barras = ax.bar(x=df_vendas_p_ano2021['Nome da Loja'].str[5:18].head(4),
                        height= df_vendas_p_ano2021['Qtd Vendida'].head(4),
                        color = cores, linewidth = 0.5, edgecolor='black')
        ax.bar_label(barras, padding=3)

        ax.set_facecolor('#FFFFC5')
        fig.patch.set_facecolor('#E0B0FF')
        ax.grid(color = 'black',linestyle='--', linewidth=0.5, alpha=0.5)

        ax.set_ylabel('Qtd Vendida')
        max_y = df_vendas_p_ano2021['Qtd Vendida'].max()
        ax.set_ylim(0, max_y + 200)
        ax.set_title('Vendas por Loja')
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        st.pyplot(fig)
    with aba_2022:
        plt.close('all')
        fig, ax = plt.subplots()
        ax.set_title('Lojas com mais vendas')
        barras = ax.bar(x=df_vendas_p_ano2022['Nome da Loja'].str[5:18].head(4),
                        height= df_vendas_p_ano2022['Qtd Vendida'].head(4),
                        color = cores, linewidth = 0.5, edgecolor='black')
        ax.bar_label(barras, padding=3)

        ax.set_facecolor('#FFFFC5')
        fig.patch.set_facecolor('#E0B0FF')
        ax.grid(color = 'black',linestyle='--', linewidth=0.5, alpha=0.5)

        ax.set_ylabel('Qtd Vendida')
        max_y = df_vendas_p_ano2022['Qtd Vendida'].max()
        ax.set_ylim(0, max_y + 200)
        ax.set_title('Vendas por Loja')
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        st.pyplot(fig)

with aba_vendasxfunc:
    aba_2020, aba_2021, aba_2022 = st.tabs(['2020', '2021', '2022'])
    with aba_2020:
        plt.close('all')
        x = np.arange(4)
        width = 0.35
        fig, ax = plt.subplots()
        ax.set_title('Vendas x Funcionarios')
        barra1 = ax.bar(x=x - width / 2,
               height=df_vendas_p_ano2020['Qtd Vendida'].head(4),
               width=width,
               color=cores[0],
               linewidth=0.5,
               edgecolor='black',
               label= 'Quantidade Vendida')


        barra2 = ax.bar(x=x + width / 2,
               height=df_vendas_p_ano2020['Quantidade Colaboradores'].head(4),
               width=width,
               color=amarelo,
               linewidth=0.5,
               edgecolor='black',
               label='Quantidade Colaboradores')

       
        ax.legend()
        ax.set_facecolor('#FFFFC5')
        fig.patch.set_facecolor('#E0B0FF')
        ax.grid(color = 'black',linestyle='--', linewidth=0.5, alpha=0.5)
        ax.set_xticks(x)
        ax.set_xticklabels(df_vendas_p_ano2021['Nome da Loja'].str[5:18].head(4))

        plt.tight_layout()
        st.pyplot(fig)

    with aba_2021:
            plt.close('all')
            x = np.arange(4)
            width = 0.35
            fig, ax = plt.subplots()
            ax.set_title('Vendas x Funcionarios')
            barra1 = ax.bar(x=x - width / 2,
                   height=df_vendas_p_ano2021['Qtd Vendida'].head(4),
                   width=width,
                   color=cores[0],
                   linewidth=0.5,
                   edgecolor='black',
                   label= 'Quantidade Vendida')
    
    
            barra2 = ax.bar(x=x + width / 2,
                   height=df_vendas_p_ano2021['Quantidade Colaboradores'].head(4),
                   width=width,
                   color=amarelo,
                   linewidth=0.5,
                   edgecolor='black',
                   label='Quantidade Colaboradores')
    
           
            ax.legend()
            ax.set_facecolor('#FFFFC5')
            fig.patch.set_facecolor('#E0B0FF')
            ax.grid(color = 'black',linestyle='--', linewidth=0.5, alpha=0.5)
            ax.set_xticks(x)
            ax.set_xticklabels(df_vendas_p_ano2021['Nome da Loja'].str[5:18].head(4))
    
            plt.tight_layout()
            st.pyplot(fig)

    with aba_2022:
                plt.close('all')
                x = np.arange(4)
                width = 0.35
                fig, ax = plt.subplots()
                ax.set_title('Vendas x Funcionarios')
                barra1 = ax.bar(x=x - width / 2,
                       height=df_vendas_p_ano2022['Qtd Vendida'].head(4),
                       width=width,
                       color=cores[0],
                       linewidth=0.5,
                       edgecolor='black',
                       label= 'Quantidade Vendida')
        
        
                barra2 = ax.bar(x=x + width / 2,
                       height=df_vendas_p_ano2022['Quantidade Colaboradores'].head(4),
                       width=width,
                       color=amarelo,
                       linewidth=0.5,
                       edgecolor='black',
                       label='Quantidade Colaboradores')
        
               
                ax.legend()
                ax.set_facecolor('#FFFFC5')
                fig.patch.set_facecolor('#E0B0FF')
                ax.grid(color = 'black',linestyle='--', linewidth=0.5, alpha=0.5)
                ax.set_xticks(x)
                ax.set_xticklabels(df_vendas_p_ano2022['Nome da Loja'].str[5:18].head(4))
        
                plt.tight_layout()
                st.pyplot(fig)



st.html("""
<h2 style= "color: #E0B0FF; font-family: 'Courier New', monospace"> 
Gráfco de Devoluções</h2>""")

aba_devol, aba_tabelas = st.tabs(['Gráficos', 'Tabelas'])
with aba_devol:
    aba_2020, aba_2021, aba_2022 = st.tabs(['2020', '2021', '2022'])
    with aba_2020:
        plt.close('all')
        fig, ax = plt.subplots()
        ax.set_title('Lojas com mais Devoluções')
        barras = ax.bar(x=devol_2020['Nome da Loja'].str[5:18].head(4),
                        height= devol_2020['Qtd Devolvida'].head(4),
                        color = cores, linewidth = 0.5, edgecolor='black')
        ax.bar_label(barras, padding=3)

        ax.set_facecolor('#FFFFC5')
        fig.patch.set_facecolor('#E0B0FF')
        ax.grid(color = 'black',linestyle='--', linewidth=0.5, alpha=0.5)

        ax.set_ylabel('Qtd Devolvida')
        max_y = devol_2020['Qtd Devolvida'].max()
        ax.set_ylim(0, max_y + 20)
        ax.set_title('Devoluções por Loja')
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()

        st.pyplot(fig)

    with aba_2021:
            plt.close('all')
            fig, ax = plt.subplots()
            ax.set_title('Lojas com mais Devoluções')
            barras = ax.bar(x=devol_2021['Nome da Loja'].str[5:18].head(4),
                            height= devol_2021['Qtd Devolvida'].head(4),
                            color = cores, linewidth = 0.5, edgecolor='black')
            ax.bar_label(barras, padding=3)
    
            ax.set_facecolor('#FFFFC5')
            fig.patch.set_facecolor('#E0B0FF')
            ax.grid(color = 'black',linestyle='--', linewidth=0.5, alpha=0.5)
    
            ax.set_ylabel('Qtd Devolvida')
            max_y = devol_2021['Qtd Devolvida'].max()
            ax.set_ylim(0, max_y + 20)
            ax.set_title('Devoluções por Loja')
            plt.xticks(rotation=45, ha='right')
    
            plt.tight_layout()
    
            st.pyplot(fig)

    with aba_2022:
                plt.close('all')
                fig, ax = plt.subplots()
                ax.set_title('Lojas com mais Devoluções')
                barras = ax.bar(x=devol_2022['Nome da Loja'].str[5:18].head(4),
                                height= devol_2022['Qtd Devolvida'].head(4),
                                color = cores, linewidth = 0.5, edgecolor='black')
                ax.bar_label(barras, padding=3)
        
                ax.set_facecolor('#FFFFC5')
                fig.patch.set_facecolor('#E0B0FF')
                ax.grid(color = 'black',linestyle='--', linewidth=0.5, alpha=0.5)
        
                ax.set_ylabel('Qtd Devolvida')
                max_y = devol_2022['Qtd Devolvida'].max()
                ax.set_ylim(0, max_y + 20)
                ax.set_title('Devoluções por Loja')
                plt.xticks(rotation=45, ha='right')
        
                plt.tight_layout()
        
                st.pyplot(fig)

with aba_tabelas:
    aba_2020, aba_2021, aba_2022 = st.tabs(['2020', '2021', '2022'])
    with aba_2020:
        with st.container(height=300):
            st.table(data=devol_2020, border=True, width="stretch",
                    height="content", hide_index=None, hide_header=None, alt=None)
    with aba_2021:
        with st.container(height=300):
            st.table(data=devol_2021, border=True, width="stretch",
                     height="content", hide_index=None, hide_header=None, alt=None)
    with aba_2022:
        with st.container(height=300):
            st.table(data=devol_2022, border=True, width="stretch",
                     height="content", hide_index=None, hide_header=None, alt=None)


