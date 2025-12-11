import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import scrolledtext

# --- 1. Struktur Data Dictionary Global (Inventaris Toko) ---
# Key: Nama Barang (String), Value: Harga Barang (Angka)
inventaris_toko = {}

# --- 2. Fungsi Pembantu GUI ---

def perbarui_tampilan():
    """Memperbarui visualisasi daftar inventaris di GUI."""
    teks_tampilan.config(state=tk.NORMAL)
    teks_tampilan.delete('1.0', tk.END)
    
    if not inventaris_toko:
        teks_tampilan.insert(tk.END, "Inventaris Toko Kosong.")
        
    # Urutkan berdasarkan Nama Barang (Kunci) untuk tampilan yang rapi
    sorted_items = sorted(inventaris_toko.items())
    
    teks_tampilan.insert(tk.END, "--- INVENTARIS TOKO (Nama Barang : Harga) ---\n", 'header')
    
    for key, value in sorted_items:
        # Format harga ke dalam mata uang (Rp)
        harga_formatted = f"Rp {value:,.0f}".replace(",", "_").replace(".", ",").replace("_", ".")
        teks_tampilan.insert(tk.END, f"'{key}' : {harga_formatted}\n")

    teks_tampilan.config(state=tk.DISABLED)

# --- 3. Fungsi Operasi Inventaris ---

def aksi_tambah_ubah():
    """Menambahkan atau memperbarui harga barang."""
    key = entry_key.get().strip().upper() # Jadikan huruf besar agar Kunci konsisten
    value_str = entry_value.get().strip()
    
    if not key or not value_str:
        messagebox.showwarning("Peringatan", "Nama Barang dan Harga harus diisi.")
        return

    try:
        # Validasi bahwa harga adalah angka
        value = int(value_str.replace(".", "")) # Hilangkan pemisah ribuan jika ada
        if value <= 0: raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Harga harus berupa angka bulat positif.")
        return

    is_update = key in inventaris_toko

    inventaris_toko[key] = value # Operasi Dictionary O(1)
    
    if is_update:
        messagebox.showinfo("Sukses", f"Harga barang '{key}' berhasil diperbarui!")
    else:
        messagebox.showinfo("Sukses", f"Barang baru '{key}' berhasil ditambahkan.")
        
    entry_key.delete(0, tk.END)
    entry_value.delete(0, tk.END)
    perbarui_tampilan()

def aksi_cari():
    """Mencari harga barang berdasarkan Nama Barang (Kunci)."""
    key = entry_key.get().strip().upper()
    
    if not key:
        messagebox.showwarning("Peringatan", "Nama Barang pencarian tidak boleh kosong.")
        return
        
    # Operasi Retrieval O(1)
    if key in inventaris_toko:
        harga = inventaris_toko[key]
        harga_formatted = f"Rp {harga:,.0f}".replace(",", "_").replace(".", ",").replace("_", ".")
        
        messagebox.showinfo("Harga Ditemukan", f"Nama Barang: '{key}'\nHarga Jual: {harga_formatted}")
        
        entry_value.delete(0, tk.END)
        entry_value.insert(0, str(harga))
    else:
        messagebox.showerror("Barang Tidak Ada", f"Barang '{key}' TIDAK ditemukan dalam Inventaris.")
        entry_value.delete(0, tk.END)
        
def aksi_hapus():
    """Menghapus barang dari inventaris."""
    key = entry_key.get().strip().upper()
    
    if not key:
        messagebox.showwarning("Peringatan", "Nama Barang yang akan dihapus tidak boleh kosong.")
        return
        
    # Operasi Deletion O(1)
    if key in inventaris_toko:
        del inventaris_toko[key]
        messagebox.showinfo("Sukses", f"Barang '{key}' berhasil dihapus dari inventaris.")
        entry_key.delete(0, tk.END)
        entry_value.delete(0, tk.END)
        perbarui_tampilan()
    else:
        messagebox.showerror("Error", f"Barang '{key}' tidak ditemukan.")

# --- 4. Konfigurasi Jendela Utama Tkinter ---

jendela_utama = tk.Tk()
jendela_utama.title("Sistem Inventaris Toko (Aplikasi Dictionary)")
jendela_utama.geometry("600x580")

judul_font = tkfont.Font(family="Arial", size=14, weight="bold")
label_font = tkfont.Font(family="Arial", size=10)

# Frame Input
frame_input = tk.Frame(jendela_utama, padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
frame_input.pack(fill='x', padx=10, pady=10)

tk.Label(frame_input, text="Pencatatan Harga Barang", font=judul_font).grid(row=0, columnspan=2, pady=10)

# Input Key (Nama Barang)
tk.Label(frame_input, text="Nama Barang (Key):", font=label_font).grid(row=1, column=0, sticky='w', padx=5, pady=5)
entry_key = tk.Entry(frame_input, width=30, font=label_font)
entry_key.grid(row=1, column=1, sticky='w', padx=5, pady=5)
entry_key.insert(0, "MIE INSTAN")

# Input Value (Harga Barang)
tk.Label(frame_input, text="Harga Jual (Value):", font=label_font).grid(row=2, column=0, sticky='w', padx=5, pady=5)
entry_value = tk.Entry(frame_input, width=30, font=label_font)
entry_value.grid(row=2, column=1, sticky='w', padx=5, pady=5)
entry_value.insert(0, "3000")

# Tombol Operasi
frame_buttons = tk.Frame(frame_input)
frame_buttons.grid(row=3, columnspan=2, pady=15)

tk.Button(frame_buttons, text="Tambah / Ubah Harga", command=aksi_tambah_ubah, bg='#90EE90', font=label_font).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Cari Harga", command=aksi_cari, bg='#ADD8E6', font=label_font).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Hapus Barang", command=aksi_hapus, bg='#F08080', font=label_font).pack(side=tk.LEFT, padx=5)


# Area Output Dictionary
tk.Label(jendela_utama, text="Daftar Inventaris", font=judul_font).pack(pady=5)
teks_tampilan = scrolledtext.ScrolledText(
    jendela_utama,
    height=15,
    width=60,
    font=('Courier', 12),
    relief=tk.SUNKEN,
    state=tk.DISABLED
)
teks_tampilan.pack(padx=10, pady=5)

# Setup tag header
teks_tampilan.tag_config('header', font=('Courier', 12, 'bold'), foreground='darkgreen')

# Inisialisasi tampilan
perbarui_tampilan()

# --- 5. Memulai Loop Utama Aplikasi ---
jendela_utama.mainloop()