import heapq
from collections import defaultdict

# A Huffman Tree Node
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # To compare nodes in priority queue (heapq)
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman tree
def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0]

# Function to generate Huffman codes from the tree
def generate_codes(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    generate_codes(root.left, current_code + '0', codes)
    generate_codes(root.right, current_code + '1', codes)

# Function to encode the input text using the generated Huffman codes
def huffman_encode(text):
    # Calculate frequency of each character
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    # Build Huffman Tree
    root = build_huffman_tree(frequency)

    # Generate Huffman Codes
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    # Encode the text
    encoded_text = ''.join([huffman_codes[char] for char in text])

    return encoded_text, huffman_codes

# Function to decode the encoded text using the Huffman tree
def huffman_decode(encoded_text, huffman_codes):
    # Reverse the huffman codes
    reverse_codes = {v: k for k, v in huffman_codes.items()}

    current_code = ""
    decoded_text = []

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text.append(reverse_codes[current_code])
            current_code = ""

    return ''.join(decoded_text)

# Example usage
if __name__ == "__main__":
    text = "ravidhawan"
    print(f"Original text: {text}")

    encoded_text, huffman_codes = huffman_encode(text)
    print(f"Encoded text: {encoded_text}")
    print(f"Huffman Codes: {huffman_codes}")

    decoded_text = huffman_decode(encoded_text, huffman_codes)
    print(f"Decoded text: {decoded_text}")
