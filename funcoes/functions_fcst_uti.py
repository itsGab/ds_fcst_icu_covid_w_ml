def remove_space(col):
    '''
    funcao que substitui espaco por underline (underscore).
    '''
    if ' ' in col:
        col = col.replace(' ', '_')
    return col


def prepara_primeira_janela(df_agrupado):
    '''
    prepara a primeira janela, caso o paciente tenha ido em algum
    momento para a UTI
    '''
    if any(df_agrupado['ICU']):
        linha = df_agrupado.loc[df_agrupado['WINDOW'] ==  '0-2', 'ICU'] = 1
    return linha


def remove_corr_var(dados, valor_corte):
    '''
    funcao para remover colunas com variaveis com correlacao
    '''
    matrix_corr = dados.iloc[:, 12:-11].corr().abs()
    matrix_upper = matrix_corr.where(np.triu(np.ones(matrix_corr.shape), k=1).astype(np.bool))
    excluir = [coluna for coluna in matrix_upper.columns if any(matrix_upper[coluna] > valor_corte)]

    return dados.drop(excluir, axis=1), excluir

def rem_cols_zero_std(df):
    '''
    removendo colunas que nao sofrem alteracao
    '''
    no_alt_cols = []
    temp_describe = df.query('window == "0-2"').describe(include='all')
    for col in df.columns:
        if temp_describe.loc['std', col] == 0:
            no_alt_cols.append(col)
    clean_df = df.drop(no_alt_cols, axis=1)
    return clean_df

def semente(padrao=73246):
    '''
    utilizando como seed padrao
    '''
    np.random.seed(padrao)

def roda_modelo(modelo, X, y, mostra=False):
    '''
    funcao que roda os modelos
    '''
    conta = 0
    semente()
    if conta <= 0:
        X_train, X_test, y_train, y_test = train_test_split(X, y)
    y_pred = modelo.fit(X_train, y_train).predict(X_test)
    conta += 1
    if mostra == True:
        print(15* '-----')
        print(modelo.__module__)
        print(15* '-----')
        print(classification_report(y_test, y_pred))
        print(15* '_____', '\n')
    return accuracy_score(y_test, y_pred)
