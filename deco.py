from faker import Faker

file_path = "st.txt"
list = []

faker = Faker()
for _ in range(1000):
    str = f"<img src='{faker.image_url()}' /> <br/>"
    list.append(str)
for i in list:
    print(i)
try:
    with open(file_path, 'w') as file:
        for item in list:
            file.write(f"{item}\n")
    print(f"List has been successfully written to '{file_path}'")
except Exception as e:
    print(f"An error occurred: {str(e)}")
