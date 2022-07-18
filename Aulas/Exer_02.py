
#carregar um arquivo do disco rigido para memoria
#Funcao: eh uma sequencia de comandos
#Recebe uma entrada
#Devolve uma saida


# #mostra na tela as primeiras 6 linhas
# #print(data.head())
#
#
#
# #usar uma funcao que converte de OBJECT (string) -> date
# data['date'] = pd.to_datetime(data['date'])
#
#
#
# # ==========================================
# # Como converter os tipos de variaveis USANDO ~ASTYPE~
# # ===========================================
# # Inteiro -> Float
# #data['bedrooms'] = data['bedrooms'].astype(float)
#
# # Float -> Inteiro ( Sempre observar se o tamanho do espaco da memoria pra alocar a variavel sao os mesmos 32 ou 64 bits )
# #data['bedrooms'] = data['bedrooms'].astype(int64)
#
# # Inteiro -> String
# #data['bedrooms'] = data['bedrooms'].astype(str)
#
# # String -> Inteiro
# #data['bedrooms'] = data['bedrooms'].astype(int64)
#
# # String -> Date
# #data['date'] = pd.to_datetime(data['date'])
#
# #mostrar na tela os tipos de variaveis em cada coluna
# print(data.dtypes)
# #print(data[['id' , 'bedrooms']].head(3))
# ctrl + I + Barra -> comenta tudo com #


# # ==========================================
# # Criando novas variaveis
# # ===========================================

# data = pd.read_csv('datasets/kc_house_data.csv')
# data['nome_do_thiago'] = "thiago"
# data['comunidade_ds'] = 80
# data['data_abertura_comunidade_ds'] = pd.to_datetime('2020-02-22')
#
#
# # # ==========================================
# # # Deletando variaveis
# # # ===========================================
#
# cols = ['nome_do_thiago' , 'comunidade_ds' , 'data_abertura_comunidade_ds']
# data = data.drop( cols, axis = 1 )
# print(data.columns)
# #print(data[['id' , 'date' , 'nome_do_thiago', 'comunidade_ds' , 'data_abertura_comunidade_ds']].head())
#
#
#
# # # ==========================================================
# # # Selecao de Dados Forma 01: Direto pelo nome das colunas
# # # =============================================================
#
# data = pd.read_csv('datasets/kc_house_data.csv')
# #print(data[['price' , 'id' , 'date']])
#
#
# # # ==========================================================
# # # Selecao de Dados Forma 02: Pelos indices das linhas e colunas
# # # =============================================================
# # DADOS[ LINHAS (linha inicial : linha final) , COLUNAS (coluna inicial : coluna final) ]
#
# #print(data.iloc[0:5 , 0:3])
#
# # # ========================================================================
# # # Selecao de Dados Forma 03: Pelos indices das linhas e nome das colunas
# # # =============================================================================
# # OBS ILOC localiza pelo 'i'ndex o LOC localiza pelo nome das colunas
#
# #cols = ['id','date' , 'price']
# #print(data.loc[0:10 , cols])
#
# # # ========================================================================
# # # Selecao de Dados Forma 04: Indices Booleanos
# # # =============================================================================
#
# #cols = ['id','date' , 'price']
# #print(data.loc[0:10 , cols])
#
# cols = [True, False, True, True, False,False, False,False, False,False, False,False, False,False, False,False, False,False, False,False, False]
# print(data.loc[0:10 , cols])
#
#
#
# # # ========================================================================
# # # Respondendo as perguntas do negocio
# # # =============================================================================

#data = pd.read_csv( 'datasets/kc_house_data.csv')

# 1.Qual a data do imóvel mais antigo do portifólio?
#data['date'] = pd.to_datetime( data['date'])
#print(data.sort_values('date' , ascending=True))


# 2.Quantos imóveis possuem o número máximo de andares?

#print(data['floors'].unique())
#print(data[data['floors'] == 3.5  ].shape)

#data['floors'] = data['floors'].astype(int64)
#print(data.sort_values('floors' , ascending=True ))

