
# ## Flight Experience Dataset

# In[92]:
import pandas as pd
import streamlit as st 

passenger_exp = pd.read_csv('train.csv')
passenger_exp.describe()


# In[125]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

passenger_exp_new = passenger_exp.drop(['id','Unnamed: 0'],axis=1)


st.set_page_config(page_title="Flight Passenger Experience", layout="wide")
st.title('Flight Passenger Experience')

col1,col2= st.columns([1,1])


plt.figure(figsize = (10, 6))
col1.markdown('Scatterplot of Flight Distance v/s Departure Delay in Minutes')
col1.pyplot(sns.scatterplot(x = 'Flight Distance', y = 'Departure Delay in Minutes', data = passenger_exp,palette="ch:.25").figure)
plt.show()

#col1.markdown('Boxplot of Type of Travel v/s Age')
#col1.pyplot(sns.boxplot(x="Type of Travel", y="Age", data=passenger_exp, palette="viridis").figure)

col2.markdown('Distribution plot of Flight Distance v/s satisfaction')
col2.pyplot(sns.displot(passenger_exp, x="Flight Distance", hue="satisfaction").figure)


col3,col4= st.columns([1,1])
plt.figure(figsize = (12, 6))
col3.markdown('Bar plot of Class v/s Baggage handling')
col3.pyplot(sns.barplot(x='Class',y='Baggage handling',data=passenger_exp).figure)


col4.markdown('Bar plot of Customer type v/s Flight distance')
col4.pyplot(sns.barplot(x='Customer Type',y='Flight Distance',data=passenger_exp).figure)



col5,col6= st.columns([1,1])
plt.figure(figsize = (12, 10))
col5.markdown('Categorical plot of seat comfort v/s Flight Distance')
col5.pyplot(sns.catplot(x='Seat comfort',y='Flight Distance',data=passenger_exp, hue="Type of Travel").figure)

plt.figure(figsize = (12, 10))
col6.markdown('Kernel Density Estimation plot of Flight distance v/s satisfaction')
col6.pyplot(sns.kdeplot(data = passenger_exp, x = "Flight Distance",hue = "satisfaction" , shade = True,palette="ch:.25",multiple="stack",fill=True, common_norm=False,alpha=.8, linewidth=0).figure)
