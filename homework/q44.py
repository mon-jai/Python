from typing import List


def main():
    special_prize_winning_number = input()
    grand_prize_winning_number = input()
    first_prize_winning_numbers = input().split(' ')
    sixth_prize_winning_numbers = input().split(' ')
    no_of_invoice = int(input())

    prize_moneys: List[int] = []

    def matches_last_nth_digits_with_first_prize_winning_numbers(invoice_id: str, nth_of_digits: int):
        return any(
            invoice_id[-nth_of_digits:] == winning_number[-nth_of_digits:]
            for winning_number in first_prize_winning_numbers
        )

    for _ in range(no_of_invoice):
        invoice_id = input()
        # 特別獎
        if invoice_id == special_prize_winning_number:
            prize_moneys.append(10000000)
        # 特獎
        elif invoice_id == grand_prize_winning_number:
            prize_moneys.append(2000000)
        # 頭獎
        elif invoice_id in first_prize_winning_numbers:
            prize_moneys.append(200000)
        # 二獎
        elif matches_last_nth_digits_with_first_prize_winning_numbers(invoice_id, 7):
            prize_moneys.append(40000)
        # 三獎
        elif matches_last_nth_digits_with_first_prize_winning_numbers(invoice_id, 6):
            prize_moneys.append(10000)
        # 四獎
        elif matches_last_nth_digits_with_first_prize_winning_numbers(invoice_id, 5):
            prize_moneys.append(4000)
        # 五獎
        elif matches_last_nth_digits_with_first_prize_winning_numbers(invoice_id, 4):
            prize_moneys.append(1000)
        # 六獎
        elif matches_last_nth_digits_with_first_prize_winning_numbers(invoice_id, 3):
            prize_moneys.append(200)
        # 增開六獎
        elif any(invoice_id[-3:] == suffix for suffix in sixth_prize_winning_numbers):
            prize_moneys.append(200)

    print(sum(prize_moneys))


main()
