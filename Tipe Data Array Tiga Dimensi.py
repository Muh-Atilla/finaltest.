import tkinter as tk
from tkinter import messagebox
import random

# 1. Definisi Array Tiga Dimensi (Matriks 2x3x2)
# [Lapisan] x [Baris] x [Kolom]
BALOK_DATA = [
    # Lapisan 0: Matriks 3x2
    [[10, 20], [30, 40], [50, 60]], 
    # Lapisan 1: Matriks 3x2
    [[70, 80], [90, 100], [110, 120]] 
]

JUMLAH_LAPISAN = len(BALOK_DATA) # 2
JUMLAH_BARIS = len(BALOK_DATA[0])    # 3
JUMLAH_KOLOM = len(BALOK_DATA[0][0]) # 2

# Variabel untuk melacak lapisan yang sedang aktif
lapisan_aktif = 0 

# --- FUNGSI TAMPILAN TKINTER ---

def tampilkan_matriks_lapisan(frame, data_lapisan, judul, lapisan_index):
    """Fungsi untuk menampilkan satu Lapisan (Matriks 2D) di GUI."""
    
    # Hapus widget lama
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text=judul, font=('Helvetica', 10, 'bold')).grid(row=0, column=0, columnspan=JUMLAH_KOLOM + 1, pady=5)
    
    # Header Kolom
    tk.Label(frame, text="", width=5, relief=tk.FLAT).grid(row=1, column=0)
    for c in range(JUMLAH_KOLOM):
        tk.Label(frame, text=f"K{c}", font=('Arial', 8, 'bold'), width=5, relief=tk.RAISED).grid(row=1, column=c+1, padx=2, pady=2)
        
    # Data Matriks (Loop Bersarang untuk Baris dan Kolom)
    for r in range(JUMLAH_BARIS):
        # Label Baris
        tk.Label(frame, text=f"B{r}", font=('Arial', 8, 'bold'), width=5, relief=tk.RAISED).grid(row=r+2, column=0, padx=2, pady=2)
        
        for c in range(JUMLAH_KOLOM):
            nilai = data_lapisan[r][c]
            # Label elemen
            label_elemen = tk.Label(frame, text=str(nilai), width=5, relief=tk.GROOVE)
            label_elemen.grid(row=r+2, column=c+1, padx=2, pady=2)

def perbarui_visualisasi():
    """Menggambar ulang kedua lapisan."""
    tampilkan_matriks_lapisan(
        frame_lapisan0, 
        BALOK_DATA[0], 
        "LAPISAN 0", 
        0
    )
    tampilkan_matriks_lapisan(
        frame_lapisan1, 
        BALOK_DATA[1], 
        "LAPISAN 1", 
        1
    )

def akses_dan_perbarui_nilai():
    """Fungsi untuk mengakses dan memperbarui elemen berdasarkan ketiga indeks."""
    try:
        # Ambil input Lapisan, Baris, dan Kolom
        lapisan = int(input_lapisan.get())
        baris = int(input_baris.get())
        kolom = int(input_kolom.get())
        
        # Validasi Indeks
        if (0 <= lapisan < JUMLAH_LAPISAN and 
            0 <= baris < JUMLAH_BARIS and 
            0 <= kolom < JUMLAH_KOLOM):
            
            # --- AKSES (Membaca) ---
            nilai_lama = BALOK_DATA[lapisan][baris][kolom]
            
            # --- PERBARUI (Menulis) ---
            nilai_baru = random.randint(500, 1000)
            BALOK_DATA[lapisan][baris][kolom] = nilai_baru

            # Tampilkan pesan dan perbarui GUI
            messagebox.showinfo(
                "Akses & Perbarui 3D Array",
                f"Elemen di [{lapisan}][{baris}][{kolom}] berhasil diakses.\n"
                f"Nilai lama: {nilai_lama}\n"
                f"Nilai baru: {nilai_baru} (Diperbarui)"
            )
            
            # Panggil fungsi untuk menggambar ulang kedua lapisan
            perbarui_visualisasi()
            
        else:
            messagebox.showerror("Error", f"Indeks tidak valid. L(0-{JUMLAH_LAPISAN-1}), B(0-{JUMLAH_BARIS-1}), K(0-{JUMLAH_KOLOM-1}).")
            
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# --- SETUP JENDELA UTAMA TKINTER ---
root = tk.Tk()
root.title("Visualisasi Array Tiga Dimensi")

# Frame Besar untuk Visualisasi (Dua Matriks Berdampingan)
frame_visualisasi = tk.Frame(root, padx=10, pady=10)
frame_visualisasi.pack(side=tk.LEFT, fill=tk.BOTH)

# Frame Kiri: Lapisan 0
frame_lapisan0 = tk.Frame(frame_visualisasi, relief=tk.RAISED, bd=2, padx=5, pady=5)
frame_lapisan0.pack(side=tk.LEFT, padx=10)

# Frame Kanan: Lapisan 1
frame_lapisan1 = tk.Frame(frame_visualisasi, relief=tk.RAISED, bd=2, padx=5, pady=5)
frame_lapisan1.pack(side=tk.LEFT, padx=10)

# Inisialisasi tampilan matriks
perbarui_visualisasi()

# Frame Kontrol Akses
frame_kontrol = tk.Frame(root, padx=15, pady=10, bg='#f0f0f0')
frame_kontrol.pack(side=tk.RIGHT, fill=tk.BOTH)

tk.Label(frame_kontrol, text="Akses Data Array 3D", font=('Helvetica', 10, 'bold'), bg='#f0f0f0').pack(pady=10)

# Input Lapisan (Kedalaman)
tk.Label(frame_kontrol, text=f"Indeks Lapisan (0-{JUMLAH_LAPISAN-1}):", bg='#f0f0f0').pack()
input_lapisan = tk.StringVar(value="0")
tk.Entry(frame_kontrol, textvariable=input_lapisan, width=5).pack(pady=3)

# Input Baris
tk.Label(frame_kontrol, text=f"Indeks Baris (0-{JUMLAH_BARIS-1}):", bg='#f0f0f0').pack()
input_baris = tk.StringVar(value="0")
tk.Entry(frame_kontrol, textvariable=input_baris, width=5).pack(pady=3)

# Input Kolom
tk.Label(frame_kontrol, text=f"Indeks Kolom (0-{JUMLAH_KOLOM-1}):", bg='#f0f0f0').pack()
input_kolom = tk.StringVar(value="0")
tk.Entry(frame_kontrol, textvariable=input_kolom, width=5).pack(pady=3)

# Tombol Akses dan Perbarui
tombol_akses = tk.Button(
    frame_kontrol, 
    text="Akses & Perbarui Nilai (3D)", 
    command=akses_dan_perbarui_nilai, 
    bg='lightcoral',
    fg='white'
)
tombol_akses.pack(pady=20)

# Jalankan loop utama Tkinter
root.mainloop()