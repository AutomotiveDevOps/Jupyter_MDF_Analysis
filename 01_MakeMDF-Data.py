import make_data


def local_data_gen():
    for idx in range(1):
        try:
            f = make_data.random_data()
            print(f"{idx:04d}: {f}")

            except KeyboardInterrupt:
            print("\n\nDone\n\n")
            break


def distributed_data_gen():
    import configparser
    import redis
    import rq

    """ Distribute file generation to a number of redis backends.

    """
    config = configparser.ConfigParser()
    config.read("config.ini")
    r = redis.StrictRedis(
        host=config["redis"]["host"],
        port=config["redis"]["port"],
        db=config["redis"]["rq"],
    )
    q = rq.Queue(connection=r)
    for idx in range(1000):
        try:
            f = q.enqueue(make_data.random_data)
            print(f"{idx:04d}: {f}")
        except KeyboardInterrupt:
            print("\n\nCanceled\n\n")
            break
        except:
            raise

if __name__ == "__main__":
    distributed_data_gen()
