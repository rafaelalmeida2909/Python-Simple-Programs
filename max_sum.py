#max sum of an interval in an array
def max_sum (v): # v is an array
    ans = 0
    mx = 0
    sz = len(v)

    for i in range(0, sz):
        mx = max(0, mx+v[i])
        ans = max(ans, mx)

    return ans