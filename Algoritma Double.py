import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# --- 1. Kelas Node dan Doubly Linked List ---

class DoublyNode:
    """Struktur data untuk Node, memiliki pointer Prev dan Next."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer ke Node berikutnya
        self.prev = None  # Pointer ke Node sebelumnya

class DoublyLinkedList:
    """Kelas untuk mengelola operasi Doubly Linked List."""
    def __init__(self):
        self.head = None
        self.tail = None # Melacak Tail untuk insert O(1) di akhir

    def insert_at_end(self, data):
        """Menambahkan Node di akhir (lebih efisien dengan Tail)."""
        new_node = DoublyNode(data)
        
        if self.head is None:
            # Jika List kosong
            self.head = new_node
            self.tail = new_node
            return

        # 1. Hubungkan Node baru ke Tail lama
        self.tail.next = new_node
        
        # 2. Hubungkan Node baru kembali ke Tail lama (menggunakan Prev)
        new_node.prev = self.tail
        
        # 3. Tetapkan Node baru sebagai Tail
        self.tail = new_node

    def get_forward_display(self):
        """Traversal Maju (Head ke Tail)."""
        current_node = self.head
        output_list = []
        if current_node is None:
            return "Daftar Kosong (Head/Tail -> None)"
            
        while current_node:
            output_list.append(str(current_node.data))
            current_node = current_node.next
            
        return "HEAD -> " + " <-> ".join(output_list) + " -> NONE (Forward)"

    def get_backward_display(self):
        """Traversal Mundur (Tail ke Head)."""
        current_node = self.tail
        output_list = []
        if current_node is None:
            return "" # Jangan tampilkan jika sudah ditangani oleh forward display
            
        while current_node:
            output_list.append(str(current_node.data))
            current_node = current_node.prev
            
        return "NONE <- " + " <-> ".join(output_list) + " <- TAIL (Backward)"


# --- 2. Inisialisasi dan Fungsi Interaksi GUI ---

my_list = DoublyLinkedList()

def perbarui_tampilan():
    """Memperbarui visualisasi Doubly Linked List di GUI."""
    list_str_forward = my_list.get_forward_display()
    list_str_backward = my_list.get_backward_display()
    
    # Gabungkan tampilan Maju dan Mundur
    full_display = f"Traversal Maju:\n{list_str_forward}\n\nTraversal Mundur:\n{list_str_backward}"
    
    # Hapus konten lama
    teks_tampilan.config(state=tk.NORMAL)
    teks_tampilan.delete('1.0', tk.END)
    
    # Masukkan konten baru
    teks_tampilan.insert(tk.END, full_display)
    teks_tampilan.config(state=tk.DISABLED)

def aksi_insert_akhir():
    """Menangani operasi Insert di Akhir (paling umum dan efisien di DLL)."""
    data = entry_input.get()
    if data.strip():
        my_list.insert_at_end(data.strip())
        perbarui_tampilan()
        entry_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Input data tidak boleh kosong.")

# --- 3. Konfigurasi Jendela Utama Tkinter ---

jendela_utama = tk.Tk()
jendela_utama.title("Simulasi Doubly Linked List (DLL)")
jendela_utama.geometry("600x400")

# --- 4. Widget Input dan Kontrol ---

frame_control = tk.Frame(jendela_utama, padx=10, pady=10)
frame_control.pack(fill='x')

tk.Label(frame_control, text="Data Node:", font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=5)

entry_input = tk.Entry(frame_control, width=15, font=('Arial', 10))
entry_input.pack(side=tk.LEFT, padx=5)

# Tombol Insert Akhir
tombol_akhir = tk.Button(
    frame_control,
    text="Insert Akhir (Append)",
    command=aksi_insert_akhir,
    bg='lightblue',
    font=('Arial', 10, 'bold')
)
tombol_akhir.pack(side=tk.LEFT, padx=10)

# --- 5. Visualisasi Linked List ---

tk.Label(jendela_utama, text="Representasi Doubly Linked List", font=('Arial', 12, 'underline')).pack(pady=(10, 5))

teks_tampilan = scrolledtext.ScrolledText(
    jendela_utama,
    height=10,
    width=70,
    font=('Courier', 12),
    relief=tk.SUNKEN,
    state=tk.DISABLED,
    wrap=tk.WORD
)
teks_tampilan.pack(padx=10, pady=5)

# Inisialisasi tampilan awal
perbarui_tampilan()

# --- 6. Memulai Loop Utama Aplikasi ---
jendela_utama.mainloop()