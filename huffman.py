"""
Write a program to implement Huffman Encoding using a greedy strategy.
"""

from collections import Counter

# Node class for the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Custom function to find the two nodes with the lowest frequency
def get_two_smallest(nodes):
    # Sort the list of nodes by frequency (ascending order)
    nodes.sort(key=lambda x: x.freq)
    # Pop the two nodes with the lowest frequency
    return nodes.pop(0), nodes.pop(0)

# Build the Huffman Tree
def build_huffman_tree(frequencies):
    # Create initial nodes for each character
    nodes = [Node(char, freq) for char, freq in frequencies.items()]

    # Iterate until there's only one node left (root of the tree)
    while len(nodes) > 1:
        # Get the two nodes with the lowest frequency
        left, right = get_two_smallest(nodes)

        # Create a new internal node with combined frequency
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node back to the list of nodes
        nodes.append(merged)

    # The last remaining node is the root of the Huffman Tree
    return nodes[0]

# Generate Huffman codes from the tree
def generate_huffman_codes(root, code="", code_map=None):
    if code_map is None:
        code_map = {}

    # Leaf node
    if root.char is not None:
        code_map[root.char] = code
        return code_map

    # Traverse the left and right branches
    if root.left:
        generate_huffman_codes(root.left, code + "0", code_map)
    if root.right:
        generate_huffman_codes(root.right, code + "1", code_map)

    return code_map

# Huffman Encoding function
def huffman_encoding(data):
    if not data:
        return "", {}

    # Calculate frequency of each character in the input data
    frequencies = Counter(data)

    # Build the Huffman Tree
    root = build_huffman_tree(frequencies)

    # Generate the codes
    huffman_codes = generate_huffman_codes(root)

    # Encode the input data
    encoded_data = "".join(huffman_codes[char] for char in data)

    return encoded_data, huffman_codes

# Huffman Decoding function
def huffman_decoding(encoded_data, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    decoded_data = ""
    code = ""
    for bit in encoded_data:
        code += bit
        if code in reverse_codes:
            decoded_data += reverse_codes[code]
            code = ""
    return decoded_data

# Example usage
if __name__ == "__main__":
    data = "hello huffman"
    encoded_data, huffman_codes = huffman_encoding(data)
    print("Huffman Codes:", huffman_codes)
    print("Encoded Data:", encoded_data)

    # Decode the data
    decoded_data = huffman_decoding(encoded_data, huffman_codes)
    print("Decoded Data:", decoded_data)
