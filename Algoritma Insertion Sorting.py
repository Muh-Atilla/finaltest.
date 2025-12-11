import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import scrolledtext

# --- 1. Algoritma Insertion Sort yang Diadaptasi (Tanpa Perubahan Logika) ---
def insertion_sort_gui(data_list):
    """
    Melakukan Insertion Sort pada daftar string dan menyimpan riwayat langkah.
    """
    n = len(data_list)
    data = list(data_list) 
    riwayat = []
    
    for i in range(1, n):
        key = data[i]
        j = i - 1 
        
        # 1. Mulai Pass
        riwayat.append({
            'tipe': 'start_pass',
            'data': list(data),
            'i': i,
            'key': key
        })
        
        # 2. Proses Pergeseran (Shift)
        while j >= 0 and key < data[j]:
            
            riwayat.append({
                'tipe': 'shift',
                'data': list(data),
                'j': j,
                'shifted_val': data[j],
                'new_pos': j + 1
            })
            
            data[j + 1] = data[j]
            j -= 1
        
        # 3. Penyisipan (Insert)
        riwayat.append({
            'tipe': 'insert',
            'data': list(data),
            'insert_idx': j + 1,
            'key': key
        })
        
        data[j + 1] = key
        
        # 4. Akhir Pass
        riwayat.append({
            'tipe': 'pass_end',
            'data': list(data)
        })
            
    return data, riwayat

# --- 2. Fungsi Interaksi GUI (Fokus pada Output yang Lebih Rapi) ---

def aksi_sort():
    """Mengambil input, menjalankan Insertion Sort pada string, dan menampilkan hasilnya."""
    
    data_str = entry_data.get().strip()
    data_list = [x.strip() for x in data_str.split(',')]

    # ... (Validasi dihilangkan untuk fokus pada output) ...

    teks_riwayat.config(state=tk.NORMAL)
    teks_riwayat.delete('1.0', tk.END)

    data_terurut, riwayat = insertion_sort_gui(data_list)
    
    # 2. Tampilkan Ringkasan Hasil
    teks_riwayat.insert(tk.END, f"DATA AWAL (String): {data_list}\n")
    teks_riwayat.insert(tk.END, f"DATA TERURUT: {data_terurut}\n\n", 'result')

    # 3. Tampilkan Riwayat Proses dalam Format Tabular/Langkah
    teks_riwayat.insert(tk.END, "--- Riwayat Pengurutan (Langkah/Step) ---\n", 'underline')
    
    pass_number = 0
    step_number = 0
    
    for step in riwayat:
        tipe = step['tipe']
        data_state = step['data']
        step_number += 1
        
        if tipe == 'start_pass':
            pass_number += 1
            i = step['i']
            key = step['key']
            teks_riwayat.insert(tk.END, f"\n===== PASS #{pass_number} (i={i}) =====\n", 'pass_end_tag')
            teks_riwayat.insert(tk.END, f"[{step_number}] KEY: '{key}' (Akan disisipkan ke Bagian Terurut)\n", 'key_tag')
            teks_riwayat.insert(tk.END, f"      Status Larik: {data_state}\n")
        
        elif tipe == 'shift':
            j = step['j']
            shifted_val = step['shifted_val']
            new_pos = step['new_pos']
            
            teks_riwayat.insert(tk.END, f"[{step_number}] SHIFT: '{shifted_val}' (Index {j}) > KEY. Geser ke Index {new_pos}.\n", 'shift_tag')
            teks_riwayat.insert(tk.END, f"      Status Larik: {data_state}\n")

        elif tipe == 'insert':
            insert_idx = step['insert_idx']
            key = step['key']
            
            teks_riwayat.insert(tk.END, f"[{step_number}] INSERT: Sisipkan '{key}' pada Index {insert_idx}.\n", 'insert_tag')
            teks_riwayat.insert(tk.END, f"      Status Larik: {data_state}\n") # Data state sebelum sisipan

        elif tipe == 'pass_end':
            teks_riwayat.insert(tk.END, f"      Larik Setelah Pass #{pass_number}: {data_state}\n", 'pass_end_tag')
            
    teks_riwayat.config(state=tk.DISABLED)

# --- 3. Konfigurasi Jendela Utama Tkinter (Tanpa Perubahan Visual) ---
# ... (Konfigurasi Jendela Utama, Frame Kontrol, Input Data, dan Tombol tetap sama) ...
# PENTING: Saya akan menggunakan konfigurasi dari kode sebelumnya di sini.

jendela_utama = tk.Tk()
jendela_utama.title("Simulasi Algoritma Insertion Sort (String/Leksikografis) - Output Diubah")
jendela_utama.geometry("750x600")

judul_font = tkfont.Font(family="Arial", size=14, weight="bold")

frame_control = tk.Frame(jendela_utama, padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
frame_control.pack(fill='x', padx=10, pady=10)

tk.Label(frame_control, text="Insertion Sort Input (String)", font=judul_font).grid(row=0, columnspan=2, pady=5)

tk.Label(frame_control, text="Data Teks (Pisahkan dengan koma):").grid(row=1, column=0, sticky='w', padx=5)
entry_data = tk.Entry(frame_control, width=50)
entry_data.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
entry_data.insert(0, "Mawar, Tulip, Anggrek, Kamboja, Lili") 

tombol_sort = tk.Button(
    frame_control,
    text="Jalankan Insertion Sort",
    command=aksi_sort,
    bg='#ADD8E6',
    font=tkfont.Font(family="Arial", size=10, weight="bold")
)
tombol_sort.grid(row=2, column=1, sticky='w', padx=10)

tk.Label(jendela_utama, text="Riwayat Proses Pergeseran dan Penyisipan", font=judul_font).pack(pady=5)
teks_riwayat = scrolledtext.ScrolledText(
    jendela_utama,
    height=25,
    width=90,
    font=('Courier', 10),
    relief=tk.SUNKEN,
    state=tk.DISABLED
)
teks_riwayat.pack(padx=10, pady=5)

# Tambahkan Tag Warna ke ScrolledText
teks_riwayat.tag_config('key_tag', foreground='#FF4500', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('shift_tag', foreground='#4169E1')
teks_riwayat.tag_config('insert_tag', foreground='#3CB371', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('pass_end_tag', background='#F0F8FF', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('result', foreground='darkgreen', font=('Courier', 10, 'bold'))
teks_riwayat.tag_config('underline', underline=1)

# --- 4. Memulai Loop Utama Aplikasi ---
jendela_utama.mainloop()