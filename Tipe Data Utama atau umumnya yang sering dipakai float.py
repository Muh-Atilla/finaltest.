import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import ttk

# --- 1. Fungsi Utama Kalkulator BMI (Float) ---

def tentukan_kategori_bmi(bmi):
    """Menentukan kategori BMI berdasarkan standar WHO."""
    if bmi < 18.5:
        return "Kekurangan berat badan", "blue"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan Normal", "green"
    elif 25.0 <= bmi < 29.9:
        return "Kelebihan berat badan (Pre-obesitas)", "orange"
    else:
        return "Obesitas", "red"

def hitung_bmi_float():
    """Mengambil berat dan tinggi, memvalidasi Float, dan menghitung BMI."""
    
    input_berat_str = entry_berat.get().strip()
    input_tinggi_str = entry_tinggi.get().strip()

    if not input_berat_str or not input_tinggi_str:
        messagebox.showwarning("Peringatan", "Berat dan Tinggi harus diisi.")
        return

    try:
        # PENTING: Menggunakan Float untuk akurasi pengukuran
        berat_kg = float(input_berat_str) 
        tinggi_m = float(input_tinggi_str)
        
        if berat_kg <= 0 or tinggi_m <= 0:
            messagebox.showerror("Error", "Berat dan Tinggi harus lebih besar dari nol.")
            return

    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka yang valid (Integer atau Desimal/Float).")
        return

    # --- Melakukan Operasi Float (Perhitungan BMI) ---
    
    # Tinggi harus dikuadratkan
    tinggi_kuadrat = tinggi_m * tinggi_m
    
    # Perhitungan BMI (Selalu menghasilkan Float karena adanya pembagian)
    bmi_float = berat_kg / tinggi_kuadrat
    
    # Tentukan Kategori
    kategori, warna = tentukan_kategori_bmi(bmi_float)
    
    # --- Menampilkan Hasil di Area Teks ---
    
    teks_hasil.config(state=tk.NORMAL)
    teks_hasil.delete('1.0', tk.END)
    
    teks_hasil.insert(tk.END, "--- Kalkulator Indeks Massa Tubuh (Float) ---\n", 'header')
    teks_hasil.insert(tk.END, f"Berat (kg): {berat_kg:.2f} (Float)\n", 'float_data')
    teks_hasil.insert(tk.END, f"Tinggi (m): {tinggi_m:.2f} (Float)\n\n", 'float_data')
    
    # Hasil BMI
    teks_hasil.insert(tk.END, "1. Hasil Perhitungan BMI:\n")
    teks_hasil.insert(tk.END, f"   Nilai BMI: {bmi_float:.2f}\n", 'result')
    teks_hasil.insert(tk.END, f"   Kategori: {kategori}\n", warna)
    teks_hasil.insert(tk.END, f"\nCatatan: Hasil pembagian yang presisi membutuhkan Float.\n")

    teks_hasil.config(state=tk.DISABLED)


# --- 2. Konfigurasi Jendela Utama Tkinter ---

def main():
    """Fungsi utama untuk inisialisasi Tkinter."""
    global entry_berat, entry_tinggi, teks_hasil
    
    jendela_utama = tk.Tk()
    jendela_utama.title("Kalkulator BMI (Simulasi Float)")
    jendela_utama.geometry("550x500")

    judul_font = tkfont.Font(family="Arial", size=14, weight="bold")
    label_font = tkfont.Font(family="Arial", size=10)

    # Frame Input
    frame_input = tk.Frame(jendela_utama, padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
    frame_input.pack(fill='x', padx=10, pady=10)

    tk.Label(frame_input, text="Perhitungan Indeks Massa Tubuh (Float)", font=judul_font).grid(row=0, columnspan=2, pady=10)

    # Input Berat
    tk.Label(frame_input, text="Berat (kg):", font=label_font).grid(row=1, column=0, sticky='w', padx=5, pady=5)
    entry_berat = tk.Entry(frame_input, width=20, font=label_font)
    entry_berat.grid(row=1, column=1, sticky='w', padx=5, pady=5)
    entry_berat.insert(0, "70.5")

    # Input Tinggi
    tk.Label(frame_input, text="Tinggi (m):", font=label_font).grid(row=2, column=0, sticky='w', padx=5, pady=5)
    entry_tinggi = tk.Entry(frame_input, width=20, font=label_font)
    entry_tinggi.grid(row=2, column=1, sticky='w', padx=5, pady=5)
    entry_tinggi.insert(0, "1.75")

    # Tombol Proses
    ttk.Button(frame_input, text="Hitung BMI", command=hitung_bmi_float).grid(row=3, columnspan=2, pady=15)


    # Area Output Hasil
    tk.Label(jendela_utama, text="Rincian Hasil BMI", font=judul_font).pack(pady=5)
    teks_hasil = tk.Text(
        jendela_utama,
        height=10,
        width=55,
        font=('Courier', 11),
        relief=tk.SUNKEN,
        state=tk.DISABLED
    )
    teks_hasil.pack(padx=10, pady=5)

    # Setup Tag Warna
    teks_hasil.tag_config('header', font=('Courier', 11, 'bold', 'underline'), foreground='darkgreen')
    teks_hasil.tag_config('float_data', foreground='purple')
    teks_hasil.tag_config('result', font=('Courier', 11, 'bold'), foreground='darkblue')
    teks_hasil.tag_config('blue', foreground='blue')
    teks_hasil.tag_config('green', foreground='green')
    teks_hasil.tag_config('orange', foreground='orange')
    teks_hasil.tag_config('red', foreground='red')

    jendela_utama.mainloop()

# Memanggil fungsi main saat skrip dijalankan
if __name__ == "__main__":
    main()