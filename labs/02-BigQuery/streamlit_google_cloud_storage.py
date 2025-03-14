# Import Libraries
import streamlit as st
from google.cloud import storage
import pandas as pd
from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data from Google Cloud Storage

# ----------------------------------------#
# Set the path to your service account key file
key_path = '/Users/onyrakotomiaramnana/Documents/GitHub/Cloud-and-Advanced-Analytics/labs/02-BigQuery/labcloud-451519-5df05d56dc6b.json' #'./big-scale-analytics-......json'
def load_data():
    try:
        bucket_name = 'ox-caa-bucket' #'big_scale_analytics_bucket'
        file_name = 'movies.csv' #'movies.csv'

        # Create a client with service account credentials
        client = storage.Client.from_service_account_json(key_path)

        bucket = client.get_bucket(bucket_name) # Get the bucket
        blob = bucket.blob(file_name) # Get file objects

        movie_csv = blob.download_as_text() # Download csv from Google Cloud and stores inside movie_csv variable
        df = pd.read_csv(StringIO(movie_csv))
        return df

    except Exception as e:
        st.error(f"Error during data loading: {e}")
        return None
# ----------------------------------------#
    
# Load Data

data = load_data()

st.title("Google Cloud Storage: Bucket and Movie CSV") # §Title

if data is not None: # If data is not empty
    st.table(data.head(20))  # Display the first 10 rows of the data
    plt.figure(figsize=(10, 6))
    sns.countplot(y='genres', data=data, order=data['genres'].value_counts().index[:10]) # Countplot
    plt.title('Number of Movies by Genre')
    plt.xlabel('Number of Movies')
    plt.ylabel('Genre')
    st.pyplot(plt)