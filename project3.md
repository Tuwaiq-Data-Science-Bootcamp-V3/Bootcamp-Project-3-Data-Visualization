# Riyadh Villas Aqar

Team members: Nourah Almuhaisen, Sarah Alyami and Zainab Melaibari.

<img width="1000" height="500" src="https://github.com/isazHfc/Bootcamp-Project-3-Data-Visualization/blob/main/Riyadh%20Villas%20Aqar.png">

## Problem Statement

The objective of this project is to analyze the "Riyadh Villas Aqar" dataset and gain insights into the real estate market of Riyadh, Saudi Arabia. The problem at hand is to explore and understand the factors that influence villa prices and property features in Riyadh. 

## Objectives

1- Analyze the distribution of villa prices across different neighborhoods in Riyadh to identify areas with higher or lower property values.

2- Examine the effect of property age on villa prices by categorizing the properties into age groups and identifying any trends or preferences among buyers.

3- Identify the most common property features in Riyadh villas, such as pool, garage, furnished status, and others, to understand the prevalent amenities offered in the market.

4- Determine any notable differences or patterns in villa prices and property features across different neighborhoods to identify areas with unique market characteristics.

5- Visualize the data through charts and graphs to provide a clear representation of the villa market in Riyadh, allowing stakeholders to easily comprehend the findings and make informed decisions.

6- Contribute to the understanding of the real estate market in Riyadh by uncovering trends, patterns, and factors influencing villa prices, thereby assisting in the overall development and growth of the real estate sector in the city.

## Dataset

### Dataset Source:

