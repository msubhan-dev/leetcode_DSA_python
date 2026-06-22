class Solution(object):
    def mergeAlternately(self, word1, word2):
    
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return "".join(result)
        # ============= HOW TO TEST =============


# Create instance
solution = Solution()

# Test Case 1
result1 = solution.mergeAlternately("abc", "pqr")
print(f"mergeAlternately('abc', 'pqr') {result1}")
# Expected: "apbqcr"

# Test Case 2 (different lengths)
result2 = solution.mergeAlternately("ab", "pqrs")
print(f"mergeAlternately('ab', 'pqrs') {result2}")
# Expected: "apbqrs"

# Test Case 3
result3 = solution.mergeAlternately("abcd", "pq")
print(f"mergeAlternately('abcd', 'pq') {result3}")
# Expected: "apbqcd"
