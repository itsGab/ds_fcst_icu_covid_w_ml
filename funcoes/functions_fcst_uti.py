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
