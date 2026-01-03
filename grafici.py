import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from datetime import datetime

# ===== CONFIGURAZIONE GLOBALE =====
plt.style.use("dark_background")
sns.set_palette("husl")

plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 15
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

# Carica CSV
df = pd.read_csv("drinks.csv")

# Preprocessing
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df["giorno_settimana"] = df["Date"].dt.day_name()
df["Mese"] = df["Date"].dt.to_period("M")
df["Anno-Mese"] = df["Date"].dt.strftime("%Y-%m")

# Dati aggregati
drink_totali = df.groupby("Type of drink")["Numers"].sum().sort_values(ascending=False)
totale = drink_totali.sum()

# ===== 1. DONUT CHART =====
fig, ax = plt.subplots(figsize=(10, 10))

colors = sns.color_palette("husl", len(drink_totali))

wedges, texts, autotexts = ax.pie(
    drink_totali,
    colors=colors,
    autopct=lambda p: f"{p:.1f}%",
    startangle=90,
    pctdistance=1.12,
    wedgeprops=dict(width=0.4, edgecolor="white", linewidth=2)
)

# Nascondi etichette duplicate SOLO per percentuali < 2%
percentuali_viste = set()

for autotext in autotexts:
    testo = autotext.get_text()

    percentuale = float(testo.replace("%", ""))

    if percentuale < 2:
        if testo in percentuali_viste:
            autotext.set_visible(False)
        else:
            percentuali_viste.add(testo)
            autotext.set_fontsize(10)
            autotext.set_fontweight("bold")
    else:
        autotext.set_fontsize(11)
        autotext.set_fontweight("bold")


# Numero totale al centro
ax.text(
    0, 0.08,
    f"{totale}",
    ha="center",
    va="center",
    fontsize=48,
    fontweight="bold"
)

ax.text(
    0, -0.15,
    "Total Drinks for 2025",
    ha="center",
    va="center",
    fontsize=13,
    color="lightgray"
)

ax.set_title("Drink Distribution 2025", pad=20, fontsize=16, fontweight="bold")

# Legenda migliorata
ax.legend(
    wedges,
    drink_totali.index,
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    frameon=False,
    fontsize=11
)

plt.tight_layout()
plt.show()

# ===== 2. BAR CHART DRINK PER TIPO =====
fig, ax = plt.subplots(figsize=(12, 6))
bars = drink_totali.plot(kind="bar", ax=ax, color=sns.color_palette("husl", len(drink_totali)))

# Aggiungi i numeri sopra ogni barra
for i, (bar, value) in enumerate(zip(ax.patches, drink_totali.values)):
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + (height * 0.01),
        f"{int(value)}",
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold',
        color='white'
    )

ax.set_ylabel("Numero di drink", fontsize=12, fontweight="bold")
ax.set_xlabel("Tipo di drink", fontsize=12, fontweight="bold")
ax.set_title("Drink Consumati per Tipo", fontsize=15, fontweight="bold", pad=20)
plt.xticks(rotation=45, ha='right')
ax.grid(alpha=0.3, axis='y')

ax.set_ylim(0, max(drink_totali.values) * 1.1)  # 10% di spazio extra sopra

plt.tight_layout()
plt.show()

