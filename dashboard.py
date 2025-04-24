import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titel
st.title("📦 Import- & Steueranalyse: d.o.o. vs Veggiemarkt GmbH")

# Eingaben
st.sidebar.header("Parameter")
import_value = st.sidebar.number_input("Jährliches Importvolumen (€)", value=180000, step=1000)
marge = st.sidebar.slider("Marge (%)", min_value=1, max_value=50, value=10) / 100

# Steuersätze
tax_hr = 0.10  # Körperschaftsteuer Kroatien
dividend_hr = 0.10  # Quellensteuer Kroatien
tax_at = 0.25  # Körperschaftsteuer Österreich

# Berechnungen
bruttogewinn = import_value * marge

# d.o.o.
netto_hr = bruttogewinn * (1 - tax_hr)
netto_hr_div = netto_hr * (1 - dividend_hr)

# Veggiemarkt
netto_at = bruttogewinn * (1 - tax_at)

# Daten zur Darstellung
data = pd.DataFrame({
    "Szenario": ["d.o.o. (in Firma)", "d.o.o. (nach Dividende)", "Veggiemarkt GmbH"],
    "Netto-Gewinn (€)": [netto_hr, netto_hr_div, netto_at]
})

# Ergebnis-Tabelle
st.subheader("📊 Ergebnis")
st.dataframe(data, use_container_width=True)

# Chart
fig, ax = plt.subplots()
ax.bar(data["Szenario"], data["Netto-Gewinn (€)"], color="skyblue")
ax.set_ylabel("€")
ax.set_title("Netto-Gewinn im Vergleich")
st.pyplot(fig)

# Vorteil anzeigen
vorteil = netto_hr - netto_at
st.success(f"💡 Steuerlicher Vorteil durch d.o.o.: {vorteil:,.2f} € (vor Ausschüttung)")
