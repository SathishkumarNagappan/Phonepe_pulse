#Import all libraries
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import mysql.connector as msql
from babel.numbers import format_currency
from PIL import Image
import webbrowser
import plotly.express as px
import plotly.graph_objects as go
import base64
import ast


#Opening mysql using create engine module
#Mydb = create_engine("mysql+mysqlconnector://root:<password>@127.0.0.1:3306/pulse")

conn =msql.connect(host = 'localhost',
            database = 'phonepe_pulse',
            user = "root",
           password = "password",
           port = 3306)

#Cursor = mysql.connector.connect(**config)
cursor = conn.cursor()

#Cursor.execute("Select * from aggregated_transaction WHERE State='Tamilnadu'")
#Rows = cursor.fetchall()
#for i in rows:
#print(i)

st.set_page_config(page_title='Phonepe Pulse', page_icon = 'phonepe.jpg', layout='wide')
st.title(':violet[PhonePe Pulse Data Visualization]')

head1,head2=st.columns([0.18,3])
with head1:
    image = Image.open('phonepe.jpg')
    st.image(image, width=60)
with head2:
    tit1,tit2=st.columns([0.456,2])
    with tit1:
        st.markdown("<h2 style= 'color: #9932CC;font-size: 34px;'>PhonePe Pulse  </h2>", unsafe_allow_html=True)
    #with tit2:
        #st.markdown("<h2 style= 'color: #9932CC;font-weight: normal;font-size: 34px;'>The Best of Progress</h2>", unsafe_allow_html=True)
#st.write('')
#st.write('')
#left,optioncontainer,right=st.columns([0.2,3,0.2])

