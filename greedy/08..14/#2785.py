def getChainCount(chains, N):
    chains.sort()

    chainCount = N
    tiedChains = 1

    for chain in chains:
        if tiedChains + chain >= chainCount:
            break
        else:
            tiedChains += chain
            chainCount -= 1

    return chainCount-1


if __name__ == '__main__':
    N = int(input())
    chains = list(map(int, input().split()))

    chainCount = getChainCount(chains, N)
    print(chainCount)