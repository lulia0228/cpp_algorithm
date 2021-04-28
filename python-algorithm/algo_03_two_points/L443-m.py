#--coding:utf-8--

# 官方双指针；变量用的很巧
class Solution(object):
    def compress(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write

class Solution1:
    def compress(self, chars: List[str]) -> int:
        last_flag = ""
        c_i = 0
        i = 0
        sub_cnt = 0
        while i<len(chars):
            if chars[i] == last_flag:
                sub_cnt += 1
            else:
                if sub_cnt == 1:
                    chars[c_i] = last_flag
                    c_i += 1
                elif sub_cnt > 1:
                    chars[c_i] = last_flag
                    c_i += 1
                    for j in range(c_i, c_i+len(str(sub_cnt))):
                        chars[j] = str(sub_cnt)[j-c_i]
                    # chars[c_i:c_i+len(str(sub_cnt))] = [ch for ch in str(sub_cnt)]
                    c_i += len(str(sub_cnt))
                last_flag = chars[i]
                sub_cnt = 1
            i += 1
        if sub_cnt == 1:
            chars[c_i] = last_flag
            c_i += 1
        elif sub_cnt > 1:
            chars[c_i] = last_flag
            c_i += 1
            for j in range(c_i, c_i + len(str(sub_cnt))):
                chars[j] = str(sub_cnt)[j - c_i]
            # chars[c_i:c_i + len(str(sub_cnt))] = [ch for ch in str(sub_cnt)]
            c_i += len(str(sub_cnt))

        return c_i
