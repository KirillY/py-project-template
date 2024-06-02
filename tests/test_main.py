from source.main import process_data


def test_process_data():
    """Test that all integers in the list are incremented by 1."""
    data = [1, 2, 3]
    result = process_data(data)
    assert result == [2, 3, 4], "Expected each element to be incremented by 1"
