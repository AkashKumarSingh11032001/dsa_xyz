
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


def main():
    LectureOne.print_name_n_times('Akash', 5)
    LectureOne.print_1_to_n(1, 10)
    LectureOne.print_n_to_1(10)
    LectureOne.print_1_to_n_bt(3)
    LectureOne.print_n_to_1_bt(3)


if __name__ == "__main__":
    main()
