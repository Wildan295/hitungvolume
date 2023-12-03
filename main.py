import streamlit as st
from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar :
    selected = option_menu ('Hitung Volume Bangun Ruang',
    ['Hitung Volume Balok',
     'Hitung Volume Kubus',
     'Hitung Volume Tabung',
     'Hitung Volume Prisma Segitiga',
     'Hitung Volume Limas Segiempat',
     'Hitung Volume Kerucut',
     'Hitung Volume Bola'],
    default_index=0)

# halaman hitung voume balok
if (selected == 'Hitung Volume Balok') :
    st.title('Hitung Volume Balok')
    
    panjang = st.number_input ("Masukkan Nilai Panjang", 0)
    lebar = st.number_input ("Masukkan Nilai Lebar", 0)
    tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        vbalok = panjang*lebar*tinggi
        st.success (f"Volume Balok Adalah = {vbalok}")
        
if (selected == "Hitung Volume Kubus") :
    st.title('Hitung Volume Kubus')
    
    sisi = st.number_input ("Masukkan Nilai Sisi", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        vkubus = sisi*sisi*sisi
        st.success (f"Volume Kubus Adalah = {vkubus}")

if (selected == "Hitung Volume Tabung") :
    st.title('Hitung Volume Tabung')
    
    jari_jari = st.number_input ("Masukkan Nilai Jari-Jari", 0)
    tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        vtabung = 3.14*jari_jari*jari_jari*tinggi
        st.success (f"Volume Tabung Adalah = {vtabung}")
        
if (selected == "Hitung Volume Prisma Segitiga") :
    st.title('Hitung Volume Prisma Segitiga')
    
    alas = st.number_input ("Masukkan Nilai Alas", 0)
    tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
    tinggip = st.number_input ("Masukkan Nilai Tinggi Prisma", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        vprisma = (0.5*alas*tinggi)*tinggip
        st.success (f"Volume Prisma Segitiga Adalah = {vprisma}")
        
if (selected == "Hitung Volume Limas Segiempat") :
    st.title('Hitung Volume Limas Segiempat')
    
    panjang = st.number_input ("Masukkan Nilai Panjang Alas", 0)
    lebar = st.number_input ("Masukkan Nilai Lebar Alas", 0)
    tinggi = st.number_input ("Masukkan Nilai Tinggi Limas", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        vlimas = 1/3*panjang*lebar*tinggi
        st.success (f"Volume Limas Segiempat Adalah = {vlimas}")
    
if (selected == "Hitung Volume Kerucut") :
    st.title('Hitung Volume Kerucut')
    
    jari_jari = st.number_input ("Masukkan Nilai Jari-Jari", 0)
    tinggi = st.number_input ("Masukkan Nilai Tinggi Kerucut", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        vkerucut = 1/3*3.14*jari_jari*jari_jari*tinggi
        st.success (f"Volume Kerucut Adalah = {vkerucut}")
        
if (selected == "Hitung Volume Bola") :
    st.title('Hitung Volume Bola')
    
    jari_jari = st.number_input ("Masukkan Nilai Jari-Jari", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        vbola = 4/3*3.14*jari_jari*jari_jari*jari_jari
        st.success (f"Volume Bola Adalah = {vbola}")