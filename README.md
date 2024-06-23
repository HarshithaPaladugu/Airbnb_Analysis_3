# Airbnb_Analysis_3
This project aims to analyze Airbnb data, perform data cleaning and preparation and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.
Dataset:https://drive.google.com/file/d/1C7AilYDf2pA09Jy-5wYysvLwKC9_Fu9X/view
#Airbnb_3y:
*Importing necessary libraries for data manipulation, visualization, and the Streamlit app.
*Load the CSV file containing the Airbnb data into a DataFrame named 'df'
*Calculate the average price of Airbnb listings and store it in the variable average_price.
*Set the title of the Streamlit app to 'Airbnb Analysis and Exploration'.
*Create a dropdown menu with options for different types of analyses. The user can select an analysis type from the dropdown.
  -Analysis 1: Relationship between Price and Accommodation
  -Analysis 2: Relationship between Price and Property_type
  -Analysis 3: Relationship among Price, Weekly_price, and Monthly_Price
  -Analysis 4: Relationship among property_type, availability_365, availability_30, availability_60, availability_90',
  -Analysis 5: Relationship between property_type and rating
  -Analysis 6: Relationship between price and rating
  -Analysis 7: Relationship between rating and availability
  -Analysis 8: Relationship between price and availability
  -9. Fetch the property_type, name, and amenities for the desired price, accommodation, and country
  -10. Fetch the name, price, accommodates, amenities, street for the specified country and property_type
  -11. Fetch the number of bathrooms and bedrooms for the desired property_type
  -12. Analysis of home stay count for each country
  -13. Analysis of country based on the sorted order of average ratings given to home stays in that particular country
*For the above Analysis appropriate visualizations is used for better understanding of the relationship between the desired attributes or 
 columns of Airbnb dataset.
#Test3_5.ipynb:
*It contains the code to convert the json dataset of airbnb to a dataframe.
*The data frame is cleaned by transforming the data types of the columns.
*The desired columns are fetched from the huge dataset containing 30 columns and 5555 rows, to create a new data frame.
*The new data frame is saved as a csv file in the desired path.
*The analysis is performed on the csv file created by fetching the desired attributes from the huge dataset.
