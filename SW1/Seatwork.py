def convert_currency(dollars):
    peso_rate = 57.17
    yen_rate = 146.67

    peso = dollars * peso_rate
    yen = dollars * yen_rate

    return peso, yen  

if __name__ == "__main__":
    
    dollars_list = [59, 200, 500]

    print("Dollar($)\tPhil Peso(P)\tJpn Yen(Y)")
    for d in dollars_list:
        peso, yen = convert_currency(d)
        print(f"{d}\t\t{peso:.2f}\t\t{yen:.2f}")
