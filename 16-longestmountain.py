class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        n = len(arr)
        ans = 0

        for i in range(1, n - 1):

            # i must be a peak
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:

                l = i
                r = i

                # move left
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1

                # move right
                while r < n - 1 and arr[r] > arr[r + 1]:
                    r += 1

                ans = max(ans, r - l + 1)

        return ans