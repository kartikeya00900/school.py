import struct


student_format = 'I 20s 50s'  
record_size = struct.calcsize(student_format)

def write_student_data(filename, student_data):
    try:
        with open(filename, 'ab') as file:
            rollno, name, address = student_data
            packed_data = struct.pack(student_format, rollno, name.encode('utf-8'), address.encode('utf-8'))
            file.write(packed_data)
    except Exception as e:
        print(f"Error while writing data: {e}")

def read_student_data(filename):
    try:
        with open(filename, 'rb') as file:
            while True:
                packed_data = file.read(record_size)
                if not packed_data:
                    break
                rollno, name, address = struct.unpack(student_format, packed_data)
                name = name.decode('utf-8').strip()
                address = address.decode('utf-8').strip()
                yield (rollno, name, address)
    except Exception as e:
        print(f"Error while reading data: {e}")

def print_student_data(filename):
    for rollno, name, address in read_student_data(filename):
        print(f"Roll No: {rollno}")
        print(f"Name: {name}")
        print(f"Address: {address}")
        print()


if __name__ == "__main__":
    filename = "student.dat"

    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            rollno = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            student_data = (rollno, name, address)
            write_student_data(filename, student_data)
        elif choice == 2:
            print("\nStudent Records:")
            print_student_data(filename)
        elif choice == 3:
            break