We used The Riyadh Villas Aqar from kaggle [Click here to access the dataset](https://www.kaggle.com/datasets/reemamuhammed/riyadh-villas-aqar).

### Dataset Overview:

The dataset provides information about various villas in different neighborhoods, including features such as the number of rooms, bathrooms, property age, property features (e.g., pool, garage, furnished), and other details.

## Data Cleaning

1- During the data cleaning process, we conducted several crucial exploratory data analysis (EDA) steps to understand the dataset and ensure its quality and consistency. These steps comprised:

- Head: We examined the initial rows of the dataset using the `head()` function to get a glimpse of the data.

- Shape: By accessing the `shape` attribute, we determined the dimensions of the dataset, which provided the number of rows and columns.

- Info: The `info()` function allowed us to obtain a summary of the dataset's structure, including the data types of each column and the number of non-null values.

- Describe: To gain insights into the distribution and statistical measures of the dataset, we utilized the `describe()` function, which generated descriptive statistics such as count, mean, standard deviation, minimum, quartiles, and maximum values for numerical columns.

By performing these EDA steps, we were able to assess the dataset's content, identify any potential issues, and prepare it for further analysis and modeling.

2- Regarding duplicated rows, after a thorough examination, we determined that the dataset does not contain any duplicated rows. We conducted a check using the `duplicated()` function, which confirmed that there were no exact duplicates within the dataset. Therefore, we can proceed with the analysis and further processing of the data, confident that each row is unique and representative of a distinct observation.

3- We encountered missing data in four columns: lounges, streetWidth, price, and square price. To address this issue, we employed various methods to process the missing data separately for each column. Our approach involved utilizing mean(), median(), mode(), ffill(), and bfill() techniques.

- For every column, we implemented different methods to handle the missing data. Subsequently, we calculated the variance for each column both before and after filling in the missing values. This allowed us to compare the variances and determine the most suitable method for each column. We selected the method that resulted in the closest variance between the original and filled data.

- In the case of the lounges column, we opted to use the ffill() method to fill in the missing data.

- To handle the missing data in the 'streetWidth' column, we followed a specific procedure. First, we utilized the `groupby()` function to compute the median 'streetWidth' value for each neighborhood, storing the results in the `mean_salaries` variable. This allowed us to determine the typical street width for each locality. Next, we identified the neighborhoods that had missing values in the 'streetWidth' column and stored them in the `null_neighbourhood` variable. We needed this information to focus on the specific neighborhoods where data imputation was required. Subsequently, we initiated a loop to iterate through each neighborhood with missing values. Within this loop, we replaced the null values in the 'streetWidth' column with the corresponding mean value that was calculated specifically for that particular neighborhood. By employing this process, we were able to fill in the missing data in the 'streetWidth' column using neighborhood-specific mean values.

- To handle missing values in the 'price' column, we applied a specific method. We used a lambda function, denoted as `meanPrice`, to calculate the mean value of the 'price' column. This lambda function was then applied to the 'price' column within each neighborhood group using the `groupby()` function. The resulting mean values were used to fill in the missing values in the 'price' column. Then the missing values in the 'price' column were replaced with the mean values computed for each neighborhood group, ensuring a more accurate representation of the missing data.

- To handle missing values in the 'square_price' column, we utilized two specific code snippets. First, we renamed the column from 'square price' to 'square_price' using the `rename()` function. This ensured consistency and ease of reference within the dataframe. Next, we defined a custom function named `squrePrice()` that calculates the square price for each row by dividing the 'price' by the 'space' values. We then applied this function to the 'square_price' column using the `apply()` function with `axis=1` to perform the calculation row-wise. The resulting square price values were used to fill in the missing values in the 'square_price' column.

## The final ten insights

### Dashboard 1 insights :

- This dashboard analysis allows users to explore the relationship between space and prices, compare neighborhoods, and understand the distribution of front types within a specific location. These insights can aid in decision-making processes related to property investments, market analysis, and understanding local preferences.

1- How does the price vary with the increase in space for the selected neighborhood?

The analysis provides a neighborhood-wise comparison considering the relationship between Space and Prices. It helps identify any variations in villa prices based on location preferences, amenities, or other factors. Potential buyers or investors can utilize this information to make informed decisions by considering both the size of the villas and their corresponding prices in different neighborhoods.
The scatter chart in the dashboard allows users to analyze the relationship between the space (area) and prices of villas in different neighborhoods within a specific location. Users can select a location and compare the prices of villas based on their sizes in various neighborhoods.

2- What is the count of each type of front in the selected area?

The bar chart in the dashboard displays the count of each front type (e.g., front facing north, south, east, west) in the selected area. Users can choose a location and a neighborhood to view the distribution of different front types in that specific area. This analysis can help identify any prevailing front preferences in certain neighborhoods, which may have an impact on property values or desirability. It provides insights into the diversity or dominance of certain front types in a given area.

### Dashboard 2 insights :
 
- This dashboard analysis provides insights into the distribution of villa properties based on category and location, enabling users to make data-driven decisions related to investment, market analysis, and property selection.
 
1- How does the count of villas in different locations vary across villa space categories?
The dashboard allows users to select a villa category (such as Small Villas, Medium Villas, etc.) and visualize the distribution of properties in that category across different locations. By selecting a specific category from the dropdown menu, users can see the proportion of villas in each location through a pie chart. This insight can help identify the most popular locations for each villa category and provide an understanding of the market demand in different areas.
 
2- What is the count of villas in each neighborhood within the selected location ?
In addition to the property count by location, the dashboard also provides a bar chart that displays the count of villas in each neighborhood. This insight allows users to explore the distribution of villas within a selected villa category and analyze the popularity of different neighborhoods. By interacting with the pie chart and selecting a specific location, users can see a more detailed breakdown of the villa count by neighborhood. This information can be valuable for investors or buyers looking for specific neighborhoods with a higher concentration of villas in their desired villa category.
  
### Dashboard 3 insights :

1- What is the distribution of villas in neighborhoods based on the selected criteria (number of rooms, bathrooms, pool, furnished status, garage, duplex, driver room, and maid room)?

The dashboard allows users to explore and gain insights into villa features and their distribution across neighborhoods in Riyadh. These insights can help inform decision-making processes, such as choosing a villa with desired features or understanding market trends in the housing sector.
 
### Dashboard 4 insights :

- This dashboard provides a user-friendly interface to explore the age categories of villas in Riyadh, visualize their distribution across neighborhoods, and understand the popularity of different property features. It empowers users with valuable insights into the real estate market, enabling them to make informed decisions and stay updated with the latest market trends.
 
1- What is the distribution of villas each neighborhoods within the selected age category?
The dashboard allows users to explore the distribution of villas based on their age categories, which provides valuable insights into the real estate market in Riyadh. Users can understand the demand for different age categories of villas and how they are distributed across neighborhoods. This information can help potential buyers or investors in making informed decisions about where to invest or which age category suits their preferences.
 
2- What is the count of each feature for the selected property age category ?
The dashboard also highlights the popular property features among the selected age category of villas. By analyzing the property features count graph, users can identify which features are most commonly found in villas of a particular age category. This information is useful for understanding the market trends and preferences of buyers. It can help individuals in deciding which property features are in high demand and potentially influence their own purchasing decisions or investment strategies.

### General insights :

- Providing a comprehensive understanding of the real estate market in Riyad.
 
- What are the factors that affect the price in Riyadh villas ?  
 
1- From the heatmap, we can observe that there is a positive correlation between 'price' and 'space'. This indicates that as the space of a property increases, the price tends to be higher. Similarly, there is a positive correlation between 'price' and 'rooms', suggesting that properties with more rooms generally have higher prices.
 
2- The scatter plot visualizes the relationship between 'space' and 'price', with each data point colored according to the number of 'rooms'. This plot helps us understand how these variables interact with each other and how they affect the price of a property. We can see that as the space of a property increases, the price tends to increase as well. Additionally, different colors represent different numbers of rooms, providing additional information about the number of rooms associated with each data point. This allows us to observe any potential patterns or clusters in the data.
 
- What are the top 5 property features in Riyadh villas?  
 
3- The bar plot displays the top 5 property features in Riyadh villas based on their counts. The features include 'driverRoom', 'patio', 'garage', 'outdoorRoom', and 'tent'. The plot shows the count of each property feature, allowing us to identify the most common features found in Riyadh villas. This information can be useful for understanding the preferences and trends in the real estate market.
