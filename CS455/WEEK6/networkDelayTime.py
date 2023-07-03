class Solution:
    MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def matching(self, ch2ij: dict[str, set[tuple[int, int]]], W: str, K: int, L: int, T: tuple[int, int]) -> bool:
        if K == L:
            return True
        for ID, JD in Solution.MOVES:
            NEWIJ = (T[0] + ID, T[1] + JD)
            if NEWIJ in ch2ij[W[K]]:
                ch2ij[W[K]].remove(NEWIJ)
                if self.matching(ch2ij, W, K + 1, L, NEWIJ):
                    return True
                ch2ij[W[K]].add(NEWIJ)
        return False

    def exist(self, B: List[List[str]], W: str) -> bool:
        M = len(B)
        N = len(B[0])
        L = len(W)
        if M * N < L or L == 0:
            return False
        FREQS = Counter(W)
        ch2ij = {}
        for i in range(M):
            for j in range(N):
                if B[i][j] not in FREQS:
                    continue
                if B[i][j] in ch2ij:
                    ch2ij[B[i][j]].add((i, j))
                else:
                    ch2ij[B[i][j]] = set([(i, j)])
        for CH, CNT in FREQS.items():
            if CH not in ch2ij or len(ch2ij[CH]) < CNT:
                return False
        first_matches = list(ch2ij[W[0]])
        while first_matches:
            T = first_matches.pop()
            ch2ij[W[0]].remove(T)
            if self.matching(ch2ij, W, 1, L, T):
                return True
            ch2ij[W[0]].add(T)
        return False