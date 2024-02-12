def is_number (value):
    try :
        int(value)
        return True
    except:
        return False

def inputBuah(stock, price , name='Apel'):
    """Fungsi untuk menambahkan stok, price dan nama buah

    args - stok (int) = jumlah buah tersissa
        - price (int) = harga perbuah  
        - name (str) = nama buah yang ada, default 'Apel'
    """

    while True:
        qty = input(f'masukan jumlah buah {name} : ')
        if is_number(qty):
            qty = int(qty)
            if qty > stock:
                print(f'Jumlah pesanan terlalu banyak, stock buah {name} sisa {stock}')
            else:
                break
        else:
            print('Masukan Angka !')
        
        total_price = qty * price
        stock -= qty

        return qty, total_price , stock

def pembayaran(nominal):
    """fungsi untuk melakukan pembayaran

        args: nominal(int) = berupa interger
    """
    while True:
        bayar = int(input('Silahkan masukkan uang Anda:'))
        if is_number(bayar):
            if bayar >= nominal:
                print('\nTerima kasih')
                print(f'Uang kembalian Anda sebesar {bayar - nominal}\n')
                break
            else:
                print(f'\nUang anda kurang sebesar {nominal - bayar}\n')
        else : 
                print('Masukan angka!')

#Main Program
# Mendefinisikan harga buah
price_apel = 10000
price_jeruk = 15000
price_anggur = 20000

# Mendefinisikan stock buah
stock_apel = 5
stock_jeruk = 10
stock_anggur = 7

print('Selamat Datang di Pasar Buah!')                
while True:

    # Hitung harga per buah
    n_apel, total_apel, stock_apel = inputBuah(stock_apel, price_apel, name='Apel')
    n_jeruk, total_jeruk, stock_jeruk = inputBuah(stock_jeruk, price_jeruk, name='Jeruk')
    n_anggur, total_anggur, stock_anggur = inputBuah(stock_anggur, price_anggur, name='Anggur')

    # Menghitung total belanjaan
    total = total_apel + total_jeruk + total_anggur

    # Show
    print(f'''\nDetail Belanjaan
        
    Apel : {n_apel} x {price_apel} = {total_apel}
    Jeruk : {n_jeruk} x {price_jeruk} = {total_jeruk}
    Anggur : {n_anggur} x {price_anggur} = {total_anggur}
        
    Total : {total}
    ''')

    #pembayaran
    pembayaran(total)
    # Konfirmasi belanja ulang
    konfirmasi = input('Apakah akan melakukan belanja lagi?: ')
    
    if konfirmasi == 'no':
        break