a = [
    [
        1 if item_idx == row_idx else 0
        for item_idx in range(0, 3)
        if item_idx < 2
    ]
    for row_idx in range(0, 3)
] 

print(a)
