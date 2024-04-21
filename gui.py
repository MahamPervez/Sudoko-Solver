import tkinter as tk

def create_grid(event=None):
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                label = tk.Label(frame, text=str(grid[i][j]), font=('Arial', 16), width=4, height=2, relief='ridge', bd=2)
                label.grid(row=i, column=j)
            else:
                entry = tk.Entry(frame, font=('Arial', 16), width=4, justify='center')
                entry.grid(row=i, column=j)
                entries[(i, j)] = entry

def Solve():
    for (i, j), entry in entries.items():
        value = entry.get()
        if value.isdigit():
            grid[i][j] = int(value)
        else:
            grid[i][j] = 0

    if Solve(grid, 0, 0):
        create_grid()
    else:
        status_label.config(text="No Solution Found")

# Your Sudoku solver functions (IsValidMove, Solve) go here

grid = [
    [0, 0, 0, 0, 0, 0, 6, 8, 9],
    [0, 0, 0, 0, 7, 3, 0, 0, 9],
    [3, 0, 9, 0, 0, 0, 0, 4, 5],
    [4, 9, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 3, 0, 5, 0, 9, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [9, 6, 0, 0, 0, 0, 3, 0, 8],
    [7, 0, 0, 6, 8, 0, 0, 0, 0],
    [0, 2, 8, 0, 0, 0, 0, 0, 0]
]
import tkinter as tk

def IsValidMove(grid, row, col, number):
    for i in range(9):  # checking in the row
        if grid[row][i] == number:
            return False
    for i in range(9):  # checking in the col
        if grid[i][col] == number:
            return False
    corner_row = row - row % 3  # finding a corner
    corner_col = col - col % 3
    for x in range(3):  # checking in the grid
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
    return True

def Solve(grid, row, col):
    if col == 9:  # overflowing, we have reached the final point, it's solved
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return Solve(grid, row, col + 1)

    for num in range(1, 10):
        if IsValidMove(grid, row, col, num):
            grid[row][col] = num
            if Solve(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

def create_grid(event=None):
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                label = tk.Label(frame, text=str(grid[i][j]), font=('Arial', 16), width=4, height=2, relief='ridge', bd=2)
                label.grid(row=i, column=j)
            else:
                entry = tk.Entry(frame, font=('Arial', 16), width=4, justify='center')
                entry.grid(row=i, column=j)
                entries[(i, j)] = entry

def solve():
    for (i, j), entry in entries.items():
        value = entry.get()
        if value.isdigit():
            grid[i][j] = int(value)
        else:
            grid[i][j] = 0

    if Solve(grid, 0, 0):
        create_grid()
    else:
        status_label.config(text="No Solution Found")

grid = [
    [0, 0, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 0, 0, 7, 3, 0, 0, 9],
    [3, 0, 9, 0, 0, 0, 0, 4, 5],
    [4, 9, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 3, 0, 5, 0, 9, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [9, 6, 0, 0, 0, 0, 3, 0, 8],
    [7, 0, 0, 6, 8, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0]
]

entries = {}

root = tk.Tk()
root.title("Sudoku Solver")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack()

create_grid()

root.mainloop()
