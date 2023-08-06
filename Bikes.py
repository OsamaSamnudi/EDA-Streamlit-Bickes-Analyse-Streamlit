import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

df = pd.read_csv('Bikes v1.csv' , index_col=0)

st.set_page_config (page_title = 'Bikes EDA 🚴‍♂️' , layout = "wide" , page_icon = '📊')
with st.sidebar:
    st.header('Bikes 🚴‍♂️ EDA Analysis')
    About = st.sidebar.checkbox(":blue[Bikes EDA]")
    Planning = st.sidebar.checkbox(":orange[Show About Application]")
    About_me = st.sidebar.checkbox(":green[Show About me]")
    if About:
        st.sidebar.header(":blue[About EDA & Application Info]")
        st.sidebar.write(""" 
        * :blue[*datetime:*].
        * :blue[*season:*].
        * :blue[*weather:*].
        * :blue[*temp:*].
        * :blue[*humidity:*].
        * :blue[*windspeed:*].
        * :blue[*casual:*] .
        * :blue[*registered:*] .
        * :blue[*rented_bikes_count:*] .
        * :blue[*Profit:*] .
        * :blue[*year:*] .
        * :blue[*month:*] .
        * :blue[*day:*] .
        * :blue[*hour:*] .
        * :blue[*day_period:*] .
        * :red[So let us see the insights 👀]
        """)
    # ______________________________________________________________________________________________________________________________________________________________________________________________________
    if Planning :
        st.sidebar.header(":orange[Application Planning]")
        st.sidebar.write("""
        * 1) Data Information :
            * Describe : All Info , Categorical , Numerical , Custom Field
            * Data Information (df.info()) : All Info , Categorical , Numerical , Custom Field
            * Corrolation (heatmap)
        * 2) Bivariate analysis :
    
        * 3) Univariate analysiss :
    
        * 4) Multivatiate analysiss
        """)
    # ______________________________________________________________________________________________________________________________________________________________________________________________________
    if About_me :
        st.sidebar.header(":green[About me]")
        st.sidebar.write("""
        - Osama SAAD
        - Data Scaience & Machine Learning Student @:blue[Epsilon AI]
        - Infor ERP Consaltant @ Ibnsina Pharma
        - Email : osamasamnudi86@gamil.com
        - LinkedIn: 
            https://www.linkedin.com/in/ossama-ahmed-saad-525785b2
        - Github : 
            https://github.com/OsamaSamnudi
        """)
# "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
Data_Info , Univariate , Bivariate  , Multivariate = st.tabs (['Data Information 💾' , 'Univariate Analysis 🔴'  , 'Bivariate Analysis 🟠' , 'Multivariate Analysis🟢'])

pd.options.display.float_format = '{:.,2f}'.format
df = pd.read_csv('Bikes v1.csv' , index_col=0)

with Data_Info:
    with st.container():
        st.header("Data Describe  💾")
        DI_select = st.selectbox('Please select:',['Please select','All Columns' , 'Categorical' , 'Numerical' , 'custom'])
        if DI_select == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        elif DI_select == 'All Columns':
            st.write(":violet[Describe Table (All Columns):]")
            st.dataframe(data=df.describe().T , use_container_width=True)
        elif DI_select == 'Numerical':
            st.write(":orange[*Describe Table (All Numerical):*]")
            st.dataframe(data=df.describe(exclude = ['object']).T , use_container_width=True)
        elif DI_select == 'Categorical':
            st.write(":orange[*Describe Table (All Categorical):*]")
            st.dataframe(data=df.describe(include = ['object']).T , use_container_width=True)
        else:
            columns = st.selectbox('Please select:',df.columns.tolist())
            st.write(":orange[*Describe Table for :*]",columns)
            st.dataframe(data=df[columns].describe())

    with st.container():
        pd.options.display.float_format = '{:,.0f}'.format
        st.header("Data Information")
        DataInfo = st.checkbox("Show Data Info")
        if DataInfo :
            st.dataframe(data=df.dtypes.reset_index(name='Type'), hide_index=True, use_container_width=True)  

    with st.container():
        st.subheader('Heatmap Corrolation')
        corrolation = st.checkbox('Show Corrolations')
        if corrolation :
            cor = df.select_dtypes(exclude='object').corr()
            fig_corr = px.imshow(cor , text_auto=True , width= 900 , height= 900  , color_continuous_scale='rdbu')
            st.plotly_chart(fig_corr,use_container_width=True)
