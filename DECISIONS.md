# Analytical and Technical Decisions

This document records the main analytical and technical decisions adopted during the development of the project.  
Its purpose is to preserve the rationale behind data transformations and methodological choices, ensuring transparency, traceability, and reproducibility over time.

---

## 1. Temporal scope of the analysis

The project is designed as an **updatable data pipeline**.  
The analysis currently focuses on the period **2016 onwards**, which corresponds to the years for which both air traffic and GDP data are consistently available.

The pipeline can be re-executed periodically to incorporate new observations as they become available.  
Each execution represents a new snapshot of the dataset and analysis at a given point in time.

---

## 2. Selection and exclusion of countries

During the construction of the gold dataset, a subset of countries is excluded from the analysis.  
This exclusion is motivated by issues related to data completeness, geopolitical disruptions, or inconsistencies between data sources.

The countries excluded at the time of analysis include:
- Iceland  
- Israel  
- Morocco  
- Ukraine  

These exclusions are applied consistently across the pipeline to preserve comparability and avoid distortions in the final results.

---

## 3. Harmonisation of country names

To enable a correct merge between air traffic data and GDP data, country names are harmonised across sources.

This includes:
- Resolving differences in naming conventions between datasets
- Applying explicit mappings (e.g. alternative country names or spelling variants)

This harmonisation is necessary to ensure that observations from different sources refer to the same entities.

---

## 4. Choice of aggregation level

Air traffic data are aggregated at the **country–year** level using the total number of flights as the main indicator.

This level of aggregation is chosen to:
- Ensure compatibility with annual GDP data
- Reduce noise present at finer spatial or temporal resolutions
- Focus the analysis on macro-level relationships

---

## 5. Logarithmic transformation of variables

Both GDP and total number of flights exhibit highly skewed distributions and extreme values.

For this reason:
- Logarithmic transformations are applied to both variables during the analysis
- This allows interpretation in relative (percentage) terms
- It facilitates the use of correlation and linear regression techniques

The log-log specification is chosen for analytical clarity rather than causal inference.

---

## 6. Interpretation of results

The analysis is explicitly **descriptive and associative** in nature.

Although strong statistical relationships are observed between air traffic and GDP:
- The results are not interpreted as causal
- No structural economic model is estimated
- Other potentially relevant variables are not included

This limitation is acknowledged to avoid overinterpretation of the findings.

---

## 7. Stability of decisions

The decisions documented in this file are intended to remain stable across pipeline executions.  
If modifications are required in the future, they should be explicitly documented through version control to preserve the analytical history of the project.
