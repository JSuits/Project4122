import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
showErrorDetails = False

@st.cache
def load_data():
    df = pd.read_csv('Crash_Reporting.csv')
    return df

df = load_data()

#dfi = df.drop(df[df['Injury Severity'] == 'NO APPARENT INJURY'].index, inplace = True)
#if st.sidebar.checkbox('Severity of Injuries'):
#    fig, ax = plt.subplots()
#    df.filter(['Injury Severity']).value_counts().plot.bar(ax=ax)
#    st.write(fig)

if st.sidebar.checkbox('Collision Type Count'):
    fig, ax = plt.subplots()
    df.filter(['Collision Type']).value_counts().plot.bar(ax=ax)
    st.write(fig)
    


# Define the available speed limits and sort them in ascending order
speed_limits = sorted(df['Speed Limit'].unique())
speed_limits.remove(70)

# Create a container for the dropdown, checkbox, and graph
container = st.container()

# Create a dropdown selection widget for speed limits inside the container
with container:
    selected_speed_limit = st.selectbox('Select a speed limit', speed_limits)

# Create a checkbox to exclude "NO APPARENT INJURY" injuries inside the container
with container:
    exclude_no_injury = st.checkbox('Exclude "NO APPARENT INJURY" values', value = True)

# Filter the data based on the selected speed limit and the checkbox value
filtered_data = df[df['Speed Limit'] == selected_speed_limit].copy()
if exclude_no_injury:
    filtered_data = filtered_data[filtered_data['Injury Severity'] != 'NO APPARENT INJURY']
    
# Create a bar chart of injury severity counts for the selected speed limit
with container:
    fig, ax = plt.subplots()
    filtered_data['Injury Severity'].value_counts().plot.bar(ax=ax)
    ax.set_title('Distribution of Injuries by Severity at {} Miles Per Hour'.format(selected_speed_limit))
    st.write(fig)