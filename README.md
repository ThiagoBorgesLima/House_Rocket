# House Sales  
<p align="center">
  <img src="imgs/house1.jpg" height="600" width="1000"/>
</p>

<p align="center">
App: https://teste-rocket-1.herokuapp.com
</p>



# Business Question
<b>The data below, as well as its context, is completely fictitious and this is an Insights Project based on the Community DS.</b>

House Rocket's CEO would like to maximize the company's revenue by finding good business opportunities. Your main strategy is to buy good properties in great locations at low prices and then resell them later at higher prices. The greater the difference between buying and selling, the greater the company's profit and therefore the greater its revenue. However, properties have many attributes that make them more or less attractive to buyers and sellers, and location and time of year can also influence prices.

So, in this project, the objective is to analyze the real estate data and help the CEO to maximize the company's profits by answering the questions below:
<b> 

- What are the properties that HR should buy and at what price??

- Once the property has been purchased, what is the best time to sell it and at what price??

- Should House Rocket do a renovation to increase the sale price? What would be the suggestions for changes? What is the price increase given for each refurbishment option?</b> 

# Business Assumptions
- It will be considered in this project that YoY real estate sales in the US increased in the years 2010 - 2020 and that real estate sales below 200,000 fell and those of 400,000 and above rose. 
<p align="center">
  <img src="imgs/usa_sales.png" height="400" width="500"/>
</p>

- As for the renovation of the property or not, it will be taken into account the fact that a renovation can increase the value of a property by 30%. [3] 

# Solution Strategy

The final product will be 3 Reports in .csv:
- Report with apartment purchase suggestions for a recommended value;
- Report with suggestions for selling a property for a recommended value;
- Report with suggestion for reform.

## Tools 
 <p>
  <ul>
    <li><a href="https://www.python.org/">Python 3.9</a></li>
    <li><a href="https://jupyter.org/">Jupyter Notebook</a></li>
    <li>CRISP-DS Management Method</li>
  </ul>
 </p>

## Procedure

### <b>What properties should HR buy and at what price?</b>
To answer this question the following steps will be followed:

- Collect data in Kaggle [1];
- Group data by region (zipcode);
- Within each region, find the median property price.
- Suggest that properties that are below the average price for each region and that are in good condition (condition) be purchased.

With this, it will be possible to assess the supply and demand for properties by region, a factor that can influence the property's valuation. 

### <b>Once the property has been purchased, when is the best time to sell it and at what price?</b>

The objective will be to evaluate in which season of the year the properties are cheaper.
As the data has already been processed and organized...
- Group properties by region (zipcode) and by seasonality (seasons of the year)
- Calculate the median price in each region and seasonality
- Sale conditions:
  - 1 - if the purchase price is greater than the regional median + seasonality, then: the sale price will be equal to the purchase price + 10%;
  - 2 - if the purchase price is less than the regional median + seasonality, then: the sale price will be equal to the purchase price + 30%

### <b>Should House Rocket do a renovation to raise the sale price? What would be the suggestions for changes? What is the price increase given for each refurbishment option?</b>
In this case, only properties that were not recommended for purchase will be selected, that is, we will simulate whether with the renovation it would become suitable for purchase or not, following the conditions: 

- The property will be renovated if its condition is 3 or 4 and the profit percentage is 10%
  - the renovation of the living room and bathrooms will be recommended, and a 10% increase in the property's sale value.

# Key Business Insights

Through exploratory data analysis, we acquired some business insights, which are as follows:

- <b>“Properties that overlook the water are 30% more expensive, on average.”<p>False:</b> Houses with a view of the water are 150% more expensive.</p>


- <b>“Properties with a construction date less than 1955 are 50% cheaper, on average.”<p>False:</b> Properties with a construction date less than 1955 are 5% cheaper.</p>


- <b>“Properties that have 3 bathrooms are 30% more expensive, on average.”<p>False:</b> Compared to properties with 1 or 2 bathrooms, the price is 50% higher. It is possible to observe that properties with more than 3 bathrooms have a very high (average) price.</p>


- <b>“Properties that have 2 bathrooms, have a good valorization during the years, on average.<p>False:</b> Properties with three bathrooms are currently well valued due to others reaching the highest average sales price values, properties with 1 bathroom have plummeted in price in recent years and those with two bathrooms have
maintains a certain constancy in the media. </p>

- <b>“The renovated properties are in regions (zipcode) that the properties have appreciated over the years.”<p>Need more Options:</b> Over the years, the renovations have decreased due to the conditions of the properties, add a button to choose, through a ZIPCODE, the graph of prices as a function of time, determining whether or not there has been an increase in the value of the given area. </p>

- <b>The attributes of the property that most influence the price are: bathrooms, living rooms (sqft_living) and the property's size separated from the basement (sqft_above):</b>
<p align="center">
  <img src="imgs/correlation.png"/>
</p>

# Financial Results

With the suggestion to purchase only properties that are below the average price in the region and are in good condition, House Rocket stops buying overvalued properties and in bad conditions that would probably not be sold easily, and may even undergo a renovation, which would increase even more the cost.

As can be seen in the item "Procedure" of this article, a sale rule was created for the properties that 'House Rocket' would buy along with the price.

Again, following what was defined in “Procedure”, a report was made available that informs whether the property should be renewed if the percentage of its profit is 10%.

**1 - Total investment price for the purchase:**

 - The sum of the sums of house prices for purchase is $3490407741.0.
 
 
**2 - Sum of houses by condition and total sum of renovation cost:** 

- Sum of house prices with bad conditions $42237511.0, and sum of cost to renovate $8451462

- Sum of house prices with good conditions $223056167.0

- Sum of house prices with regular conditions $3225314563.0, and sum of cost to renovate $375863411.56.

 

**3 - Sales Result:** 

- *Houses with bad conditions will have 10% added at the end for sale.*

- *Houses with regular conditions will have 15% added at the end of the sale.*

- *Houses with good conditions will have 20% added at the end for sale.*
 
<b>- Profit from sales of 10902 homes is $582.541.205,2.</b>


# Conclusion

At the end of this project it was possible to reach a very good number for maximizing the profits of 'House Rocket', the CEO now has in hand which houses should buy or not, the sale price and whether or not they need a renovation, being thus it is correct to say that the main objective of this project was successfully achieved.

<p align="center">
  <img src="imgs/map.png" height="500" width="800"/>
</p>


# Next Steps

The next steps for this project would be to create a classification for the properties, for example: if the property was an urban or rural property, if it is a house, an apartment, a studio. This would be possible by evaluating its attributes, for example, the number of bathrooms, the number of floors, whether it has a basement or not, among others.


<p align="center">
  <img src="imgs/app.png" height="600" width="1000"/>
</p>



<p align="center">
App: https://teste-rocket-1.herokuapp.com
</p>

# References

House Sales in King County, USA. <b>Kaggle</b>. Available in:
<https://www.kaggle.com/harlfoxem/housesalesprediction>.

Comunidade DS “Seja um DataScientist - Meigarom”. Available in: <https://www.comunidadedatascience.com/>



# Author

Thiago Borges Lima


[<img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>](https://www.linkedin.com/in/thiago-borges-lima-a731115b)
