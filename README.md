# Airbnb_Analysis_3
This project aims to analyze Airbnb data, perform data cleaning and preparation and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.
Dataset:https://drive.google.com/file/d/1C7AilYDf2pA09Jy-5wYysvLwKC9_Fu9X/view
#Airbnb_3y:

```
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
```

- streamlit: Used for creating web applications.
- pandas: Used for data manipulation and analysis.
- plotly.express: Used for creating interactive plots.
- seaborn: Used for statistical data visualization.
- matplotlib.pyplot: Used for creating static, animated, and interactive visualizations.

```
file_path = "C://Users//HP//GUVI_PROJ//Air_Second_five.csv"
df = pd.read_csv(file_path)
```

- file_path: Path to the CSV file containing the Airbnb data.
- pd.read_csv: Loads the data from the specified CSV file into a pandas DataFrame named `df`.


```
def home_page():
```

- Defines a function `home_page` to display the home page of the Streamlit app.



```
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
```

- Uses st.markdown() to apply custom CSS styles to the Streamlit app.
  - .stApp: Styles the entire app, setting background image, size, position, text color, font, etc.
  - .top-center-image: Positions an image at the top center of the screen.
  - h1, h2, p, ul li: Sets styles for headings, paragraphs, and list items.
  - .stButton>button: Styles the button.


```
st.markdown('<img src="https://cdn-eahjn.nitrocdn.com/ChEvwayTHZmZJUAdsUNMLXuXZdBprFoQ/assets/images/optimized/rev-efee877/www.spinxdigital.com/app/uploads/2022/11/image-airbnb.jpg" class="top-center-image">', unsafe_allow_html=True)
```

- Inserts an image at the top center using HTML and applies the `.top-center-image` CSS class for styling.


```
st.markdown('<div class="stApp">', unsafe_allow_html=True)
```

- Opens a `<div>` tag with the class `.stApp` to style the main content area.


```
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
```

- st.title: Sets the main title of the page.
- st.markdown: Displays a description of Airbnb and its key features using HTML for formatting.


```
if st.button("Explore Airbnb Data"):
    st.session_state.page = "analysis"
```

- st.button: Creates a button labeled "Explore Airbnb Data".
- If the button is clicked, sets the `page` variable in `st.session_state` to `"analysis"` to navigate to the analysis page.

```
st.markdown('</div>', unsafe_allow_html=True)
```

- Closes the `<div>` tag opened earlier to wrap up the main content area.

`def analysis_page():`: Defines the function `analysis_page`.

 `st.markdown(...)`: Applies custom CSS styles to the Streamlit app using an HTML `<style>` tag.
   - `.top-left-image`: Styles an image to be positioned at the top-left of the page.
   - `.top-right-image`: Styles an image to be positioned at the top-right of the page.
   - `.stAppAnalysis`: Styles the main content area to center-align items and add padding at the top.
   - `.skyblue`: Defines a CSS class to color text in sky blue.
`st.markdown('<img src="..." class="top-left-image">', unsafe_allow_html=True)`: Displays an image at the top-left position with the given class.
`st.markdown('<img src="..." class="top-right-image">', unsafe_allow_html=True)`: Displays an image at the top-right position with the given class.
`st.markdown('<div class="stAppAnalysis">', unsafe_allow_html=True)`: Starts a `<div>` tag to group the main content area with the class `stAppAnalysis`.
`st.markdown('<h1 style="color: lightgreen;">Airbnb Data Analysis and Exploration</h1>', unsafe_allow_html=True)`: Adds a main heading (H1) with the text "Airbnb Data Analysis and Exploration" styled in light green.
`st.markdown('<h3 style="color: skyblue;">Why to explore Airbnb Data?</h3>', unsafe_allow_html=True)`: Adds a subheading (H3) with the text "Why to explore Airbnb Data?" styled in sky blue.
`st.markdown(...)`: Adds a detailed markdown text block explaining the benefits of exploring Airbnb data for various stakeholders like investors, travelers, and policymakers.
`st.markdown('<h3 style="color: skyblue;">Select an analysis to learn more about the Airbnb data.</h3>',unsafe_allow_html=True)`: Adds another subheading prompting the user to select an analysis, styled in sky blue.
`analysis_options = [...]`: Creates a list of analysis options that users can choose from.
`analysis_choice = st.selectbox("Select an analysis to learn more", analysis_options)`: Adds a dropdown (selectbox) for users to select an analysis option from the provided list.
`if st.button("Go to Analysis"):`: Checks if the "Go to Analysis" button is clicked.
    - `st.session_state.page = "visualization"`: Sets the session state page to "visualization" to navigate to the visualization page.
    - `st.session_state.analysis_choice = analysis_choice`: Stores the selected analysis choice in the session state.
