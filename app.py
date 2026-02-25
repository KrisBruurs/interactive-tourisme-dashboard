import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title='Global Tourism Dashboard',
                   layout = 'wide'
)

# Load in data
df = pd.read_csv('data/transformed_tourism_data.csv')

# --- Title --- #
st.title('Global Tourism Dashboard')

# --- Tabs --- # 
tab1, tab2 = st.tabs(['World Map', 'Country Metric Comparison'])

# --- tab1 --- #
with tab1:
     st.header('Global Tourism Revenue and GDP Growth')
     st.write('Explore the global distribution of tourism revenue and GDP growth across countries. Use the sidebar to select the metric and year you want to visualize on the world map.')
     st.write('Hover over countries to see the exact values for the selected metric. The color intensity on the map represents the magnitude of the metric, allowing you to quickly identify trends and patterns across different regions.')
     
     col1, col2 = st.columns(2)
     
     with col1:
        metric = st.selectbox(
            label='Select Metric',
            options=['GDP_Growth_Percent', 'Tourism_Revenue'],
            format_func=lambda x: 
                'GDP Growth (%)' if x == 'GDP_Growth_Percent' 
                else 'Tourism Revenue (USD)'
        )
     with col2:
        year = st.slider(
            label='Select Year',
            min_value=int(df['Year'].min()),
            max_value=int(df['Year'].max()),
            value=int(df['Year'].min()),
            step=1
        )

    # --- Filter Data --- # 
     df_filtered = df[
        df['Year'] == year
    ].copy()



    # --- Main Page --- #
     labels = {}
     if metric == 'GDP_Growth_Percent':
        labels = {'GDP_Growth_Percent': 'GDP Growth (%)'}
     elif metric == 'Tourism_Revenue':
        labels = {'Tourism_Revenue': 'Tourism Revenue (USD)'}

     if metric == 'GDP_Growth_Percent':
        scale = 'RdYlGn'
        range_values = (-20, 20)
     elif metric == 'Tourism_Revenue':
        scale = 'Greens'
        range_values = (0, df_filtered['Tourism_Revenue'].max())

     labels = {metric: ''}

     fig = px.choropleth(
        df_filtered,
        locations='ISO3',
        locationmode='ISO-3',
        color= metric,
        hover_name='Country',
        hover_data={
            metric: ':,.0f' if metric == 'Tourism_Revenue' else ':.2f',
            'ISO3': False
        },
        color_continuous_scale=scale,  
        range_color=range_values,  
        title=f'By Country ({year})',
        labels=labels
    )

     fig.update_layout(
        margin=dict(l=0, r=0, t=40, b=0)
    )

     fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>%{z}<extra></extra>"
    )

     if metric == 'GDP_Growth_Percent':
        fig.update_traces(
            hovertemplate='<b>%{hovertext}</b><br>%{z:.2f}%<extra></extra>'
        )
     else:
        fig.update_traces(
            hovertemplate='<b>%{hovertext}</b><br>%{z:,.0f}<extra></extra>'
        )


     st.plotly_chart(fig, use_container_width=True)

# --- tab2 --- #
with tab2:
   st.title('Country Metric Comparison')
   st.write('Compare the trends of GDP growth and tourism revenue for selected countries over time. Use the dropdown menu to select a country and visualise how these metrics have evolved over the years. This comparison can help you understand the relationship between economic growth and tourism revenue in different countries.')
   
   # --- Country Selection --- #
   country = st.selectbox(
        label='Select Country',
        options=df['Country'].unique(),
        index=None,
        placeholder='Select Country...'
   )

   df_country = df[df['Country'] == country]

   # --- Line Chart --- #
   fig_line = go.Figure()

   fig_line.add_trace(
      go.Scatter(
         x = df_country['Year'],
         y = df_country['GDP_Growth_Percent'],
         name = 'GDP Growth (%)',
         yaxis='y',
   ))

   fig_line.add_trace(
      go.Scatter(
         x = df_country['Year'],
         y = df_country['Tourism_Revenue'],
         name = 'Tourism Revenue (USD)',
         yaxis='y2'
    ))
   
   fig_line.update_layout(
      xaxis = dict(title='Year'),
      yaxis = dict(title='GDP Growth (%)', side='left'),
      yaxis2 = dict(title='Tourism Revenue', side='right', overlaying='y'),
      legend = dict(x=0.01, y=0.99, bordercolor='black', borderwidth=1)
   )

   st.plotly_chart(fig_line)

