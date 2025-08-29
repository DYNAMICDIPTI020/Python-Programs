def write_k_pattern(n, filename="k_pattern.txt"):
    with open(filename, "w") as f:
        for i in range(n):
            for j in range(n):
                if j == 0 or j == n - i - 1:
                    f.write("k")
                else:
                    f.write(" ")
            f.write("\n")

# Example usage
size = 7
write_k_pattern(size)

print(f"K pattern written to 'k_pattern.txt'")
