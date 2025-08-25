# Check GPU availability
import torch
if torch.cuda.is_available:
    print("Device: CUDA", )
else:
    print("Device: CPU")


# Read the file
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Length of dataset in characters: {len(text)}")

# Look at the first 100 characters
print(text[:100])

# Print all the unique characters that occur in the text
chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(f"Vocabulary size: {vocab_size}")

for i,c in enumerate(chars[:20]):
    print(i, c)

# create a mapping from characters to integers
stoi = {ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)}

encode = lambda s: [stoi[c] for c in s] # encoder: takes a string, outputs a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: takes a list of integers, outputs a string

print(encode("hi there"))
print(decode(encode("hi there")))

# Encode the entire test set and store in a torch.tensor

import torch
data = torch.tensor(encode(text), dtype=torch.long)
print(data.shape, data.dtype)
print(data[:10]) # print the first 1000 encoded data

# train-val split
n = int(0.9*len(data))

train_data = data[:n]
val_data = data[n:]

print(f"Train size: {len(train_data)}")
print(f"Val size: {len(val_data)}")

block_size = 8 # max length of context the model sees at a time
train_data[:block_size+1]

# Visualize how the context-target modeling works
x = train_data[:block_size] # contexts
y = train_data[1:block_size+1] # target
for t in range(block_size):
    context = x[:t+1]
    target = y[t]
    print(f"When input is {context} the target: {target}")

torch.manual_seed(1337)
batch_size = 4 # how many independent sequences will we process in parallel?
block_size = 8 # what is the maximum context length for predictions?

def get_batch(split):
    # generate a small batch of data of inputs x and targets y
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x, y

xb, yb = get_batch('train')
print('inputs:')
print(xb.shape)
print(xb)
print('targets:')
print(yb.shape)
print(yb)

print('----')

for b in range(batch_size): # batch dimension
    for t in range(block_size): # time dimension
        context = xb[b, :t+1]
        target = yb[b,t]
        print(f"when input is {context.tolist()} the target: {target}")