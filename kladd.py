def walk(steps):
    if steps == 0:
        return
    walk(steps - 2)
    print(f"You take step #{steps}")

walk(100)