# "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
with Univariate:
    st.header('Univariate Analysis 🔴')
    with st.container():
        st.subheader('Categorical Timly Analysis for custom columns')
        lst = ['Please select','season', 'weather', 'year', 'month' , 'day','day_period']
        lst_select = st.selectbox("Select" , lst)
        st.write(f'Pie Chart by : {lst_select}')
        if lst_select == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        else:
            fig = px.pie(data_frame=df , names=lst_select , color_discrete_sequence=px.colors.qualitative.D3)
            st.plotly_chart(fig,use_container_width=True)

    with st.container():
        st.subheader('Distribution Analysis for custom columns')
        lst_1 = ['Please select (Dist)','season', 'weather', 'month' ,'day','day_period']
        lst_select_1 = st.selectbox("Select" , lst_1)
        st.write(f'Hsiogram Chart by : {lst_select_1}')
        if lst_select_1 == 'Please select (Dist)':
            st.write(":red[Please Choise a column from the list:]")
        else:
            fig = px.histogram(data_frame=df , x=lst_select_1 , color = 'year', barmode='group' , text_auto = True,color_discrete_sequence=px.colors.qualitative.Bold)
                
            st.plotly_chart(fig,use_container_width=True)

# # "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
with Bivariate:
    with st.container():
        st.header('Bivariate Analysis 🟠')
        st.subheader('Custom selection Analysis : x (Categorical) vs y (Numerical)')
        col1, col2, col3 = st.columns([7,7,7])
        with col1:
            x = st.selectbox('Select xaxis :' , ['Please select','season', 'weather', 'month' , 'day','day_period','hour'])
        with col2:
            y = st.selectbox('Select yaxis :' , ['Please select','rented_bikes_count', 'Profit'])
        with col3:
            color = st.selectbox('Colored by :' , ['Please select','season', 'weather', 'month' , 'day','day_period','hour'])
        if x == 'Please select' or y == 'Please select' or color == 'Please select':
            st.write(":red[Please Choise a column from x & y & color:]")
        else:
            st.write(f'Sum of ("{x}" vs "{y}") colored by : {color}')
            fig_bi_1 = px.histogram(data_frame=df , x = x , y = y , color = color , text_auto=True , color_discrete_sequence=px.colors.qualitative.Pastel)
                       # px.histogram(data_frame=df , x = x , y = y , histfunc='sum' , color = color , text_auto=True
            st.plotly_chart(fig_bi_1,use_container_width=True)

    with st.container():
        st.subheader('YoY Analysis for " casual , registered , rented_bikes_count , Profit "')
        YoYlst = ['Please select','casual','registered','rented_bikes_count','Profit']
        YoYBox = st.selectbox('Numerical List' , YoYlst)
        if YoYBox == 'Please select':
            st.write(":red[Please Choise a column from x & y:]")
        else:
            st.write(f'YoY Line Chart for {YoYBox}')
            msk_bi_2 = df.groupby(['month_numb','year'])[['casual','registered','rented_bikes_count','Profit']].sum().sort_values(by = ['year','month_numb']).reset_index()
            fig_bi_2 = px.line(msk_bi_2 , x = 'month_numb' , y = YoYBox , color='year' , markers=True)
            st.plotly_chart(fig_bi_2 , use_container_width=True)
# # "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
with Multivariate:
    with st.container():
        st.header('Multivariate Analysis🟢')
        st.subheader('Custom selection x (Categorical) vs y (Numerical) - Scatter Plot')
        col1, col2, col3 = st.columns([7,7,7])
        with col1:
            Sc_x = st.selectbox('Scatter X:' , ['Please select','datetime','day_period','day','season', 'weather','month','year'])
        with col2:
            Sc_y = st.selectbox('Scatter Y :' , ['Please select','registered', 'rented_bikes_count', 'Profit'])
        with col3:
            color_1 = st.selectbox('Scatter Color :' , ['Please select','season', 'weather', 'year', 'month' ,'day_period',])
        if Sc_x == Sc_y:
            st.write(":red[Scatter Y = Scatter Y , Please select different values]")
        else:
            if Sc_x == 'Please select' or Sc_y == 'Please select' or color_1 == 'Please select':
                st.write(":red[Please Choise a column from x & y:]")
            else:
                if Sc_x == Sc_y:
                    st.write(":red[Please Choise a column from x & y:]")
                else:
                    st.write(f'Scatter Plot of {Sc_x} vs {Sc_y}')
                    fig_5 = px.scatter(df , x=Sc_x , y=Sc_y , marginal_x='box' , color = color_1 ,color_discrete_sequence=px.colors.colorbrewer.Accent)
                    st.plotly_chart(fig_5,use_container_width=True)
