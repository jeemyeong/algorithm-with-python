from quicksort import sort, partition1, partition2

def test_sort():
    assert sort([5,3,7,6,1,2,4], partition1) == [1,2,3,4,5,6,7]
    assert sort([5,3,7,6,1,2,4], partition2) == [1,2,3,4,5,6,7]
    assert sort([1,2,3,4,5,6,7], partition1) == [1,2,3,4,5,6,7]
    assert sort([1,2,3,4,5,6,7], partition2) == [1,2,3,4,5,6,7]
    assert sort([1,1], partition1) == [1,1]
    assert sort([1,1], partition2) == [1,1]
    assert sort([3,2,1], partition1) == [1,2,3]
    assert sort([3,2,1], partition2) == [1,2,3]
    assert sort([3,1,2], partition1) == [1,2,3]
    assert sort([3,1,2], partition2) == [1,2,3]
    assert sort([4,1,2,3], partition1) == [1,2,3,4]
    assert sort([4,1,2,3], partition2) == [1,2,3,4]
    assert sort([1], partition1) == [1]
    assert sort([1], partition2) == [1]
    assert sort([], partition1) == []
    assert sort([], partition2) == []
