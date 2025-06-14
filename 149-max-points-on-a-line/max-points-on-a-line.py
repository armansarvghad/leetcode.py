class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        result = 1
        for i in range(len(points)):
            slopes = {}
            duplicates = 0
            cur_max = 0
            for j in range(i+1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                # Compute gcd manually (since LeetCode may not allow math.gcd)
                def calc_gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a
                g = calc_gcd(dy, dx)
                if g != 0:
                    dy //= g
                    dx //= g
                slope = (dy, dx)
                slopes[slope] = slopes.get(slope, 0) + 1
                cur_max = max(cur_max, slopes[slope])
            result = max(result, cur_max + duplicates + 1)
        return result