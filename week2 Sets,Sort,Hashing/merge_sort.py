def merge_sort(arr):
  """
  归并排序算法。

  Args:
    arr: 待排序的数组。

  Returns:
    排序后的数组。
  """
  if len(arr) <= 1:
    return arr  # 基本情况：长度为 0 或 1 的数组已经排序

  # 1. 分解 (Subproblems)
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  # 2. 递归排序 (Relation)
  left = merge_sort(left)
  right = merge_sort(right)

  # 3. 合并 (Topological Order - implicit)
  return merge(left, right)


def merge(left, right):
  """
  合并两个已排序的数组。

  Args:
    left: 已排序的左半部分数组。
    right: 已排序的右半部分数组。

  Returns:
    合并后的已排序数组。
  """
  merged = []
  i = 0  # 左半部分的索引
  j = 0  # 右半部分的索引

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  # 将剩余的元素添加到 merged 数组中
  merged += left[i:]
  merged += right[j:]

  return merged

# 示例用法:
my_array = [12, 11, 13, 5, 6, 7]
sorted_array = merge_sort(my_array)
print("排序后的数组:", sorted_array)  # 输出: 排序后的数组: [5, 6, 7, 11, 12, 13]
