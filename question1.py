def find_biggest_str(strings):
	if not strings:
		return None
	return max(strings, key=len)

# Example usage
if __name__ == "__main__":
	str_list = ["apple", "banana", "cherry", "watermelon"]
	print(find_biggest_str(str_list))  # Output: watermelon
strs = ["dog","racecar","car"]
