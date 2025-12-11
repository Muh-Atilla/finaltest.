import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import scrolledtext

# --- 1. Algoritma Selection Sort yang Diadaptasi ---

def selection_sort_gui(data_list):
    """
    Melakukan Selection Sort dan menyimpan riwayat setiap langkah:
    pencarian minimum dan penukaran (swap) tunggal.
    """
    n = len(data_list)
    data = list(data_list) # Buat salinan data
    riwayat = []
    
    # Perulangan luar: Mengontrol posisi elemen yang akan ditempati (i)
    for i in range(n):
        min_idx = i # Asumsikan elemen di posisi i adalah yang terkecil
        
        # Riwayat awal Pass (Mulai mencari elemen terkecil)
        riwayat.append({
            'tipe': 'start_pass',
            'data': list(data),
            'i': i,
            'min_idx': min_idx
        })
        
        # Perulangan dalam: Mencari elemen terkecil dari i + 1 hingga akhir
        for j in range(i + 1, n):
            
            # Simpan riwayat perbandingan (mengecek elemen j)
            riwayat.append({
                'tipe': 'compare',
                'data': list(data),
                'j': j,
                'current_min_idx': min_idx
            })
            
            # Jika ditemukan elemen yang lebih kecil
            if data[j] < data[min_idx]:
                min_idx = j # Perbarui indeks elemen terkecil yang baru ditemukan
                
                # Simpan riwayat penemuan minimum baru
                riwayat.append({
                    'tipe': 'new_min',
                    'data': list(data),
                    'min_idx': min_idx
                })
        
        # --- Hanya SATU kali penukaran (swap) per iterasi luar ---
        if min_idx != i:
            # Melakukan Penukaran (Swap)
            data[i], data[min_idx] = data[min_idx], data[i]
            
            # Simpan riwayat penukaran
            riwayat.append({
                'tipe': 'swap',
                'data': list(data),
                'i': i,
                'min_idx': min_idx
            })
        else:
            # Tidak ada swap, elemen di posisi i sudah benar
            riwayat.append({
                'tipe': 'no_swap',
                'data': list(data),
                'i': i
            })
            
    return data, riwayat

# --- 2. Fungsi Interaksi GUI ---

def aksi_sort():
    """Mengambil input, menjalankan Selection Sort, dan menampilkan hasilnya."""
    
    data_str = entry_data.get().strip()

    if not data_str:
        messagebox.showwarning("Peringatan", "Input data tidak boleh kosong.")
        return

    try:
        # Konversi data list dari string ke list integer
        data_list = [int(x.strip()) for x in data_str.split(',')]
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka dipisahkan koma.")
        return

    # Clear tampilan sebelumnya
    teks_riwayat.config(state=tk.NORMAL)
    teks_riwayat.delete('1.0', tk.END)

    # 1. Jalankan Algoritma
    data_terurut, riwayat = selection_sort_gui(data_list)
    
    # 2. Tampilkan Ringkasan Hasil
    teks_riwayat.insert(tk.END, f"DATA AWAL: {data_list}\n")
    teks_riwayat.insert(tk.END, f"DATA TERURUT: {data_terurut}\n\n", 'result')
    teks_riwayat.insert(tk.END, f"Total Langkah (Perbandingan, Penemuan Min, Swap): {len(riwayat)}\n\n")

    # 3. Tampilkan Riwayat Proses
    teks_riwayat.insert(tk.END, "--- Riwayat Pengurutan Selection Sort ---\n", 'underline')
    
    pass_count = 0
    for step in riwayat:
        data_state = step['data']
        tipe = step['tipe']
        
        if tipe == 'start_pass':
            pass_count += 1
            i = step['i']
            teks_riwayat.insert(tk.END, f"\nPASS #{pass_count} - Posisi Target (i): {i}\n", 'pass_end_tag')
            teks_riwayat.insert(tk.END, f"  Diasumsikan Minimum: {data_state[i]}\n", 'low_tag')
            teks_riwayat.insert(tk.END, f"  Larik: {data_state}\n", 'low_tag')
            
        elif tipe == 'compare':
            j = step['j']
            min_idx = step['current_min_idx']
            
            if j == min_idx: # Hanya mencetak saat indeks min berubah
                 continue
            
            teks_riwayat.insert(tk.END, f"  Mencari Min: Bandingkan {data_state[j]} (j={j}) dengan {data_state[min_idx]} (min_idx={min_idx})\n", 'compare_tag')
            
        elif tipe == 'new_min':
            min_idx = step['min_idx']
            teks_riwayat.insert(tk.END, f"  >> MIN BARU ditemukan pada Index {min_idx}: {data_state[min_idx]} <<\n", 'new_min_tag')
            
        elif tipe == 'swap':
            i = step['i']
            min_idx = step['min_idx']
            teks_riwayat.insert(tk.END, f"  **SWAP**! Menukar Elemen Terkecil ({data_state[i]}) dari Index {min_idx} ke Posisi Target {i}.\n", 'swap_tag')
            teks_riwayat.insert(tk.END, f"  Larik Setelah Swap: {data_state}\n", 'swap_tag')
            
        elif tipe == 'no_swap':
            i = step['i']
            teks_riwayat.insert(tk.END, f"  Tidak ada Swap. Elemen {data_state[i]} sudah di posisi yang benar (Index {i}).\n", 'pass_end_tag')

            
    teks_riwayat.config(state=tk.DISABLED)

