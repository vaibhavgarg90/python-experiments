# blockchain

The code has been shamelessly copied from: https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

**Block:** A simple block looks like this:
`block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}`

**Proof of Work (POW):** A Proof of Work algorithm (PoW) is how new Blocks are created or mined on the blockchain.
The goal of PoW is to discover a number which solves a problem.
The number must be difficult to find but easy to verify—computationally speaking—by anyone on the network.
This is the core idea behind Proof of Work.
`
from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1
print(f'The solution is y = {y}')
`