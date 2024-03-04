# library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Format date
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Filter data
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

### Streamlit Sidebar

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Time Range',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Start and End Date
day_df = day_df[(day_df["dteday"] >= str(start_date)) &
                (day_df["dteday"] <= str(end_date))]
hour_df = hour_df[(hour_df["dteday"] >= str(start_date)) &
                (hour_df["dteday"] <= str(end_date))]


### Streamlit Main

st.header('Dicoding Collection Dashboard :sparkles:')
st.subheader('Bike Sharing')
st.caption('Dataset: https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset')


## Bike Share per Day
st.subheader('Number of Bike Sharing per Day')

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    day_df["dteday"],
    day_df["cnt"],
    marker='o',
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

st.subheader("The average amount of bike share based on time")

## colors function when the value is max
def color(data):
  colors = []
  for count in data["cnt"]:
    if count == data["cnt"].max():
      colors.append("#90CAF9")
    else:
      colors.append("#D3D3D3")
  return colors


col1, col2 = st.columns(2)

with col1:
  # by Weekday

  fig, ax = plt.subplots(figsize=(20, 10))

  weekday_df = day_df.groupby(by="weekday").agg({
    "instant": "nunique",
    "cnt": "mean"
    })

  weekday_df.rename(index={0:'sunday',1: 'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'}, inplace=True)

  sns.barplot(
      y=weekday_df["cnt"],
      x=weekday_df.index,
      palette=color(weekday_df),
      ax=ax
  )
  ax.set_title("Average of Bike Sharing by Weekday", loc="center", fontsize=50)
  ax.set_ylabel(None)
  ax.set_xlabel(None)
  ax.tick_params(axis='x', labelsize=29)
  ax.tick_params(axis='y', labelsize=30)
  st.pyplot(fig)

with col2:
  # by Season

  fig, ax = plt.subplots(figsize=(20, 10))

  season_df = day_df.groupby(by="season").agg({
    "instant": "nunique",
    "cnt": "mean"
  })

  season_df.rename(index={1: 'spring',2:'summer',3:'fall',4:'winter'}, inplace=True)

  sns.barplot(
       y=season_df["cnt"],
       x=season_df.index,
       palette=color(season_df),
      ax=ax
  )
  ax.set_title("Average of Bike Sharing by Season", loc="center", fontsize=50)
  ax.set_ylabel(None)
  ax.set_xlabel(None)
  ax.tick_params(axis='x', labelsize=35)
  ax.tick_params(axis='y', labelsize=30)
  st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
  # by Holiday

  fig, ax = plt.subplots(figsize=(20, 10))

  holiday_df = day_df.groupby(by="holiday").agg({
    "instant": "nunique",
    "cnt": "mean"
  })

  holiday_df.rename(index={0: 'non-holiday',1:'holiday'}, inplace=True)

  sns.barplot(
      y=holiday_df["cnt"],
      x=holiday_df.index,
      palette=color(holiday_df),
      ax=ax
  )
  ax.set_title("Average of Bike Sharing by Holiday", loc="center", fontsize=50)
  ax.set_ylabel(None)
  ax.set_xlabel(None)
  ax.tick_params(axis='x', labelsize=35)
  ax.tick_params(axis='y', labelsize=30)
  st.pyplot(fig)

with col2:
  # by Hour

  fig, ax = plt.subplots(figsize=(20, 10))

  hoursdf = hour_df.groupby(by="hr").agg({
    "instant": "nunique",
    "cnt": "mean"
  })

  sns.barplot(
       y=hoursdf["cnt"],
       x=hoursdf.index,
       palette=color(hoursdf),
      ax=ax
  )
  ax.set_title("Average of Bike Sharing by Hour", loc="center", fontsize=50)
  ax.set_ylabel(None)
  ax.set_xlabel(None)
  ax.tick_params(axis='x', labelsize=29)
  ax.tick_params(axis='y', labelsize=30)
  st.pyplot(fig)

st.caption('The blue color represents the maximum value of bike share.')