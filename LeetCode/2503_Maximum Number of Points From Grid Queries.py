MOD = 10**9 + 7

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # 1. �w�B�z�G�p���]�Ƥ���
        # ���p�� 1 ~ max_val ���̤p��]�ơA�οz�k
        max_val = max(nums)
        spf = list(range(max_val+1))  # spf[x] = smallest prime factor of x

        for i in range(2, int(max_val**0.5)+1):
            if spf[i] == i:  # i �O���
                for j in range(i*i, max_val+1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # ��ơG�p�� x ����]�Ƥ���
        def primeScore(x):
            score = 0
            prev = -1
            while x > 1:
                #���o x ���̤p��]��
                p = spf[x]
                if p != prev:
                    score += 1
                    prev = p
                # ��ư��k���ѽ�]��
                x //= p
            return score
        
        # �p��C�ӼƦr����]�Ƥ���
        pscore = [primeScore(x) for x in nums]
        
        # 2. �ϥγ�մ̭p��C�ӯ��ު����Ĥl�}�C�ƶq count[i]
        # L[i] = �̪������ j, j < i, �ϱo pscore[j] >= pscore[i]�A�p�G�L�h -1
        L = [-1] * n
        stack = []
        for i in range(n):
            # ��e�Ʀr����]�Ƥ���
            while stack and pscore[stack[-1]] < pscore[i]:
                stack.pop()
            L[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # R[i] = �̪�k����� j, j > i, �ϱo pscore[j] > pscore[i]�A�p�G�L�h n
        R = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and pscore[stack[-1]] <= pscore[i]:
                stack.pop()
            R[i] = stack[-1] if stack else n
            stack.append(i)
        
        # count[i] �� (i - L[i]) * (R[i] - i)
        count = [ (i - L[i]) * (R[i] - i) for i in range(n) ]
        
        # 3. �N�C�ӯ��� i �Φ� (nums[i], count[i]) �t��
        # �ڭ̧Ʊ�ھ� nums[i] �q�j��p�ƧǡA�]�����j�����Ƨ󦳧Q
        pairs = [(nums[i], count[i]) for i in range(n)]
        pairs.sort(key=lambda x: x[0], reverse=True)
        
        # 4. �g�߿���ާ@���ơA���W�L k
        remaining = k
        score = 1
        for x, cnt in pairs:
            if remaining <= 0:
                break
            use = min(cnt, remaining)
            # score *= x^use  (�� MOD)
            # �ϥΧֳt��
            score = (score * pow(x, use, MOD)) % MOD
            remaining -= use
        
        return score


if __name__ == '__main__':
    s = Solution()
    print(s.maximumScore([8,3,9,3,8], 2)) # 81
    print(s.maximumScore([19,12,14,6,10,18], 3)) # 4788

    