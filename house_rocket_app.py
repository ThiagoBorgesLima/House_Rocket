import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config( layout='wide')

def get_data( path ):
    data = pd.read_csv( path )

    return data

st.title( 'House Rocket Company' )

st.markdown( 'Welcome to House Rocket Data Analysys')


# ETL

# Data Extraction
path = 'datasets/kc_house_data.csv'

data = get_data( path )

############################
# Transform

# Load

############################

# 1 Quais são os imóveis que a House Rocket deveria comprar e por qual preço?
st.header( '1.0 Should Buy Numbers')

df_median = data[['zipcode', 'price']].groupby('zipcode').median().reset_index()
df = pd.merge( data, df_median, on='zipcode', how='inner', suffixes=("","_median") )


for i in range( len( data )):
      if (df.loc[i, 'price'] < df.loc[i,'price_median']) & (df.loc[i, 'condition'] > 2):
          df.loc[i,'status'] = 'Buy'

      else:
          df.loc[i,'status'] = 'Do not Buy'

count = df[['id','status']].groupby('status').count()

st.write(count)
st.header('1.1 Buy Data')
st.write(df[['id','price', 'price_median', 'condition', 'status']])


# 2 Uma vez o imóvel comprado, qual o melhor momento para vendê-lo e por qual preço?

st.header('2.0 Should Sell In:')

df2 = data
df2['season'] = 'NA'
df2['sell_price'] = 'NA'
df2['profit'] = 'NA'
df2['month'] = pd.to_datetime(df2['date']).dt.month

# condicoes de sazonalidade USA
# spring runs from March(03) 1 to May(05) 31;
# summer runs from June(06) 1 to August(08) 31;
# fall(09) (autumn) runs from September 1 to November(11) 30; and
# winter runs from December(12) 1 to February(02) 28

for i in range( len( df ) ):
    if (df2.loc[i, 'month'] >= 3) & (df2.loc[i, 'month'] <= 5):
        df2.loc[i, 'season'] = 'spring'
    if (df2.loc[i, 'month'] >= 6) & (df2.loc[i, 'month'] <= 8):
        df2.loc[i, 'season'] = 'summer'
    if (df2.loc[i, 'month'] >= 9) & (df2.loc[i, 'month'] <= 11):
        df2.loc[i, 'season'] = 'fall'
    if (df2.loc[i, 'month'] <= 2):
        df2.loc[i, 'season'] = 'winter'
    if (df2.loc[i, 'month'] == 12):
        df2.loc[i, 'season'] = 'winter'

df_season = data[['price', 'season','zipcode']].groupby(['zipcode',
                                                         'season']).median().reset_index()

df2 = pd.merge(data, df_season, on=["zipcode", "season"], how='inner', suffixes=("","_median"))


for i in range( len( df ) ):
    if (df2.loc[i, 'price'] > df2.loc[i, 'price_median']):
        df2.loc[i, 'sell_price'] = df2.loc[i, 'price'] * 1.1
        df2.loc[i, 'profit'] = df2.loc[i, 'sell_price'] - df2.loc[i, 'price']

    else:
        df2.loc[i, 'sell_price'] = df2.loc[i, 'price'] * 1.3
        df2.loc[i, 'profit'] = df2.loc[i, 'sell_price'] - df2.loc[i, 'price']


st.markdown('ZIPCODE x PRICE per Season')
st.write(df_season)
st.write(df2[['price','zipcode', 'season', 'sell_price', 'price_median', 'profit']])


# 3 Imóveis que possuem vista para água, são 30% ( baseline ) mais caros na média.

st.header('3.0 Waterfront Price Info:')
df3 = data[['price', 'waterfront']].groupby('waterfront').mean().reset_index()

if df3.loc[0, 'price'] < df3.loc[1, 'price']:
    st.write('Waterfront more expensive')
    df3_sum = (df3.loc[1, 'price'] / df3.loc[0, 'price']) * 100

else:
    st.write('No Waterfront more expensive')
    df3_sum = ( ( df3.loc[0, 'price'] / df3.loc[1, 'price'] ) * 100 )

st.write(df3)
st.write('Price relation of waterfront or no waterfront: ',df3_sum,'%')

# 4 Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.

st.header('4.0 Year Built < 1955 price overview:')
df4_down = data.query('yr_built < 1955')
df4_down_mean = df4_down['price'].mean()
st.write('Year Built < 1955 Price mean:', df4_down_mean)


df4_up = data.query('yr_built > 1955')
df4_up_mean = df4_up['price'].mean()
st.write('Year Built > 1955 Price mean:',df4_up_mean)

df4 = (( df4_up_mean / df4_down_mean ) - 1) * 100
st.write('Properties Price Relation:', df4,'%')
# Resposta -  Os imoveis com data de construcao apos 1955 sao 1,1% mais caros que os construidos antes de 1955


# 5 Imóveis sem porão possuem área total (sqft_lot), são 40% maiores que os imóveis com porão.
#sqft_lot
#sqft_basement

st.header('5.0 Properties with basement:')
df5_basement = data.query( 'sqft_basement != 0')
df5_basement_mean = df5_basement['sqft_lot'].mean()

df5_nobasement = data.query( 'sqft_basement == 0')
df5_nobasement_mean = df5_nobasement['sqft_lot'].mean()

df5 = ( ( df5_nobasement_mean / df5_basement_mean )  - 1 ) * 100

