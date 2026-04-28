import asyncio

async def process_transaction(account_holder, amount):
    print(f"Starting transaction for {account_holder}")
    await asyncio.sleep(2)
    print(f"Transaction complete for {account_holder} - £{amount}")

async def main():
    await asyncio.gather(
        process_transaction("Kcee Michael", 500),
        process_transaction("James Carlwell", 300)
    )

asyncio.run(main())