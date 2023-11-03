import random

def monobit_test(bit_sequence):
    ones_count = bit_sequence.count('1')
    zeros_count = bit_sequence.count('0')
    
    if 9654 <= ones_count <= 10346:
        return True
    else:
        return False

def max_run_length_test(bit_sequence):
    max_zero_run = 0
    max_one_run = 0
    zero_run = 0
    one_run = 0

    for bit in bit_sequence:
        if bit == '0':
            zero_run += 1
            one_run = 0
            max_zero_run = max(max_zero_run, zero_run)
        else:
            one_run += 1
            zero_run = 0
            max_one_run = max(max_one_run, one_run)

    if max_zero_run <= 36 and max_one_run <= 36:
        return True
    else:
        return False

def poker_test(bit_sequence):
    m = 4  # Довжина блоку Поккера
    k = len(bit_sequence) // m  # Кількість блоків Поккера
    block_counts = {}  # Словник для підрахунку кількості зустрічання кожного блоку

    for i in range(0, len(bit_sequence), m):
        block = bit_sequence[i:i + m]
        if block in block_counts:
            block_counts[block] += 1
        else:
            block_counts[block] = 1

    X3 = (16 / 5000) * sum([(ni ** 2) for ni in block_counts.values()]) - 5000

    if 1.03 <= X3 <= 57.4:
        return True
    else:
        return False
    

def run_length_test(bit_sequence):
    ones_runs = []
    zeros_runs = []

    current_run = 0
    current_bit = bit_sequence[0]

    for bit in bit_sequence:
        if bit == current_bit:
            current_run += 1
        else:
            if current_bit == '1':
                ones_runs.append(current_run)
            else:
                zeros_runs.append(current_run)
            current_bit = bit
            current_run = 1

    if current_bit == '1':
        ones_runs.append(current_run)
    else:
        zeros_runs.append(current_run)

    one_series_counter = {}
    for series in ones_runs:
        if series >= 6:
            temp_counter = 6
        else:
            temp_counter = series
        if temp_counter in one_series_counter:
            one_series_counter[temp_counter] += 1
        else:
            one_series_counter[temp_counter] = 1

    zero_series_counter = {}
    for series in zeros_runs:
        if series >= 6:
            temp_counter = 6
        else:
            temp_counter = series
        if temp_counter in zero_series_counter:
            zero_series_counter[temp_counter] += 1
        else:
            zero_series_counter[temp_counter] = 1

    intervals = [(2267, 2733), (1079, 1421), (502, 748), (223, 402), (90, 223), (90, 223)]

    one_passed = False
    zero_passed = False

    for iteration in one_series_counter: 
        one_passed = True if intervals[iteration-1][0] < one_series_counter[iteration] < intervals[iteration-1][1] else False
        print(iteration, "----", one_passed, ":", intervals[iteration-1][0], "<", one_series_counter[iteration], "<", intervals[iteration-1][1])

    for iteration in zero_series_counter: 
        zero_passed = True if intervals[iteration-1][0] < zero_series_counter[iteration] < intervals[iteration-1][1] else False
        print(iteration, "----", zero_passed, ":", intervals[iteration-1][0], "<", zero_series_counter[iteration], "<", intervals[iteration-1][1])

    return one_passed and zero_passed

def generate_random_bit_sequence(length):
    bit_sequence = "".join([random.choice("01") for _ in range(length)])
    return bit_sequence

if __name__ == "__main__":
    
    random_sequence = generate_random_bit_sequence(20000)
    result_monobit = monobit_test(random_sequence)
    print("Monobit test result:", result_monobit)
    result_max_run_length = max_run_length_test(random_sequence)
    print("Max run length test result:", result_max_run_length)
    result_poker = poker_test(random_sequence)
    print("Poker test result:", result_poker)
    result_run_length = run_length_test(random_sequence)
    print("Run length test result:", result_run_length)
    if result_monobit and result_max_run_length and result_poker and result_run_length:
        print("20 000 бітів є достатньо випадковими")
    else:
        print("Послідовність бітів відхиляється")