def maxWater(height):
    l = 0
    r = len(height) - 1
    maxArea = 0
    while l < r:
        area = (r - l) * min(height[l], height[r])
        maxArea = max(maxArea, area)
        if height[l] <= height[r]:
            l = l + 1
        else:
            r = r - 1
    return maxArea

