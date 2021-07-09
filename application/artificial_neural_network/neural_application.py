import numpy as np
import pandas as pd
import streamlit as st
import matplotlib as plt



def Begin_test():
    dataframe_8var_select1 = pd.read_excel(

        '/home/luanolescowc/ProgramDevelopment/Python/Github/Previsor_de_Demanda_TCC/application/database/Basededados_Porto_8Variaveis.xlsx'

    )
    dataframe_8var_select = dataframe_8var_select1.dropna()
    dataframe_8var_select.columns = dataframe_8var_select.iloc[0]
    dataframe_8var_select = dataframe_8var_select.drop(0)
    #dataframe_8var_select["Demanda FP (kW)", "Demanda P (kW)"] = dataframe_8var_select["Demanda FP (kW)","Demanda P (kW)"].astype(np.float64)
    #st.dataframe(dataframe_8var_select.info())
    dataframe_8var_select = dataframe_8var_select.drop(columns=['Data'])
    dataframe_8var_select = dataframe_8var_select.astype(np.float64)

    explicativas = dataframe_8var_select.drop(columns=['Demanda_FP_(kW)', 'Demanda_P_(kW)'])
    Demanda_FP = dataframe_8var_select.drop(columns=['Demanda_P_(kW)',
                                                    'Temperatura',
                                                     'Zona_do_Euro-PIB',
                                                     'Formação_Bruta_de_Capital_Fixo',
                                                     'Importações-preços-%vmmaa',
                                                     'IPCA_Brasil(%_ao_mês)',
                                                     'Taxa_de_juros-CDI',
                                                     'Câmbio(Real/Peso(Argentina))'])

    Demanda_P = dataframe_8var_select.drop(columns=['Demanda_FP_(kW)',
                                                     'Temperatura',
                                                     'Zona_do_Euro-PIB',
                                                     'Formação_Bruta_de_Capital_Fixo',
                                                     'Importações-preços-%vmmaa',
                                                     'IPCA_Brasil(%_ao_mês)',
                                                     'Taxa_de_juros-CDI',
                                                     'Câmbio(Real/Peso(Argentina))'])
    dataframe_8var_select.info()
    st.dataframe(dataframe_8var_select)




    from sklearn.linear_model import SGDRegressor
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn import svm, linear_model, neighbors, gaussian_process

    # contruindo o modelo de regreção por SGD (Stochastic Gradient Descent)
    # Standardscaler é usado para escalonar todos os valores entre -1 e 1

    modelo1 = make_pipeline(StandardScaler(), SGDRegressor(loss = 'epsilon_insensitive', tol = 1e-4))

    # modelo1 = make_pipeline(StandardScaler(), svm.SVR()) #0.81

    # modelo1 = make_pipeline(StandardScaler(), svm.NuSVR())  # 0.81

    # modelo1 = make_pipeline(StandardScaler(), linear_model.Ridge(alpha = .3)) #0.5794

    # modelo1 = make_pipeline(StandardScaler(), linear_model.Lasso(alpha = 0.2)) #0.57

    #  modelo1 = make_pipeline(StandardScaler(), neighbors.KNeighborsRegressor()) #0.9948

    # modelo1 = make_pipeline(StandardScaler(), gaussian_process.GaussianProcessRegressor())

    # treinando o modelo

    # YY = modelo1.fit(x_train, y_train.ravel())


    # %%----------------------- Implementando da regressão ----------------------------------

    from sklearn.neural_network import MLPRegressor
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    x_train = explicativas[:73]
    x_test = explicativas[73:]
    y_train = Demanda_FP[:73]
    y_test = Demanda_FP[73:]

    #st.dataframe(x_test)
    #st.dataframe(x_train)
    #st.dataframe(y_test)
    #st.dataframe(y_train)

    #modelo1 = make_pipeline(StandardScaler(), MLPRegressor())
    modelo2 = modelo1.fit(x_train, y_train)

    from sklearn import metrics
    T = range(0, 73, 1)



    # verificando a exatidão dos dados de treinamento
    SGD_predict_train = modelo2.predict(x_train)
    print('exatidão treinamento (accuracy): {0:.4f}'.format(metrics.r2_score(y_train, SGD_predict_train)))

    #verificando a exatidão dos dados de teste
    SGD_predict_test = modelo2.predict(x_test)
    print('exatidão teste (accuracy): {0:.4f}'.format(metrics.r2_score(y_test, SGD_predict_test)))

    plt.subplot(2,1,1)
    plt.plot(T, y_test, label = 'data')
    plt.legend()

    plt.subplot(2,1,2)
    plt.plot(T, SGD_predict_test, label = 'RNA')
    plt.legend()