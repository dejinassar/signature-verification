import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# ----------------------------
#  Load the Model
# ----------------------------
model = load_model('cnn_model.keras')
IMG_HEIGHT = 128
IMG_WIDTH = 128

st.title("Signature Verification Demo")
st.write("Upload one or more signature images to see if they are Genuine or Forged.")

# ----------------------------
# Upload Multiple Images
# ----------------------------
uploaded_files = st.file_uploader(
    "Choose signature images", 
    type=["png","jpg","jpeg"], 
    accept_multiple_files=True
)

if uploaded_files:
    results = []
    
    # Display uploaded images with predictions
    fig, axs = plt.subplots(1, len(uploaded_files), figsize=(5*len(uploaded_files),5))
    if len(uploaded_files) == 1:
        axs = [axs]  # make iterable
    
    for i, uploaded_file in enumerate(uploaded_files):
        img = Image.open(uploaded_file).convert('L').resize((IMG_HEIGHT, IMG_WIDTH))
        img_array = np.array(img)/255.0
        img_array = img_array.reshape(1, IMG_HEIGHT, IMG_WIDTH,1)

        # Predict
        pred_prob = model.predict(img_array)[0][0]
        pred_class = 'Genuine' if pred_prob > 0.5 else 'Forgery'
        
        results.append({
            "File Name": uploaded_file.name,
            "Prediction": pred_class,
            "Probability": round(float(pred_prob), 4)
        })

        # Display image with title
        axs[i].imshow(img, cmap='gray')
        axs[i].axis('off')
        axs[i].set_title(f"{pred_class}\nProb: {pred_prob:.2f}")

    st.pyplot(fig)

    # ----------------------------
    # Show Results in a Table
    # ----------------------------
    df_results = pd.DataFrame(results)
    st.subheader("Prediction Results")
    st.dataframe(df_results)

    # ----------------------------
    # Interactive Pie Chart for Genuine vs Forged
    # ----------------------------
    st.subheader("Prediction Distribution (Interactive Pie Chart)")
    pie_data = df_results['Prediction'].value_counts().reset_index()
    pie_data.columns = ['Prediction', 'Count']

    fig_pie = px.pie(
        pie_data,
        names='Prediction',
        values='Count',
        color='Prediction',
        color_discrete_map={'Genuine':'#4CAF50','Forgery':'#F44336'},
        hover_data=['Count'],
        title='Genuine vs Forged Signatures'
    )
    fig_pie.update_traces(textinfo='percent+label')
    st.plotly_chart(fig_pie)

    # ----------------------------
    # Probability Distribution Bar Chart (Interactive)
    # ----------------------------
    st.subheader("Probability Distribution")
    fig_bar = px.bar(
        df_results,
        x='File Name',
        y='Probability',
        color='Prediction',
        color_discrete_map={'Genuine':'#4CAF50','Forgery':'#F44336'},
        text='Probability',
        title='Signature Probability Distribution'
    )
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    st.plotly_chart(fig_bar)

    # ----------------------------
    # Download Results as CSV
    # ----------------------------
    csv = df_results.to_csv(index=False)
    st.download_button(
        label="Download Results as CSV",
        data=csv,
        file_name='signature_predictions.csv',
        mime='text/csv'
    )
