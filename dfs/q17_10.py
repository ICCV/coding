为什么当数组中存在主要元素时，\text{Boyer-Moore}Boyer-Moore 投票算法可以确保得到主要元素？

在 \text{Boyer-Moore}Boyer-Moore 投票算法中，遇到相同的数则将 \textit{count}count 加 11，遇到不同的数则将 \textit{count}count 减 11。根据主要元素的定义，主要元素的出现次数大于其他元素的出现次数之和，因此在遍历过程中，主要元素和其他元素两两抵消，最后一定剩下至少一个主要元素，此时 \textit{candidate}candidate 为主要元素，且 \textit{count} \ge 1count≥1。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-majority-element-lcci/solution/zhu-yao-yuan-su-by-leetcode-solution-xr1p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。