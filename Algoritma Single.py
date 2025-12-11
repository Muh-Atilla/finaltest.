import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# --- 1. Kelas Node dan SinglyLinkedList ---

class Node:
    """Struktur data dasar untuk Node."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Kelas untuk mengelola operasi Linked List."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Menambahkan Node di awal (mengubah Head)."""
        new_node = Node(data)
        new_node.next = self.head # Pointer Node baru menunjuk ke Head lama
        self.head = new_node       # Head dipindahkan ke Node baru

    def insert_at_end(self, data):
        """Menambahkan Node di akhir (Traverse ke Tail)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node # Tail lama menunjuk ke Node baru

    def get_list_display(self):
        """Melakukan Traversal dan mengembalikan representasi string."""
        current_node = self.head
        output_list = []
        if current_node is None:
            return "Daftar Kosong (Head -> None)"
            
        while current_node:
            output_list.append(str(current_node.data))
            current_node = current_node.next
            
        # Menggabungkan elemen dengan panah untuk visualisasi Linked List
        return "HEAD -> " + " -> ".join(output_list) + " -> NONE"

# --- 2. Inisialisasi dan Fungsi Interaksi GUI ---

my_list = SinglyLinkedList()

def perbarui_tampilan():
    """Memperbarui visualisasi Linked List di GUI."""
    list_str = my_list.get_list_display()
    
    # Hapus konten lama
    teks_tampilan.config(state=tk.NORMAL)
    teks_tampilan.delete('1.0', tk.END)
    
    # Masukkan konten baru
    teks_tampilan.insert(tk.END, list_str)
    teks_tampilan.config(state=tk.DISABLED)

def aksi_insert_awal():
    """Menangani operasi Insert di Awal."""
    data = entry_input.get()
    if data.strip():
        my_list.insert_at_beginning(data.strip())
        perbarui_tampilan()
        entry_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Input data tidak boleh kosong.")

def aksi_insert_akhir():
    """Menangani operasi Insert di Akhir."""
    data = entry_input.get()
    if data.strip():
        my_list.insert_at_end(data.strip())
        perbarui_tampilan()
        entry_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Input data tidak boleh kosong.")

# --- 3. Konfigurasi Jendela Utama Tkinter ---

jendela_utama = tk.Tk()
jendela_utama.title("Simulasi Singly Linked List")
jendela_utama.geometry("550x300")

# --- 4. Widget Input dan Kontrol ---

frame_control = tk.Frame(jendela_utama, padx=10, pady=10)
frame_control.pack(fill='x')

tk.Label(frame_control, text="Data Node:", font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=5)

entry_input = tk.Entry(frame_control, width=15, font=('Arial', 10))
entry_input.pack(side=tk.LEFT, padx=5)

# Tombol Insert Awal
tombol_awal = tk.Button(
    frame_control,
    text="Insert Awal (O(1))",
    command=aksi_insert_awal,
    bg='lightgreen',
    font=('Arial', 10, 'bold')
)
tombol_awal.pack(side=tk.LEFT, padx=10)

# Tombol Insert Akhir
tombol_akhir = tk.Button(
    frame_control,
    text="Insert Akhir (O(n))",
    command=aksi_insert_akhir,
    bg='lightblue',
    font=('Arial', 10, 'bold')
)
tombol_akhir.pack(side=tk.LEFT, padx=10)

# --- 5. Visualisasi Linked List ---

tk.Label(jendela_utama, text="Representasi Singly Linked List (HEAD ke NONE)", font=('Arial', 12, 'underline')).pack(pady=(10, 5))

teks_tampilan = scrolledtext.ScrolledText(
    jendela_utama,
    height=5,
    width=60,
    font=('Courier', 12),
    relief=tk.SUNKEN,
    state=tk.DISABLED,
    wrap=tk.WORD # Pastikan teks bisa pindah baris
)
teks_tampilan.pack(padx=10, pady=5)

# Inisialisasi tampilan awal
perbarui_tampilan()

# --- 6. Memulai Loop Utama Aplikasi ---
jendela_utama.mainloop()