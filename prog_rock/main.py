from . import spinners


if __name__ == '__main__':
    import time
    with spinners.snake() as s:
        for i in range(10):
            s.tick()
            time.sleep(1)