selected=option_menu(menu_title='', options=['Home','Map','Insights'],icons=['house','globe2','graph-up-arrow'],orientation='horizontal',styles={
            "container": {"padding": "0!important", "background-color": "white","size":"cover"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#391C59"},
            "nav-link-selected": {"background-color": "#691592"}  })
st.write('')

#st.write('')

if selected == 'Home':
    col1,col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/watch?v=c_1H6vivsiA")
        st.download_button(label="Download PhonePe App!",
                       data="https://www.phonepe.com/app-download/")

        st.title('GitHub')
        st.write('')
        st.write('A home for the data that powers the PhonePe Pulse website.')
        st.write('')
        url = 'https://github.com/PhonePe/pulse#readme'

        if st.button('GitHub'):
            webbrowser.open_new_tab(url)

    with col2:
        st.write(
        "The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data.")

        st.write(
        "When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?"
        "This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.")

        st.write(
        "This year, as we crossed 2000 Cr. transactions and 30 Crore registered users, we thought as India's largest digital payments platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages and grows its money. So it was time to demystify and share the what, why and how of digital payments in India.")

        st.write(
        "PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.")

        st.title('Data APIs')

        #st.write('')
        st.write("""
            This data has been structured to provide details on data cuts of Transactions and Users on the Explore tab.
            """)
        
        #st.write('')
        aggcol, mapcol, topcol = st.columns([2.1, 1.4, 1.3])
        with aggcol:
            st.subheader('Aggregated')
            #st.write('')
            st.write('Aggregated values of various payment categories as shown under Categories section')
            #st.write('')
        with mapcol:
            st.subheader('Map')
            #st.write('')
            st.write('Total values at the State and District levels')
            #st.write('')
        with topcol:
            st.subheader('Top')
            #st.write('')
            st.write('Totals of top States / Districts / Pin Codes')
            #st.write('')


if selected=='Map':
    col1, col2 = st.columns([1, 1])
    with col1:
        optcol,yearcol,qurcol,noncol=st.columns([0.5,0.2,0.2,0.1])
        with optcol:
            option=st.selectbox(label='Select Type',options=['Transaction','Users'])
        with yearcol:
            year=st.selectbox(label='Select Year',options=['2018','2019','2020','2021','2022'])
        with qurcol:
            quarter=st.selectbox(label='Select Quarter',options=['1','2','3','4'])
        with noncol:
            st.write('')
        if option=='Transaction':

            st.markdown("<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 48px;'><b>Transaction Map</b></h2>",unsafe_allow_html=True)

            select = 'select * from phonepe_pulse.maptran where Year={} and Quarter={} '.format(year, quarter)
            cursor.execute(select)
            result = cursor.fetchall()
            maptranstate = []
            for i in (result):
                maptranstate.append(i[2:5])
            statenamelst=[]
            statecountlst=[]
            stateamountlst=[]
            for i in maptranstate:
                    statenamelst.append(i[0])
                    statecountlst.append(i[1])
                    stateamountlst.append(i[2])



            lat=[10.0001051,15.9240905,28.0937702,26.4073841,25.6440845,30.72984395,21.6637359,20.7181749499999,28.6517178,15.3004543,22.3850051,29,31.81676015,32.7185614,23.4559809,14.5203896,10.3528744,33.9456407,10.8132489,23.8143419,18.9068356,24.7208818,25.5379432,23.2146169,26.1630556,20.5431241,10.91564885,30.9293211,26.8105777,27.601029,10.9094334,17.8495919,23.7750823,27.1303344,30.0417376,22.9964948]
            log =[93.0000194,80.1863809,94.5921326,93.2551303,85.906508,76.7841456701605,81.8406351,70.9323834101063,77.2219388,74.0855134,71.745261,76,77.3493205196885,74.8580917,85.2557301,75.7223521,76.5120396,77.6568576,73.6804620941119,77.5340719,75.6741579,93.9229386,91.2999102,92.8687612,94.5884911,84.6897321,79.8069487984423,75.5004841,73.7684549,88.4541363868014,78.3665347,79.1151663,91.7025091,80.859666,79.089691,87.6855882]


            df = pd.DataFrame({'lat':lat,'lon':log, 'statenamelst': statenamelst,'count':statecountlst,'amount':stateamountlst})
            df['count'] = df['count'].astype('int64')
            df['amount'] = df['amount'].astype('int64')

            fig = px.scatter_geo(df,size='count',lat='lat',lon='lon',color='count',hover_name='statenamelst'
                                 ,hover_data=(['count','amount']),scope='asia',size_max=20,width=600,height=400,color_continuous_scale=["orange", "yellow", "red"])
            fig.update_geos(visible=False, resolution=50, scope="asia",
                showcountries=True, countrycolor="Black",
                showsubunits=True, subunitcolor="black",fitbounds='locations',showland=True,landcolor='rgb(153,50,204)')
            fig.update_layout(
                {'plot_bgcolor': 'rgb(34,13,56)', 'paper_bgcolor': 'rgb(34,13,56)',},margin={"r":0,"t":0,"l":0,"b":0},coloraxis_colorbar=dict(
                len=0.5,
                xanchor="right", x=0.97,
                yanchor='bottom', y=0.28,
                thickness=20,))
            fig.add_trace(go.Scattergeo(lon=df["lon"],
                                        lat=df["lat"],
                                        text=df["statenamelst"],
                                        textposition="middle center",
                                        mode='text',
                                        showlegend=False,opacity=0.6))
            fig.update_traces(marker=dict(symbol="octagon",
                                          line=dict(width=2.4,
                                                    color='black')),
                              selector=dict(mode='markers'))

            st.plotly_chart(fig)

        elif option=='Users':
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 48px;'><b>Users Map</b></h2>",unsafe_allow_html=True)

            select = 'select * from phonepe_pulse.mapuser where Year={} and Quarter={} '.format(year, quarter)
            cursor.execute(select)
            result = cursor.fetchall()
            mapuserstate = []
            mapuserstatenamelst=[]
            mapuserregistelst=[]
            mapuserappopenlst=[]
            for i in (result):
                mapuserstate.append(i[2:5])
            for i in mapuserstate:
                mapuserstatenamelst.append(i[0])
                mapuserregistelst.append(i[1])
                mapuserappopenlst.append(i[2])

            lat = [10.0001051, 15.9240905, 28.0937702, 26.4073841, 25.6440845, 30.72984395, 21.6637359,
                   20.7181749499999, 28.6517178, 15.3004543, 22.3850051, 29, 31.81676015, 32.7185614, 23.4559809,
                   14.5203896, 10.3528744, 33.9456407, 10.8132489, 23.8143419, 18.9068356, 24.7208818, 25.5379432,
                   23.2146169, 26.1630556, 20.5431241, 10.91564885, 30.9293211, 26.8105777, 27.601029, 10.9094334,
                   17.8495919, 23.7750823, 27.1303344, 30.0417376, 22.9964948]
            log = [93.0000194, 80.1863809, 94.5921326, 93.2551303, 85.906508, 76.7841456701605, 81.8406351,
                   70.9323834101063, 77.2219388, 74.0855134, 71.745261, 76, 77.3493205196885, 74.8580917, 85.2557301,
                   75.7223521, 76.5120396, 77.6568576, 73.6804620941119, 77.5340719, 75.6741579, 93.9229386, 91.2999102,
                   92.8687612, 94.5884911, 84.6897321, 79.8069487984423, 75.5004841, 73.7684549, 88.4541363868014,
                   78.3665347, 79.1151663, 91.7025091, 80.859666, 79.089691, 87.6855882]

            df = pd.DataFrame({'lat': lat, 'lon': log, 'statenamelst': mapuserstatenamelst, 'registered': mapuserregistelst,'appopens':mapuserappopenlst})
            df['lat']=df['lat'].astype('float')
            df['lon'] = df['lon'].astype('float')
            df['registered'] = df['registered'].astype('int64')
            df['appopens']=df['appopens'].astype('int64')

            fig = px.scatter_geo(df, size='registered', lat='lat', lon='lon', color='registered', hover_name='statenamelst'
                                 ,hover_data=(['registered','appopens']),scope='asia', size_max=20, width=600, height=400,
                                 color_continuous_scale=["orange", "yellow", "red"],opacity=0.79)

            fig.update_geos(visible=False, resolution=50, scope="asia",
                            showcountries=True, countrycolor="white",
                            showsubunits=True, subunitcolor="white", fitbounds='locations', showland=True,
                            landcolor='rgb(153,50,204)')
            fig.update_layout(
                {'plot_bgcolor': 'rgb(34,13,56)', 'paper_bgcolor': 'rgb(34,13,56)', },
                margin={"r": 0, "t": 0, "l": 0, "b": 0},coloraxis_colorbar=dict(
                len=0.5,
                xanchor="right", x=0.97,
                yanchor='bottom', y=0.28,
                thickness=20,))
            fig.add_trace(go.Scattergeo(lon=df["lon"],
                                        lat=df["lat"],
                                        text=df["statenamelst"],
                                        textposition="middle center",
                                        mode='text',
                                        showlegend=False, opacity=0.6))

            fig.update_traces(marker=dict(symbol="octagon",
                                          line=dict(width=2.4,
                                                    color='Black')),
                              selector=dict(mode='markers'))

            st.plotly_chart(fig)

    with col2:
        if option == 'Transaction':
            qurt = quarter
            select = 'select * from phonepe_pulse.aggtrans where Year={} and Quarter={}'.format(year, qurt)
            cursor.execute(select)
            result = cursor.fetchall()
            print(result)
            allpptran = 0
            total = 0
            catekey = []
            cateval = []
            for i in result:
                allpptran += i[3]
                total += int(i[4])
                catekey.append(i[2])
                cateval.append((i[3]))
            avg = int(total / allpptran)

            st.markdown("<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Transaction</b></h2>",
                        unsafe_allow_html=True)
            #st.write('')
            st.markdown(
                "<h2 style= 'color: black;font-weight: normal;font-size: 18px;'><b>All PhonePe Transaction(UPI+Cards+Wallets)</b></h2>",
                unsafe_allow_html=True)
            amount = format_currency(allpptran, 'INR', locale='en_IN')[:-3]
            tot = format_currency(total, 'INR', locale='en_IN')[:-3]
            average = format_currency(avg, 'INR', locale='en_IN')[:-3]
            st.markdown(
                r"<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 40px;'><b>{}</b></h2>".format(amount),
                unsafe_allow_html=True)
            # st.write('')
            totcol, avgcol = st.columns([1,1])
            with totcol:
                st.markdown(
                    "<h2 style= 'color: black;font-weight: normal;font-size: 18px;'><b>Total payment </b></h2>",
                    unsafe_allow_html=True)
                st.markdown(
                    r"<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 24px;'><b>{} Cr</b></h2>".format(tot),
                    unsafe_allow_html=True)
            with avgcol:
                st.markdown(
                    "<h2 style= 'color: black;font-weight: normal;font-size: 18px;'><b>Avg. transaction </b></h2>",
                    unsafe_allow_html=True)
                st.markdown(
                    r"<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 24px;'><b>{}</b></h2>".format(average),
                    unsafe_allow_html=True)
            #st.write('')
            st.subheader('Categories')
            #st.write('')
            keycate, valcate = st.columns([0.8,0.8])
            with keycate:
                for i in range(5):
                    st.markdown(
                        "<h2 style= 'color: black;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                            catekey[i]),
                        unsafe_allow_html=True)
            #st.write('')
            with valcate:
                for i in range(5):
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                            format_currency(cateval[i], 'INR', locale='en_IN')[1:-3]),
                        unsafe_allow_html=True)
            #st.write('#')
            #selecttop = st.selectbox(label='Top 10 Records ', options=['States', 'Districts', 'Pincodes'])

            selecttop = option_menu(menu_title='', icons=['bar-chart-line', 'bar-chart', 'bar-chart-line-fill'],
                                    options=['States', 'Districts', 'Pincodes'], orientation='horizontal', styles={
                    "container": {"background-color": "#480668"},
                    "icon": {"color": "orange", "font-size": "18px"},
                    "nav-link": {"font-size": "12px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#391C59"},
                    "nav-link-selected": {"background-color": "#691592"}})
            #st.write('')
            select = 'select * from phonepe_pulse.toptrans where Year={} and Quarter={} '.format(year, qurt)
            cursor.execute(select)
            result = cursor.fetchall()
            totlst = []
            topstateamount = []
            topdistamount = []
            toppinamount = []
            for i in result:
                totlst.append(i[0:6])
            for i in totlst:
                if 'State' in i:
                    topstateamount.append(i)
                elif 'District' in i:
                    topdistamount.append(i)
                elif 'Pincode' in i:
                    toppinamount.append(i)
            if selecttop == 'States':
                st.subheader('Top 10 States')
                #st.write('')
                statekey, stateval = st.columns([1,1])
                with statekey:
                    for i in range(0, 10):
                        st.markdown(
                            "<h2 style= 'color: black;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                topstateamount[i][0].title()),
                            unsafe_allow_html=True)
                with stateval:
                    for i in range(0, 10):
                        st.markdown(
                            "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                format_currency(topstateamount[i][4], 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)

            elif selecttop == 'Districts':
                st.subheader('Top 10 Districts')
                #st.write('')
                diskey,disval=st.columns([1, 1])
                with diskey:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: black;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(topdistamount[i][0].title()),
                            unsafe_allow_html=True)
                with disval:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(format_currency(topdistamount[i][4], 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)
            else:
                st.subheader('Top 10 Pincodes')
                #st.write('')
                pinkey,pinval=st.columns([1,1])
                with pinkey:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: black;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(toppinamount[i][0].title()),
                            unsafe_allow_html=True)
                with pinval:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(format_currency(toppinamount[i][4], 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)

        else:
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Users</b></h2>",unsafe_allow_html=True)

            select = 'select * from phonepe_pulse.agguser where Year={} and Quarter={}'.format(year, quarter)
            cursor.execute(select)
            result = cursor.fetchall()
            for i in result:
                registereduser=i[2]
                appopen=i[3]
            #st.write(f'Registered PhonePe users till Q{quartile} {year}'.format(quartile,year))
            st.markdown("<h2 style= 'black: white;font-weight: normal;font-size: 18px;'><b>Registered PhonePe users till Q{} {}</b></h2>".format(quarter,year),unsafe_allow_html=True)
            st.markdown(r"<h2 style= 'black: #C98BDB;font-weight: normal;font-size: 40px;'><b>{}</b></h2>".format(format_currency(registereduser,'INR', locale='en_IN')[1:-3]),unsafe_allow_html=True)
            st.markdown("<h2 style= 'black: white;font-weight: normal;font-size: 18px;'><b>PhonePe app opens in Q{} {}</b></h2>".format(quarter,year),unsafe_allow_html=True)
            if appopen!='0':
                st.markdown(r"<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 40px;'><b>{}</b></h2>".format(format_currency(appopen,'INR', locale='en_IN')[1:-3]),unsafe_allow_html=True)
                st.write('')
            elif appopen=='0':
                st.markdown(r"<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 40px;'><b>Unavailable</b></h2>", unsafe_allow_html=True)
            st.write('#')

            #selecttop=st.selectbox(label='Top 10 Records',options=['States','Districts','Pincodes'])
            selecttop = option_menu(menu_title='',icons=['bar-chart-line','bar-chart','bar-chart-line-fill'], options=['States', 'Districts', 'Pincodes'],
                                    orientation='horizontal', styles={
                    "container": {"background-color": "#480668"},
                    "icon": {"color": "orange", "font-size": "18px"},
                    "nav-link": {"font-size": "12px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#391C59"},
                    "nav-link-selected": {"background-color": "#691592"}})
            select = 'select * from phonepe_pulse.topuser where Year={} and Quarter={}'.format(year, quarter)
            cursor.execute(select)
            result = cursor.fetchall()
            userlst = []
            userstateamount = []
            userdistamount = []
            userpinamount = []
            for i in result:
                userlst.append(i[0:5])
            for i in userlst:
                if 'State' in i:
                    userstateamount.append(i)
                elif 'District' in i:
                    userdistamount.append(i)
                elif 'Pincode' in i:
                    userpinamount.append(i)

            if selecttop=='States':
                st.subheader('Top 10 States')
                st.write('')
                stateusekey,stateuseval=st.columns([2.8, 0.8])
                with stateusekey:
                    for i in range(0, 10):
                        st.markdown(
                            "<h2 style= 'color: black;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                userstateamount[i][0].title()),
                            unsafe_allow_html=True)
                with stateuseval:
                    for i in range(0, 10):
                        st.markdown(
                            "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                format_currency(userstateamount[i][4], 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)


            elif selecttop=='Districts':
                st.subheader('Top 10 Districts')
                st.write('')
                disusekey,disuseval=st.columns([2.8, 0.8])
                with disusekey:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: black;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                userdistamount[i][0].title()),
                            unsafe_allow_html=True)
                with disuseval:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                format_currency(userdistamount[i][4], 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)

            else:
                st.subheader('Top 10 Pincodes')
                st.write('')
                pinuserkey,pinuserval=st.columns([2.8, 0.8])
                with pinuserkey:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'black: white;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                userpinamount[i][0]),
                            unsafe_allow_html=True)
                with pinuserval:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                format_currency(userpinamount[i][4], 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)


