class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        """Menambah tugas ke dalam list."""
        self.tasks.append({"task": task, "done": False})
        print(f"Tugas '{task}' berhasil ditambahkan.")

    def remove_task(self, task_index):
        """Menghapus tugas berdasarkan indeks."""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Tugas '{removed_task['task']}' berhasil dihapus.")
        else:
            print("Indeks tugas tidak valid!")

    def mark_done(self, task_index):
        """Menandai tugas sebagai selesai."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            print(f"Tugas '{self.tasks[task_index]['task']}' telah selesai.")
        else:
            print("Indeks tugas tidak valid!")

    def show_tasks(self):
        """Menampilkan daftar tugas."""
        if not self.tasks:
            print("Tidak ada tugas dalam daftar.")
        else:
            print("\nDaftar Tugas:")
            for i, task in enumerate(self.tasks):
                status = "✓" if task["done"] else "✗"
                print(f"{i + 1}. {task['task']} [{status}]")
        print()

# Menu interaktif
def menu():
    todo_list = ToDoList()
    while True:
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tandai Selesai")
        print("4. Tampilkan Tugas")
        print("5. Keluar")
        pilihan = input("Pilih opsi: ")

        

        if pilihan == "1":
            task = input("Masukkan tugas: ")
            todo_list.add_task(task)
        elif pilihan == "2":
            todo_list.show_tasks()
            index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            todo_list.remove_task(index)
        elif pilihan == "3":
            todo_list.show_tasks()
            index = int(input("Masukkan nomor tugas yang sudah selesai: ")) - 1
            todo_list.mark_done(index)
        elif pilihan == "4":
            todo_list.show_tasks()
        elif pilihan == "5":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

