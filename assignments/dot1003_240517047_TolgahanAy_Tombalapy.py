import random
from datetime import datetime

ROWS = 3
COLS = 5
MIN_NUM = 1
MAX_NUM = 90


def make_card():
    # Select 15 unique numbers between 1-90, sort them, place into 3x5
    nums = random.sample(range(MIN_NUM, MAX_NUM + 1), ROWS * COLS)
    nums.sort()
    card = []
    idx = 0
    r = 0
    while r < ROWS:
        row = []
        c = 0
        while c < COLS:
            row.append(nums[idx])
            idx += 1
            c += 1
        card.append(row)
        r += 1
    return card


def make_marks():
    marks = []
    r = 0
    while r < ROWS:
        row = []
        c = 0
        while c < COLS:
            row.append(False)
            c += 1
        marks.append(row)
        r += 1
    return marks


def print_card(card, marks=None, title=None):
    if title is not None:
        print(title)
    print("+-----------------------+")
    r = 0
    while r < ROWS:
        line = "| "
        c = 0
        while c < COLS:
            val = card[r][c]
            if marks is not None and marks[r][c]:
                cell = " X "
            else:
                cell = f"{val:2d} "
            line += cell
            c += 1
        line += "|"
        print(line)
        r += 1
    print("+-----------------------+")


def has_number(card, number):
    r = 0
    while r < ROWS:
        c = 0
        while c < COLS:
            if card[r][c] == number:
                return True
            c += 1
        r += 1
    return False


def mark_number(card, marks, number):
    # Mark the number if it exists on the card
    r = 0
    while r < ROWS:
        c = 0
        while c < COLS:
            if card[r][c] == number:
                marks[r][c] = True
            c += 1
        r += 1


def count_completed_rows(marks):
    completed = 0
    r = 0
    while r < ROWS:
        row_complete = True
        c = 0
        while c < COLS:
            if not marks[r][c]:
                row_complete = False
            c += 1
        if row_complete:
            completed += 1
        r += 1
    return completed


def all_marked(marks):
    r = 0
    while r < ROWS:
        c = 0
        while c < COLS:
            if not marks[r][c]:
                return False
            c += 1
        r += 1
    return True


def flatten_card(card):
    # Convert card to a single list for logging
    out = []
    r = 0
    while r < ROWS:
        c = 0
        while c < COLS:
            out.append(card[r][c])
            c += 1
        r += 1
    return out


def main():
    print("=== TOMBALA ===")
    user_name = input("Please enter your name: ").strip()
    if user_name == "":
        user_name = "Unknown"

    print("\nPreparing 4 cards...\n")
    cards = [make_card(), make_card(), make_card(), make_card()]

    i = 0
    while i < 4:
        print_card(cards[i], None, title=f"CARD {i+1}")
        print()
        i += 1

    choice = 0
    while choice < 1 or choice > 4:
        raw = input("Which card do you choose? (1-4): ").strip()
        if raw.isdigit():
            choice = int(raw)

    card = cards[choice - 1]
    marks = make_marks()

    print("\nYour selected card:")
    print_card(card, marks)

    draw_pool = list(range(MIN_NUM, MAX_NUM + 1))
    random.shuffle(draw_pool)

    drawn_numbers = []
    inconsistencies = 0
    shown_chinko = 0

    game_over = False
    result = "LOSE"

    idx = 0
    while idx < len(draw_pool) and not game_over:
        number = draw_pool[idx]
        idx += 1

        drawn_numbers.append(number)
        print(f"\nDrawn number: {number}")

        answer = ""
        while answer not in ["e", "h"]:
            answer = input("Do you have this number? (e/h): ").strip().lower()

        actual = has_number(card, number)

        # Check user's answer (lying or distracted)
        if answer == "e" and not actual:
            inconsistencies += 1
            print("Warning: This number is not on your card. (Incorrect answer detected.)")
        if answer == "h" and actual:
            inconsistencies += 1
            print("Warning: This number is on your card. (You may have missed it.)")

        # Mark according to the correct result
        if actual:
            mark_number(card, marks, number)
            print("Number found on your card -> marked.")

        # Check for Chinko
        completed = count_completed_rows(marks)
        if completed > shown_chinko and completed < ROWS:
            shown_chinko = completed
            print(f"*** CHINKO {shown_chinko}! (Completed rows: {shown_chinko}) ***")

        print_card(card, marks, title="Current card:")

        if all_marked(marks):
            game_over = True
            result = "WIN"

    # End of game
    print("\n=== GAME OVER ===")
    if result == "WIN":
        print("TOMBALA! Congratulations, you win! 🎉")
    else:
        print("Unfortunately, you could not make Tombala. You lose. 😢")

    if inconsistencies > 0:
        print(f"Note: {inconsistencies} incorrect or inconsistent answers were detected.")
    else:
        print("Note: All your answers were consistent.")

    # Write log
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = (
        f"[{now}] name={user_name} card={flatten_card(card)} "
        f"drawn={drawn_numbers} result={result} inconsistencies={inconsistencies}\n"
    )
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log_line)

    print("\nGame information has been saved to log.txt.")


if __name__ == "__main__":
    main()
