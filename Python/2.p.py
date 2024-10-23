class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        return f"{status} {self.title}: {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Index tidak valid.")

    def show_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx}. {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Index tidak valid.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Tandai Tugas Selesai")
        print("3. Tampilkan Tugas")
        print("4. Hapus Tugas")
        print("5. Keluar")
        choice = input("Pilih opsi: ")

        if choice == "1":
            title = input("Masukkan judul tugas: ")
            description = input("Masukkan deskripsi tugas: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            todo_list.show_tasks()
            index = int(input("Masukkan index tugas yang selesai: "))
            todo_list.complete_task(index)
        elif choice == "3":
            todo_list.show_tasks()
        elif choice == "4":
            todo_list.show_tasks()
            index = int(input("Masukkan index tugas yang ingin dihapus: "))
            todo_list.remove_task(index)
        elif choice == "5":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Opsi tidak valid.")

if __name__ == "__main__":
    main()
