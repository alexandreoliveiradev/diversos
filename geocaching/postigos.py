# Generate coordinates exactly as requested
# Stop if BBB > 999

# Target sums for (X + Y)
target_sums = [20, 22]  # you said up to 20 or 22

print("Generated Coordinates:\n")

for S in target_sums:
    # Loop over all possible X, Y such that X + Y = S
    for X in range(1, S):  # X positive
        Y = S - X           # Y positive
        if Y > 0 and Y <= 20:  # keep Y <= 20
            AA = S / 2
            BBB = 776 + S * (6 + Y) + 3

            # Skip if BBB > 999
            if BBB > 999:
                continue

            # Print in N 41° AA.BBB format
            N_coord = f"N 41 {AA:.0f}.{BBB:.0f}"
            W_coord = "W 008 40.097"
            print(f"X={X}, Y={Y} -> {N_coord}, {W_coord}")
