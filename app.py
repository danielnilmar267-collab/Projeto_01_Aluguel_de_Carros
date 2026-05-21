import streamlit as st

st.title("🚗Nilmar Car Rental")  
st.title(" -Alugue seu carro- ")

st.sidebar.title("Escolhar o seu modelo")
st.sidebar.image("logo.png")

st.sidebar.title("CARROS e MOTOS")
carros = ["M2 BMW","GOLF GTI","CIVIC G10","OPALA","SW4","S1000RR","FAN 160","BMW r1250 GS","africa twin"]

opcao = st.sidebar.selectbox(' o carro ou moto que foi alugado', carros)

st.image(f'{opcao}.png')
st.markdown(f'## você alugou o modelo: {opcao}')
st.markdown('---')
dias = st.text_input(f'Por quantos dias o {opcao} foi alugado? ')

km = st.text_input(f'Quantos Km você rodou com o {opcao}?')

if opcao in "M2 BMW":
    diaria = 1500

elif opcao in "GOLF GTI":
    diaria = 550    

elif opcao in "CIVIC G10":
    diaria = 1000

elif opcao in "OPALA":  
    diaria = 700

elif opcao in "SW4":
    diaria = 650

elif opcao in "S1000RR":
    diaria = 300
elif opcao in "FAN 160":
    diaria = 400

elif opcao in "BMW r1250 GS":
    diaria = 600

elif opcao in "africa twin":
    diaria = 500

if st.button('Calcular'):
    dias = int(dias)
    km = int(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km} Km. O valor total do aluguel é de R$ {aluguel_total:.2f}.')