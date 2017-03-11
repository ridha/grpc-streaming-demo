import time
import grpc

import primefactor_pb2
import primefactor_pb2_grpc


def gen():
    while 1:
        i = input("\nEnter a number or 'q' to quit: \n")
        if i == "q":
            break
        try:
            num = int(i)
        except ValueError:
            continue
        yield primefactor_pb2.Request(num=num)
        time.sleep(0.1)


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = primefactor_pb2_grpc.FactorsStub(channel)
    it = stub.PrimeFactors(gen())
    try:
        for r in it:
            print(f"Prime factor = {r.result}")
    except grpc._channel._Rendezvous as err:
        print(err)


if __name__ == '__main__':
    run()
