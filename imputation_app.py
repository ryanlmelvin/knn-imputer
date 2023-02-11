import streamlit as st
import pandas as pd
import io

from sklearn.impute import KNNImputer


@st.cache_data
def impute_missing_values(df, column, k):
    imputer = KNNImputer(n_neighbors=k)
    df[column] = imputer.fit_transform(df[[column]])
    return df

def to_excel(df):
    output = io.BytesIO()
    df.to_excel(output, index=False, sheet_name='Grades')
    processed_data = output.getvalue()
    return processed_data

def main():
    st.title("Imputation App")
    uploaded_file = st.file_uploader("Upload your Excel spreadsheet", type=["xlsx"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Data Preview:", df[df.isnull().any(axis=1)].head())
        column = st.selectbox("Select a column", df.columns)
        k = st.number_input("Enter the value of k", min_value=1, value=3)
        if st.button("Impute"):
            df = impute_missing_values(df, column, k)
            st.write("Imputed Data Preview:", df.head())
            df_xlsx = to_excel(df)
            st.download_button(label='Download Result',
                               data = df_xlsx,
                               file_name = "MissingsFilled_" + uploaded_file.name)

if __name__ == "__main__":
    main()
