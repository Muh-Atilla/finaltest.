import tkinter as tk
from tkinter import messagebox
import random

# 1. Definisi Array Dua Dimensi (Matriks 3 Baris x 4 Kolom)
MATRIKS_DATA = [
    [10, 20, 30, 40],   # Baris 0
    [50, 60, 70, 80],   # Baris 1
    [90, 100, 110, 120] # Baris 2
]
JUMLAH_BARIS = len(MATRIKS_DATA)
JUMLAH_KOLOM = len(MATRIKS_DATA[0])

# --- FUNGSI TAMPILAN TKINTER ---

def tampilkan_matriks(frame_matriks):
    """Fungsi untuk menampilkan elemen array 2D ke dalam grid Label di Tkinter."""
    
    # Hapus widget lama di frame_matriks sebelum membuat ulang
    for widget in frame_matriks.winfo_children():
        widget.destroy()

    tk.Label(frame_matriks, text="Array Dua Dimensi (3x4)", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=JUMLAH_KOLOM + 1, pady=10)

    # Header Kolom (C0, C1, C2, C3)
    tk.Label(frame_matriks, text="", width=5, relief=tk.FLAT).grid(row=1, column=0)
    for c in range(JUMLAH_KOLOM):
        tk.Label(frame_matriks, text=f"K{c}", font=('Arial', 9, 'bold'), width=5, relief=tk.RAISED).grid(row=1, column=c+1, padx=2, pady=2)
        
    # Data Matriks (Loop Bersarang)
    for r in range(JUMLAH_BARIS):
        # Label Baris (R0, R1, R2)
        tk.Label(frame_matriks, text=f"B{r}", font=('Arial', 9, 'bold'), width=5, relief=tk.RAISED).grid(row=r+2, column=0, padx=2, pady=2)
        
        for c in range(JUMLAH_KOLOM):
            nilai = MATRIKS_DATA[r][c]
            # Setiap elemen array ditampilkan sebagai Label di posisi (r+2, c+1)
            label_elemen = tk.Label(frame_matriks, text=str(nilai), width=5, relief=tk.GROOVE)
            label_elemen.grid(row=r+2, column=c+1, padx=2, pady=2)

def akses_dan_perbarui_nilai():
    """Fungsi untuk mengakses dan memperbarui elemen berdasarkan input Baris/Kolom."""
    try:
        baris = int(input_baris.get())
        kolom = int(input_kolom.get())
        
        # Validasi Indeks
        if 0 <= baris < JUMLAH_BARIS and 0 <= kolom < JUMLAH_KOLOM:
            
            # --- AKSES (Membaca) ---
            nilai_lama = MATRIKS_DATA[baris][kolom]
            
            # --- PERBARUI (Menulis) ---
            # Contoh: Perbarui nilai dengan angka acak baru
            nilai_baru = random.randint(200, 500)
            MATRIKS_DATA[baris][kolom] = nilai_baru

            # Tampilkan pesan dan perbarui GUI
            messagebox.showinfo(
                "Akses & Perbarui",
                f"Matriks[{baris}][{kolom}] berhasil diakses.\n"
                f"Nilai lama: {nilai_lama}\n"
                f"Nilai baru: {nilai_baru} (Diperbarui)"
            )
            
            # Panggil fungsi untuk menggambar ulang matriks dengan nilai baru
            tampilkan_matriks(frame_matriks)
            
        else:
            messagebox.showerror("Error", f"Indeks tidak valid. Baris harus (0-{JUMLAH_BARIS-1}), Kolom harus (0-{JUMLAH_KOLOM-1}).")
            
    except ValueError:
        messagebox.showerror("Error", "Input Baris dan Kolom harus berupa angka.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# --- SETUP JENDELA UTAMA TKINTER ---
root = tk.Tk()
root.title("Visualisasi Array Dua Dimensi (Matriks)")

# Frame Kiri: Visualisasi Matriks
frame_matriks = tk.Frame(root, padx=10, pady=10, relief=tk.SUNKEN, bd=2)
frame_matriks.pack(side=tk.LEFT, fill=tk.BOTH)

# Panggil fungsi untuk menampilkan matriks awal
tampilkan_matriks(frame_matriks)

# Frame Kanan: Kontrol Akses
frame_kontrol = tk.Frame(root, padx=15, pady=10)
frame_kontrol.pack(side=tk.RIGHT, fill=tk.BOTH)

tk.Label(frame_kontrol, text="Akses Data Matriks (2D)", font=('Helvetica', 10, 'bold')).pack(pady=10)

# Input Baris
tk.Label(frame_kontrol, text=f"Masukkan Indeks Baris (0-{JUMLAH_BARIS-1}):").pack()
input_baris = tk.StringVar(value="0")
tk.Entry(frame_kontrol, textvariable=input_baris, width=5).pack(pady=5)

# Input Kolom
tk.Label(frame_kontrol, text=f"Masukkan Indeks Kolom (0-{JUMLAH_KOLOM-1}):").pack()
input_kolom = tk.StringVar(value="0")
tk.Entry(frame_kontrol, textvariable=input_kolom, width=5).pack(pady=5)

# Tombol Akses dan Perbarui
tombol_akses = tk.Button(
    frame_kontrol, 
    text="Akses & Perbarui Nilai (Random)", 
    command=akses_dan_perbarui_nilai, 
    bg='lightblue'
)
tombol_akses.pack(pady=20)

# Jalankan loop utama Tkinter
root.mainloop()