
class LectureOne:
    @staticmethod
    def print_name_n_times(name, n):
        if n <= 0:
            return
        print(f'{n} = {name}')
        LectureOne.print_name_n_times(name=name, n=n-1)

    @staticmethod
    def print_1_to_n(i, n):
        if i > n:
            return
        print(i)
        LectureOne.print_1_to_n(i=i+1, n=n)

    @staticmethod
    def print_n_to_1(n):
        if n <= 0:
            return
        print(n)
        LectureOne.print_n_to_1(n-1)

    @staticmethod
    def print_1_to_n_bt(i):
        if i <= 1:
            return
        LectureOne.print_1_to_n_bt(i-1)
        print(i)

    @staticmethod
    def print_n_to_1_bt(n):
        if n < 1:
            return
        print(n)
        LectureOne.print_n_to_1_bt(n-1)


class LectureTwo:

    @staticmethod
    def sum_of_first_n_num(n):
        # base cond.
        if n == 0:
            return 0

        x = n + LectureTwo.sum_of_first_n_num(n-1)
        return x

    @staticmethod
    def reverse_array(i, arr, n):
        # base cond.
        if i >= n/2:
            return

        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]  # swap i & n-i-1
        LectureTwo.reverse_array(i+1, arr, n)

    @staticmethod
    def string_palindrom(i, str, n):
        # base cond.
        if i >= n/2:
            return True

        if str[i] != str[n-i-1]:
            return False

        return LectureTwo.string_palindrom(i+1, str, n)


def main():
    # LectureOne.print_name_n_times('Akash', 5)
    # LectureOne.print_1_to_n(1, 10)
    # LectureOne.print_n_to_1(10)
    # LectureOne.print_1_to_n_bt(3)
    # LectureOne.print_n_to_1_bt(3)

    print(LectureTwo.sum_of_first_n_num(5))

    arr = [1, 2, 3, 4]
    LectureTwo.reverse_array(i=0, arr=arr, n=4)
    print(arr)

    print(LectureTwo.string_palindrom(i=0, str='madam', n=5))


if __name__ == "__main__":
    main()
