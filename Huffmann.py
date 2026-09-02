import heapq
from collections import Counter, defaultdict

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # For priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_huffman_tree(freq_map):
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

# Generate Huffman Codes
def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node.char is not None:
        code_map[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map

# Main program
def huffman_encoding(sentence):
    # Extract only English alphabet characters
    filtered = [ch for ch in sentence.lower() if ch.isalpha()]
    
    # Frequency map
    freq_map = Counter(filtered)
    
    # Build Huffman Tree
    root = build_huffman_tree(freq_map)
    
    # Generate codes
    codes = generate_codes(root)
    
    # Display results
    print("Character | Frequency | Huffman Code")
    print("------------------------------------")
    for char, freq in freq_map.items():
        print(f"    {char}     |     {freq}     |    {codes[char]}")
    
    return codes, freq_map

# Example usage
sentence = input("Enter a sentence: ")
codes, freq_map = huffman_encoding(sentence)
