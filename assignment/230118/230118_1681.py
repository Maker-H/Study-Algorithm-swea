val = input()
val_len = len(val)

if val_len % 2 == 0:
    idx = val_len // 2
    print(f'{val[idx-1]}{val[idx]}')
else:
    idx = val_len //2
    print(val[idx])
