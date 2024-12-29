correct = open('nms.txt', 'r').read().splitlines()
wrong = open('c.txt', 'r').read().splitlines()

for i in range(len(correct)):
    if correct[i] != wrong[i]:
        print(f'Line: {i+1}')
        print(correct[i])
        print(wrong[i])
        print()
