import streamlit as st
import pandas as pd
from sklearn.impute import KNNImputer

def impute_missing_values_knn(df, column, k):
    knn_imputer = KNNImputer(n_neighbors=k)
    df[column] = knn_imputer.fit_transform(df[[column]])
    return df

def main():
    st.title("Imputing Missing Values with kNN")
    uploaded_file = st.file_uploader("Upload an Excel Spreadsheet", type=["xlsx", "xls"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df.head())

        column = st.selectbox("Select a column from the spreadsheet", df.columns)
        k = st.number_input("Enter the number of neighbors (k)", min_value=1, value=5)
        if st.button("Impute Missing Values"):
            df = impute_missing_values_knn(df, column, k)
            st.dataframe(df.head())

if __name__ == "__main__":
    main()
