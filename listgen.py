from config import num_blocks, num_trials


def genStim():
    blocks = []

    for x in num_blocks:
        block = []
        for y in num_trials:
            if y%2 == 0:
                block.append({"stim":"left",})
            else:
                block.append({"stim":"right",})
        blocks.append(block)
    return blocks
