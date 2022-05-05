import unittest
import time

from pbar import pbar, pbrange

class TestBasicStuff(unittest.TestCase):
    def test_basic_usage(self):
        n = 10000
        s = 1e-4

        def time_wo_pbar():
            tic = time.time()
            for _ in range(n):
                time.sleep(s)
            toc = time.time()
            print(f"Without progress bar: {n / (toc - tic):.2f}it/s")

        # The true speed.
        print(f"Expected it/s: {1/s:.2f}")

        # Print speed without the progress bar.
        # This is the fastest speed we can expect due to loop overhead.
        time_wo_pbar()

        # Basic usage.
        for i in pbar(range(n)):
            time.sleep(s)

        # Another basic usage.
        for i in pbrange(n):
            time.sleep(s)

        # Define pb.
        pb = pbar(range(n))
        for i in pb:
            time.sleep(s)

        # Context and add extra args.
        xs = range(0, 5 * n, 5)
        with pbar(xs) as pb:
            for i in pb:
                pb.extra = {f"{i}^2": i ** 2}
                time.sleep(s)

        # Context and add extra args, using prange.
        print("pbrange in context:")
        with pbrange(0, 5 * n, 5) as pb:
            for i in pb:
                pb.extra = {f"{i}^2": i ** 2}
                time.sleep(s)

        # Works with lists.
        with pbar(list(xs)) as pb:
            for x in pb:
                pb.extra = {f"{x}^2": x ** 2}
                time.sleep(s)

        # Works with numpy arrays. Note the speed difference.
        # import numpy as np
        # ys = np.array(xs)[:, None]
        # with pbar(ys) as pb:
        #     for y in pb:
        #         pb.extra = {f"{y}^2": y ** 2}
        #         time.sleep(s)

        print("Other usages...")
        # Messages are consistent with the iteration number.
        pb = pbrange(3)
        for i in pb:
            time.sleep(1)
            pb.extra = {"i+1": i + 1}

        # Converting to list behaves as expected.
        N = int(1e6)
        x = [i + 1 for i in pbrange(N)]
        assert x[0] == 1 and x[-1] == N
        assert list(range(5)) == list(pbrange(5))

        # Print to file.
        for i in pbrange(n, fname=".test-log.txt"):
            pass
