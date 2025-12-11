import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import scrolledtext

# --- 1. Algoritma Bubble Sort yang Diadaptasi ---

def bubble_sort_gui(data_list):
    """
    Melakukan Bubble Sort dan menyimpan riwayat lengkap setiap swap.
    """
    n = len(data_list)
    data = list(data_list) # Buat salinan data agar data asli tidak berubah
    riwayat = []
    
    # Perulangan luar: Mengontrol jumlah pass
    for i in range(n - 1):
        swapped = False
        
        # Perulangan dalam: Melakukan perbandingan dan penukaran
        for j in range(0, n - 1 - i):
            
            # Simpan riwayat perbandingan (sebelum penukaran)
            riwayat.append({
                'tipe': 'compare',
                'data': list(data), # Salinan data saat ini
                'idx1': j,
                'idx2': j + 1
            })

            # KONDISI PENUKARAN (SWAP)
            if data[j] > data[j + 1]:
                
                # Melakukan Penukaran (Swap)
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                
                # Simpan riwayat penukaran (setelah penukaran)
                riwayat.append({
                    'tipe': 'swap',
                    'data': list(data), # Salinan data setelah swap
                    'idx1': j,
                    'idx2': j + 1
                })
        
        # Simpan riwayat setelah pass selesai (Menandai elemen terbesar berada di posisi akhir)
        riwayat.append({
            'tipe': 'pass_end',
            'data': list(data),
            'sorted_idx': n - 1 - i 
        })
        
        # Optimasi: Jika tidak ada penukaran, hentikan pengurutan
        if swapped == False:
            riwayat.append({'tipe': 'break', 'data': list(data)})
            break
            
    return data, riwayat

# --- 2. Fungsi Interaksi GUI ---

def aksi_sort():
    """Mengambil input, menjalankan Bubble Sort, dan menampilkan hasilnya."""
    
    data_str = entry_data.get().strip()

    if not data_str:
        messagebox.showwarning("Peringatan", "Input data tidak boleh kosong.")
        return

    try:
        # Konversi data list dari string ke list integer
        data_list = [int(x.strip()) for x in data_str.split(',')]
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka (bilangan bulat) dipisahkan koma.")
        return

    # Clear tampilan sebelumnya
    teks_riwayat.config(state=tk.NORMAL)
    teks_riwayat.delete('1.0', tk.END)

    # 1. Jalankan Algoritma
    data_terurut, riwayat = bubble_sort_gui(data_list)
    
    # 2. Tampilkan Ringkasan Hasil
    teks_riwayat.insert(tk.END, f"DATA AWAL: {data_list}\n")
    teks_riwayat.insert(tk.END, f"DATA TERURUT: {data_terurut}\n\n", 'result')
    teks_riwayat.insert(tk.END, f"Total Langkah (Perbandingan atau Penukaran): {len(riwayat)}\n\n")

    # 3. Tampilkan Riwayat Proses
    teks_riwayat.insert(tk.END, "--- Riwayat Pengurutan Bubble Sort ---\n", 'underline')
    
    pass_count = 0
    for step in riwayat:
        data_state = step['data']
        
        if step['tipe'] == 'compare':
            # Highlight elemen yang dibandingkan
            idx1, idx2 = step['idx1'], step['idx2']
            formatted_list = [str(val) for val in data_state]
            formatted_list[idx1] = f"[{formatted_list[idx1]}]" # Penanda [x]
            formatted_list[idx2] = f"({formatted_list[idx2]})" # Penanda (y)
            
            teks_riwayat.insert(tk.END, f"\n{pass_count}. Membandingkan Index {idx1} ({data_state[idx1]}) dan {idx2} ({data_state[idx2]})\n")
            teks_riwayat.insert(tk.END, f"   Larik: {' '.join(formatted_list)}\n", 'compare_tag')
        
        elif step['tipe'] == 'swap':
            # Highlight elemen yang ditukar
            idx1, idx2 = step['idx1'], step['idx2']
            formatted_list = [str(val) for val in data_state]
            formatted_list[idx1] = f"<{formatted_list[idx1]}>" # Penanda <x> (setelah swap)
            formatted_list[idx2] = f"<{formatted_list[idx2]}>"
            
            teks_riwayat.insert(tk.END, f"   **SWAP**! Posisi {idx1} dan {idx2} ditukar.\n", 'swap_tag')
            teks_riwayat.insert(tk.END, f"   Larik: {' '.join(formatted_list)}\n", 'swap_tag')
            
        elif step['tipe'] == 'pass_end':
            pass_count += 1
            sorted_idx = step['sorted_idx']
            teks_riwayat.insert(tk.END, f"\nPASS #{pass_count} SELESAI. {data_state[sorted_idx]} 'Menggelembung' ke posisi akhirnya (Indeks {sorted_idx}).\n", 'pass_end_tag')
            teks_riwayat.insert(tk.END, f"   Larik Akhir Pass: {data_state}\n", 'pass_end_tag')
            
        elif step['tipe'] == 'break':
            teks_riwayat.insert(tk.END, "\n--- OPTIMASI: TIDAK ADA SWAP PADA PASS TERAKHIR. Sorting Selesai! ---\n", 'break_tag')
            break
            
    teks_riwayat.config(state=tk.DISABLED)

# --- 3. Konfigurasi Jendela Utama Tkinter ---

jendela_utama = tk.Tk()
jendela_utama.title("Simulasi Algoritma Bubble Sort")
jendela_utama.geometry("700x550")

# Setup Font & Tag Warna
judul_font = tkfont.Font(family="Arial", size=14, weight="bold")

# Frame Input & Kontrol
frame_control = tk.Frame(jendela_utama, padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
frame_control.pack(fill='x', padx=10, pady=10)

tk.Label(frame_control, text="Bubble Sort Input", font=judul_font).grid(row=0, columnspan=2, pady=5)

# Input Data Larik
tk.Label(frame_control, text="Data Acak (Koma):").grid(row=1, column=0, sticky='w', padx=5)
entry_data = tk.Entry(frame_control, width=50)
entry_data.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
# Contoh data acak
entry_data.insert(0, "5, 1, 4, 2, 8") 

# Tombol Sort
tombol_sort = tk.Button(
    frame_control,
    text="Jalankan Bubble Sort",
    command=aksi_sort,
    bg='#ADD8E6',
    font=tkfont.Font(family="Arial", size=10, weight="bold")
)
tombol_sort.grid(row=2, column=1, sticky='w', padx=10)

# Area Output Riwayat
tk.Label(jendela_utama, text="Riwayat Proses Perbandingan dan Penukaran", font=judul_font).pack(pady=5)
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
teks_riwayat.tag_config('swap_tag', foreground='#FF4500')    # Orange Red untuk Swap
teks_riwayat.tag_config('pass_end_tag', foreground='#3CB371', font=('Courier', 10, 'bold')) # Medium Sea Green
teks_riwayat.tag_config('result', foreground='darkgreen', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('break_tag', foreground='black', background='yellow')
teks_riwayat.tag_config('underline', underline=1)

# --- 4. Memulai Loop Utama Aplikasi ---
jendela_utama.mainloop()