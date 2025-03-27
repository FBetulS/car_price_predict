import streamlit as st
import torch
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# Model ve Scaler'ları yükleme fonksiyonu
@st.cache_resource
def load_model():
    checkpoint = torch.load('car_price_model.pth')
    
    class CarPricePredictor(torch.nn.Module):
        def __init__(self, input_size):
            super().__init__()
            self.stack = torch.nn.Sequential(
                torch.nn.Linear(input_size, 128),
                torch.nn.ReLU(),
                torch.nn.Dropout(0.2),
                torch.nn.Linear(128, 64),
                torch.nn.ReLU(),
                torch.nn.Linear(64, 1)
            )
        
        def forward(self, x):
            return self.stack(x)
    
    model = CarPricePredictor(7)
    model.load_state_dict(checkpoint['model_state'])
    model.eval()
    
    return model, checkpoint['scaler_X'], checkpoint['scaler_y']

# Streamlit arayüzü
st.title('🚗 Araç Fiyat Tahmin Uygulaması')
st.markdown("""
Bu uygulama makine öğrenimi kullanarak araç fiyat tahmini yapar. 
Lütfen aşağıdaki bilgileri girin ve **Tahmin Et** butonuna tıklayın.
""")

# Kullanıcı girdileri
col1, col2 = st.columns(2)
with col1:
    year = st.number_input('Üretim Yılı', min_value=2000, max_value=2024, value=2015)
    present_price = st.number_input('Mevcut Fiyat (Lakh)', min_value=0.1, value=5.0)
    kms_driven = st.number_input('Kilometre (km)', min_value=0, value=25000)
    
with col2:
    owner = st.selectbox('Sahip Sayısı', [0, 1, 2, 3])
    fuel_type = st.selectbox('Yakıt Türü', ['Petrol', 'Diesel'])
    seller_type = st.selectbox('Satıcı Türü', ['Bayi', 'Bireysel'])
    transmission = st.selectbox('Vites Türü', ['Manuel', 'Otomatik'])

# Tahmin butonu
if st.button('Tahmin Et'):
    model, scaler_X, scaler_y = load_model()
    
    # Kategorik değişkenleri kodlama
    fuel_code = 1 if fuel_type == 'Petrol' else 0
    seller_code = 1 if seller_type == 'Bayi' else 0
    transmission_code = 1 if transmission == 'Manuel' else 0
    
    # Girdi vektörü oluşturma
    input_data = pd.DataFrame([[year, present_price, kms_driven, owner, 
                               fuel_code, seller_code, transmission_code]],
                             columns=["Year", "Present_Price", "Kms_Driven", "Owner",
                                     "Fuel_Type", "Seller_Type", "Transmission"])
    
    # Ölçeklendirme ve tahmin
    scaled_input = scaler_X.transform(input_data)
    with torch.no_grad():
        prediction = model(torch.FloatTensor(scaled_input))
        price = scaler_y.inverse_transform(prediction.numpy())[0][0]
    
    st.success(f"Tahmini Satış Fiyatı: ₹{price:,.2f} Lakh")
    st.info("Not: 1 Lakh = 100,000 Hint Rupisi (~1.200 USD)")