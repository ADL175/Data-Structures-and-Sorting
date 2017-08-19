"""//////////////////////////////////////////
//////
//////  Bubble Sort
//////
//////////////////////////////////////////."""


def bubble_sort(array_of_stuff):
    """Bubble sort function"""
    if not all(isinstance(n, int) for n in array_of_stuff):
        return
    if len(array_of_stuff) == 0:
        return
    for i in range(len(array_of_stuff)):
        did_swap = False
        for j in range(i+1, len(array_of_stuff)):
            if array_of_stuff[j] < array_of_stuff[i]:
                array_of_stuff[j], array_of_stuff[i] = array_of_stuff[i], array_of_stuff[j]
                did_swap = True
            if not did_swap:
                break


"""//////////////////////////////////////////
//////
//////  Merge Sort
//////
//////////////////////////////////////////."""


def merge_sort(array_of_stuff):
    """Merge sort function"""
    if not all(isinstance(n, int) for n in array_of_stuff):
        return
    if len(array_of_stuff) == 0:
        return
    if len(array_of_stuff) < 2:
        return array_of_stuff
    left_list = []
    right_list = []
    mid = int(len(array_of_stuff)/2)
    for idx in range(0, mid):
        left_list.append(array_of_stuff[idx])
    for idx in range(mid, len(array_of_stuff)):
        right_list.append(array_of_stuff[idx])
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge_helper(left_list, right_list)


def merge_helper(left, right):
    i = 0
    j = 0
    sorted_array = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    return sorted_array


"""//////////////////////////////////////////
//////
//////  Quick Sort
//////
//////////////////////////////////////////."""

from random import randint


def quick_sort(array_of_stuff, start, end):
    """Quick sort function"""
    if not all(isinstance(n, int) for n in array_of_stuff):
        return
    if len(array_of_stuff) == 0:
        return
    if len(array_of_stuff) < 2:
        return array_of_stuff

    if start < end:
        pivot_pt = randomized_partition(array_of_stuff, start, end)
        quick_sort(array_of_stuff, start, pivot_pt - 1)
        quick_sort(array_of_stuff, pivot_pt + 1, end)


def randomized_partition(array_of_stuff, start, end):
    """Randomize the pivot point."""
    pivot_idx = randint(start, end)
    swap(array_of_stuff, pivot_idx, end)
    return partition(array_of_stuff, start, end)


def swap(array_of_stuff, start, end):
    """Swaps the elements in a collection."""
    array_of_stuff[start], array_of_stuff[end] = array_of_stuff[end], array_of_stuff[start]


def partition(array_of_stuff, start, end):
    """items < pivot pt on left, items > pivot pt on right."""
    pivot = array_of_stuff[end]
    p_idx = start
    for i in range(start, end):
        if array_of_stuff[i] <= pivot:
            swap(array_of_stuff, i, p_idx)
            p_idx += 1
    swap(array_of_stuff, p_idx, end)
    return p_idx


"""//////////////////////////////////////////
//////
//////  Insertion Sort
//////
//////////////////////////////////////////."""


def insertion_sort(array_of_stuff):
    """Insertion sort function"""
    if not all(isinstance(n, int) for n in array_of_stuff):
        return
    if len(array_of_stuff) == 0:
        return
    for i in range(1, len(array_of_stuff)):
        r = i
        temp_idx = array_of_stuff[i]
        while r > 0 and array_of_stuff[r-1] > temp_idx:
            array_of_stuff[r] = array_of_stuff[r-1]
            r -= 1
        array_of_stuff[r] = temp_idx


"""//////////////////////////////////////////
//////
//////  Radix Sort
//////
//////////////////////////////////////////."""

import math


def radix_sort(iter):
    """Sort the interable using the radix sort method."""
    if not isinstance(iter, (list, tuple)):
        raise TypeError("Input only a list/tuple of integers")
    if not all(isinstance(x, (int, float)) for x in iter):
        raise ValueError("Input only a list/tuple of integers")

    places = 0
    for num in iter:
        digits = num_digits(num)
        if digits > places:
            places = digits

    for place in range(1, places + 1):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for num in iter:
            digit = get_digit(num, place + 1)
            bucket[digit].append(num)
        iter = []
        for sub in bucket:
            for number in sub:
                iter.append(number)
    return iter


def get_digit(num, place):
    """Return the place-th digit of num."""
    return int(num / 10 ** (place - 1)) % 10


def num_digits(num):
    """Give the length of a given number."""
    if num > 0:
        return int(math.log10(num)) + 1
    elif num == 0:
        return 1
