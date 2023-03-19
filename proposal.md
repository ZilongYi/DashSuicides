# DASHboard Proposal

Zilong YI, adapted from [here](https://github.com/ZilongYi/suicide_indicator/edit/main/proposal.md)

This report outlines the identified problem and proposed dashboard solution.

## Motivation & Purpose

According to [World Health Organization](https://www.who.int/health-topics/suicide), suicides take away the lives of over 700,00 people globally every year, but many of these are preventable if there are sufficient support resources available. If we could understand the correlation between suicides among different cohorts and across the social economic spectrum, then we may be able to target the appropriate resources to a specific demographic of population. To address this challenge, we propose building a data visualization app that allows doctors and mental health researchers to visually explore a dataset of suicides in countries around the world. Our app will show various socio-economic measurements and allow users to explore the data by filtering and re-ordering on different variables to order to compare socio-economic factors that may affect suicide rates.

## Data Description

In this project , we are using the [Suicide Rate overview(1985 to 2021)](https://www.kaggle.com/datasets/omkargowda/suicide-rates-overview-1985-to-2021). This data set contains rate of suicides based on various socio-economic factors such as `country`, `GDP`, `age`, `gender` etc. 

The Kaggle Dataset is an extension of the original one, created by combining four other datasets that are related in terms of time and location. Its purpose is to identify patterns that may be linked to higher suicide rates across various demographic groups worldwide, spanning the full range of socioeconomic levels. It contains 31,756 global observations from 1985 to 2021 over 12 variables. 

We will be visualizing data from multiple perspectives. Map of country-wise comparison based on `GDP`/`suicide rate` would give us insight of whether GDP and suicide rate are overall correlated or not. Several line/bar charts, based on `age` and `gender`, take us one step further to see whether age/gender is correlated to suicide rate and if so by how much, graphically speaking. If time permits, we might be tempted to make an animation of our data to visualize the change over `years`. 

## User Persona & Research Questions

**User Persona**: Medical professionals such as psychiatrists, nurses, or doctors who want to understand how suicide rates have changed between countries over time. Our users typically have moderate data/computer literacy so this dashboard allows for them to explore and attempt to answer their own questions easily and efficiently.

**Example Use Case Research Questions (Primary tasks [bolded])**:
1. Brian is a doctor working in mental health and is considering moving to a different country. Brian wants to **[compare]** how his current countries suicide rate and attributes compares to the countries he is considering moving to.
2. Josee is a nursing student and wants to understand & **[visualize]** how suicide rates in her country and surrounding countries have changed over time.
3. Connie is a mental health researcher and wants to **[dissect]** the suicide dataset into her population of interest. By looking at countries comparisons by age, date range, region, sex, etc. she hopes to save time from doing the analysis herself and decide where to focus her effort.