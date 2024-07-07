import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load the updated data
file_path = "C://Users//HP//GUVI_PROJ//Air_Second_five.csv"
df = pd.read_csv(file_path)

# Function for the home page
def home_page():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://skift.com/wp-content/uploads/2014/07/airbnb.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: lightgreen; /* Change color to dark pink */
            font-size: 20px;
            font-weight: bold;
            font-family: 'Times New Roman', Times, serif; /* Change font to Times New Roman */
        }
         .top-center-image {
            position: fixed;
            top: 5px;
            left: 50%;
            transform: translateX(-50%);
            width: 450px; /* Adjust the size as needed */
            z-index: 10;
        }
        .stApp h1 {
            font-size: 48px;
            margin-bottom: 20px;
            color: skyblue; /* Change color to dark blue */
            font-weight: bold; /* Increase font weight for h1 */
        }
        .stApp h2 {
            color: skyblue; /* Change color to dark red */
            font-size: 30px;
            font-weight: bold; /* Increase font weight for h2 */
            margin-bottom: 10px;
        }
        .stApp p, .stApp ul li {
            font-size: 24px;
            line-height: 1.6;
            margin-bottom: 20px;
            font-weight: bold; /* Increase font weight for paragraphs and list items */
            color: lightgreen; /* Change text color to dark pink */
        }
        .stButton>button {
            background-color: darkpink;
            color: black;
            font-size: 24px;
            font-weight: bold; /* Increase font weight for button text */
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<img src="https://cdn-eahjn.nitrocdn.com/ChEvwayTHZmZJUAdsUNMLXuXZdBprFoQ/assets/images/optimized/rev-efee877/www.spinxdigital.com/app/uploads/2022/11/image-airbnb.jpg" class="top-center-image">', unsafe_allow_html=True)
    st.markdown('<div class="stApp">', unsafe_allow_html=True)
    st.title("Welcome to Airbnb")
    st.markdown(
        """
        Airbnb is an online marketplace that connects people who want to rent out their homes with people who are looking for accommodations. Whether you're a traveler looking for unique lodging experiences or a host wanting to earn money by renting out your space, Airbnb offers a platform for listing, discovering, and booking unique stays around the world.

        <h2>Key Features:</h2>
        Travelers: Find affordable, unique, and personalized lodging experiences.
        Hosts: Earn money by renting out your space, be it a spare room, an apartment, or an entire house.
        Communities: Benefit from tourism and cultural exchange.

        Ready to explore Airbnb? Click the button below to get started!
        """,
        unsafe_allow_html=True
    )
    if st.button("Explore Airbnb Data"):
        st.session_state.page = "analysis"
    
    st.markdown('</div>', unsafe_allow_html=True)

# Function for the analysis page
def analysis_page():
    st.markdown(
        """
        <style>
        .top-left-image {
            position: absolute;
            top: 15px;
            left: 10px;
            width: 300px; /* Adjust the size as needed */
            z-index: 10;
        }
        .top-right-image {
            position: absolute;
            top: 0px;
            right: 10px;
            width: 400px; /* Adjust the width as needed */
            height: 210px; /* Adjust the height as needed */
            z-index: 10;
        }
        .stAppAnalysis {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 200px; /* Adjust padding to avoid overlap with image */
        }
        .skyblue {
            color: skyblue;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<img src="https://cloudfront-us-east-2.images.arcpublishing.com/reuters/BXA3NGY2DZPMHACHL2LCJ3JRO4.jpg" class="top-left-image">', unsafe_allow_html=True)
    st.markdown('<img src="https://img.freepik.com/premium-photo/data-visualization-information-representation-datadriven-insights-analytical-brilliance-graphical-data-exploration-data-brilliant-color-generated-by-ai_661108-16388.jpg" class="top-right-image">', unsafe_allow_html=True)
    st.markdown('<div class="stAppAnalysis">', unsafe_allow_html=True)
    st.markdown('<h1 style="color: lightgreen;">Airbnb Data Analysis and Exploration</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: skyblue;">Why to explore Airbnb Data?</h3>', unsafe_allow_html=True)
    st.markdown(
        """
        
       
1.Understanding Pricing Dynamics:

Investors: Helps in identifying profitable property types and pricing strategies.

Travelers: Allows for budget planning and understanding cost variations based on accommodation type and location.

2.Property Type Insights:

Investors: Guides decisions on property acquisition and management based on market demand for different types of accommodations.

Travelers: Facilitates choosing accommodations that suit preferences and needs.

3.Availability Analysis:

Investors: Assists in managing property occupancy and planning marketing strategies.

Travelers: Helps in scheduling trips based on availability and booking patterns.

4.Customer Satisfaction (Rating):

Investors: Influences reputation management and operational improvements to enhance guest experience.

Travelers: Provides insights into the quality of accommodations and helps in making informed booking decisions.

5.Geographic Insights:

Investors: Supports location-based investment decisions and market expansion strategies.

Policymakers: Informs regulatory decisions regarding short-term rentals and their impact on local communities.

6.Amenities and Features:

Investors: Guides property enhancement decisions to attract specific customer segments.

Travelers: Facilitates selecting accommodations that meet specific amenity preferences.

Overall, these analyses contribute to informed decision-making across various aspects of the short-term rental market, improving operational efficiency, customer satisfaction, and profitability for stakeholders involved in or affected by the Airbnb ecosystem.
        

        """
    )
    st.markdown('<h3 style="color: skyblue;">Select an analysis to learn more about the Airbnb data.</h3>',unsafe_allow_html=True)   
    analysis_options = [
        "Analysis of the relationship between Price and Accommodation",
        'Analysis of relationship between Price and Property_type',
        'Analysis of relationship among Property_Type, Weekly_price, and Monthly_Price',
        'Analysis of the relationship between property_type, availability_365, availability_30, availability_60, availability_90',
        "Analysis of the relationship between Property_Type and rating",
        'Analysis of the relationship between price and rating',
        'Analysis of the relationship between price and availability',
        'Fetch the property_type, listing, accomodation and amenities for the desired price and country',
        "Fetch the name, price, accommodates, amenities, street for the specified country and property_type",
        "Fetch the name, country, street, number of bathrooms and bedrooms for the desired property_type",
        "Analysis of home stay count for each country",
        "Analysis of country based on the sorted order of average ratings given to home stays in that particular country"
    ]
    analysis_choice = st.selectbox("Select an analysis to learn more", analysis_options)
    if st.button("Go to Analysis"):
        st.session_state.page = "visualization"
        st.session_state.analysis_choice = analysis_choice
    
    if st.button("Back to Home"):
        st.session_state.page = "home"
    
    st.markdown('</div>', unsafe_allow_html=True)
def visualization_page():
    image_url = "https://cdn.sanity.io/images/tlr8oxjg/production/f0a4a4cffc25b2f7253300a27c58687a28808c7a-1456x816.png?w=3840&q=80&fit=clip&auto=format"
    st.image(image_url, use_column_width=True)


    st.title("Airbnb Data Visualization")
    st.write(f"You selected: {st.session_state.analysis_choice}")
    analysis = st.session_state.analysis_choice
    
    # Analysis Visualizations
    
    if analysis == 'Analysis of the relationship between Price and Accommodation':
        # Display the average price
        st.markdown('<h3 style="color: skyblue;">This analysis examines how the price of a rental property varies with the number of people it can accommodate.</h3>', unsafe_allow_html=True)
        st.markdown('<h3 style="color: skyblue;">It aims to determine if there is a correlation between the accommodation capacity and the rental price.</h3>',unsafe_allow_html=True)
        st.markdown('<h3 style="color: skyblue;"></h3>',unsafe_allow_html=True)     
        # Group by 'accommodates' and calculate the average price</h3>', unsafe_allow_html=True)
        

        avg_price_by_accommodates = df.groupby('accommodates')['price'].mean().reset_index()

        # Add a dropdown menu for selecting the average price and accommodation capacity
        options = avg_price_by_accommodates.apply(lambda row: f"Accommodates {row['accommodates']}: ${row['price']:.2f}", axis=1).tolist()
        selected_option = st.selectbox('Select the average price for an accommodation capacity:', options)

        # Extract the selected accommodation value and price
        selected_accommodates, selected_avg_price = map(float, selected_option.replace('Accommodates ', '').replace('$', '').split(': '))

        # Fetch the names with prices close to the selected average price and accommodation value
        tolerance = 10  # Define a tolerance range for price matching
        matching_listings = df[(df['accommodates'] == selected_accommodates) & (df['price'].between(selected_avg_price - tolerance, selected_avg_price + tolerance))]

        # Display the matching listings
        st.subheader(f"Listings with {int(selected_accommodates)} accommodations close to the average price of ${selected_avg_price:.2f}")
        st.write(matching_listings[['name', 'price']])

        # Create a bar chart to show the average price for each accommodation type
        fig = px.bar(
            avg_price_by_accommodates,
            x='accommodates',
            y='price',
            title='Average Price by Accommodation Capacity',
            labels={'accommodates': 'Accommodation Capacity', 'price': 'Average Price'},
            color='price',
            color_continuous_scale='Viridis'
        )

        # Customize the layout
        fig.update_layout(
            xaxis_title='Accommodation Capacity',
            yaxis_title='Average Price',
            showlegend=False
        )

        # Show the plot using Streamlit's Plotly support
        st.plotly_chart(fig)

    elif analysis == 'Analysis of relationship between Price and Property_type':
        # Group by 'property_type' and calculate the average price
        st.markdown('<h3 style="color: skyblue;">This analysis explores the relationship between the type of property (e.g., apartment, house, villa) and its rental price.</h3>',unsafe_allow_html=True)     
        st.markdown('<h3 style="color: skyblue;">It helps to identify which property types tend to be more or less expensive.</h3>',unsafe_allow_html=True) 
        avg_price_by_property_type = df.groupby('property_type')['price'].mean().reset_index()
        
        # Create a bar chart to visualize the relationship between price and property_type
        fig_property_type = px.bar(
            avg_price_by_property_type,
            x='property_type',
            y='price',
            title='Average Price by Property Type',
            labels={'property_type': 'Property Type', 'price': 'Average Price'},
            color='price',
            color_continuous_scale='Plasma'
        )

        # Customize the layout
        fig_property_type.update_layout(
            xaxis_title='Property Type',
            yaxis_title='Average Price',
            showlegend=False
        )

        # Show the plot using Streamlit's Plotly support
        st.plotly_chart(fig_property_type)

        # Display the data of the relationship between price and property_type in the form of a table
        st.subheader("Average Price by Property Type")
        st.write(avg_price_by_property_type)

    elif analysis == 'Analysis of relationship among Property_Type, Weekly_price, and Monthly_Price':
        # Group by 'property_type' and calculate the average weekly and monthly price
        avg_weekly_monthly_price_by_property_type = df.groupby('property_type')[['weekly_price', 'monthly_price']].mean().reset_index()
        st.markdown('<h3 style="color: skyblue;">This analysis looks at the availability of different property types over various timeframes (365 days, 30 days, 60 days, 90 days).</h3>',unsafe_allow_html=True) 
        st.markdown('<h3 style="color: skyblue;">It helps to understand how the availability of properties changes with the type of property and different time periods.</h3>',unsafe_allow_html=True) 
              
        # Melt the dataframe to have 'weekly_price' and 'monthly_price' in a single column
        melted_df = avg_weekly_monthly_price_by_property_type.melt(id_vars='property_type', value_vars=['weekly_price', 'monthly_price'], 
                                                                var_name='Price Type', value_name='Average Price')

        # Create a grouped bar chart to visualize the relationship between property_type and weekly_price, monthly_price
        fig_weekly_monthly = px.bar(
            melted_df,
            x='property_type',
            y='Average Price',
            color='Price Type',
            barmode='group',
            title='Average Weekly and Monthly Price by Property Type',
            labels={'property_type': 'Property Type', 'Average Price': 'Average Price'}
        )

        # Customize the layout
        fig_weekly_monthly.update_layout(
            xaxis_title='Property Type',
            yaxis_title='Average Price'
        )

        # Show the plot using Streamlit's Plotly support
        st.plotly_chart(fig_weekly_monthly)

        # Display the data of the relationship between property_type and weekly_price, monthly_price in the form of a table
        st.subheader("Average Weekly and Monthly Price by Property Type")
        st.write(avg_weekly_monthly_price_by_property_type)

    elif analysis == 'Analysis of the relationship between property_type, availability_365, availability_30, availability_60, availability_90':
        # Group by 'property_type' and calculate the average availability for each period
        avg_availability_by_property_type = df.groupby('property_type')[['availability.availability_365', 'availability.availability_30', 'availability.availability_60', 'availability.availability_90']].mean().reset_index()
        st.markdown('<h3 style="color: skyblue;">This analysis looks at the availability of different property types over various timeframes (365 days, 30 days, 60 days, 90 days).</h3>',unsafe_allow_html=True) 
        st.markdown('<h3 style="color: skyblue;">It helps to understand how the availability of properties changes with the type of property and different time periods.</h3>',unsafe_allow_html=True)
        
        
        # Melt the dataframe to have 'availability_365', 'availability_30', 'availability_60', and 'availability_90' in a single column
        melted_availability_df = avg_availability_by_property_type.melt(id_vars='property_type', value_vars=['availability.availability_365', 'availability.availability_30', 'availability.availability_60', 'availability.availability_90'], 
                                                                        var_name='Availability Period', value_name='Average Availability')

        # Create a grouped bar chart to visualize the relationship between property_type and availability periods
        fig_availability = px.bar(
            melted_availability_df,
            x='property_type',
            y='Average Availability',
            color='Availability Period',
            barmode='group',
            title='Average Availability by Property Type and Period',
            labels={'property_type': 'Property Type', 'Average Availability': 'Average Availability'}
        )

        # Customize the layout
        fig_availability.update_layout(
            xaxis_title='Property Type',
            yaxis_title='Average Availability'
        )

        # Show the plot using Streamlit's Plotly support
        st.plotly_chart(fig_availability)

        # Display the data of the relationship between property_type and availability in the form of a table
        st.subheader("Average Availability by Property Type and Period")
        st.write(avg_availability_by_property_type)

    elif analysis == "Analysis of the relationship between Property_Type and rating":
        # Group by 'property_type' and calculate the average review score rating
        avg_rating_by_property_type = df.groupby('property_type')['review_scores.review_scores_rating'].mean().reset_index()
        st.markdown('<h3 style="color: skyblue;">This analysis examines the relationship between the type of property and its ratings.</h3>',unsafe_allow_html=True) 
        st.markdown('<h3 style="color: skyblue;">It helps to identify if certain property types tend to receive higher or lower ratings from guests.</h3>',unsafe_allow_html=True)
        
        # Create a bar chart to visualize the relationship between property_type and rating
        fig_rating = px.bar(
            avg_rating_by_property_type,
            x='property_type',
            y='review_scores.review_scores_rating',
            title='Average Rating by Property Type',
            labels={'property_type': 'Property Type', 'review_scores.review_scores_rating': 'Average Rating'},
            color='review_scores.review_scores_rating',
            color_continuous_scale='Cividis'
        )

        # Customize the layout
        fig_rating.update_layout(
            xaxis_title='Property Type',
            yaxis_title='Average Rating',
            showlegend=False
        )

        # Show the plot using Streamlit's Plotly support
        st.plotly_chart(fig_rating)

        # Display the data of the relationship between property_type and rating in the form of a table
        st.subheader("Average Rating by Property Type")
        st.write(avg_rating_by_property_type)

    elif analysis == 'Analysis of the relationship between price and rating':
        st.markdown('<h3 style="color: skyblue;">This analysis explores how the price of a rental property is related to its ratings.</h3>',unsafe_allow_html=True) 
        st.markdown('<h3 style="color: skyblue;">It aims to determine if higher-priced properties generally receive higher ratings or if there is no significant correlation.</h3>',unsafe_allow_html=True)
       
        # Scatter plot to visualize the relationship between price and review_scores_rating
        fig_price_rating = px.scatter(
            df,
            x='price',
            y='review_scores.review_scores_rating',
            title='Relationship between Price and Rating',
            labels={'price': 'Price', 'review_scores.review_scores_rating': 'Rating'},
            color='review_scores.review_scores_rating',
            color_continuous_scale='Bluered'
        )

        # Customize the layout
        fig_price_rating.update_layout(
            xaxis_title='Price',
            yaxis_title='Rating',
            xaxis=dict(range=[0, 12000]),  # Set the range for the x-axis
            showlegend=False
        )

        # Show the plot using Streamlit's Plotly support
        st.plotly_chart(fig_price_rating)

        # Display the data of the relationship between price and rating in the form of a table
        st.subheader("Price and Rating Data")
        st.write(df[['price', 'review_scores.review_scores_rating']])



    elif analysis == 'Analysis of the relationship between price and availability':
        st.markdown('<h3 style="color: skyblue;">This analysis investigates how the rental price of a property is related to its availability.</h3>',unsafe_allow_html=True) 
        st.markdown('<h3 style="color: skyblue;">It helps to determine if properties with certain pricing patterns are more or less available.</h3>',unsafe_allow_html=True) 
        
        availability_columns = [
        'availability.availability_365',
        'availability.availability_30',
        'availability.availability_60',
        'availability.availability_90'
    ]
        for col in availability_columns:
            if df[col].dtype == object:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        # Group by 'price' and calculate the average availability for each period
        avg_availability_by_price = df.groupby('price')[availability_columns].mean().reset_index()

        # Melt the dataframe to have 'availability_365', 'availability_30', 'availability_60', and 'availability_90' in a single column
        melted_availability_df = avg_availability_by_price.melt(id_vars='price', value_vars=availability_columns, 
                                                                var_name='Availability Period', value_name='Average Availability')

        # Create a bar chart to visualize the relationship between price and availability periods
        fig_availability_price = px.bar(
            melted_availability_df,
            x='price',
            y='Average Availability',
            color='Availability Period',
            barmode='group',
            title='Average Availability by Price and Period',
            labels={'price': 'Price', 'Average Availability': 'Average Availability'},
            hover_data=['price', 'Average Availability', 'Availability Period']
        )

        # Customize the layout
        fig_availability_price.update_layout(
            xaxis_title='Price',
            yaxis_title='Average Availability',
            xaxis=dict(range=[0, 12000])  # Set the range for the x-axis
        )

        # Show the plot using Streamlit's Plotly support
        st.plotly_chart(fig_availability_price)

        # Display the data of the relationship between price and availability in the form of a table
        st.subheader("Average Availability by Price and Period")
        st.write(avg_availability_by_price)

    elif analysis == 'Fetch the property_type, listing, accomodation and amenities for the desired price and country':
        st.markdown('<h3 style="color: skyblue;">This query fetches specific details such as property type, listing details, accommodation capacity,and amenities for properties within a specified price range and country.</h3>',unsafe_allow_html=True) 
         
        
        # Get unique values for price and country
        unique_prices = sorted(df['price'].unique())
        unique_countries = sorted(df['address.country'].unique())

        # Dropdown menus for price range
        min_price_value = st.selectbox('Select the minimum price:', unique_prices, index=0)
        max_price_value = st.selectbox('Select the maximum price:', unique_prices, index=len(unique_prices) - 1)

        # Ensure the selected minimum price is less than or equal to the selected maximum price
        if min_price_value > max_price_value:
            st.error('Minimum price cannot be greater than maximum price.')
        else:
            # Dropdown menu for country
            country_value = st.selectbox('Select the country:', unique_countries)

            # Filter the data based on selected values
            filtered_df = df[(df['price'] >= min_price_value) & 
                            (df['price'] <= max_price_value) & 
                            (df['address.country'] == country_value)]

            if not filtered_df.empty:
                max_rating_row = filtered_df.loc[filtered_df['review_scores.review_scores_rating'].idxmax()]
                best_listing_name = max_rating_row['name']
                property_type = max_rating_row['property_type']
                amenities = max_rating_row['amenities']
                accommodates=max_rating_row['accommodates']
                best_listing_price = max_rating_row['price']

                # Display the best listing name, property type, amenities, and price
                st.subheader('Best Listing:')
                st.write(best_listing_name)
                st.subheader('Property Type:')
                st.write(property_type)
                st.subheader('Amenities:')
                st.write(amenities)
                st.subheader('Accomodation')
                st.write(accommodates)
                st.subheader('Price:')
                st.write(best_listing_price)

                # Optionally, display the rating
                st.subheader('Rating:')
                st.write(max_rating_row['review_scores.review_scores_rating'])
            else:
                st.write('No listings found for the given price range and country.')
    elif analysis == 'Fetch the name, price, accommodates, amenities, street for the specified country and property_type':
        
        st.markdown('<h3 style="color: skyblue;">This query retrieves information including the name, price, accommodation capacity, amenities, and street address for properties in a specified country and of a specified property type.</h3>',unsafe_allow_html=True)
        # Create dropdown menus for country and property_type
        selected_country = st.selectbox('Select Country', df['address.country'].unique())
        selected_property_type = st.selectbox('Select Property Type', df['property_type'].unique())

        # Filter the dataframe based on the selected values
        filtered_df = df[(df['address.country'] == selected_country) & (df['property_type'] == selected_property_type)]

        # Display the filtered dataframe with selected columns
        st.subheader(f"Properties in {selected_country} with Property Type = {selected_property_type}")
        st.write(filtered_df[['name', 'price', 'accommodates', 'amenities','address.street']])

    elif analysis == 'Fetch the name, country, street, number of bathrooms and bedrooms for the desired property_type':
        st.markdown('<h3 style="color: skyblue;">This query extracts details such as the name, country, street address, and the number of bathrooms and bedrooms for properties of a specified property type.</h3>',unsafe_allow_html=True) 
        
        
        # Dropdown menu for selecting property_type
        unique_property_types = df['property_type'].unique()
        selected_property_type = st.selectbox('Select the property type:', unique_property_types)

        # Filter the dataframe based on the selected property type
        filtered_df_11 = df[df['property_type'] == selected_property_type]

        # Display the filtered data
        st.subheader("Listing name, country, street, number of bathrooms and bedrooms for the desired property_type")
        st.write(filtered_df_11[['name','bathrooms', 'bedrooms','address.country','address.street']])
    elif analysis == 'Analysis of home stay count for each country':
        st.markdown('<h3 style="color: skyblue;">This analysis counts the number of home stay listings available in each country.</h3>',unsafe_allow_html=True) 
        st.markdown('<h3 style="color: skyblue;">It helps to understand the distribution and popularity of home stays across different countries.</h3>',unsafe_allow_html=True) 
       
            # Group by 'address.country' and count the number of values in the 'name' column
        country_homestay_count = df.groupby('address.country')['name'].count().reset_index()
        country_homestay_count.columns = ['Country', 'Homestay Count']
            
            # Sort the data by homestay count in descending order
        country_homestay_count = country_homestay_count.sort_values(by='Homestay Count', ascending=False)

            # Create a choropleth map to visualize the home stay count for each country
        fig_homestay_count = px.choropleth(
                country_homestay_count,
                locations='Country',
                locationmode='country names',
                color='Homestay Count',
                title='Home Stay Count by Country',
                color_continuous_scale='Viridis'
            )

            # Customize the layout
        fig_homestay_count.update_layout(
                geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular'),
                coloraxis_colorbar=dict(title='Homestay Count')
            )

            # Show the plot using Streamlit's Plotly support
        st.plotly_chart(fig_homestay_count)

            # Display the data in the form of a table
        st.subheader("Home Stay Count by Country")
        st.write(country_homestay_count)
    elif analysis == 'Analysis of country based on the sorted order of average ratings given to home stays in that particular country':
        st.markdown('<h3 style="color: skyblue;">This analysis ranks countries based on the average ratings given to home stays.</h3>',unsafe_allow_html=True) 
        st.markdown('<h3 style="color: skyblue;">It helps to identify which countries tend to have higher-rated home stay options.</h3>',unsafe_allow_html=True) 
        # Group by 'country' and calculate the average rating
        avg_rating_by_country = df.groupby('address.country')['review_scores.review_scores_rating'].mean().reset_index()
        
        # Sort the countries based on average ratings
        avg_rating_by_country = avg_rating_by_country.sort_values(by='review_scores.review_scores_rating', ascending=False)

        # Create a choropleth map to visualize the average ratings by country
        fig_avg_rating_by_country_choropleth = px.choropleth(
            avg_rating_by_country,
            locations='address.country',
            locationmode='country names',
            color='review_scores.review_scores_rating',
            hover_name='address.country',
            color_continuous_scale='Magma',
            title='Average Ratings of Home Stays by Country'
        )

        # Customize the layout
        fig_avg_rating_by_country_choropleth.update_layout(
            geo=dict(showframe=False, showcoastlines=False),
            coloraxis_colorbar=dict(title='Average Rating')
        )

        # Show the plot using Streamlit's Plotly support
        st.plotly_chart(fig_avg_rating_by_country_choropleth)

        # Display the data of average ratings by country in the form of a table
        st.subheader("Average Ratings of Home Stays by Country")
        st.write(avg_rating_by_country)


    if st.button("Back to Analysis Selection"):
        st.session_state.page = "analysis"
        
# Initial page setup
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'analysis_choice' not in st.session_state:
    st.session_state.analysis_choice = None

# Page navigation
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'analysis':
    analysis_page()
elif st.session_state.page == 'visualization':
    visualization_page()
