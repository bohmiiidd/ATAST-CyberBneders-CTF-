def reversed_chakchouka(transformed_chars, key=807):
    transformed_chars.reverse()  # Unscramble
    
    original_chars = []
    dynamic_key = (key + len(transformed_chars)) % 256

    for i, val in enumerate(transformed_chars):
        shift_amount = (i + 3) % 8
        
        # Step 3 (Reverse): Circular shift bits right by (position + 3) mod 8
        val = ((val >> shift_amount) | (val << (8 - shift_amount))) & 0xFF
        
        # Step 2 (Reverse): XOR with the same dynamic key
        val ^= (dynamic_key >> (i % 8))
        
        # Step 1 (Reverse): Subtract position-dependent value
        val = (val - (i + dynamic_key)) % 256
        
        original_chars.append(chr(val))
    
    return ''.join(original_chars)
