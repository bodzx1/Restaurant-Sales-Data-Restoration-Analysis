import streamlit as st
import pandas as pd
import plotly.express as px
##setting the page
st.set_page_config(
    page_title='Mid Project,Restaurant Analysis',
    layout='wide'
    )
st.title('Restaurant Dashboard')
st.markdown('Sale trends and Revenue drivers')
@st.cache_data ##loads data efficiently
def load_data():
    df=pd.read_csv('cleaned_restaurant_data.csv')
    return df
df=load_data()
##side bar
st.sidebar.header('filter options')
season_options=df['Season'].unique()
selected_seasons=st.sidebar.multiselect('select season',season_options,default=season_options)
category_options=df['Category_Label'].unique()
selected_category=st.sidebar.multiselect('select category',category_options,default=category_options)
year_options=df['Year'].unique()
selected_year=st.sidebar.multiselect('select year',year_options,default=year_options)
filtered_df = df[ ##putting filtered df to make columns variable
    (df['Season'].isin(selected_seasons)) & 
    (df['Year'].isin(selected_year))&
    (df['Category_Label'].isin(selected_category))
]
st.subheader('Data Summary')
##giving a data summary for business owner
col1,col2,col3=st.columns(3)
total_sales=df['Order Total'].sum()
total_orders=filtered_df.shape[0]
avg_order_value = filtered_df['Order Total'].mean()
col1.metric('Total Sales',f'${total_sales}')
col2.metric('Total Orders',f'{total_orders}')
col3.metric('Average Order Value',f'${avg_order_value:.2f}')
st.divider()
tab1,tab2,tab3=st.tabs(['sale trends','customer behavior','yearly comparison'])
with tab1:
    st.subheader("Sales by Category")
    fig_cat = px.bar(
        filtered_df, 
        x='Category_Label', 
        y='Order Total', 
        color='Category_Label',
        title="Sale by Category"
    )
    st.plotly_chart(fig_cat, use_container_width=True)

    st.subheader("Seasonal Trends")
    season_group = filtered_df.groupby(['Season', 'Category_Label']).size().reset_index(name='Count')
    fig_season = px.bar(
        season_group, 
        x='Season', 
        y='Count', 
        color='Category_Label', 
        barmode='group',
        title="Order Volume by Season"
    )
    st.plotly_chart(fig_season, use_container_width=True)

with tab2:
    st.subheader("Loyalty Analysis")
    fig_scatter = px.density_heatmap(
        filtered_df, 
        x='Customer Past Orders', 
        y='Order Total',
        title="Customer Loyalty vs. Order Value"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
with tab3:
    st.header("2022 vs. 2023 Performance")
    st.subheader("Total Revenue by Year")
    yearly_sales = filtered_df.groupby('Year')['Order Total'].sum().reset_index()
    fig_year = px.bar(
        yearly_sales, 
        x='Year', 
        y='Order Total', 
        color='Year',
        title="Revenue: 2022 vs 2023"
    )
    fig_year.update_xaxes(dtick=1) 
    
    st.plotly_chart(fig_year, use_container_width=True)
st.markdown("""
    * **Seasons:** Spring is our busiest season we should consider running promotions in fall to boost traffic.
    * **Loyalty:** we have many repeat customers, their average spend is consistent with new customers. 
    * **Revenue Driver:** Main Dishes drive the highest revenue
    """)