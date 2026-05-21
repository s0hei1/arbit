import random
import trio


async def method_a():
    i = 0
    while True:
        print(f"A: step {i}")
        i += 1
        await trio.sleep(0.4)


async def method_b():
    i = 0
    while True:
        print(f"B: step {i}")
        i += 1
        await trio.sleep(0.6)


async def method_c():
    i = 0
    while True:
        print(f"C: step {i}")
        i += 1
        await trio.sleep(0.8)


async def pauser(cancel_scopes):
    # Every few seconds, randomly pause one method for 5 seconds
    while True:
        await trio.sleep(2)

        name = random.choice(list(cancel_scopes.keys()))
        print(f"\n--- Pausing {name} for 5 seconds ---")

        # Cancel the current run of that method, then restart it after 5s
        cancel_scopes[name].cancel()

        await trio.sleep(5)

        print(f"--- Resuming {name} ---\n")


async def run_worker(name, worker_fn, cancel_scopes):
    # Loop forever: worker runs until cancelled; then we restart it
    while True:
        with trio.CancelScope() as scope:
            cancel_scopes[name] = scope
            await worker_fn()


async def main():
    cancel_scopes = {}

    async with trio.open_nursery() as nursery:
        nursery.start_soon(run_worker, "A", method_a, cancel_scopes)
        nursery.start_soon(run_worker, "B", method_b, cancel_scopes)
        nursery.start_soon(run_worker, "C", method_c, cancel_scopes)

        nursery.start_soon(pauser, cancel_scopes)

        # Let the demo run for a while then exit
        await trio.sleep(25)
        nursery.cancel_scope.cancel()


trio.run(main)