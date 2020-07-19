DP顺推模板

    def dp():
        dp = [][]
        for i = 0..M {
            for j = 0..N{
                dp[i][j] = _function(dp[i`][j`])
            }
        }
        return de[M][N]