# Day-4-Merge-Sort
Here Python Program for Merge Sort. Day 4 of Day 365.
- Initial Setup: Divide the unsorted array into two approximately equal halves.
- Recursive Splitting: Recursively continue to split these halves until each sub-array contains only one element.
- Merging: Begin merging the sub-arrays back together:
  - Compare the first elements of each sub-array.
  - Place the smaller element into the merged array.
  - Move to the next element in the sub-array from which the smaller element was taken.
- Continue Merging: Repeat the merging process until all elements from the sub-arrays are merged into a single sorted array.

Here's a visual representation using the example array [38, 27, 43, 3, 9, 82, 10]:

1. Initial Array: [38, 27, 43, 3, 9, 82, 10]
2. Split into Halves: [38, 27, 43, 3] and [9, 82, 10]
3. Further Split:
   - [38, 27], [43, 3]
   - [9, 82], [10]
4. Continue Splitting:
   - [38], [27]
   - [43], [3]
   - [9], [82]
   - [10]
5. Start Merging:
   - Merge [38] and [27] to get [27, 38]
   - Merge [43] and [3] to get [3, 43]
   - Merge [9] and [82] to get [9, 82]
   - [10] remains as is
6. Continue Merging:
   - Merge [27, 38] and [3, 43] to get [3, 27, 38, 43]
   - Merge [9, 82] and [10] to get [9, 10, 82]
7. Final Merge:
   - Merge [3, 27, 38, 43] and [9, 10, 82] to get [3, 9, 10, 27, 38, 43, 82]

This process results in a fully sorted array: [3, 9, 10, 27, 38, 43, 82].