if selected=='Insights':
    titleft, titmid, titrgt = st.columns([1,3,1])
    with titmid:
        st.subheader('Select Your Choice')
        #visselection=st.selectbox('',['Transaction','Users','Top 10 ( State ,District ,Pincode )','Mobile Brand'])
        visselection=option_menu(menu_title='',icons=['send','people-fill','sort-numeric-up','phone-fill'], options=['Transaction and Payment', 'Users', 'Top 10','Brand details'],
                                    orientation='horizontal', styles={
                    "container": {"background-color": 'white'},
                    "icon": {"color": "orange", "font-size": "18px"},
                    "nav-link": {"font-size": "12px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#391C59"},
                    "nav-link-selected": {"background-color": "#691592"}})

    rightcon,midcol,leftcon=st.columns([2,0.5,1.3])
    st.write('')
    with rightcon:
        if visselection=='Transaction and Payment':
            st.markdown(
                "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 48px;'><b>Transaction</b></h2>",
                unsafe_allow_html=True)
            # st.write('')
            leftcon1, leftcon2 = st.columns([3, 1])
            with leftcon1:
                transelect = st.selectbox('', ['All PhonePe Transaction', 'Total Payment', 'Average Transaction'])
            with leftcon2:
                selectedyear = st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])

            def fetchalltransaction(tranyear):
                alltranlst = []
                totalamtlst=[]
                paymentmethod=[]
                totaltran = 0
                totalamt=0
                for i in range(1, 5):
                    select1 = 'select * from phonepe_pulse.aggtrans where Year={} and Quarter={}'.format(tranyear, i)
                    cursor.execute(select1)
                    result = cursor.fetchall()
                    for i in result:
                        totaltran += i[3]
                        totalamt+=int(i[4])
                        paymentmethod.append(i[0:])
                    alltranlst.append(totaltran)
                    totalamtlst.append(totalamt)
                    totaltran = 0
                    totalamt=0
                return alltranlst,totalamtlst,paymentmethod

            if transelect=='All PhonePe Transaction':
                Alltransaction,tot,paymenttype1=fetchalltransaction(selectedyear)
                Alltransactionqrt=['Q1','Q2','Q3','Q4']
                Alltransactionamt={Alltransaction[0],Alltransaction[1],Alltransaction[2],Alltransaction[3]}
                trandf=pd.DataFrame([Alltransactionqrt,Alltransactionamt],index=['Quarter','All Transaction']).T
                st.write('')
                # st.write('')
                # st.write('')
                st.markdown(
                    "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>All PhonePe Transaction</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                fig=px.bar(trandf,x='Quarter',y='All Transaction',color='Quarter',height=500)
                fig.update_traces( textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)
                ptq1 = []
                ptq2 = []
                ptq3 = []
                ptq4 = []
                ptq5 = []
                for i in paymenttype1:
                    if 1 in i:
                        ptq1.append(i)
                    elif 2 in i:
                        ptq2.append(i)
                    elif 3 in i:
                        ptq3.append(i)
                    elif 4 in i:
                        ptq4.append(i)
                    elif 5 in i:
                        ptq5.append(i)
                ptname1 = []
                ptcount1 = []
                ptname2 = []
                ptcount2 = []
                ptname3 = []
                ptcount3 = []
                ptname4 = []
                ptcount4 = []
                pq1 = []
                pq2 = []
                pq3 = []
                pq4 = []
                for i in range(5):
                    ptname1.append(ptq1[i][2])
                    ptcount1.append(ptq1[i][3])
                    pq1.append(ptq1[i][-1])
                for i in range(5):
                    ptname2.append(ptq2[i][2])
                    ptcount2.append(ptq2[i][3])
                    pq2.append(ptq2[i][-1])
                for i in range(5):
                    ptname3.append(ptq3[i][2])
                    ptcount3.append(ptq3[i][3])
                    pq3.append(ptq3[i][-1])
                for i in range(5):
                    ptname4.append(ptq4[i][2])
                    ptcount4.append(ptq4[i][3])
                    pq4.append(ptq4[i][-1])
                dicq1 = {'Type': ptname1, 'Count': ptcount1, 'Quartile': pq1}
                dicq2 = {'Type': ptname2, 'Count': ptcount2, 'Quartile': pq2}
                dicq3 = {'Type': ptname3, 'Count': ptcount3, 'Quartile': pq3}
                dicq4 = {'Type': ptname4, 'Count': ptcount4, 'Quartile': pq4}
                df1 = pd.DataFrame(dicq1)
                df2 = pd.DataFrame(dicq2)
                df3 = pd.DataFrame(dicq3)
                df4 = pd.DataFrame(dicq4)
                pie1, pie2  = st.columns([1,1])
                with pie1:
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 32px;'><b>1st Quarter</b></h2>",
                        unsafe_allow_html=True)
                    fig1 = px.pie(df1, values='Count', names='Type', labels='Type', hole=.4, height=400, width=350)
                    fig1.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',}
                    )
                    st.plotly_chart(fig1)
                #with pie3:
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 32px;'><b>3rd Quarter</b></h2>",
                        unsafe_allow_html=True)
                    fig2 = px.pie(df3, values='Count', names='Type', labels='Type', hole=.4, height=400, width=350)
                    fig2.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                    )
                    st.plotly_chart(fig2)

                with pie2:
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 32px;'><b>2nd Quarter</b></h2>",
                        unsafe_allow_html=True)
                    fig1 = px.pie(df2, values='Count', names='Type', labels='Type', hole=.4, height=400, width=350)
                    fig1.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                    )
                    st.plotly_chart(fig1)
                #with pie4:
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 32px;'><b>4th Quarter</b></h2>",
                        unsafe_allow_html=True)
                    fig2 = px.pie(df4, values='Count', names='Type', labels='Type', hole=.4, height=400, width=350)
                    fig2.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                    )
                    st.plotly_chart(fig2)

            elif transelect=='Total Payment':
                Alltran,totalpayment,paymenttype2=fetchalltransaction(selectedyear)
                totaltranqrt = ['Q1', 'Q2', 'Q3', 'Q4']
                Alltransactionamt = {totalpayment[0], totalpayment[1], totalpayment[2], totalpayment[3]}
                trandf = pd.DataFrame([totaltranqrt, Alltransactionamt], index=['Quarter', 'Total Payments']).T
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Total Payment</b></h2>",
                    unsafe_allow_html=True)

                st.write('')
                fig = px.bar(trandf, x='Quarter', y='Total Payments',color='Quarter')
                fig.update_traces( textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

            elif transelect=='Average Transaction':
                avgtran,avgpay,paymenttype3=fetchalltransaction(selectedyear)
                avglst=[]
                for i in range(4):
                    avglst.append(avgpay[i]/avgtran[i])
                avgqrt = ['Q1', 'Q2', 'Q3', 'Q4']
                trandf = pd.DataFrame([avgqrt, avglst], index=['Quarter', 'Average Transaction']).T
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Average Transaction</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                fig = px.bar(trandf, x='Quarter', y='Average Transaction',text='Average Transaction',color='Quarter')
                fig.update_traces(textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

        elif visselection=='Users':
            st.markdown(
                "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 48px;'><b>Users</b></h2>",
                unsafe_allow_html=True)

            def fetchregistereduser(useryear,userqrt):
                mapuserstate = []
                select = 'select * from phonepe_pulse.mapuser where Year={} and Quarter={} '.format(useryear,userqrt )
                cursor.execute(select)
                result = cursor.fetchall()
                for i in (result):
                    mapuserstate.append(i)
                return mapuserstate

            leftcon1,leftcon2, leftcon3 = st.columns([2, 1,1])
            with leftcon1:
                userselect=st.selectbox('',['Registered Phonepe','App Opens'])
            with leftcon2:
                selectedyear = st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])
            with leftcon3:
                selectedqrt= st.selectbox('',['1','2','3','4'])

            if userselect=='Registered Phonepe':
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Registered Phonepe Users</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                val=fetchregistereduser(selectedyear,selectedqrt)
                state=[]
                count=[]
                qrt=[]
                year=[]
                for i in val:
                    state.append(i[2].title())
                    count.append(i[3])
                    qrt.append(i[1])
                    year.append(str(i[0]))
                userdic={'State':state,'Count':count,'Quartile':qrt,'Year':year}
                df=pd.DataFrame(userdic)

                fig=px.bar(df,x='State',y='Count',color='State',width=850,height=700)
                #fig.update_traces( textposition='outside')

                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                                )
                st.plotly_chart(fig)

            elif userselect=='App Opens':
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>App Opens</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                val = fetchregistereduser(selectedyear, selectedqrt)
                state = []
                Open = []
                qrt = []
                year = []
                for i in val:
                    print(i)
                    state.append(i[2].title())
                    Open.append(i[4])
                    qrt.append(i[1])
                    year.append(str(i[0]))
                userdic = {'State': state, 'AppOpens': Open, 'Quartile': qrt, 'Year': year}
                df = pd.DataFrame(userdic)
                fig = px.bar(df, x='State', y='AppOpens',color='State', width=850,height=700)
                #fig.update_traces( textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

        elif visselection=='Top 10':
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 48px;'><b>Top 10 - State , District , Pincode</b></h2>",unsafe_allow_html=True)
            topselect=st.selectbox('',['State','District','Pincode'])
            def fetchtopten(topyear,topqrt):
                select = 'select * from phonepe_pulse.topuser where Year={} and Quarter={}'.format(topyear, topqrt)
                cursor.execute(select)
                result = cursor.fetchall()
                userlst = []
                userstateamount = []
                userdistamount = []
                userpinamount = []
                for i in result:
                    userlst.append(i[0:])
                for i in userlst:
                    if 'State' in i:
                        userstateamount.append(i)
                    elif 'District' in i:
                        userdistamount.append(i)
                    elif 'Pincode' in i:
                        userpinamount.append(i)
                topdic={'State':userstateamount,'District':userdistamount,'Pincode':userpinamount}
                return  topdic

            if topselect=='State':
                topstateright,topstateleft=st.columns([1,1])
                with topstateright:
                    topstatyear=st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])
                with topstateleft:
                    topstatqrt=st.selectbox('', ['1', '2', '3', '4'])

                state=fetchtopten(topstatyear,topstatqrt)
                df=pd.DataFrame(state['State'],columns=['Entity_Name','Year','Quarter','Type','Registered_User'])
                df['State']=df['Entity_Name'].str.title()
                df['Year']=df['Year'].astype('str')
                #df['Registered_User']=df['Registered_User'].astype('str')
                #st.dataframe(df)
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Top 10 State</b></h2>",
                    unsafe_allow_html=True)

                st.write('')
                fig=px.area(df,x='Entity_Name',y='Registered_User',text='Registered_User',color='Entity_Name',width=810,height=600)
                #fig.update_traces(textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

            elif topselect == 'District':
                topcounright, topcounleft = st.columns([1, 1])
                with topcounright:
                    topcounyear = st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])
                with topcounleft:
                    topcounqrt = st.selectbox('', ['1', '2', '3', '4'])

                district = fetchtopten(topcounyear, topcounqrt)
                df = pd.DataFrame(district['District'], columns=['Entity_Name','Year','Quarter','Type','Registered_User'])
                df['District'] = df['Entity_Name'].str.title()
                df['Year'] = df['Year'].astype('str')
                #st.dataframe(df)
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Top 10 District</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                fig = px.bar(df, x='Entity_Name', y='Registered_User', text='Registered_User', color='Entity_Name', width=810, height=600)
                #fig.update_traces( textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

            elif topselect == 'Pincode':
                toppinright, toppinleft = st.columns([1, 1])
                with toppinright:
                    toppinyear = st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])
                with toppinleft:
                    toppinqrt = st.selectbox('', ['1', '2', '3', '4'])

                pincode = fetchtopten(toppinyear, toppinqrt)
                df = pd.DataFrame(pincode['Pincode'], columns=['Entity_Name','Year','Quarter','Type','Registered_User'])
                df['Pincode'] = df['Entity_Name'].astype('str')
                df['Year'] = df['Year'].astype('str')
                #st.dataframe(df)
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Top 10 Pincode</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                fig = px.bar(df, x='Entity_Name', y='Registered_User', text='Registered_User', color='Entity_Name', width=810, height=600)
                fig.update_traces(textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

        elif visselection == 'Brand details':
            st.markdown(
                "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 48px;'><b>Mobile Brand</b></h2>",
                unsafe_allow_html=True)

            years,qurtrs = st.columns([1,1])

            with years:
                yearselect = st.selectbox(' ', [2018,2019,2020,2021,2022])

            with qurtrs:
                qurtsselect = st.selectbox('',[1,2,3,4])

            select = 'select * from phonepe_pulse.mobile where Year={} and Quarter={}'.format(yearselect, qurtsselect)
            cursor.execute(select)
            result = cursor.fetchall()
            col = {'Brand': [],
                   'Count': [], 'Percentage': []}
            Brand = col['Brand']
            for i in result:
                col['Brand'].append(i[2])
                col['Count'].append(i[3])
                col['Percentage'].append(i[4])
            df = pd.DataFrame(col, columns=['Brand', 'Count'])
            fig = px.bar(df, x='Brand', y= 'Count', text= 'Count', color='Brand')
            fig.update_traces(textposition='outside')
            fig.update_layout(
                {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
            )
            st.plotly_chart(fig)

    with leftcon:
        if visselection=='Transaction and Payment':
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.write('#')
            st.markdown("<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Transaction Data</b></h2>",unsafe_allow_html=True)
            st.write('')
            if transelect=='All PhonePe Transaction':
                rtcol1,rtcol2, rtcol3 = st.columns([0.5,1,0.5])
                with rtcol1:
                    st.subheader('Quarter')
                    for i in range(4):
                        st.write(trandf['Quarter'][i])
                with rtcol2:
                    st.subheader('All Transaction')
                    for i in range(4):
                        st.write(str(trandf['All Transaction'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(4):
                        st.write(str(selectedyear))

            elif transelect=='Total Payment':
                rtcol1, rtcol2, rtcol3 = st.columns([0.5, 1, 0.5])
                with rtcol1:
                    st.subheader('Quarter')
                    for i in range(4):
                        st.write(trandf['Quarter'][i])
                with rtcol2:
                    st.subheader('Total Payments')
                    for i in range(4):
                        st.write(str(trandf['Total Payments'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(4):
                        st.write(str(selectedyear))
            elif transelect=='Average Transaction':
                rtcol1, rtcol2, rtcol3 = st.columns([0.5, 1, 0.5])
                with rtcol1:
                    st.subheader('Quarter')
                    for i in range(4):
                        st.write(trandf['Quarter'][i])
                with rtcol2:
                    st.subheader('Avg Transaction')
                    for i in range(4):
                        st.write(str(trandf['Average Transaction'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(4):
                        st.write(str(selectedyear))


        elif visselection=='Users':
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.write('')
            st.write('')
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Users Data</b></h2>",unsafe_allow_html=True)

            st.write('')
            if userselect=='Registered Phonepe':
                rtcol1, rtcol2 = st.columns([1.8, 1])
                with rtcol1:
                    st.subheader('State')
                    for i in range(36):
                        st.write(df['State'][i])
                with rtcol2:
                    st.subheader('Registered_Count')
                    for i in range(36):
                        st.write(str(df['Count'][i]))
                # with rtcol3:
                #st.subheader('Year')
                #for i in range(36):
                #st.write(str(selectedyear))
            elif userselect=='App Opens':
                rtcol1, rtcol2 = st.columns([1.8, 1])
                with rtcol1:
                    st.subheader('State')
                    for i in range(36):
                        st.write(df['State'][i])
                with rtcol2:
                    st.subheader('AppOpens')
                    for i in range(36):
                        st.write(str(df['AppOpens'][i]))
                # with rtcol3:
                #st.subheader('Year')
                #for i in range(36):
                #t.write(str(selectedyear))


        elif visselection=='Top 10':
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.write('')
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Top 10 Data</b></h2>",unsafe_allow_html=True)

            st.write('')
            if topselect=='State':
                rtcol1, rtcol2 = st.columns([1.5, 1.9])
                with rtcol1:
                    st.subheader('State')
                    for i in range(10):
                        st.write(df['State'][i])
                with rtcol2:
                    st.subheader('Registered_User')
                    for i in range(10):
                        st.write(str(df['Registered_User'][i]))


            elif topselect=='District':
                rtcol1, rtcol2, rtcol3= st.columns([1.5, 1.9])
                with rtcol1:
                    st.subheader('District')
                    for i in range(10):
                        st.write(df['District'][i])
                with rtcol2:
                    st.subheader('Registered_User')
                    for i in range(10):
                        st.write(str(df['Registered_User'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(10):
                        st.write(str(topcounyear))

            #elif topselect=='Pincode':
            else:
                rtcol1, rtcol2, rtcol3 = st.columns([1.5, 1.9])
                with rtcol1:
                    st.subheader('Pincode')
                    for i in range(10):
                        st.write(df['Pincode'][i])
                with rtcol2:
                    st.subheader('Registered_User')
                    for i in range(10):
                        st.write(str(df['Registered_User'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(10):
                        st.write(str(toppinyear))


        elif visselection=='Brand details':

            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown("<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Top Brands </b></h2>",unsafe_allow_html=True)

            #st.write('')
            brandcol, countcol, percentcol = st.columns([0.5, 0.5, 0.5])
            with brandcol:
                st.subheader('Brands')
                for i in range(5):
                    st.markdown(
                        "<h2 style= 'black: white;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                            Brand[i]),
                        unsafe_allow_html=True)

                    st.write(' ')

            with countcol:
                st.subheader('Counts')
                for i in range(5):
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                            format_currency(col['Count'][i], 'INR', locale='en_IN')[1:-3]),
                        unsafe_allow_html=True)
                    st.write(' ')

            with percentcol:
                st.subheader('Percentage')
                for i in range(5):
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                            col['Percentage'][i])[0:],
                        unsafe_allow_html=True)
                    st.write(' ')