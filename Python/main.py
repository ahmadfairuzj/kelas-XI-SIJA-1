def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Tambah Tugas")
        print("2. Tampilkan Tugas")
        print("3. Tandai Dengan Tugas Selesai")
        print("4. Keluar")

        choice = input("masukkan pilihan Anda: ")

        if choice == '1':
            print()
            n_tasks = int(input("Tugas Yang Ingin Di Tambahkan: "))
            
            for i in range(n_tasks):
                task = input("Masukan Tugas: ")
                tasks.append({"task": task, "done": False})
                print("Tugas Ditambahkan!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()