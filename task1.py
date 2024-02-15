import glob


def main():

    for file in glob.iglob('TEST_Folder_*/TEST_*'):
        target_name = file.split('/')[-1]
        result_numbers = []

        with open(file, 'r') as fp:
            numbers_line: str = fp.read()
            numbers_line = numbers_line.replace('"', '')

            numbers = numbers_line.split(',')

            for number in numbers:
                if '-' in number:
                    start, end = map(int, number.split('-'))
                    result_numbers.extend(range(start, end+1))
                else:
                    result_numbers.append(int(number))

        with open(f'Result/TEST_AUCHAN_success{target_name}', 'w') as fp:
            fp.writelines(map(lambda s: f"{s}\n", result_numbers))


if __name__ == "__main__":
    main()