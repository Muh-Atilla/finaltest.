import tkinter as tk
from tkinter import messagebox

# 1. Definisi Array Satu Dimensi (List Python)
DATA_ARRAY = ["Apel", "Jeruk", "Mangga", "Nanas", "Pisang"]

def tampilkan_array(frame):
    """Fungsi untuk menampilkan setiap elemen array sebagai Label di GUI."""
    
    # Hapus widget yang sudah ada sebelum menampilkan ulang
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Array: Buah-buahan", font=('Helvetica', 12, 'bold')).pack(pady=10)
    
    # Iterasi melalui array untuk menampilkan Index dan Nilai
    for index, nilai in enumerate(DATA_ARRAY):
        # Format string untuk menampilkan Index dan Nilai
        teks = f"Indeks [{index}]: {nilai}"
        
        # Buat Label untuk setiap elemen
        label_elemen = tk.Label(frame, text=teks, relief=tk.RIDGE, width=25, anchor="w")
        label_elemen.pack(padx=10, pady=2)

def ambil_nilai_berdasarkan_indeks():
    """Fungsi untuk mengakses elemen array berdasarkan input indeks dari pengguna."""
    try:
        # Ambil input indeks dari Entry dan konversi ke integer
        indeks = int(input_indeks.get())
        
        # Cek apakah indeks valid (dalam batas 0 hingga panjang array - 1)
        if 0 <= indeks < len(DATA_ARRAY):
            nilai = DATA_ARRAY[indeks]
            messagebox.showinfo("Hasil Akses Array", f"Nilai pada Indeks [{indeks}] adalah: {nilai}")
        else:
            # Jika indeks di luar batas (Index Out of Bounds)
            messagebox.showerror("Error", f"Indeks {indeks} tidak valid. Indeks harus antara 0 sampai {len(DATA_ARRAY) - 1}.")
    except ValueError:
        # Menangani kesalahan jika input bukan angka
        messagebox.showerror("Error", "Input harus berupa angka (indeks).")
    except Exception as e:
        # Menangani error umum lainnya
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# --- SETUP JENDELA UTAMA TKINTER ---
root = tk.Tk()
root.title("Visualisasi Array Satu Dimensi")

# Frame untuk Menampilkan Array
frame_array = tk.Frame(root, padx=10, pady=10, relief=tk.GROOVE, bd=2)
frame_array.pack(side=tk.LEFT, fill=tk.BOTH)

# Panggil fungsi untuk mengisi frame_array
tampilkan_array(frame_array)

# Frame untuk Kontrol Akses
frame_kontrol = tk.Frame(root, padx=10, pady=10)
frame_kontrol.pack(side=tk.RIGHT, fill=tk.BOTH)

# Komponen Kontrol
tk.Label(frame_kontrol, text="Akses Data Berdasarkan Indeks", font=('Helvetica', 10, 'bold')).pack(pady=10)

tk.Label(frame_kontrol, text="Masukkan Indeks (0-4):").pack()

# Variabel untuk menyimpan input pengguna
input_indeks = tk.StringVar()

# Entry (Kolom Input) untuk Indeks
entry_indeks = tk.Entry(frame_kontrol, textvariable=input_indeks, width=10)
entry_indeks.pack(pady=5)

# Tombol untuk Melakukan Akses
tombol_akses = tk.Button(frame_kontrol, text="Ambil Nilai", command=ambil_nilai_berdasarkan_indeks)
tombol_akses.pack(pady=10)

# Jalankan loop utama Tkinter
root.mainloop()