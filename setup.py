from application.data_mining import data_transform
from application.artificial_neural_network import neural_application
import streamlit as st


class MainPage:
    def execute(self):
        st.markdown("""
         Pagina criada para ajudar na interpretação e transformação de dados
         do Previsor de demanda de energia elétrica   
        """)

        lista_operacoes = [
            "0. Página inicial",
            "1. Data transform",
            "2. Neural Application"

        ]

        operacao_selecionada = st.sidebar.selectbox("Operação escolhida", lista_operacoes)

        if operacao_selecionada == lista_operacoes[1]:
            return data_transform.Input_Data()

        if operacao_selecionada == lista_operacoes[2]:
            return neural_application.Begin_test()

    '''  @staticmethod
    def _download_celesc_faturas_as_pdfs():
        st.markdown("""
            ## Crawl and Download Pipeline ##

            Pipeline que loga no site da CELESC, e baixa todos os PDFs de 2ª via do cliente.

            Aperte o botão abaixo para que seja feito o download das faturas do primeiro
            cliente que se encontra na planilha referência.

            **Observação: A cada clique é executado todo este pipeline, então
            só aperte ele caso realmente necessário. **
        """)
        if st.button("Fazer download das faturas"):
            CoreExecutor(enable_download_from_site=True).execute()

        if st.checkbox("Conferir quantidade de PDFs baixados?"):
            st.markdown(f"""
            - Quantidade: {count_number_of_pdfs()["count"]}
            - Pasta em que se encontram: `{count_number_of_pdfs()["folder"]}`
            """)
    '''

if __name__ == '__main__':
    MainPage().execute()




