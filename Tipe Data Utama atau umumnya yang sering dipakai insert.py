import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import ttk

# --- Data Global ---
shopping_list = ["Apel", "Roti", "Susu"] # List awal
list_font = ('Courier', 12)

# --- 1. Fungsi Manipulasi List ---

def update_output():
    """Memperbarui tampilan List di area teks output."""
    teks_hasil.config(state=tk.NORMAL)
    teks_hasil.delete('1.0', tk.END)
    
    teks_hasil.insert(tk.END, "--- Struktur Data: List (Daftar Belanja) ---\n", 'header')
    teks_hasil.insert(tk.END, f"Jumlah Item: {len(shopping_list)}\n", 'info')
    
    if not shopping_list:
        teks_hasil.insert(tk.END, "\nList kosong. Tambahkan item pertama Anda.\n", 'empty')
    else:
        teks_hasil.insert(tk.END, "\nIsi List:\n", 'info')
        # Tampilkan setiap item dengan Indeks (indeks dimulai dari 0)
        for index, item in enumerate(shopping_list):
            teks_hasil.insert(tk.END, f"  [{index}] = {item}\n", 'list_item')
            
    teks_hasil.config(state=tk.DISABLED)

def tambah_item():
    """Menambahkan item baru ke akhir List (operasi APPEND)."""
    item_baru = entry_item.get().strip()
    if item_baru:
        # Operasi List: APPEND
        shopping_list.append(item_baru)
        entry_item.delete(0, tk.END)
        update_output()
    else:
        messagebox.showwarning("Input Kosong", "Masukkan nama item yang akan ditambahkan.")

def hapus_item():
    """Menghapus item dari List berdasarkan nama atau Indeks."""
    identifier = entry_item.get().strip()
    if not identifier:
        messagebox.showwarning("Input Kosong", "Masukkan nama item atau Indeks untuk dihapus.")
        return
        
    try:
        # Coba hapus berdasarkan Indeks (jika input adalah angka)
        indeks = int(identifier)
        if 0 <= indeks < len(shopping_list):
            # Operasi List: POP (menghapus berdasarkan indeks)
            shopping_list.pop(indeks)
            entry_item.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"Indeks '{indeks}' di luar jangkauan (0 sampai {len(shopping_list)-1}).")
            return
            
    except ValueError:
        # Jika input bukan angka, hapus berdasarkan Nama Item
        try:
            # Operasi List: REMOVE (menghapus berdasarkan nilai)
            shopping_list.remove(identifier)
            entry_item.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", f"Item '{identifier}' tidak ditemukan dalam list.")
            return

    update_output()

def akses_dan_ubah_item():
    """Mengakses item berdasarkan indeks dan menunjukkan nilainya."""
    indeks_str = entry_indeks.get().strip()
    nilai_baru = entry_nilai_baru.get().strip()
    
    try:
        indeks = int(indeks_str)
        if not (0 <= indeks < len(shopping_list)):
             messagebox.showerror("Error", f"Indeks '{indeks}' di luar jangkauan (0 sampai {len(shopping_list)-1}).")
             return
             
        if nilai_baru:
            # Operasi List: INDEXING (mengubah nilai)
            shopping_list[indeks] = nilai_baru
            messagebox.showinfo("Berhasil", f"Item pada indeks [{indeks}] telah diubah menjadi '{nilai_baru}'.")
        else:
            # Operasi List: INDEXING (mengakses nilai)
            item_diakses = shopping_list[indeks]
            messagebox.showinfo("Akses Item", f"Item pada indeks [{indeks}] adalah: '{item_diakses}'.")
            
    except ValueError:
        messagebox.showerror("Error", "Indeks harus berupa bilangan bulat.")
        return
        
    update_output()

# --- 2. Konfigurasi Jendela Utama Tkinter ---

def main():
    """Fungsi utama untuk inisialisasi Tkinter."""
    global entry_item, entry_indeks, entry_nilai_baru, teks_hasil
    
    jendela_utama = tk.Tk()
    jendela_utama.title("Simulasi Tipe Data List (Daftar)")
    jendela_utama.geometry("600x650")

    judul_font = tkfont.Font(family="Arial", size=14, weight="bold")

    # --- FRAME INPUT & AKSI ---
    frame_aksi = tk.LabelFrame(jendela_utama, text="Manipulasi List", font=judul_font, padx=10, pady=10)
    frame_aksi.pack(fill='x', padx=15, pady=10)

    # Sub-Frame 1: Tambah/Hapus
    sub_frame_1 = tk.LabelFrame(frame_aksi, text="Tambah / Hapus Item", padx=10, pady=10)
    sub_frame_1.pack(fill='x', pady=5)
    
    tk.Label(sub_frame_1, text="Item / Indeks:", font=list_font).pack(side=tk.LEFT, padx=5)
    entry_item = tk.Entry(sub_frame_1, width=20, font=list_font)
    entry_item.pack(side=tk.LEFT, padx=5)

    ttk.Button(sub_frame_1, text="➕ Tambah", command=tambah_item).pack(side=tk.LEFT, padx=5)
    ttk.Button(sub_frame_1, text="❌ Hapus", command=hapus_item).pack(side=tk.LEFT, padx=5)

    # Sub-Frame 2: Akses/Ubah
    sub_frame_2 = tk.LabelFrame(frame_aksi, text="Akses / Ubah Item (Indexing)", padx=10, pady=10)
    sub_frame_2.pack(fill='x', pady=10)
    
    tk.Label(sub_frame_2, text="Indeks [i]:", font=list_font).pack(side=tk.LEFT, padx=5)
    entry_indeks = tk.Entry(sub_frame_2, width=5, font=list_font)
    entry_indeks.pack(side=tk.LEFT, padx=5)

    tk.Label(sub_frame_2, text="Nilai Baru:", font=list_font).pack(side=tk.LEFT, padx=5)
    entry_nilai_baru = tk.Entry(sub_frame_2, width=15, font=list_font)
    entry_nilai_baru.pack(side=tk.LEFT, padx=5)

    ttk.Button(sub_frame_2, text="👁️ Akses/Ubah", command=akses_dan_ubah_item).pack(side=tk.LEFT, padx=5)

    # --- AREA OUTPUT ---
    tk.Label(jendela_utama, text="Visualisasi List", font=judul_font).pack(pady=5)
    teks_hasil = tk.Text(
        jendela_utama,
        height=15,
        width=55,
        font=('Courier', 12),
        relief=tk.SUNKEN,
        state=tk.DISABLED
    )
    teks_hasil.pack(padx=10, pady=5)

    # Setup Tag Warna
    teks_hasil.tag_config('header', font=('Courier', 12, 'bold', 'underline'), foreground='darkblue')
    teks_hasil.tag_config('info', foreground='gray50')
    teks_hasil.tag_config('list_item', foreground='black')
    teks_hasil.tag_config('empty', foreground='red')

    # Inisialisasi tampilan list saat aplikasi dibuka
    update_output()

    jendela_utama.mainloop()

# Memanggil fungsi main saat skrip dijalankan
if __name__ == "__main__":
    main()