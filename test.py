def extract_3x3_boxes(matrix):
    boxes = []
    # Anta at 'matrix' er en 2D-liste med dimensjoner som er multipler av 3
    for start_row in range(0, len(matrix), 3):
        for start_col in range(0, len(matrix[0]), 3):
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(matrix[start_row + i][start_col + j])
            boxes.append(box)
    return boxes
# Eksempelbruk
matrix = [
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [4, 4, 4, 5, 5, 5, 6, 6, 6],
    [4, 4, 4, 5, 5, 5, 6, 6, 6],
    [4, 4, 4, 5, 5, 5, 6, 6, 6],
    [7, 7, 7, 8, 8, 8, 9, 9, 9],
    [7, 7, 7, 8, 8, 8, 9, 9, 9],
    [7, 7, 7, 8, 8, 8, 9, 9, 9]
]
boxes = extract_3x3_boxes(matrix)
for box in boxes:
    print(box)