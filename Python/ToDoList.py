class Task:
    def __init__(self, title, due_date, category):
        self.title = title
        self.due_date = due_date
        self.cetagory = category
        self.is_complete = False

    def mark_as_completed(self):
        self.is_complete = True

    def __str__(self):
        status = "selesai" if self.is_complete else "belum selesai"
        return f"judul: {self.title}, batas waktu{self.due_date}, ketagori{self.category}, status{status}"

class ToDoList:
    def __init__(self):
        self.task = []

    def add_task(self,task):
        self.task.append(task)
        print(f'tugas"{task.title}"berhasil dihapus.')

    def remove_task(self, title):
        for task in self.task:
            if task.title == title:
                self.task.remove(task)
                print(f'Tugas"{title}"berhasil dihapus')
                return
            print(f'tugas dengan judul"{title}"berhasil ditemukan')

    def mark_task_as_completed(self, title):
        for task in self.task:
            if task.title == title:
                task.mark_as_completed()
            print(f'Tugas"{title}"ditandai sebagai selesai')
            return
        print(f'tugas dengan judul"{title}"tidak ditemukan')

    def display_task(self, filter_category = None):
        if not self.task:
            print("Tidak ada tugas yang tersedia")
        else:
            for task in self.task:
                if filter_category is None or task.category == filter_category:
                    print(task)

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)

todo_list = ToDoList()
  
while True:
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tampilkan Tugas berdasarkan ketagori")
    print("4. Tandai tugas sebagai selesai")
    print("5. Hapus Tugas")
    print("6. Keluar")

    choice = input("Pilih opsi (1/2/3/4/5/6): ")

    if choice == "1":
            title = input("Masukkan judul tugas: ")
            description = input("Masukkan deskripsi tugas: ")
    elif choice == "2":
            todo_list.show_tasks()
    elif choice == "3":
        category = input("Masukan Ketagori yang ingin ditampilkan: ")
        print(f"\nDaftar Tugas ketagori {category}: ")
    elif choice == "4":
        title = input("Masukan judul tugas yang ingin di tambahkan sebagai selesai: ")
        todo_list.mark_task_as_completed(title)
    elif choice == "5":
        title = input("Masukan judul tugas yang ingin di hapus: ")
        todo_list.remove_task(title)
    elif choice == "6":
        print("Keluar dari program. ")
        break
    else:
        print("Opsi tidak valid, silahkan coba lagi. ")