import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sensor_sim import read_sensor_data, average

@pytest.fixture
def sample_file(tmp_path):
    p = tmp_path / "data.csv"
    p.write_text("1.0\n2.0\n3.0\n")
    return str(p)

def test_read_sensor_data(sample_file):
    data = read_sensor_data(sample_file)
    assert data == [1.0, 2.0, 3.0]

def test_average():
    assert average([1, 2, 3, 4]) == pytest.approx(2.5)