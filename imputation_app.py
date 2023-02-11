import streamlit as st
import pandas as pd
from sklearn.impute import KNNImputer

@st.cache
def impute_missing_values(df, column, k):
    imputer = KNNImputer(n_neighbors=k)
    df[column] = imputer.fit_transform(df[[column]])
    return df

def main():
    st.title("Imputation App")
    uploaded_file = st.file_uploader("Upload your Excel spreadsheet", type=["xlsx"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Data Preview:", df.head())
        column = st.selectbox("Select a column", df.columns)
        k = st.number_input("Enter the value of k", min_value=1, value=1)
        if st.button("Impute"):
            df = impute_missing_values(df, column, k)
            st.write("Imputed Data Preview:", df.head())
            if st.button("Download"):
                df.to_excel("imputed_data.xlsx", index=False)
                st.success("Data has been downloaded successfully!")

if __name__ == "__main__":
    main()
