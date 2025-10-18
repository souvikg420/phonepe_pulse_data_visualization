import os
import json
from pathlib import Path
from typing import List

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Base data directory (assumes app.py is in project root alongside the 'pulse' folder)
BASE_DIR = Path.cwd() / "pulse" / "data"

st.set_page_config(layout="wide", page_title="PhonePe Pulse Streamlit", page_icon="📱")

@st.cache_data
def load_aggregated_transaction() -> pd.DataFrame:
    path = BASE_DIR / "aggregated" / "transaction" / "country" / "india" / "state"
    rows = []
    if not path.exists():
        return pd.DataFrame()
    for state in os.listdir(path):
        state_dir = path / state
        if not state_dir.is_dir():
            continue
        for year in os.listdir(state_dir):
            year_dir = state_dir / year
            if not year_dir.is_dir():
                continue
            for quarter_file in os.listdir(year_dir):
                try:
                    q = int(quarter_file.replace('.json', ''))
                except Exception:
                    continue
                with open(year_dir / quarter_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for item in data.get('data', {}).get('transactionData', []):
                    name = item.get('name')
                    instruments = item.get('paymentInstruments', [])
                    cnt = None
                    amt = None
                    if instruments:
                        metric = instruments[0]
                        cnt = metric.get('count')
                        amt = metric.get('amount')
                    rows.append({
                        'States': state,
                        'Year': int(year),
                        'Quarter': int(q),
                        'Transaction_Type': name,
                        'Transaction_Count': cnt,
                        'Transaction_Amount': amt,
                    })
    df = pd.DataFrame(rows)
    if not df.empty:
        df['States'] = df['States'].str.replace('-', ' ').str.title()
    return df

@st.cache_data
def load_aggregated_insurance() -> pd.DataFrame:
    path = BASE_DIR / "aggregated" / "insurance" / "country" / "india" / "state"
    rows = []
    if not path.exists():
        return pd.DataFrame()
    for state in os.listdir(path):
        state_dir = path / state
        if not state_dir.is_dir():
            continue
        for year in os.listdir(state_dir):
            year_dir = state_dir / year
            if not year_dir.is_dir():
                continue
            for quarter_file in os.listdir(year_dir):
                try:
                    q = int(quarter_file.replace('.json', ''))
                except Exception:
                    continue
                with open(year_dir / quarter_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for item in data.get('data', {}).get('transactionData', []):
                    name = item.get('name')
                    instruments = item.get('paymentInstruments', [])
                    cnt = None
                    amt = None
                    if instruments:
                        metric = instruments[0]
                        cnt = metric.get('count')
                        amt = metric.get('amount')
                    rows.append({
                        'States': state,
                        'Year': int(year),
                        'Quarter': int(q),
                        'Transaction_Type': name,
                        'Transaction_Count': cnt,
                        'Transaction_Amount': amt,
                    })
    df = pd.DataFrame(rows)
    if not df.empty:
        df['States'] = df['States'].str.replace('-', ' ').str.title()
    return df

@st.cache_data
def load_aggregated_user() -> pd.DataFrame:
    path = BASE_DIR / "aggregated" / "user" / "country" / "india" / "state"
    rows = []
    if not path.exists():
        return pd.DataFrame()
    for state in os.listdir(path):
        state_dir = path / state
        if not state_dir.is_dir():
            continue
        for year in os.listdir(state_dir):
            year_dir = state_dir / year
            if not year_dir.is_dir():
                continue
            for quarter_file in os.listdir(year_dir):
                try:
                    q = int(quarter_file.replace('.json', ''))
                except Exception:
                    continue
                with open(year_dir / quarter_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                users_by_device = data.get('data', {}).get('usersByDevice')
                if users_by_device:
                    for item in users_by_device:
                        rows.append({
                            'States': state,
                            'Year': int(year),
                            'Quarter': int(q),
                            'Brand': item.get('brand'),
                            'Transaction_Count': item.get('count'),
                            'Percentage': item.get('percentage'),
                        })
    df = pd.DataFrame(rows)
    if not df.empty:
        df['States'] = df['States'].str.replace('-', ' ').str.title()
    return df

@st.cache_data
def load_top_transaction() -> pd.DataFrame:
    path = BASE_DIR / "top" / "transaction" / "country" / "india" / "state"
    rows = []
    if not path.exists():
        return pd.DataFrame()
    for state in os.listdir(path):
        state_dir = path / state
        if not state_dir.is_dir():
            continue
        for year in os.listdir(state_dir):
            year_dir = state_dir / year
            if not year_dir.is_dir():
                continue
            for quarter_file in os.listdir(year_dir):
                try:
                    q = int(quarter_file.replace('.json', ''))
                except Exception:
                    continue
                with open(year_dir / quarter_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for d in data.get('data', {}).get('districts', []):
                    rows.append({
                        'States': state,
                        'Year': int(year),
                        'Quarter': int(q),
                        'District': d.get('entityName'),
                        'Transaction_Count': d.get('metric', {}).get('count'),
                        'Transaction_Amount': d.get('metric', {}).get('amount'),
                    })
    df = pd.DataFrame(rows)
    if not df.empty:
        df['States'] = df['States'].str.replace('-', ' ').str.title()
        df['District'] = df['District'].str.title()
    return df

@st.cache_data
def load_top_user() -> pd.DataFrame:
    path = BASE_DIR / "top" / "user" / "country" / "india" / "state"
    rows = []
    if not path.exists():
        return pd.DataFrame()
    for state in os.listdir(path):
        state_dir = path / state
        if not state_dir.is_dir():
            continue
        for year in os.listdir(state_dir):
            year_dir = state_dir / year
            if not year_dir.is_dir():
                continue
            for quarter_file in os.listdir(year_dir):
                try:
                    q = int(quarter_file.replace('.json', ''))
                except Exception:
                    continue
                with open(year_dir / quarter_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for p in data.get('data', {}).get('pincodes', []):
                    rows.append({
                        'States': state,
                        'Year': int(year),
                        'Quarter': int(q),
                        'Pincode': p.get('name'),
                        'RegisteredUsers': p.get('registeredUsers'),
                    })
    df = pd.DataFrame(rows)
    if not df.empty:
        df['States'] = df['States'].str.replace('-', ' ').str.title()
    return df

# --- Streamlit UI ---
st.title("PhonePe Pulse — Streamlit Explorer")

menu = st.sidebar.selectbox("Choose view", ["Home", "Aggregated", "Top Charts"])

if menu == "Home":
    st.header("Available datasets")
    st.write("This app reads the PhonePe `pulse` JSON files from the repository and exposes basic analysis views.")
    df_t = load_aggregated_transaction()
    df_u = load_aggregated_user()
    df_i = load_aggregated_insurance()
    st.metric("Aggregated Transaction rows", 0 if df_t.empty else len(df_t))
    st.metric("Aggregated User rows", 0 if df_u.empty else len(df_u))
    st.metric("Aggregated Insurance rows", 0 if df_i.empty else len(df_i))

elif menu == "Aggregated":
    st.header("Aggregated Analysis")
    tab1, tab2, tab3 = st.tabs(["Transactions", "Users", "Insurance"])

    with tab1:
        df = load_aggregated_transaction()
        if df.empty:
            st.warning("No aggregated transaction data found in repository/pulse/data path")
        else:
            years = sorted(df['Year'].unique())
            year = st.selectbox('Year', years, index=0)
            q = st.selectbox('Quarter', sorted(df[df['Year']==year]['Quarter'].unique()))
            view = df[(df['Year']==year) & (df['Quarter']==q)]
            st.dataframe(view.head(200))
            agg = view.groupby('Transaction_Type')['Transaction_Amount'].sum().reset_index()
            fig = px.bar(agg, x='Transaction_Type', y='Transaction_Amount', title=f'Transaction amount by type ({year} Q{q})')
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        df = load_aggregated_user()
        if df.empty:
            st.warning("No aggregated user data found in repository/pulse/data path")
        else:
            years = sorted(df['Year'].unique())
            year = st.selectbox('Year (users)', years, index=0)
            q = st.selectbox('Quarter (users)', sorted(df[df['Year']==year]['Quarter'].unique()))
            view = df[(df['Year']==year) & (df['Quarter']==q)]
            st.dataframe(view.head(200))
            brand = view.groupby('Brand')['Transaction_Count'].sum().reset_index()
            fig = px.pie(brand, names='Brand', values='Transaction_Count', title=f'User Brand distribution ({year} Q{q})')
            st.plotly_chart(fig)

    with tab3:
        df = load_aggregated_insurance()
        if df.empty:
            st.warning("No aggregated insurance data found in repository/pulse/data path")
        else:
            years = sorted(df['Year'].unique())
            year = st.selectbox('Year (insurance)', years, index=0)
            q = st.selectbox('Quarter (insurance)', sorted(df[df['Year']==year]['Quarter'].unique()))
            view = df[(df['Year']==year) & (df['Quarter']==q)]
            st.dataframe(view.head(200))
            agg = view.groupby('Transaction_Type')['Transaction_Amount'].sum().reset_index()
            fig = px.bar(agg, x='Transaction_Type', y='Transaction_Amount', title=f'Insurance amount by type ({year} Q{q})')
            st.plotly_chart(fig)

elif menu == "Top Charts":
    st.header("Top Charts")
    tab1, tab2 = st.tabs(["Top Transactions", "Top Users"])

    with tab1:
        df = load_top_transaction()
        if df.empty:
            st.warning("No top transaction data found")
        else:
            years = sorted(df['Year'].unique())
            year = st.selectbox('Year (top trans)', years, index=0)
            q = st.selectbox('Quarter (top trans)', sorted(df[df['Year']==year]['Quarter'].unique()))
            view = df[(df['Year']==year) & (df['Quarter']==q)]
            top = view.nlargest(10, 'Transaction_Amount')
            st.dataframe(top)
            fig = px.bar(top, x='District', y='Transaction_Amount', title=f'Top 10 districts by transaction amount ({year} Q{q})')
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        df = load_top_user()
        if df.empty:
            st.warning("No top user data found")
        else:
            years = sorted(df['Year'].unique())
            year = st.selectbox('Year (top users)', years, index=0)
            q = st.selectbox('Quarter (top users)', sorted(df[df['Year']==year]['Quarter'].unique()))
            view = df[(df['Year']==year) & (df['Quarter']==q)]
            top = view.nlargest(10, 'RegisteredUsers')
            st.dataframe(top)
            fig = px.bar(top, x='Pincode', y='RegisteredUsers', title=f'Top 10 pincodes by registered users ({year} Q{q})')
            st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Data loaded from local `pulse/data` directory. If the app shows empty datasets, make sure the repository contains the original Pulse JSON files under `pulse/data`.")