# --- 3. Konfigurasi Jendela Utama Tkinter ---

jendela_utama = tk.Tk()
jendela_utama.title("Simulasi Algoritma Selection Sort")
jendela_utama.geometry("700x550")

# Setup Font & Tag Warna
judul_font = tkfont.Font(family="Arial", size=14, weight="bold")

# Frame Input & Kontrol
frame_control = tk.Frame(jendela_utama, padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
frame_control.pack(fill='x', padx=10, pady=10)

tk.Label(frame_control, text="Selection Sort Input", font=judul_font).grid(row=0, columnspan=2, pady=5)

# Input Data Larik
tk.Label(frame_control, text="Data Acak (Koma):").grid(row=1, column=0, sticky='w', padx=5)
entry_data = tk.Entry(frame_control, width=50)
entry_data.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
entry_data.insert(0, "64, 25, 12, 22, 11") 

# Tombol Sort
tombol_sort = tk.Button(
    frame_control,
    text="Jalankan Selection Sort",
    command=aksi_sort,
    bg='#ADD8E6',
    font=tkfont.Font(family="Arial", size=10, weight="bold")
)
tombol_sort.grid(row=2, column=1, sticky='w', padx=10)

# Area Output Riwayat
tk.Label(jendela_utama, text="Riwayat Proses Pencarian dan Penukaran", font=judul_font).pack(pady=5)
teks_riwayat = scrolledtext.ScrolledText(
    jendela_utama,
    height=20,
    width=80,
    font=('Courier', 10),
    relief=tk.SUNKEN,
    state=tk.DISABLED
)
teks_riwayat.pack(padx=10, pady=5)

# Tambahkan Tag Warna ke ScrolledText
teks_riwayat.tag_config('compare_tag', foreground='#4169E1') # Royal Blue untuk Perbandingan
teks_riwayat.tag_config('new_min_tag', foreground='#FFD700', background='#8B0000', font=('Courier', 10, 'bold')) # Emas/Merah untuk Min Baru
teks_riwayat.tag_config('swap_tag', foreground='#FF4500')    # Orange Red untuk Swap
teks_riwayat.tag_config('pass_end_tag', foreground='#3CB371', font=('Courier', 10, 'bold')) # Medium Sea Green
teks_riwayat.tag_config('result', foreground='darkgreen', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('low_tag', foreground='blue') # Blue untuk posisi awal pass
teks_riwayat.tag_config('underline', underline=1)

# --- 4. Memulai Loop Utama Aplikasi ---
jendela_utama.mainloop()