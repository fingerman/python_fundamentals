from multiprocessing import Process, Array


def shared_square(nums, result):
    for i in range(len(nums)):
        result[i] = nums[i]*nums[i]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    result = Array('i', len(nums))

    p = Process(shared_square(nums, result))
    p.start()
    p.join()

    for r in result:
        print(r)

    print(result[:])