# ===== 3. TIMELINE CHART CON AREA =====
fig, ax = plt.subplots(figsize=(14, 6))
per_giorno = df.groupby("Date")["Numers"].sum()
ax.fill_between(per_giorno.index, per_giorno.values, alpha=0.6, color="steelblue")
ax.plot(per_giorno.index, per_giorno.values, color="lightblue", linewidth=2, marker='o', markersize=4)
ax.set_ylabel("Numero di drink", fontsize=12, fontweight="bold")
ax.set_xlabel("Data", fontsize=12, fontweight="bold")
ax.set_title("Consumo nel Tempo", fontsize=15, fontweight="bold", pad=20)
ax.grid(alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ===== 5. DRINK PER GIORNO DELLA SETTIMANA =====
fig, ax = plt.subplots(figsize=(12, 6))
giorni_ordine = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
drink_per_giorno = df.groupby("giorno_settimana")["Numers"].sum().reindex(giorni_ordine, fill_value=0)
drink_per_giorno.plot(kind="bar", ax=ax, color=sns.color_palette("coolwarm", len(drink_per_giorno)))
ax.set_ylabel("Numero di drink", fontsize=12, fontweight="bold")
ax.set_xlabel("Giorno della settimana", fontsize=12, fontweight="bold")
ax.set_title("Drink per Giorno della Settimana", fontsize=15, fontweight="bold", pad=20)
plt.xticks(rotation=45, ha='right')
ax.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# ===== 7. CONFRONTO TIPO DRINK PER GIORNO DELLA SETTIMANA =====
fig, ax = plt.subplots(figsize=(14, 7))
pivot = df.pivot_table(
    values="Numers",
    index="giorno_settimana",
    columns="Type of drink",
    aggfunc="sum",
    fill_value=0
)
pivot = pivot.reindex(giorni_ordine, fill_value=0)
pivot.plot(kind="bar", ax=ax, stacked=False, colormap="tab20")
ax.set_ylabel("Numero di drink", fontsize=12, fontweight="bold")
ax.set_xlabel("Giorno della settimana", fontsize=12, fontweight="bold")
ax.set_title("Tipo di Drink per Giorno della Settimana", fontsize=15, fontweight="bold", pad=20)
plt.xticks(rotation=45, ha='right')
ax.legend(title="Tipo di drink", bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# ===== 8. STATISTICHE MENSILI =====
fig, ax = plt.subplots(figsize=(12, 6))
mensile = df.groupby("Mese")["Numers"].sum()
mensile.plot(kind="bar", ax=ax, color="steelblue")
ax.set_ylabel("Numero di drink", fontsize=12, fontweight="bold")
ax.set_xlabel("Mese", fontsize=12, fontweight="bold")
ax.set_title("Drink per Mese", fontsize=15, fontweight="bold", pad=20)
plt.xticks(rotation=45, ha='right')
ax.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# ===== 6. HEATMAP MESE/GIORNO DELLA SETTIMANA =====
fig, ax = plt.subplots(figsize=(14, 6))
heatmap_data = df.pivot_table(
    values="Numers",
    index="Anno-Mese",
    columns="giorno_settimana",
    aggfunc="sum",
    fill_value=0
)
# Riordina le colonne
heatmap_data = heatmap_data[giorni_ordine]
sns.heatmap(heatmap_data, annot=True, fmt='g', cmap="YlOrRd", cbar_kws={'label': 'Drink'}, ax=ax)
ax.set_title("Heatmap: Drink per Mese e Giorno della Settimana", fontsize=15, fontweight="bold", pad=20)
ax.set_xlabel("Giorno della settimana", fontsize=12, fontweight="bold")
ax.set_ylabel("Mese", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.show()

# ===== 9. TOP 15 EVENTI CON PIÙ DRINK =====
fig, ax = plt.subplots(figsize=(12, 8))
top_eventi = df.groupby("Name")["Numers"].sum().nlargest(15)
top_eventi.plot(kind="barh", ax=ax, color=sns.color_palette("viridis", len(top_eventi)))
ax.set_xlabel("Numero di drink", fontsize=12, fontweight="bold")
ax.set_title("Top 15 Eventi con Più Drink", fontsize=15, fontweight="bold", pad=20)
ax.grid(alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

# ===== 4. ANDAMENTO CUMULATIVO =====
fig, ax = plt.subplots(figsize=(14, 6))
cumulativo = df.groupby("Date")["Numers"].sum().cumsum()
ax.fill_between(cumulativo.index, cumulativo.values, alpha=0.5, color="orange")
ax.plot(cumulativo.index, cumulativo.values, color="yellow", linewidth=3, marker='o', markersize=5)
ax.set_ylabel("Numero cumulativo", fontsize=12, fontweight="bold")
ax.set_xlabel("Data", fontsize=12, fontweight="bold")
ax.set_title("Andamento Cumulativo 2025", fontsize=15, fontweight="bold", pad=20)
ax.grid(alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ===== 10. SCATTER PLOT INTENSITÀ EVENTI =====
fig, ax = plt.subplots(figsize=(14, 6))
scatter = ax.scatter(range(len(df)), df["Numers"], c=range(len(df)), cmap="viridis", s=100, alpha=0.6, edgecolors='white')
ax.set_ylabel("Numero di drink", fontsize=12, fontweight="bold")
ax.set_xlabel("Evento (ordine temporale)", fontsize=12, fontweight="bold")
ax.set_title("Intensità degli Eventi nel Tempo", fontsize=15, fontweight="bold", pad=20)
ax.grid(alpha=0.3)
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Ordine temporale', fontsize=11)
plt.tight_layout()
plt.show()

# ===== 11. DISTRIBUZIONE PER TIPO DI DRINK (CONTEGGIO) =====
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_ylabel("Numero di volte bevuto", fontsize=12, fontweight="bold")
ax.set_xlabel("Tipo di drink", fontsize=12, fontweight="bold")
ax.set_title("Frequenza di Consumo per Tipo di Drink", fontsize=15, fontweight="bold", pad=20)
plt.xticks(rotation=45, ha='right')
ax.grid(alpha=0.3, axis='y')

# Aggiungi il valore sopra ogni barra
drink_conteggio = df.groupby("Type of drink").size().sort_values(ascending=False)
drink_conteggio.plot(kind="bar", ax=ax, color=sns.color_palette("husl", len(drink_conteggio)))
for i, v in enumerate(drink_conteggio.values):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# ===== 12. STATISTICHE GENERALI =====

fig, ax = plt.subplots(figsize=(9, 6))
ax.axis('off')

stats_text = f"""
STATISTICHE GENERALI 2025

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NUMERI GENERALI
   • Drink totali consumati: {totale}
   • Numero di eventi: {len(df)}
   • Numero di tipi di drink: {len(drink_totali)}
   • Media drink per evento: {totale/len(df):.2f}

TOP DRINK
   • Drink più popolare: {drink_totali.idxmax()} ({drink_totali.max()} drink)

TIMELINE
   • Giorni con attività: {df['Date'].nunique()}
   • Giorno con più drink: {per_giorno.idxmax().date()} ({per_giorno.max()} drink)
   • Data inizio: {df['Date'].min().date()}
   • Data fine: {df['Date'].max().date()}

PATTERN SETTIMANALE
   • Giorno della settimana con più drink: {drink_per_giorno.idxmax()} ({drink_per_giorno.max()} drink)
   • Giorno della settimana con meno drink: {drink_per_giorno.idxmin()} ({drink_per_giorno.min()} drink)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.1))

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages("grafici.pdf") as pdf:
    for i in range(5):
        plt.figure()
        plt.plot([1, 2, 3], [i, i+1, i+2])
        plt.title(f"Grafico {i}")
        pdf.savefig()   # salva la figura corrente come una pagina
        plt.close()
