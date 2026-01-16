# Analysis of GDP and Air Traffic

## Objective of the analysis

The main objective of this analysis is to study the relationship between air traffic, measured through the total number of flights, and the level of economic activity, represented by Gross Domestic Product (GDP), across a set of countries over the period 2016–2024. In particular, the analysis aims to assess whether a statistically significant association exists between both variables and to characterise the nature of this relationship in relative terms, taking into account the high heterogeneity across countries and the presence of extreme values.

## Research question

The central research question guiding this analysis is:

Is there a statistically significant relationship between the number of flights and GDP across countries, and how does this relationship behave when analysed in relative terms using a logarithmic transformation?

More specifically, the analysis investigates whether countries with higher air traffic levels tend to exhibit higher GDP levels and whether this relationship can be interpreted as proportional or more than proportional in percentage terms.

## Methodological approach

Given that both variables exhibit highly skewed distributions and extreme values, the analysis is conducted in two complementary stages. First, the relationship between flights and GDP is explored visually using the original scale, which allows for the identification of outliers and highlights the limitations of interpreting the relationship in absolute levels. Second, logarithmic transformations are applied to both variables, facilitating interpretation in relative terms and enabling the use of statistical techniques such as Pearson correlation and log-log linear regression.

## Key results and relevance

The results reveal several relevant findings. The analysis conducted in logarithmic scale shows an approximately linear relationship between the number of flights and GDP, suggesting a positive multiplicative association between both variables. This result is confirmed by a high and statistically significant Pearson correlation coefficient, indicating a strong positive linear relationship between log(flights) and log(GDP).

Furthermore, the estimation of a log-log regression model indicates that the coefficient associated with the number of flights is positive and statistically significant, with a value close to one. This implies that a 1% increase in the number of flights is associated, on average, with an approximate 1% increase in GDP. The magnitude of the coefficient of determination (R²) suggests that air traffic explains a substantial proportion of the variability in GDP across countries and years.

These findings provide solid empirical evidence of a close association between air connectivity and economic activity, while also highlighting the advantages of analysing such relationships in relative terms. Nevertheless, the results should be interpreted as statistical associations rather than causal relationships, as the model does not incorporate other potentially relevant economic variables.

## Contents of this folder

- `Analysis_results.html`: rendered output of the exploratory and descriptive data analysis, including visualisations and statistical results derived from the gold datasets.
