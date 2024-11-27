import openpyxl

# Specify the file to read and write
file_path = "data_file.xlsx"  # Replace with your file name

# Load the workbook and get the active sheet
wb = openpyxl.load_workbook(file_path)
sheet = wb.active

# Iterate through each cell and modify the data
for row in sheet.iter_rows():
    for cell in row:
        if cell.value is not None:  # If the cell is not empty
            cell.value = str(cell.value) + "A"
        else:  # If the cell is empty
            cell.value = "A"

# Save the changes to the same file
wb.save(file_path)
print(f"Modified data written back to {file_path}")