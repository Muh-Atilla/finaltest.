import tkinter as tk
from tkinter import messagebox

# --- 1. Kelas Implementasi Stack (Struktur Data) ---
class Stack:
    """Kelas untuk mengimplementasikan struktur data Stack menggunakan list."""
    def __init__(self):
        # Stack diimplementasikan menggunakan list Python
        self.items = []

    def is_empty(self):
        """Memeriksa apakah stack kosong."""
        return not self.items

    def push(self, item):
        """Menambahkan elemen ke puncak stack (operasi PUSH)."""
        self.items.append(item)

    def pop(self):
        """Menghapus dan mengembalikan elemen dari puncak stack (operasi POP)."""
        if not self.is_empty():
            return self.items.pop()
        else:
            # Mengembalikan None jika Stack Underflow
            return None 

    def peek(self):
        """Melihat elemen teratas tanpa menghapusnya."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def get_items(self):
        """Mengembalikan semua elemen stack."""
        return self.items

# --- 2. Logika Fungsi Interaksi GUI ---
my_stack = Stack()

def perbarui_tampilan():
    """Memperbarui visualisasi stack di GUI."""
    # Ambil elemen stack dan balikkan urutannya agar elemen Top ada di atas
    elemen_stack = my_stack.get_items()
    
    # Memperbarui status Top
    top_element = my_stack.peek()
    if top_element is not None:
        status_top.config(text=f"TOP: {top_element}", fg="red")
    else:
        status_top.config(text="TOP: Stack Kosong", fg="gray")

    # Memperbarui listbox (Visualisasi Stack)
    listbox_stack.delete(0, tk.END) # Hapus isi lama
    
    # Masukkan elemen dari bawah ke atas agar terlihat seperti tumpukan
    # Kita balikkan urutan list agar elemen terbaru (Top) berada di atas Listbox
    for item in reversed(elemen_stack):
        listbox_stack.insert(tk.END, item)
    
def aksi_push():
    """Menangani operasi PUSH dari input GUI."""
    nilai = entry_input.get()
    if nilai:
        my_stack.push(nilai)
        perbarui_tampilan()
        entry_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Input tidak boleh kosong.")

def aksi_pop():
    """Menangani operasi POP dari GUI."""
    elemen_dikeluarkan = my_stack.pop()
    if elemen_dikeluarkan is not None:
        messagebox.showinfo("POP Berhasil", f"Elemen yang dikeluarkan: {elemen_dikeluarkan}")
        perbarui_tampilan()
    else:
        messagebox.showerror("Error", "Stack Underflow! Stack sudah kosong, tidak bisa di-Pop.")

# --- 3. Konfigurasi Jendela Utama Tkinter ---
jendela_utama = tk.Tk()
jendela_utama.title("Simulasi Algoritma Stack (LIFO)")
jendela_utama.geometry("400x450")

# --- 4. Membuat Widget Input & Tombol ---

frame_input = tk.Frame(jendela_utama, padx=10, pady=10)
frame_input.pack(fill='x')

label_input = tk.Label(frame_input, text="Nilai Baru:", font=('Arial', 10))
label_input.pack(side=tk.LEFT, padx=5)

entry_input = tk.Entry(frame_input, width=15, font=('Arial', 10))
entry_input.pack(side=tk.LEFT, padx=5)

tombol_push = tk.Button(
    frame_input,
    text="PUSH",
    command=aksi_push,
    bg='lightgreen',
    font=('Arial', 10, 'bold')
)
tombol_push.pack(side=tk.LEFT, padx=10)

tombol_pop = tk.Button(
    jendela_utama,
    text="POP (Keluarkan Teratas)",
    command=aksi_pop,
    bg='salmon',
    font=('Arial', 10, 'bold')
)
tombol_pop.pack(pady=10)

# --- 5. Visualisasi Stack ---

# Status Elemen Teratas (TOP)
status_top = tk.Label(jendela_utama, text="TOP: Stack Kosong", font=('Arial', 12, 'bold'), fg="gray")
status_top.pack(pady=(10, 5))

label_stack = tk.Label(jendela_utama, text="Visualisasi Stack (LIFO)", font=('Arial', 12, 'underline'))
label_stack.pack()

# Listbox untuk menampilkan elemen Stack secara berurutan
listbox_stack = tk.Listbox(
    jendela_utama,
    height=15,
    width=30,
    font=('Courier', 12),
    relief=tk.SUNKEN,
    bg='#f0f0f0'
)
listbox_stack.pack(padx=10, pady=5)

# Inisialisasi tampilan awal
perbarui_tampilan()

# --- 6. Memulai Loop Utama Aplikasi ---
jendela_utama.mainloop()