
# Tuwaiq Data Science Bootcamp-v3 

## Project 3
- Essa Alhamad
- Lama Alshabani
- Fai Alamri

## Riyadh Real Estate Data Analysis

Many people move to Ryiadh since it is the city of oppurtonities for anyone aspiring to acheive more in their careers. We used "RiyadhVillasAqar.csv" dataset made by Reema Muhammed in kaggle to check the best region to live in
based on different situations. Our data had some ambigous values such as having some bathroom and lounge entries as '5+' or '7+' so we modified it to take raw numbers only since
it is not optimal to give imaginary values to them. We dropped "unnamed: 0" column and fixed the spelling on the "furnished" column. We found some missing values on our data set and we
dealt with them by:

- Filling the "square price" and "price" values by the mean since there were only 2 missing values.
- Filling the "lounges" column with it's mean.
- Implementing forward filling on the "streetWidth" column.

We futher cleaned the data by turning our numerical columns into integers specifically since rooms can not have float values. Furthermore, we initialized a new column called "total rooms" which is the sum of all the rooms columns.
Lastly, we changed some of the columns that were catogerized as "0.0" and "1.0" into arabic cateegories to fit our analysis better.

Our analysis process consists of two segments.

### Insights on all regions:
- What are the most populated regions?
- What are the most expensive regions?
- How vast spaces are in each region?
- What is the total number of rooms in each region?
- What is the most common street width in each region?

### Insights on the most populated region:
- What are the most common fronts in the chosen region?
- What is the correlation between the property's age and it's square price?
- How much effect does the number of rooms have on the price?
- How many apartments are furnished in the chosen region?
- Does price and square price have the same effect on space?

### What are the most populated regions in Riyadh?

We wanted to know which region has the most residents in Riyadh so we displayed the results as a Histogram.

![newplot (4)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/76b61db1-8653-42ac-a286-723812c9f0df)

After Displaying the chart, we concluded that the west region has the most residents in Riyadh.

### What are the most expensive regions in Riyadh?

Every person has their own budget where they need to choose the residence that best fits their budget which is why we displayed how expensive each region is by displaying the results in a pie chart.

![newplot (5)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/b8e8954a-d948-447a-a51c-e25dbbdba1dd)

We can confirm that the north region is the most expensive region followed by the east region, the west region, the south region, and the downtown region.

### What is the total number of rooms in each region?

We made a Box chart to display the total number of rooms in each region.

![newplot (6)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/43492969-c098-464e-aabd-f31bb2b644cb)

Most regions are ranging from three to twenty room but the east region is the only one with an apartment of twenty two rooms.

### How vast spaces are in each region?

We wanted to see how much space each region have by using an area chart.

![newplot (7)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/56b15387-9dc1-4391-8b64-c991fd4b5f4e)

We conclude that the north region has the most space followed by the west, east, downtown, and the south region.

### What is the most common street width in each region?

To know the most used street widths in Riyadh, we plotted a violin chart to see the results clearly.

![newplot (8)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/6e47f5f3-54c5-449a-9b4e-bf871f3f39e7)

The most used street width by a small margin is fifteen, then twenty.

###After inspecting every region in Riyadh, we decided it is best to choose the west region for further inspection due to the number of entries this region has and it's affordability.

### What are the most common fronts in the chosen region?

To get an idea on how most apartments in the west region are placed, we need to check the most common fronts in that region by using a Boxplot.

![newplot (9)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/f11d97c6-0472-4ac6-952c-fee31f282b68)

We discover that the most used fronts are north, south, and east fronts

### What is the correlation between the property's age and it's square price?

Does the property's age affect the west region's square price negatively or positively? Too see the type of effect we made a scatter plot to answer our question.

![newplot (10)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/6933d56c-c986-423a-9ebb-cc3b4f706708)

generally, the propertyage does affect the square price negatively.

### How much effect does the number of rooms have on the price?

We Wanted to display the correlation between the number of rooms and the price by plotting an area chart.

![newplot (11)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/3843113d-e603-4584-a5d1-1f31bac759a8)

We can see the difference in price is not as huge with more rooms but could start spiking greatly from ten rooms and more.

### How many apartments are furnished in the chosen region?

Depending on the reason for moving to Riyadh, some people might want their apartment to be already furnished and others would like to start furnishing themselves. We displayed the amounf of furnished and non furnished apartments
in the west region by using a pie chart.

![newplot (12)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/dd6bc544-63f9-4c56-9cd9-730e24e94fa0)

As we can see, 88% of the apartment are not furnished so it is more suitable for people who want to settle in Riyadh.

### Does price and square price have the same effect on space?

Price and square price have a strong positive correlation with each other but do they affect space in the west region the same way? We did two scatter plots to display the effect they have on space.

![newplot (13)](https://github.com/LamaAlshabani/Bootcamp-Project-3-Data-Visualization/assets/85634276/ebd7a8f2-5842-41ae-a59c-37505b66b892)

As we can see, the square price have a negative effect on space but the price have a positive effect.

 Finally, we made dashboard to make our figures interactive.