`if st.button("Back to Home"):`: Checks if the "Back to Home" button is clicked.
    - `st.session_state.page = "home"`: Sets the session state page to "home" to navigate back to the home page.
`st.markdown('</div>', unsafe_allow_html=True)`: Closes the `<div>` tag started earlier, ending the main content area styling.


```
def visualization_page():
    image_url = "https://cdn.sanity.io/images/tlr8oxjg/production/f0a4a4cffc25b2f7253300a27c58687a28808c7a-1456x816.png?w=3840&q=80&fit=clip&auto=format"
    st.image(image_url, use_column_width=True)
```
- This function starts by defining an `image_url` that points to an image hosted online. It then uses Streamlit's `st.image` function to display the image on the page with `use_column_width=True`, ensuring it fits within the available column width.

```
    st.title("Airbnb Data Visualization")
```
- Sets the title of the page using Streamlit's `st.title` function.

```
    st.write(f"You selected: {st.session_state.analysis_choice}")
```
- Displays the user's selected analysis choice, which is stored in `st.session_state.analysis_choice`. This value is retrieved and displayed using `st.write`.

```
    analysis = st.session_state.analysis_choice
```
- Assigns the value of `st.session_state.analysis_choice` to the variable `analysis` for easier access in the subsequent code.

```
    # Analysis Visualizations
    if analysis == 'Analysis of the relationship between Price and Accommodation':
        # Display the average price
        st.markdown('<h3 style="color: skyblue;">This analysis examines how the price of a rental property varies with the number of people it can accommodate.</h3>', unsafe_allow_html=True)
        st.markdown('<h3 style="color: skyblue;">It aims to determine if there is a correlation between the accommodation capacity and the rental price.</h3>',unsafe_allow_html=True)
```
- Checks if the selected analysis is "Analysis of the relationship between Price and Accommodation". If true, it uses `st.markdown` to display informative text in HTML format about the analysis.

```
        avg_price_by_accommodates = df.groupby('accommodates')['price'].mean().reset_index()

        # Add a dropdown menu for selecting the average price and accommodation capacity
        options = avg_price_by_accommodates.apply(lambda row: f"Accommodates {row['accommodates']}: ${row['price']:.2f}", axis=1).tolist()
        selected_option = st.selectbox('Select the average price for an accommodation capacity:', options)
```
- Computes the average price grouped by the number of accommodates (`accommodates`) using `groupby` and `mean()`. Then, it creates a dropdown menu (`st.selectbox`) populated with options based on the computed averages.

```
        selected_accommodates, selected_avg_price = map(float, selected_option.replace('Accommodates ', '').replace('$', '').split(': '))
```
- Extracts the selected accommodation value and average price from the selected option in the dropdown menu, converting them to float values for further processing.

```
        matching_listings = df[(df['accommodates'] == selected_accommodates) & (df['price'].between(selected_avg_price - tolerance, selected_avg_price + tolerance))]
```
- Filters the DataFrame (`df`) to find listings that match the selected accommodation and fall within a price tolerance range around the selected average price.

```
        st.subheader(f"Listings with {int(selected_accommodates)} accommodations close to the average price of ${selected_avg_price:.2f}")
        st.write(matching_listings[['name', 'price']])
```
- Displays a subheader and the filtered DataFrame (`matching_listings`), showing listings with accommodation capacity close to the selected value and their prices.

```
        fig = px.bar(
            avg_price_by_accommodates,
            x='accommodates',
            y='price',
            title='Average Price by Accommodation Capacity',
            labels={'accommodates': 'Accommodation Capacity', 'price': 'Average Price'},
            color='price',
            color_continuous_scale='Viridis'
        )
```
- Creates a bar chart (`fig`) using Plotly Express (`px.bar`) to visualize the relationship between accommodation capacity (`accommodates`) and average price (`price`).

```
        fig.update_layout(
            xaxis_title='Accommodation Capacity',
            yaxis_title='Average Price',
            showlegend=False
        )

        st.plotly_chart(fig)
```
- Updates the layout of the chart (`fig`) and then displays it using `st.plotly_chart`.

The function continues similarly for other selected analyses, displaying relevant visualizations and data based on the user's choice stored in `st.session_state.analysis_choice`. Each `if` block corresponds to a different analysis selected by the user on the previous page.
#Test3_5.ipynb:
*It contains the code to convert the json dataset of airbnb to a dataframe.
*The data frame is cleaned by transforming the data types of the columns.
*The desired columns are fetched from the huge dataset containing 30 columns and 5555 rows, to create a new data frame.
*The new data frame is saved as a csv file in the desired path.
*The analysis is performed on the csv file created by fetching the desired attributes from the huge dataset.
#Airbnb_pBI_Report.pdf:
*Contains the visualizations of the Airbnb dataset drawn using powerBI tool
