# Daftar untuk menyimpan tugas
tasks = []

def display_tasks():
    """Menampilkan semua tugas."""
    if not tasks:
        print("\nTidak ada tugas.\n")
    else:
        print("\nDaftar Tugas:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print()

def add_task():
    """Menambahkan tugas baru."""
    task = input("Masukkan tugas baru: ").strip()
    if task:
        tasks.append(task)
        print(f"Tugas '{task}' berhasil ditambahkan.\n")
    else:
        print("Tugas tidak boleh kosong.\n")

def remove_task():
    """Menghapus tugas berdasarkan nomor."""
    display_tasks()
    if tasks:
        try:
            task_num = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Tugas '{removed_task}' berhasil dihapus.\n")
            else:
                print("Nomor tugas tidak valid.\n")
        except ValueError:
            print("Masukkan angka yang valid.\n")

def main():
    """Fungsi utama aplikasi."""
    while True:
        print("=== Aplikasi To-Do List Sederhana ===")
        print("1. Tampilkan Semua Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        choice = input("Pilih opsi (1-4): ").strip()

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Terima kasih telah menggunakan aplikasi To-Do List. Sampai jumpa!")
            break
        else:
            print("Opsi tidak valid. Silakan pilih antara 1-4.\n")

if _name_ == "_main_":
 main()