#
# # 3.Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com o preço.
# #
# data['level'] = 'standard'
# #
# data.loc[data['price'] > 540000 , 'level'] = 'high_level'
# data.loc[data['price'] < 540000 , 'level'] = 'low_level'
# # print(data.head())
# #
# # #print(data.columns)
# # #print(data.head)
#
# # 4.Gostaria de um relatório ordenado pelo preço e contendo as seguintes informações:
#
#
# data['sqft_lot'] = data['sqft_lot'].astype(int64)
# data['date'] = pd.to_datetime(data['date'])
# data['sqft_lot'] = round(data['sqft_lot'] / 10.764 , 2)
# report = data[['id' , 'date' , 'price' , 'bedrooms' , 'sqft_lot' , 'level']].sort_values('price' , ascending=False)
#
# #print(report.head())
#
# #report.to_csv('datasets/report_aula02.csv', index=False )
#
# #print(data.dtypes)
#
#
# # 5.Gostaria de um Mapa indicando onde as casas estão localizadas geograficamente.
#
# # Plotly - Biblioteca que armazena uma funcao que desenha mapa
# # Scatter MapBox - Funcao que desenha um mapa


# import plotly.express as px
# data = pd.read_csv('datasets/kc_house_data.csv')
#
# data_mapa = data[['id' , 'lat' , 'long' , 'price']]
#
# mapa = px.scatter_mapbox(data_mapa, lat='lat' , lon='long', hover_name='id' , hover_data=['price'], color_discrete_sequence=['palegreen'], zoom=3 , height=3000 )
#
# mapa.update_layout(mapbox_style='open-street-map')
# mapa.update_layout(height=600 , margin={'r':0 , 't':0 , 'l':0 , 'b':0})
# mapa.show()
#
# mapa.write_html('datasets/mapa_house_rocket2.html')



# # # ========================================================================
# # # Exercicios Aula 02
# # # =============================================================================

#
# import pandas as pd
#
#
# # 1 - Crie uma nova coluna chamada: “house_age”
# # Se o valor da coluna “date” for maior do que 2014-01-01 -> “new_house”
# # Se o valor da coluna “date” for menor do que 2014-01-01 -> “old_house”
#
# data = pd.read_csv('datasets/kc_house_data.csv')
#
# # Idade das casas
# data['house_age'] = "new_house"
# data['date'] = pd.to_datetime(data['date'])
# data.loc[data['date'] > "2015-01-01" , 'house_age'] = 'new_house'
# data.loc[data['date'] < "2015-01-01" , 'house_age'] = 'old_house'
#
#
# # Quartos
# data['dormitory_type'] = "studio"
# data.loc[data['bedrooms'] == 2 , 'dormitory_type'] = 'apartment'
# data.loc[data['bedrooms'] > 2 , 'dormitory_type'] = 'house'
#
# # Condicoes do imovel
#
# data['condition_type'] = "regular"
# data.loc[data['condition'] <= 2 , 'condition_type'] = 'bad'
# data.loc[data['condition'] == 5 , 'condition_type'] = 'good'
#
# # Deletando as colunas SQFT_living e SQFT_LOT15
#
# cols = ['sqft_living15' , 'sqft_lot15']
# data = data.drop( cols, axis = 1 )

#Modifique o TIPO da coluna “yr_build” para DATE ERRO

#data['yr_built'] = pd.to_datetime(data['yr_built'])

#Modifique o TIPO da coluna “yr_renovated” para DATE ERRO

#data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])


# 10 Quantas casas tem mais de 2 andares??

#casas = data.query( 'floors == 2')['id'].count()
#print(casas)

# 11 Quantos imóveis estão com a condição igual a “regular”?

#casas = data.query( 'condition_type == "regular"')['id'].count()
#print(casas)


# 12 Quantos imóveis estão com a condição igual a “bad” e possuem “vista para o mar”?

#casas = data.query( 'condition_type == "bad" & waterfront == 1')['id'].count()

#print(casas)


#13 Quantos imóveis estão com a condição “good” e sao "new_house"?

#casas = data.query( 'condition_type == "good" & house_age == "new_house"')['id'].count()

#print(casas)

# 14 Qual o valor do imovel mais caro do tipo “studio” ?

#casas = data.query( 'dormitory_type == "studio"')
#print(casas.sort_values('price' , ascending=True))

#reportcasas = casas[['id' , 'date' , 'price' , 'bedrooms' ,'dormitory_type']].sort_values('price' , ascending=False)

