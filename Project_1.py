#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r"C:\sample data\student_dataset.csv")
df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


#df.info() gives the data that there are 4 objects that are needed to be converted into categorical to numerical


# In[6]:


#for checking missing values
df.isnull().sum()


# In[7]:


df.duplicated().sum()


# In[8]:


#for checking duplicate values
df.duplicated()


# In[10]:


df.shape


# In[11]:


# Our target variable for this dataset is final_exam_marks


# # Outlier Detection and Removal

# In[13]:


# To check the We will use boxplot


# Outliers are usually checked in numerical columns, not categorical ones.

# In[15]:


numeric_cols = df.select_dtypes(include=['int64','float64']).columns
plt.figure(figsize=(15,8)) #What it does:,Creates a big figure (canvas),Width = 15,Height = 8,This makes plots bigger and clearer.
for i, col in enumerate(numeric_cols):
    plt.subplot(3,3,i+1)
    sns.boxplot(y=df[col])
    plt.title(col)
plt.tight_layout()  #Adjusts spacing automatically and Prevents overlapping of plots
plt.show()


# In[20]:


#There is one outlier in final_exam_marks and we can confirm it using IQR method
Q1 = df['final_exam_marks'].quantile(0.25)
Q3 = df['final_exam_marks'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR


# In[21]:


#There is only one row confirmed using IQR method


# In[23]:


df = df[(df['final_exam_marks'] >= lower_limit) & 
        (df['final_exam_marks'] <= upper_limit)]


# In[25]:


df.shape


# In[26]:


# Out of 300 rows there are only showing 299 rows it means the outlier is removed
#To prove it use boxplot


# In[27]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(y=df['final_exam_marks'])
plt.title('Boxplot of Final Exam Marks')
plt.show()


# In[28]:


#It is showing no outlier as it is being removed


# # Converting Categorical Data to Numerical Data

# In[29]:


df.columns


# In[30]:


df.select_dtypes(include=['object']).columns


# In[31]:


# How to get ordinal and nominal columns? : For that we will check unique values
for col in df.select_dtypes(include=['object']).columns:
    print(col)
    print(df[col].unique())
    print("-------------")


# For nominal there should be only two possible values : 0 and 1,pass or fail , true ya false etc
# 
# Here nominal columns are gender,extracurricular,internet_access
# 
# We will use One Hot Encoding

# In[32]:


df = pd.get_dummies(df, columns=['gender','internet_access','extracurricular'], drop_first=True)


# For ordinal columns there should be 3 or more possible values:
# 
# Here they are family_income
# 
# So we will use Label Encoding

# In[33]:


# We will use manual mapping
income_mapping = {'Low': 0, 'Medium': 1, 'High': 2}

df['family_income'] = df['family_income'].map(income_mapping)


# After encoding check for unique values if gives numerical values means we have successfully converted categorical column to numerical

# In[34]:


df['family_income'].unique()


# In[35]:


df.info()


# In[36]:


# There is no objects or no categorical columns 


# # Correlation Matrix(Showed using HeatMap)

# In[37]:


plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()


# # Distribution Of Target Variable

# In[39]:


sns.histplot(df['final_exam_marks'], kde=True)
plt.show()


# # Study Hours vs Final Marks

# In[40]:


sns.scatterplot(x=df['study_hours'], y=df['final_exam_marks'])
plt.show()


# # Attendance vs Final Marks

# In[42]:


sns.scatterplot(x=df['attendance_percentage'], y=df['final_exam_marks'])
plt.show()


# # Gender vs Final Marks

# In[45]:


sns.boxplot(x=df['gender_Male'], y=df['final_exam_marks'])
plt.show()


# # Family Income vs Final Marks

# In[46]:


sns.boxplot(x=df['family_income'], y=df['final_exam_marks'])
plt.show()


# # Simple Student Dashboard

# In[50]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Student Performance Analysis Dashboard</h1>", unsafe_allow_html=True)

st.markdown("---")

# ===============================
# Sidebar Filters
# ===============================
st.sidebar.header("🔎 Filter Options")

min_hours = int(df['study_hours'].min())
max_hours = int(df['study_hours'].max())

selected_hours = st.sidebar.slider(
    "Select Study Hours Range",
    min_value=min_hours,
    max_value=max_hours,
    value=(min_hours, max_hours)
)

filtered_df = df[(df['study_hours'] >= selected_hours[0]) & 
                 (df['study_hours'] <= selected_hours[1])]

# ===============================
# Key Metrics Section
# ===============================
st.subheader("📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(filtered_df))
col2.metric("Average Marks", round(filtered_df['final_exam_marks'].mean(), 2))
col3.metric("Highest Marks", filtered_df['final_exam_marks'].max())

st.markdown("---")

# ===============================
# Dataset Preview
# ===============================
with st.expander("📂 View Dataset"):
    st.dataframe(filtered_df)

# ===============================
# Visualizations Section
# ===============================
st.subheader("📈 Visual Analysis")

col1, col2 = st.columns(2)

# Scatter Plot
with col1:
    st.markdown("### Study Hours vs Final Marks")
    fig1, ax1 = plt.subplots()
    sns.scatterplot(x=filtered_df['study_hours'], 
                    y=filtered_df['final_exam_marks'], 
                    hue=filtered_df['final_exam_marks'],
                    palette="viridis",
                    ax=ax1)
    st.pyplot(fig1)

# Histogram
with col2:
    st.markdown("### Distribution of Final Marks")
    fig2, ax2 = plt.subplots()
    sns.histplot(filtered_df['final_exam_marks'], 
                 kde=True, 
                 color='skyblue',
                 ax=ax2)
    st.pyplot(fig2)

st.markdown("---")

# ===============================
# Correlation Heatmap
# ===============================
st.subheader("🔗 Correlation Heatmap")

fig3, ax3 = plt.subplots(figsize=(8,5))
sns.heatmap(filtered_df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm",
            ax=ax3)
st.pyplot(fig3)

st.markdown("---")

# ===============================
# Insights Section
# ===============================
st.subheader("💡 Key Insights")

st.success("""
• Students who study more hours tend to score higher marks.  
• There is a positive correlation between study hours and final exam marks.  
• Marks distribution appears moderately spread with few high performers.  
""")

st.markdown("<center>🚀 Built with Streamlit</center>", unsafe_allow_html=True)


# In[48]:


import os
os.getcwd()


# In[ ]:




# In[ ]:




