from utils import quicksort, gnome_sort

def test_quicksort():
    arr = [4, 2, 1, 3]
    assert quicksort(arr) == [1, 2, 3, 4]

def test_quicksort_reverse():
    arr = [4, 2, 1, 3]
    assert quicksort(arr, reverse=True) == [4, 3, 2, 1]

def test_quicksort_key():
    arr = [4, 2, 1, 3]
    assert quicksort(arr, key=lambda x: -x) == [4, 3, 2, 1]

def test_quicksort_cmp():
    arr = [4, 2, 1, 3]
    assert quicksort(arr, cmp=lambda x, y: (x < y) - (x > y)) == [4, 3, 2, 1]

def test_gnome_sort():
    arr = [4, 2, 1, 3]
    assert gnome_sort(arr) == [1, 2, 3, 4]

def test_gnome_sort_reverse():
    arr = [4, 2, 1, 3]
    assert gnome_sort(arr, reverse=True) == [4, 3, 2, 1]

def test_gnome_sort_key():
    arr = [4, 2, 1, 3]
    assert gnome_sort(arr, key=lambda x: -x) == [4, 3, 2, 1]

def test_gnome_sort_cmp():
    arr = [4, 2, 1, 3]
    assert gnome_sort(arr, cmp=lambda x, y: x > y) == [4, 3, 2, 1]
