import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
# Load the updated data
file_path = "C://Users//HP//GUVI_PROJ//Air_Second_five.csv"
df = pd.read_csv(file_path)

# Calculate the average price
average_price = df['price'].mean()

# Streamlit app
st.title('Airbnb Analysis and Exploration')
analysis = st.selectbox("Select Analysis", [
    '1. Analysis of the relationship between Price and Accommodation',
    '2. Analysis of relationship between Price and Property_type',
    '3. Analysis of relationship among Price, Weekly_price, and Monthly_Price',
    '4. Analysis of the relationship between property_type, availability_365, availability_30, availability_60, availability_90',
    '5. Analysis of the relationship between property_type and rating',
    '6. Analysis of the relationship between price and rating',
    '7. Analysis of the relationship between rating and availability',
    '8. Analysis of the relationship between price and availability',
    '9. Fetch the property_type, name, and amenities for the desired price, accommodation, and country',
    '10. Fetch the name, price, accommodates, amenities, street for the specified country and property_type',
    '11. Fetch the number of bathrooms and bedrooms for the desired property_type'
], key="analysis_select")

if analysis == '1. Analysis of the relationship between Price and Accommodation':
    # Display the average price
    st.subheader(f'The average price of Airbnb listings is: ${average_price:.2f}')

    # Group by 'accommodates' and calculate the average price
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

elif analysis == '2. Analysis of relationship between Price and Property_type':
    # Group by 'property_type' and calculate the average price
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

elif analysis == '3. Analysis of relationship among Price, Weekly_price, and Monthly_Price':
    # Group by 'property_type' and calculate the average weekly and monthly price
    avg_weekly_monthly_price_by_property_type = df.groupby('property_type')[['weekly_price', 'monthly_price']].mean().reset_index()

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

elif analysis == '4. Analysis of the relationship between property_type, availability_365, availability_30, availability_60, availability_90':
    # Group by 'property_type' and calculate the average availability for each period
    avg_availability_by_property_type = df.groupby('property_type')[['availability.availability_365', 'availability.availability_30', 'availability.availability_60', 'availability.availability_90']].mean().reset_index()

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

elif analysis == '5. Analysis of the relationship between property_type and rating':
    # Group by 'property_type' and calculate the average review score rating
    avg_rating_by_property_type = df.groupby('property_type')['review_scores.review_scores_rating'].mean().reset_index()

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

elif analysis == '6. Analysis of the relationship between price and rating':
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

elif analysis == '7. Analysis of the relationship between rating and availability':
    availability_columns = ['availability.availability_365', 'availability.availability_30', 'availability.availability_60', 'availability.availability_90']
    
    # Ensure availability columns are present and convert to numeric if necessary
    for col in availability_columns:
        if df[col].dtype == object:  # Convert to numeric if the columns are not already numeric
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Melt the dataframe to have availability periods and average rating in a single column
    melted_availability_df = df.melt(id_vars='review_scores.review_scores_rating', value_vars=availability_columns, 
                                     var_name='Availability Period', value_name='Availability')

    # Filter out rows where availability or rating is NaN
    melted_availability_df = melted_availability_df.dropna(subset=['review_scores.review_scores_rating', 'Availability'])

    # Create a bar chart to visualize the relationship between distinct ratings and availability periods
    fig_availability_rating = px.bar(
        melted_availability_df,
        x='Availability Period',
        y='review_scores.review_scores_rating',
        color='Availability Period',
        barmode='group',
        title='Distinct Ratings by Availability Period',
        labels={'Availability Period': 'Availability Period', 'review_scores.review_scores_rating': 'Distinct Rating'}
    )

    # Customize the layout
    fig_availability_rating.update_layout(
        xaxis_title='Availability Period',
        yaxis_title='Distinct Rating'
    )

    # Show the plot using Streamlit's Plotly support
    st.plotly_chart(fig_availability_rating)

    # Display the distinct ratings and availability periods in the form of a table
    st.subheader("Distinct Ratings by Availability Period")
    st.write(melted_availability_df[['Availability Period', 'review_scores.review_scores_rating']].drop_duplicates())

elif analysis == '8. Analysis of the relationship between price and availability':
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

elif analysis == '9. Fetch the property_type, name, and amenities for the desired price, accommodation, and country':
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
            best_listing_price = max_rating_row['price']

            # Display the best listing name, property type, amenities, and price
            st.subheader('Best Listing:')
            st.write(best_listing_name)
            st.subheader('Property Type:')
            st.write(property_type)
            st.subheader('Amenities:')
            st.write(amenities)
            st.subheader('Price:')
            st.write(best_listing_price)

            # Optionally, display the rating
            st.subheader('Rating:')
            st.write(max_rating_row['review_scores.review_scores_rating'])
        else:
            st.write('No listings found for the given price range and country.')
elif analysis == '10. Fetch the name, price, accommodates, amenities, street for the specified country and property_type':
    # Create dropdown menus for country and property_type
    selected_country = st.selectbox('Select Country', df['address.country'].unique())
    selected_property_type = st.selectbox('Select Property Type', df['property_type'].unique())

    # Filter the dataframe based on the selected values
    filtered_df = df[(df['address.country'] == selected_country) & (df['property_type'] == selected_property_type)]

    # Display the filtered dataframe with selected columns
    st.subheader(f"Properties in {selected_country} with Property Type = {selected_property_type}")
    st.write(filtered_df[['name', 'price', 'accommodates', 'amenities','address.street']])

elif analysis == '11. Fetch the number of bathrooms and bedrooms for the desired property_type':
    # Dropdown menu for selecting property_type
    unique_property_types = df['property_type'].unique()
    selected_property_type = st.selectbox('Select the property type:', unique_property_types)

    # Filter the dataframe based on the selected property type
    filtered_df_11 = df[df['property_type'] == selected_property_type]

    # Display the filtered data
    st.subheader("Number of Bathrooms and Bedrooms")
    st.write(filtered_df_11[['name','bathrooms', 'bedrooms','address.country','address.street']])
elif analysis == '12. Analysis of home stay count for each country':
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
elif analysis == '13. Analysis of country based on the sorted order of average ratings given to home stays for each country':
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
