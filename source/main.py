def process_data(data: list[int]) -> list[int]:
    """Process a list of integers and return a new list with each element incremented by 1."""
    return [x + 1 for x in data]


if __name__ == "__main__":
    sample_data = [1, 2, 3]
    processed_data = process_data(sample_data)
    print("Processed Data:", processed_data)
