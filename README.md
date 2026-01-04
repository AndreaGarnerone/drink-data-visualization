# Drink Data Visualization 🍹

This project is a **personal side project** created to explore and visualize data from a CSV file containing information on drink consumption over time.

The goal is not to create a reusable library or an “enterprise” product, but to experiment with **pandas**, **matplotlib**, and **seaborn** to obtain clear, readable, and (hopefully) beautiful graphs.

---

## What the project does

Starting from a `drinks.csv` file, the script:

- loads and preprocesses the time data
- aggregates consumption by drink type, date, month, and day of the week
- generates a series of exploratory graphs
- calculates some general statistics
- exports graphs to **PDF**

---

## Types of graphs included

Among others, the project generates:

- Donut charts with drink distribution
- Bar charts by drink type
- Daily time trends
- Cumulative trends
- Consumption by day of the week
- Comparison of drink type vs. day of the week
- Monthly statistics
- Heatmap by month/day of the week
- Top events with the most drinks
- Scatter plot on event intensity
- Text summary of key statistics

Each chart is designed to explore a different perspective of the data.

---

## Dataset

The CSV file must contain at least the following columns:

- `Date` – date of the event
- `Type of drink` – type of drink
- `Numbers` – quantity consumed
- `Name` – name of the event

The project does not include advanced validations: a “reasonable” dataset is assumed.

---

## Technologies used

- Python
- pandas
- matplotlib
- seaborn
- numpy

---

## Notes

- The code is deliberately **monolithic and linear**.
- No claims of optimization or advanced architecture.
- Ground for future extensions (new fields, refactor, modularization, dashboard, etc.).

---
