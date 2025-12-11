import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import scrolledtext

# --- 1. Algoritma Binary Search yang Diadaptasi ---
def binary_search_gui(data_list, target):
    """
    Melakukan pencarian biner dan menyimpan riwayat lengkap.
    """
    low = 0
    high = len(data_list) - 1
    langkah = 0
    riwayat = []

    while low <= high:
        langkah += 1
        mid = (low + high) // 2
        guess = data_list[mid]
        
        # Simpan state saat ini
        riwayat.append({
            'langkah': langkah,
            'low': low,
            'mid': mid,
            'high': high,
            'guess': guess
        })
        
        if guess == target:
            return mid, langkah, riwayat
            
        elif target < guess:
            high = mid - 1
            
        else: # target > guess
            low = mid + 1
            
    # Target tidak ditemukan
    return -1, langkah, riwayat

# --- 2. Fungsi Interaksi GUI ---
def aksi_cari():
    """Mengambil input, menjalankan Binary Search, dan menampilkan hasilnya."""
    
    data_str = entry_data.get().strip()
    target_str = entry_target.get().strip()

    # Validasi input
    if not data_str or not target_str:
        messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")
        return

    try:
        data_list = [int(x.strip()) for x in data_str.split(',')]
        target = int(target_str)
        
        if data_list != sorted(data_list):
            messagebox.showerror("Error", "Binary Search memerlukan data yang sudah diurutkan!")
            return

    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka.")
        return

    # Clear tampilan sebelumnya
    listbox_data.delete(0, tk.END)
    teks_riwayat.config(state=tk.NORMAL)
    teks_riwayat.delete('1.0', tk.END)

    # 1. Tampilkan Data Larik di Listbox
    for i, val in enumerate(data_list):
        listbox_data.insert(tk.END, f"[{i}] : {val}")
        
    # 2. Jalankan Algoritma
    indeks, langkah, riwayat = binary_search_gui(data_list, target)
    
    # 3. Tampilkan Ringkasan Hasil
    if indeks != -1:
        hasil_text = f"✅ TARGET DITEMUKAN pada Indeks {indeks} (Total {langkah} langkah)"
        listbox_data.itemconfig(indeks, {'bg': 'yellowgreen'}) # Highlight hasil di Listbox
    else:
        hasil_text = f"❌ TARGET TIDAK DITEMUKAN (Total {langkah} langkah)"
        
    teks_riwayat.insert(tk.END, f"DATA LARIK: {data_list}\n")
    teks_riwayat.insert(tk.END, f"TARGET DICARI: {target}\n")
    teks_riwayat.insert(tk.END, f"HASIL: {hasil_text}\n\n")

    # 4. Tampilkan Riwayat Proses
    teks_riwayat.insert(tk.END, "--- Riwayat Pencarian Langkah demi Langkah ---\n", 'underline')
    
    for step in riwayat:
        low = step['low']
        mid = step['mid']
        high = step['high']
        guess = step['guess']
        
        hasil = "Ditemukan!" if guess == target else ("Target di Kiri" if target < guess else "Target di Kanan")
        
        teks_riwayat.insert(tk.END, f"\nLangkah {step['langkah']}:\n", 'bold')
        teks_riwayat.insert(tk.END, f"  low={low}, mid={mid}, high={high}\n")
        
        # Tambahkan visualisasi warna pada teks riwayat
        teks_riwayat.insert(tk.END, "  Tebakan (Mid): ", 'normal')
        teks_riwayat.insert(tk.END, f"{guess}", 'mid_tag')
        
        teks_riwayat.insert(tk.END, f" | Batas Kiri (Low): ", 'normal')
        teks_riwayat.insert(tk.END, f"{data_list[low]}", 'low_tag')
        
        teks_riwayat.insert(tk.END, f" | Batas Kanan (High): ", 'normal')
        teks_riwayat.insert(tk.END, f"{data_list[high]}", 'high_tag')
        
        teks_riwayat.insert(tk.END, f" | Keputusan: {hasil}\n", 'normal')

        if guess == target: break
        
    teks_riwayat.config(state=tk.DISABLED)

# --- 3. Konfigurasi Jendela Utama Tkinter ---

jendela_utama = tk.Tk()
jendela_utama.title("Simulasi Binary Search v3.0 (Visual)")
jendela_utama.geometry("800x600")

# Setup Font & Tag Warna untuk ScrolledText
judul_font = tkfont.Font(family="Arial", size=14, weight="bold")
teks_font = tkfont.Font(family="Courier", size=10)

# Frame Input & Kontrol
frame_control = tk.Frame(jendela_utama, padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
frame_control.pack(fill='x', padx=10, pady=10)

tk.Label(frame_control, text="Binary Search Input", font=judul_font).grid(row=0, columnspan=3, pady=5)

# Input Data Larik
tk.Label(frame_control, text="Data Terurut (Koma):").grid(row=1, column=0, sticky='w', padx=5)
entry_data = tk.Entry(frame_control, width=50)
entry_data.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
entry_data.insert(0, "2, 5, 8, 12, 16, 23, 38, 56, 72, 91") 

# Input Target
tk.Label(frame_control, text="Target Pencarian:").grid(row=1, column=2, sticky='w', padx=5)
entry_target = tk.Entry(frame_control, width=15)
entry_target.grid(row=2, column=2, sticky='w', padx=5, pady=5)
entry_target.insert(0, "72") 

# Tombol Cari
tombol_cari = tk.Button(
    frame_control,
    text="Jalankan Pencarian Biner",
    command=aksi_cari,
    bg='#ADD8E6',
    font=tkfont.Font(family="Arial", size=10, weight="bold")
)
tombol_cari.grid(row=3, columnspan=3, pady=10, sticky='ew')

# --- 4. Frame Visualisasi Data & Riwayat ---
frame_visual = tk.Frame(jendela_utama, padx=10, pady=10)
frame_visual.pack(fill='both', expand=True, padx=10, pady=5)

# Listbox untuk Data Larik
tk.Label(frame_visual, text="Data Larik (Index : Value)", font=judul_font).grid(row=0, column=0, sticky='n')
listbox_data = tk.Listbox(
    frame_visual,
    height=20,
    width=20,
    font=teks_font,
    relief=tk.SUNKEN
)
listbox_data.grid(row=1, column=0, sticky='nswe', padx=10)

# ScrolledText untuk Riwayat
tk.Label(frame_visual, text="Riwayat Proses dan Keputusan", font=judul_font).grid(row=0, column=1, sticky='n')
teks_riwayat = scrolledtext.ScrolledText(
    frame_visual,
    height=20,
    width=60,
    font=teks_font,
    relief=tk.SUNKEN,
    state=tk.DISABLED
)
teks_riwayat.grid(row=1, column=1, sticky='nswe', padx=10)

# Konfigurasi Grid Weight
frame_visual.grid_columnconfigure(1, weight=1)
frame_visual.grid_rowconfigure(1, weight=1)

# Tambahkan Tag Warna ke ScrolledText
teks_riwayat.tag_config('mid_tag', foreground='red', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('low_tag', foreground='blue', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('high_tag', foreground='green', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('bold', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('underline', underline=1)

# --- 5. Memulai Loop Utama Aplikasi ---
jendela_utama.mainloop()