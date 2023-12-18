import pytest
import os
from repository import Repo
from service import Service

@pytest.fixture
def setup_test_files():
    # Setup: Create test files and write test data to them
    with open('../data/test_data/events.csv', 'w') as f:
       pass
    with open('../data/test_data/guests.csv', 'w') as f:
       pass
    with open('../data/test_data/logs.csv', 'w') as f:
       pass
    yield
    # Teardown: Remove test files after test is done
    os.remove('../data/test_data/events.csv')
    os.remove('../data/test_data/guests.csv')
    os.remove('../data/test_data/logs.csv')

def test_add_event(setup_test_files):
    repo = Repo(
        '../data/test_data/events.csv', 
        '../data/test_data/guests.csv', 
        '../data/test_data/logs.csv',
    )
    service = Service(repo)
    service.add_event('2021-01-01', '12:00', 'Test event')
    event = service.repo.events[0]
    assert event.id_ == 4
    assert event.date == '2021-01-01'
    assert event.time == '12:00'
    assert event.description == 'Test event'

def test_add_guest(setup_test_files):
    repo = Repo(
        '../data/test_data/events.csv', 
        '../data/test_data/guests.csv', 
        '../data/test_data/logs.csv',
    )
    service = Service(repo)
    service.add_guest('Test guest', 'test address')
    guest = service.repo.guests[0]
    assert guest.id_ == 4
    assert guest.name == 'Test guest'
    assert guest.address == 'test address'

# def test_sort_guest_events_by_description_and_date(setup_test_files):
#     repo = Repo(
#         '../data/test_data/events.csv', 
#         '../data/test_data/guests.csv', 
#         '../data/test_data/logs.csv',
#     )
#     service = Service(repo)
#     service.add_guest('Test guest', 'test address')
#     assert repo.guests[0].id_ == 4
#     service.add_event('2021-01-01', '12:00', 'Test event2')
#     assert repo.events[0].id_ == 4
#     service.add_event('2023-01-01', '12:00', 'Test event1')
#     assert repo.events[1].id_ == 5
#     service.add_event('2023-02-01', '12:00', 'Test event1')
#     assert repo.events[2].id_ == 6
#     service.register(4, 4)
#     service.register(4, 5)
#     service.register(4, 6)
#     assert service.sort_guest_events_by_description_and_date(4) == [
#     ]
