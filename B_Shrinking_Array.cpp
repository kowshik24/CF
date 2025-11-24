#include<bits/stdc++.h>
using namespace std;

const int INF = 1e9;
const int MAXN = 1005;
const int K = 11;

int a[MAXN];
int st_min[MAXN][K];
int st_max[MAXN][K];
int log_table[MAXN];

void build(int n) {
    log_table[1] = 0;
    for (int i = 2; i <= n; i++) {
        log_table[i] = log_table[i/2] + 1;
    }
    for (int i = 1; i <= n; i++) {
        st_min[i][0] = a[i];
        st_max[i][0] = a[i];
    }
    for (int j = 1; j < K; j++) {
        for (int i = 1; i + (1 << j) <= n + 1; i++) {
            st_min[i][j] = std::min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1]);
            st_max[i][j] = std::max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1]);
        }
    }
}

int query_min(int l, int r) {
    int j = log_table[r - l + 1];
    return std::min(st_min[l][j], st_min[r - (1 << j) + 1][j]);
}

int query_max(int l, int r) {
    int j = log_table[r - l + 1];
    return std::max(st_max[l][j], st_max[r - (1 << j) + 1][j]);
}

void solve() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; i++) {
        std::cin >> a[i];
    }

    for (int i = 1; i < n; i++) {
        if (std::abs(a[i] - a[i+1]) <= 1) {
            std::cout << 0 << std::endl;
            return;
        }
    }

    build(n);

    int min_ops = INF;

    
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j++) {
            int ops = j - i;
            if (ops == 0) continue;
            if (n - ops < 2) continue;

            int min_val = query_min(i, j);
            int max_val = query_max(i, j);

            if (i > 1) {
                if (min_val <= a[i-1] + 1 && max_val >= a[i-1] - 1) {
                    min_ops = std::min(min_ops, ops);
                }
            }
            if (j < n) {
                if (min_val <= a[j+1] + 1 && max_val >= a[j+1] - 1) {
                    min_ops = std::min(min_ops, ops);
                }
            }
        }
    }

    
    for (int j = 1; j < n; j++) {
        for (int i = 1; i <= j; i++) {
            int ops1 = j - i;
            int l1 = query_min(i, j);
            int r1 = query_max(i, j);

            
            int low = j + 1, high = n, best_k = -1;
            while (low <= high) {
                int mid_k = low + (high - low) / 2;
                int l2 = query_min(j + 1, mid_k);
                int r2 = query_max(j + 1, mid_k);

                if (l1 <= r2 + 1 && l2 <= r1 + 1) {
                    best_k = mid_k;
                    high = mid_k - 1;
                } else {
                    low = mid_k + 1;
                }
            }

            if (best_k != -1) {
                int ops2 = best_k - (j + 1);
                int total_ops = ops1 + ops2;
                if (n - total_ops >= 2) {
                    min_ops = std::min(min_ops, total_ops);
                }
            }
        }
    }

    if (min_ops == INF) {
        std::cout << -1 << std::endl;
    } else {
        std::cout << min_ops << std::endl;
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
