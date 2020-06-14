# def max_gap(x):
#     max_gap_length = 0
#     current_gap_length = 0
#     for i in range(x.bit_length()):
#         if x & (1 << i):
#             # Set, any gap is over.
#             if current_gap_length > max_gap_length:
#                 max_gap_length = current_gap_length
#                 current_gap_length = 0
#         else:
#             # Not set, the gap widens.
#             current_gap_length += 1
#     # Gap might end at the end.
#     if current_gap_length > max_gap_length:
#         max_gap_length = current_gap_length
#     return max_gap_length


def max_gap(N):
    return len(max(format(N, 'b').strip('0').split('1')))


out = max_gap(32)
print(out)