#print(reportcasas.head())

#report.to_csv('datasets/reportcasas_aula02.csv', index=False )

# 15 Quantos imóveis do tipo “apartment” foram reformados em 2015?

#casas = data.query( 'dormitory_type == "apartment" & yr_renovated >= 01-01-2015')['id'].count()

#print(casas)
# casas = data.query( 'dormitory_type == "apartment" ')
# reportcasas = casas[['id' , 'date' , 'price' , 'yr_renovated' ,'dormitory_type']].sort_values('yr_renovated' , ascending=False)
#
# print(reportcasas)
# #print(reportcasas)

# 16 Qual o maior número de quartos de um imovel do tipo “house" possui?

# casas = data.query( 'dormitory_type == "house" ')
# reportcasas = casas[['id' , 'date' , 'price' , 'bedrooms' ,'dormitory_type']].sort_values('bedrooms' , ascending=False)
#
# print(reportcasas)

# 17 Quantos imóveis “new_house” foram reformados no ano de 2014?

#casas = data.query( 'house_age == "new_house" & yr_renovated == 2014 ')['id'].count()

#reportcasas = casas[['id' , 'date' , 'price' , 'yr_renovated' ,'house_age']].sort_values('yr_renovated' , ascending=False)
#print(casas)


# 18 Selecione as colunas: “id” , “date” , “price” , “floors” , “zipcode” pelo método:
# Direto pelo nome das colunas
# Pelos índices
# Pelos índices das linhas e o nome das colunas
# Índices Booleanos


# # # ==========================================================
# # # Selecao de Dados Forma 01: Direto pelo nome das colunas
# # # =============================================================

# data = pd.read_csv('datasets/kc_house_data.csv')
# print(data[['price' , 'id' , 'date' , 'floors', 'zipcode']])


# # # ==========================================================
# # # Selecao de Dados Forma 02: Pelos indices das linhas e colunas
# # # =============================================================
# # DADOS[ LINHAS (linha inicial : linha final) , COLUNAS (coluna inicial : coluna final) ]

#print(data.iloc[0:5 , 0:8])

# # # ========================================================================
# # # Selecao de Dados Forma 03: Pelos indices das linhas e nome das colunas
# # # =============================================================================
# # OBS ILOC localiza pelo 'i'ndex o LOC localiza pelo nome das colunas
#
#cols = ['id','date' , 'price' , 'zipcode' , 'floors']
#print(data.loc[0:10 , cols])
#
# # # ========================================================================
# # # Selecao de Dados Forma 04: Indices Booleanos
# # # =============================================================================
#
# #cols = ['id','date' , 'price']
# #print(data.loc[0:10 , cols])
#
#cols = [True, True, True, False, False,False, False,True, False,False, False,False, False,False, False,False, True,False, False,False, False, False]
#print(data.loc[0:10 , cols])
#print(data.columns)


# 19 Salve um arquivo .csv com somente as colunas do item 10 ao 17.
#
# report = data[['floors' , 'condition_type' , 'dormitory_type', 'house_age']]
# #print(report.head())
#
# report.to_csv('datasets/reportcasas_aula02_exer19.csv', index=False )







# #print(report.head())
#
# #report.to_csv('datasets/report_aula02.csv', index=False )
#
# #print(data.dtypes)




#print(data.head())
#print(data['dormitory_type'].unique())
#print(data[['price' , 'id' , 'dormitory_type']])
#print(data.sort_values('price' , ascending=False ))






#casas = data.query( 'dormitory_type == "apartment" ')
#cols = ['id','date' , 'price' , 'yr_renovated'].sort_values('yr_renovated' , ascending=True)


#print(data[['price' , 'id' , 'date']])
#print(data.sort_values('yr_renovated' , ascending=False ))


#print(data.columns)   4697
#print(data.dtypes)
#print(data.loc('yr_built'))

#cols = ['id','date' , 'price' , 'yr_built']
#print(data.loc[0:10 , cols])


#print(data.sort_values('condition_type' ))

#print(data.sort_values('floors' , ascending=True ))
#data['comunidade_ds'] = 80
#data['data_abertura_comunidade_ds'] = pd.to_datetime('2020-02-22')

