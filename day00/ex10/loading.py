import time
import sys

def ft_progress(lst):
    start = time.time()
    for i in lst:
        yield i

        percent = (i + 1) / len(lst)
        progress = "=" * int(percent * 19)
        ela = time.time() - start
        eta = 0 if i == 0 else ela * (len(lst) - i) / i

        print(
            "ETA: {:6.2f}s [{:3d}%] [{:<20s}] {:d}/{:d} elapsed time {:6.2f}s"
            .format(
                eta,
                int(percent * 100),
                progress+">",
                i + 1,
                len(lst),
                ela
            ),
            end="\r",
        )


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)

print()

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)