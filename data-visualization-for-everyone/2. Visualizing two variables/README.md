# Visualizing two variables

## Scatter plots

### Interpreting scatter plots

Scatter plots let you explore the relationship between two continuous variables.

Here you can see a scatter plot of average life expectancy (on the y-axis) versus average length of schooling (on the x-axis) for countries around the world. Each point in the plot represents one country. A straight trend line from a linear regression model is shown.

![scatter-who-life-exp-vs-school](scatter-who-life-exp-vs-school.png)

Data source: United Nations

True

- Exactly one country averages more than 14 years schooling
- There is positive correlation between the life expectancy and the length of schooling
- Every country with an average life expectancy of less than 60 years has an average length of schooling years less than 7 years
- As the average length of schooling increases, the average life expectancy typically increases too

False

- There is a negative correlation between the life expectancy and the length of schooling
- If one country has a longer average length of schooling than another country, that country will also have a greater average life expectancy
- No countries have an average life expectancy of less than 55 years
- No countries have an average length of schooling less than 6 years and an average expectancy of more than 75 years

### Trends with scatter plots

Adding trend lines to a scatter plot can make it easier to articulate the relationship between the two variables.

Here you can see the life expectancy for each country again, this time plotted against the Gross National Income (GNI) per capita (a measure of how rich the country is). You have a choice between linear and logarithmic scales on the x-axis, and can add linear of curved trend lines.

Which statement best describes the trend?

Possible Answers: Life expectancy increases linearly with the logarithm of GNI when GNI is between $1k and $50k.

## Line plots

### Interpreting line plots

Line plots are excellent for comparing two continuous variables, where consecutive observations are connected somehow. A common type of line plot is to have dates or times on the x-axis, and a numeric quantity on the y-axis. In this case, "consecutive observations" means values on successive dates, like today and tomorrow. By drawing multiple lines on the same plot, you can compare values.

The following line plot shows the percentage of households in the United States that adopted each of four technologies (automobiles, refrigerators, stoves, and vacuums) from 1930 to 1970.

![line-tech-adoption](line-tech-adoption.png)

Data source: Hannah Ritchie and Max Roser (2019) - Technology Adoption

True

- In 1954, two of four technologies had lower adoption than in 1940
- After 1940, adoption of refrigerators was always higher than adoption of stoves
- In 1930, adoption of automobiles was greater than 50%

False

- After 1940, adoption of automobiles was always higer than adoption of vacuums
- In 1940, adoption of stoves was greater than adoption of automobiles
- It took longer for refrigerators to go from 50% adoption to 75% adoption than it took vacuums

### Logarithmic scales for line plots

If you have a dataset where the values span several orders of magnitude, it can be easier to view them on a logarithmic scale.

A subset of the COVID-19 coronavirus data is shown in the line plot. You saw in the video that most of the cases in early 2020 occurred in mainland China. You might wonder what is happening in the rest of the world. Here, the six countries with the most number of confirmed cases outside of mainland China are shown.

On the linear scale, notice that moving up one grid line in the plot adds 20000. On the logarithmic scale, moving up one grid line in the plot multiplies by 4.

Considering the six countries on the plot, which statement is true?

Possible Answers: On Feb 17, Germany had more cumulative confirmed cases of COVID-19 than France.

### Line plots without dates on the x-axis

Although dates and times are the most common type of variable for the x-axis in line plot, other types of variable are possible.

In the video, you saw data on the ages of juvenile offenders in Switzerland. That data was presented with time on the x-axis and one line for each age. Since that plot wasn't very satisfactory, we'll try again. This time, age is on the x-axis and there is one line for each year. In the plot you can see two separate clusters of lines representing different age profiles for the offenders.

Which year did the change in age profile of juvenile offenders take place?

Data source: Senior Attorney of the Canton of Zurich

Possible Answers: 2011

## Bar plots

### Interpreting bar plots

Bar plots are a great way to see counts of each category in a categorical variable.

The ESPN Top 100 famous athletes dataset has two categorical variables: country and sport.

Explore the plots and determine which statement is false.

Possible Answers: Soccer players from the USA had more famous athletes than any other country/sport combination.

### Interpreting stacked bar plots

If you care about percentages rather than counts, then stacked bar plots are often a good choice of plot.

The dataset for this exercise relates to another question from the Health Survey for England. Adults aged 65 or more were asked how many "activities of daily living" (day-to-day tasks) they needed assistance with.

Type show_plot in the DataCamp console and press ENTER to see the plot. It's interactive – hover your mouse over the bars to see the percentage for that block.

Which statement is true?

Possible Answers: The group with the largest percentage of people needing no assistance was men aged 70-74.

## Dot plots

### Interpreting dot plots

Dot plots are similar to bar plots in that they show a numeric metric for each category of a categorical variable. They have two advantages over bar plots: you can use a log scale for the metric, and you can display more than one metric per category.

Here is a dot plot of the social media followings of the ESPN 2017 top 100 famous athletes, with one row per athlete. Three metrics are shown for each athlete: the number of followers on Facebook, Instagram, and Twitter. Only the athletes for Basketball, Cricket, Soccer, and Tennis who had accounts on each platform are shown. Rows are sorted alphabetically for each sport.

![dot-espn-by-social-media](dot-espn-by-social-media.png)

Based on the plot, which statement about the athlete's social media following is false?

Possible Answers: Soccer: Christiano Ronaldo has more Twitter followers than Marcelo Viera.

### Sorting dot plots

As with box plots and bar plots, how you order the rows in a dot plot affects the kinds of questions that are easy to answer.

Here you can see the Big Mac Index: the price of a McDonalds Big Mac in various countries around the world (in Jan 2020). The "Actual price" is the price converted to US dollars. The "GDP adjusted price" has an additional correction for the gross domestic product of a country. Roughly, if people earn less in a country, it will cost more using the adjusted price.

By default, the rows in the dot plot are ordered alphabetically. This makes it really easy to look up the price for a specific country, but difficult to answer question about where the most expensive or least expensive Big Macs can be found. By sorting the rows by price, those questions are easier to answer.

Which statement is true?

Data source: The Economist

Possible Answers: Two countries have Big Macs that cost over 100 USD after adjusting for GDP.