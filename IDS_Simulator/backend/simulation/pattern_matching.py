# Description: This file contains the implementation of the Knuth-Morris-Pratt (KMP) algorithm for pattern matching.
# The KMP algorithm is used to search for a pattern within a text string efficiently.

def compute_lps_array(pattern):
    """Compute the longest prefix suffix (LPS) array for the KMP algorithm."""
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """Search for a pattern in a text using the KMP algorithm."""
    lps = compute_lps_array(pattern)
    i = 0  # Index for text
    j = 0  # Index for pattern
    matches = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches