class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col in range(len(board)):
            col_nums = set()
            for row in range(len(board)):
                cell = board[col][row]
                if cell != "." and cell in col_nums:
                    return False
                else:
                    col_nums.add(cell) 
        for col in range(len(board)):
            col_nums = set()
            for row in range(len(board)):
                cell = board[row][col]
                if cell != "." and cell in col_nums:
                    return False
                else:
                    col_nums.add(cell)
        block_size = 3
        row_blocks = int(len(board) / block_size)
        col_blocks = int(len(board) / block_size)
        for row_block in range(row_blocks):
            for col_block in range(col_blocks):
                block_nums = set()
                for row in range(row_block * block_size, row_block * block_size + block_size):
                    for col in range(col_block * block_size, col_block * block_size + block_size):
                        cell = board[row][col]
                        if cell != "." and cell in block_nums:
                            return False
                        else:
                            block_nums.add(cell)
        return True