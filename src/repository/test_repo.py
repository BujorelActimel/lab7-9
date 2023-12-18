import pytest
import os
from repository import Repo

@pytest.fixture
def setup_test_files():
    # Setup: Create test files and write test data to them
    with open('../data/test_data/events.csv', 'w') as f:
        f.write('test_event_data')
    with open('../data/test_data/guests.csv', 'w') as f:
        f.write('test_guest_data')
    with open('../data/test_data/logs.csv', 'w') as f:
        f.write('test_log_data')
    yield
    # Teardown: Remove test files after test is done
    os.remove('../data/test_data/events.csv')
    os.remove('../data/test_data/guests.csv')
    os.remove('../data/test_data/logs.csv')

def test_repo(setup_test_files):
    # Test that Repo correctly reads from files
    repo = Repo('../data/test_data/events.csv', '../data/test_data/guests.csv', '../data/test_data/logs.csv')
    assert repo.events_file_name == '../data/test_data/events.csv'
    assert repo.guests_file_name == '../data/test_data/guests.csv'
    assert repo.registrations_file_name == '../data/test_data/logs.csv'