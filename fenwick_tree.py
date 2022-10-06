class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.fwick_tree = [0] * (size + 1)
    
    def prefix_sum(self, position):
        sum = 0
        while position > 0:
            sum += self.fwick_tree[position]
            position -= position & -position
        return sum

    def range_sum(self, left_pos, right_pos):
        return self.prefix_sum(right_pos) - self.prefix_sum(left_pos - 1)

    def point_update(self, position, value):
        index = position
        while index <= self.size:
            self.fwick_tree[index] += value
            index += index & -index

if __name__ == '__main__':

    FT = FenwickTree(5)
    FT.point_update(3, 1)
    FT.point_update(4, 3)
    print(FT.range_sum(3, 4))