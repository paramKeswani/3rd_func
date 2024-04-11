from flask import Flask, render_template, request
import pandas as pd
import helper
import json

import plotly

app = Flask(__name__)

# Read the CSV file
# df = pd.read_excel('data.xlsx')
# df = pd.read_csv("final.csv")

# Extract unique state, city, and restaurant names and sort them
unique_states = "karnataka"
unique_cities = "Bangalore"
# restaurant_name1 = sorted(df['res_name'].unique())
# restaurant_name2 = sorted(df['res_name'].unique())

# df = pd.read_excel('data.xlsx')
#
#
#
#
#
# loc_list = df['location'].unique()
#
# print("loc_list")
# print(loc_list)
# # locality = st.selectbox('Select Locality', loc_list)
# df4 = df[df.location == "Residency Road"]
#
# print(df4)
# df5 = df4.reset_index(drop=True)
# print("df5")
# print(df5)
# loc_count = df[df.location == "Residency Road"]['location'].value_counts()
# fig = helper.locality_count(loc_count)
# # st.plotly_chart(fig)
#
#
# df_loc = pd.read_csv("locations.csv")
#
# lat = [i for i in df_loc['latitude']]
# # print("lat" + lat)
# long = [j for j in df_loc['longitude']]
# # print("long" + long)
#
# map2 = helper.mul_rest(df5, lat, long)
# st.subheader('Restaurant in ' + locality + ' on basis of price range')
# st_folium(map2, width=800, height=550)
# st.subheader('Restaurant in ' + locality + ' on basis of Rating')
# map2 = helper.mul_rest_rating(df5, lat, long)
df = pd.read_csv('final.csv')
# st_folium(map2, width=800, height=550)
# st_folium(map2, width=800, height=550)

state_list = df['state'].sort_values().unique()
state = "Karnataka"
city_list = df[df.state == state]['city'].unique()
city = "Banglore"
df4 = df[(df.state == state) & (df.city == city)]
print("df4")
print(df4.columns)
loc_list = df4['locality'].unique()

dfloc = pd.read_csv('locations.csv')

df_loc = dfloc["name"]

state_list = df['state'].sort_values().unique()
state = "Karnataka"
city_list = df[df.state == state]['city'].unique()
city = "Bangalore"
df4 = df[(df.state == state) & (df.city == city)]
print("df4")
print(df4)
loc_list = df4['locality'].unique()

print("loc_list")
print(loc_list)


# Define routes
@app.route('/')
def index():
    map1 = 0
    map2 = 0
    return render_template('restaurant_on_map.html',
                           unique_states=unique_states,
                           unique_cities=unique_cities,
                           loc_list=loc_list,
                           map1 = map1,
                           map2 = map2
                           )


# @app.route('/', methods=['POST'])
@app.route('/', methods=['POST'])
def submit():
    locality = request.form["loc"]

    state_list = df['state'].sort_values().unique()
    state = "Karnataka"
    city_list = df[df.state == state]['city'].unique()
    city = "Bangalore"
    df4 = df[(df.state == state) & (df.city == city)]

    loc_list = df4['locality'].unique()


    # locality = st.selectbox('Select Locality', loc_list)
    df4 = df4[df4.locality == locality]
    df5 = df4.reset_index(drop=True)
    # print("df5")
    # print(df5.columns)
    loc_count = df[df.city == city]['locality'].value_counts()


    lat = [i for i in df5['latitude']]
    print("lat")
    print(lat)
    long = [j for j in df5['longitude']]
    print("long")
    print(long)
    map1 = helper.mul_rest(df5, lat, long)
    # st.subheader('Restaurant in ' + locality + ' on basis of price range')
    # st_folium(map2, width=800, height=550)
    # st.subheader('Restaurant in ' + locality + ' on basis of Rating')
    map2 = helper.mul_rest_rating(df5, lat, long)
    if map1 is not None and map2 is not None:
        map1_html = map1._repr_html_()
        map2_html = map2._repr_html_()

        return render_template('restaurant_on_map.html',
                               map1_html=map1_html,
                               map2_html=map2_html,
                               locality=locality)
    else:
        return "No data available for the selected locality."
# def submit():
#     selected_state = request.form['state']
#     selected_city = request.form['city']
#
#     locality = request.form['loc']
#     df = pd.read_excel('data.xlsx')
#
#     loc_list = df['location'].unique()
#
#     print("loc_list")
#     print(loc_list)
#     # locality = st.selectbox('Select Locality', loc_list)
#     df4 = df[df.location == locality]
#
#     print(df4)
#     df5 = df4.reset_index(drop=True)
#     print("df5")
#     print(df5)
#     loc_count = df[df.location == locality]['location'].value_counts()
#     # fig = helper.locality_count(loc_count)
#     # st.plotly_chart(fig)
#
#     df_loc = pd.read_csv("locations.csv")
#
#     lat = [i for i in df_loc['latitude']]
#     # print("lat" + lat)
#     long = [j for j in df_loc['longitude']]
#     # print("long" + long)
#
#     # map2 = helper.mul_rest(df5, lat, long)
#     # st.subheader('Restaurant in ' + locality + ' on basis of price range')
#     # st_folium(map2, width=800, height=550)
#     # st.subheader('Restaurant in ' + locality + ' on basis of Rating')
#     # map2 = helper.mul_rest_rating(df5, lat, long)
#     # st_folium(map2, width=800, height=550)
#
#
#
#
#
#     # rest1 = df[df.res_name == rest_1]['id']
#     # if not rest1.empty:
#     #     rest1 = rest1.reset_index(drop=True)[0]
#     # else:
#     #     # Handle case when no matching restaurant is found
#     #     return "Restaurant 1 not found."
#     #
#     # rest2 = df[df.res_name == rest_2]['id']
#     # if not rest2.empty:
#     #     rest2 = rest2.reset_index(drop=True)[0]
#     # else:
#     #     # Handle case when no matching restaurant is found
#     #     return "Restaurant 2 not found."
#
#     map1 = helper.mul_rest(df5, lat, long)
#     map2 = helper.mul_rest_rating(df5, lat, long)
#
#     # n1 = list(df[df.id == rest1]['res_name'])[0]
#     # n2 = list(df[df.id == rest2]['res_name'])[0]
#
#     # graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
#     # print(graphJSON1)
#     # graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
#     # print(graphJSON2)
#
#     return render_template('restaurant_on_map.html',
#                            # graphJSON1=graphJSON1,
#                            # graphJSON2=graphJSON2,
#                            # restaurant1=n1,
#                            # restaurant2=n2,
#                            selected_state = selected_state,
#                            selected_city = selected_city,
#                            map1 = map1,
#                            map2 = map2,
#                            locality = locality)
#

if __name__ == '__main__':
    app.run(debug=True)
