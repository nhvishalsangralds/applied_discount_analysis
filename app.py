import os
from PIL import Image
import streamlit as st

# Path to the visualizations folder
image_directory = 'visualization'
image_list = os.listdir(image_directory)

# Dictionary mapping image filenames to insights
insights = {
    'Fig:1 - Null Value Counts by Column.png': 'This visualization shows the trend of sales over the past year.',
    'Fig:2 - Discount Usage by Hour of the day.png': 'This chart illustrates the null values in the data for each column, ',
    'Fig:3 - Discount Usage by Day of the Week.png': 'This chart illustrates the null values in the data for each column, ',
    'Fig:4 - Discount Usage by Year.png': 'This chart illustrates the null values in the data for each column, ',
    'Fig:5 - Discount Usage Heatmap (Year & Month).png': 'This chart illustrates the null values in the data for each column, ',
    'Fig:6 - Discount Usage Heatmap (Year & Quarter).png': 'This chart illustrates the null values in the data for each column, ',
    'Fig:7 - Discount Code Usage Over Time.png': 'This chart illustrates the null values in the data for each column, ',
    'Fig:8 - applied_count_distribution.png': 'This chart illustrates the null values in the data for each column, ',
    'Fig:9 - Success vs. Failed Discount Codes (Monthly Trend).png': 'This chart illustrates the null values in the data for each column, ',
    'Fig:10 - Success vs. Failed Discount Codes (Monthly Trend).png': 'This chart illustrates the null values in the data for each column, ',
    'Fig:11 - Failure Rate of Discount Codes (Heatmap).png': 'This chart illustrates the null values in the data for each column, ',
}

st.title('Visualization Dashboard')

for image_file in image_list:
    image_path = os.path.join(image_directory, image_file)
    if os.path.isfile(image_path):  # Ensure it's a file
        image = Image.open(image_path)
        st.image(image, caption=image_file, use_container_width=True)
        
        # Retrieve insight for the current image
        insight_text = insights.get(image_file, 'No insight available for this image.')
        st.caption(insight_text)

