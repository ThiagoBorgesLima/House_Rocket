

#import statistics

import pandas as pd

data = pd.read_csv( 'datasets/kc_house_data.csv' )


#mostre na tela as 5 primeiras linhas do conjunto de dados
#print( data.head() )


#mostre na tela o numero de colunas e o numero de linhas do conjunto de dados
#print( data.shape )

#mostre na tela o nome das colunas do conjunto de dados
#print( data.columns )

#mostre na tela o conjunto de dados ordenados pela coluna price
#print( data[[ 'id' , 'price' , 'bedrooms' ]].sort_values( 'price' ) )

#mostre na tela o conjunto de dados ordenados do maior para o menor
#print( data[['id' , 'price']].sort_values( 'price' , ascending=False))

#mostre na tela a casa com maior numero de quartos
#print( data[[ 'id' , 'price' , 'bedrooms' ]].sort_values( 'bedrooms' ) )

#mostre na tela a soma total de quartos do conjunto de dados
#soma_de_valores = data[ 'bedrooms'].sum()
#print(soma_de_valores)


#mostre na tela a soma total de casas com dois banheiros COUNTIFS
#countif = data.query('bedrooms == 2')['id'].count()
#print(countif)

#soma dos valores totais das casas
#soma_valores = data['price'].count()
#print(soma_valores)

#valor medio das casas do conjunto
#mean_values = data['price'].mean()
#print(mean_values)

#exibe os tipos de dados do conjunto
#print(data.dtypes)

#mostre na tela a soma total de casas com dois banheiros COUNTIFS
#meanif = data.query('bedrooms == 2')['price']
#x = statistics.mean(meanif)

#print(x)


#mostre na tela o preco minimo entre casas com 3 quartos
#minvalue = data.query('bedrooms == 3')['price']
#x = min(minvalue)
#print (x)

#quantas casas posssuem mais de 300 metross quadrados
#casas = data.query( 'sqft_lot > 3229')['id'].count()

#print(casas)


#quantas casas tem mais de 2 andares
#casas = data.query( 'floors > 2')['id'].count()
#print(casas)

#quantas casas tem vista para o mar
#casas = data.query('waterfront == 1')['id'].count()
#print(casas)

# quantas casas tem vista para o mar e 3 quartos
#countif = data.query(' waterfront ==1 & bedrooms > 3')['id'].count()
#print(countif)

#mais de 300 metros de sala de estar tem dois banheiros

#countif = data.query('sqft_living > 3229 & bathrooms == 2')['id'].count()
#print(countif)