st.write('Properties with Basement mean:',df5_basement_mean)
st.write('Properties with No Basement mean:',df5_nobasement_mean)
st.write('Relation of Prices of properties:',df5,'%')

# Resposta - Os imoveis sem porao sao 22% maiores que os imoveis com porao


# 6 O crescimento do preço dos imóveis YoY ( Year over Year ) é de 10%.

st.header('6.0 Properties Price Relation ( Year over Year ):')
df6 = data[['price', 'yr_built']].groupby('yr_built').mean().reset_index()

# Plot

fig = px.line( df6, x='yr_built', y='price' )
st.plotly_chart( fig, use_container_width=True )



# 7 Imóveis com 3 banheiros tem um crescimento de MoM ( Month over Month ) de 15%.

st.header('7.0 Price of Properties with 3 Bathrooms ( Month over Month ):')
data['date'] = pd.to_datetime(data['date'])
df7_3 = data.query( 'bathrooms == 3' )[['price', 'date']]

st.markdown('Average Price x Sell Date of Properties with 3 bathrooms:')
fig = px.histogram( df7_3, x='date', y='price', nbins=50, opacity=0.6, histfunc="avg", text_auto=True )
st.plotly_chart( fig, use_container_width=True )

df7 = data[['price', 'bathrooms']].groupby('bathrooms').mean().reset_index()

st.markdown('Mean Price x Number os Bathrooms:')
fig = px.line( df7, x='bathrooms', y='price' )
st.plotly_chart( fig, use_container_width=True )


# 8 Os imóveis mais valorizados em função do tempo são os que possuem dois banheiros.

st.header('8.0 Properties Price with 1, 2 and 3 bathrooms:')
data['date'] = pd.to_datetime(data['date'])
df8_1 = data.query( 'bathrooms == 1' )[['price', 'yr_built']]
df8_2 = data.query( 'bathrooms == 2' )[['price', 'yr_built']]
df8_3 = data.query( 'bathrooms == 3' )[['price', 'yr_built']]

st.markdown('Sum of Properties Prices with 1 Bathroom x Year Built:')
fig1 = px.histogram( df8_1, x='yr_built', y='price', nbins=30 )
st.plotly_chart( fig1, use_container_width=True )

st.markdown('Sum of Properties Prices with 2 Bathroom x Year Built:')
fig2 = px.histogram( df8_2, x='yr_built', y='price', nbins=30 )
st.plotly_chart( fig2, use_container_width=True )

st.markdown('Sum of Properties Prices with 3 Bathroom x Year Built:')
fig3 = px.histogram( df8_3, x='yr_built', y='price', nbins=30 )
st.plotly_chart( fig3, use_container_width=True )
st.write('Properties with 3 bathrooms gained some value during years, and we can see that properties with one bathroom just devalued ')
#Resposta - Os imóveis com tres  banheiros estao atualmente bem valorizados em funcao dos outros alcancando os maiores
#valores medios de preco de venda, os imoveis com 1 banheiro despencaram o preco nos ultimos anos e os com dois banheiros se
# mantem em uma certa constancia na media.


# 9. Os imóveis reformados estão em regiões (zipcode) que os imóveis se valorizaram ao longo dos anos.

st.header('9.0 Properties reformated gained some value during years?')
df9_query = data.query('yr_renovated != 0')
df9 = df9_query[['zipcode','price']].groupby('zipcode').mean().reset_index(())
st.write('Price Mean per ZIPCODE:')
st.write(df9)

st.write('Sum of Price for Renovated Properties over years:')
fig = px.histogram( df9_query, x='yr_built', y='price', nbins=30 )
st.plotly_chart( fig, use_container_width=True )

#filter
f_zipcode = str(st.selectbox('Enter Zip Code', data['zipcode'].unique()))

st.write(f'Price valorization over years for ZIPCODE {f_zipcode} of renovated Properties:')
df9_query2 = df9_query.query(f"zipcode == {f_zipcode}")

fig2 = px.scatter( df9_query2, x='yr_built', y='price' )
st.plotly_chart( fig2, use_container_width=True )





#Resposta - com o passar dos anos, as reformas diminuiram devido as condicoes dos imoveis, adicionar um botao
# para escolher atraves de um ZIPCODE o grafico dos precos em funcao do tempo, determinando se houve ou não valorizacao da determinada area


# 10. Vale a pena investir na reforma das casas em condições ruins para vendê-las depois.

st.header('10.0 We should buy bad conditions properties to renove and sell?')
df10_zip = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()

st.write('Price Mean per ZIPCODE:')
st.write(df10_zip)

df10 = data.query( 'condition <= 2')


df10_merge = pd.merge( df10, df10_zip, on='zipcode', how='inner', suffixes=("", "_mean") )

df10_merge['price_ref'] = 'NA'

for i in range( len( df10 )):
    df10_merge.loc[i, 'price_ref'] = ( ( df10_merge.loc[i, 'price'] - df10_merge.loc[i, 'price_mean'] ) / df10_merge.loc[i, 'price'] ) * 100

st.markdown('Properties Analises to buy/renove and sell:')
st.write(df10_merge[['price', 'zipcode', 'price_mean','condition', 'price_ref']])


# Resposta - caso o valor de compra da casa em condicoes ruins seja bem abaixo do valor de preco medio da regiao, talvez seja interessante
# investir no imovel, realizar uma reforma e depois vende-lo.

