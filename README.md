# Drink Data Visualization 🍹

Questo progetto è un **side project personale** nato per esplorare e visualizzare dati a partire da un file CSV contenente informazioni sul consumo di drink nel tempo.

L’obiettivo non è creare una libreria riutilizzabile o un prodotto “enterprise”, ma sperimentare con **pandas**, **matplotlib** e **seaborn** per ottenere grafici chiari, leggibili e (si spera) anche belli da vedere.

---

## Cosa fa il progetto

A partire da un file `drinks.csv`, lo script:

- carica e preprocessa i dati temporali
- aggrega il consumo per tipo di drink, data, mese e giorno della settimana
- genera una serie di grafici esplorativi
- calcola alcune statistiche generali
- esporta grafici anche in **PDF**

---

## Tipi di grafici inclusi

Il progetto genera, tra gli altri:

- Donut chart con distribuzione dei drink
- Bar chart per tipo di drink
- Andamento temporale giornaliero
- Andamento cumulativo
- Consumo per giorno della settimana
- Confronto tipo di drink vs giorno della settimana
- Statistiche mensili
- Heatmap mese / giorno della settimana
- Top eventi con più drink
- Scatter plot sull’intensità degli eventi
- Riepilogo testuale delle statistiche principali

Ogni grafico è pensato per esplorare una prospettiva diversa dei dati.

---

## Dataset

Il file CSV deve contenere almeno le seguenti colonne:

- `Date` – data dell’evento
- `Type of drink` – tipo di drink
- `Numers` – quantità consumata
- `Name` – nome dell’evento

Il progetto non include validazioni avanzate: si assume un dataset “ragionevole”.

---

## Tecnologie utilizzate

- Python
- pandas
- matplotlib
- seaborn
- numpy

---

## Note

- Il codice è volutamente **monolitico e lineare**, tipico di un side project esplorativo
- Nessuna pretesa di ottimizzazione o architettura avanzata
- Ottimo terreno per future estensioni (refactor, modularizzazione, dashboard, ecc.)

---

## Licenza

Progetto distribuito sotto licenza **MIT**.
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

Il progetto non include validazioni avanzate: si assume un dataset “ragionevole”.

---

## Tecnologie utilizzate

- Python
- pandas
- matplotlib
- seaborn
- numpy

---

## Note

- Il codice è volutamente **monolitico e lineare**, tipico di un side project esplorativo
- Nessuna pretesa di ottimizzazione o architettura avanzata
- Ottimo terreno per future estensioni (refactor, modularizzazione, dashboard, ecc.)

---
